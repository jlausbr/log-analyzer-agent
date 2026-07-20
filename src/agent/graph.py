"""LangGraph definition for the log analyzer agent."""

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os
from datetime import datetime
from dotenv import load_dotenv

from .state import LogAnalysisState
from ..tools.log_reader import read_log_file
from ..tools.log_processor import process_log_events

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4-turbo-preview",
    temperature=0.3,
    api_key=os.getenv("OPENAI_API_KEY"),
)


def validate_input(state: LogAnalysisState) -> LogAnalysisState:
    """
    Validate the input log file path.
    Node 1: Validates user input before processing.
    """
    if not state.log_file_path:
        state.validation_errors.append("Log file path is required")
        state.is_valid = False
    
    if not state.log_file_path.endswith((".log", ".txt")):
        state.validation_errors.append("File must be a .log or .txt file")
        state.is_valid = False
    
    return state


def read_log(state: LogAnalysisState) -> LogAnalysisState:
    """
    Read the log file using the custom tool.
    Node 2: Executes the file reading tool.
    """
    if not state.is_valid:
        state.validation_errors.append("Skipping log read due to validation errors")
        return state
    
    max_lines = int(os.getenv("MAX_LOG_LINES", 500))
    result = read_log_file(state.log_file_path, max_lines=max_lines)
    
    if not result["success"]:
        state.validation_errors.append(f"Failed to read log: {result['error']}")
        state.is_valid = False
        return state
    
    state.log_file_content = result["content"]
    state.log_metadata = {
        "file_path": state.log_file_path,
        "total_lines": result["total_lines"],
        "lines_read": result["lines_read"],
        "file_size": result["file_size"],
    }
    
    return state


def parse_events(state: LogAnalysisState) -> LogAnalysisState:
    """
    Parse and categorize log events.
    Node 3: Processes the raw log content.
    """
    if not state.is_valid or not state.log_file_content:
        return state
    
    state.parsed_events = process_log_events(state.log_file_content)
    
    return state


def analyze_with_llm(state: LogAnalysisState) -> LogAnalysisState:
    """
    Use LLM to analyze log events and generate insights.
    Node 4: LLM-powered analysis of the parsed events.
    """
    if not state.is_valid or not state.parsed_events:
        return state
    
    # Prepare context for the LLM
    events_summary = f"""
Log Analysis Summary:
- Total Lines: {state.parsed_events['total_lines']}
- Error Count: {state.parsed_events['error_count']}
- Warning Count: {state.parsed_events['warning_count']}
- Info Count: {state.parsed_events['info_count']}

Top Error Patterns:
{chr(10).join([f"  - {pattern[0][:80]}... (appears {pattern[1]} times)" for pattern in state.parsed_events['top_error_patterns']])}

Recent Errors (up to 10 most recent):
{chr(10).join(state.parsed_events['error_lines'][-3:])}

Recent Warnings (up to 5 most recent):
{chr(10).join(state.parsed_events['warning_lines'][-2:])}
    """
    
    system_prompt = """You are a technical log analysis expert. Your task is to analyze application logs and provide:
1. A summary of the log health
2. Critical issues identified
3. Patterns and root causes
4. Recommended actions

Be concise, technical, and actionable."""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Please analyze these logs and provide insights:\n\n{events_summary}")
    ]
    
    response = llm.invoke(messages)
    state.analysis_result = {"llm_analysis": response.content}
    
    return state


def generate_report(state: LogAnalysisState) -> LogAnalysisState:
    """
    Generate a structured technical report.
    Node 5: Formats the analysis into a professional report.
    """
    if not state.is_valid:
        state.report = "\n".join([f"ERROR: {err}" for err in state.validation_errors])
        return state
    
    if not state.parsed_events or not state.analysis_result:
        state.report = "Insufficient data to generate report"
        return state
    
    events = state.parsed_events
    analysis = state.analysis_result["llm_analysis"]
    
    report = f"""# Technical Log Analysis Report

## Executive Summary
File: {state.log_metadata['file_path']}
Analysis Date: {datetime.now().strftime('%a %b %d %H:%M:%S %Y')}

## Log Statistics
- **Total Lines**: {events['total_lines']}
- **Lines Analyzed**: {state.log_metadata['lines_read']}
- **File Size**: {state.log_metadata['file_size']} bytes

## Issue Distribution
| Level | Count |
|-------|-------|
| ERROR | {events['error_count']} |
| WARNING | {events['warning_count']} |
| INFO | {events['info_count']} |
| OTHER | {events['other_count']} |

## Analysis & Insights
{analysis}

## Top Error Patterns
{chr(10).join([f"- Pattern {i+1}: {p[0][:100]}... (Occurrences: {p[1]})" for i, p in enumerate(events['top_error_patterns'])])}

---
*Generated by Log Analyzer Agent using LangGraph*
    """
    
    state.report = report
    return state


def create_log_analyzer_agent():
    """
    Create and compile the log analyzer agent graph.
    
    Graph flow:
    validate_input → read_log → parse_events → analyze_with_llm → generate_report → END
    
    Returns:
        Compiled LangGraph StateGraph ready for invocation
    """
    workflow = StateGraph(LogAnalysisState)
    
    # Add nodes
    workflow.add_node("validate_input", validate_input)
    workflow.add_node("read_log", read_log)
    workflow.add_node("parse_events", parse_events)
    workflow.add_node("analyze_with_llm", analyze_with_llm)
    workflow.add_node("generate_report", generate_report)
    
    # Add edges
    workflow.add_edge("validate_input", "read_log")
    workflow.add_edge("read_log", "parse_events")
    workflow.add_edge("parse_events", "analyze_with_llm")
    workflow.add_edge("analyze_with_llm", "generate_report")
    workflow.add_edge("generate_report", END)
    
    # Set entry point
    workflow.set_entry_point("validate_input")
    
    # Compile graph
    return workflow.compile()
