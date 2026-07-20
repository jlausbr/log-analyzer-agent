"""Tool for processing and analyzing log events."""

from typing import List, Dict
from collections import defaultdict


def process_log_events(log_content: str) -> dict:
    """
    Process log content and extract key information.
    
    Args:
        log_content: Raw log file content as string
    
    Returns:
        dict with analyzed log information:
            - total_lines: int total number of log lines
            - error_count: int number of ERROR level entries
            - warning_count: int number of WARNING level entries
            - info_count: int number of INFO level entries
            - other_count: int other log levels
            - error_lines: List[str] extracted error lines
            - warning_lines: List[str] extracted warning lines
            - top_error_patterns: List[tuple] most common error patterns
    """
    
    if not log_content:
        return {
            "total_lines": 0,
            "error_count": 0,
            "warning_count": 0,
            "info_count": 0,
            "other_count": 0,
            "error_lines": [],
            "warning_lines": [],
            "top_error_patterns": [],
        }
    
    lines = log_content.strip().split("\n")
    
    error_lines = []
    warning_lines = []
    error_patterns = defaultdict(int)
    
    error_count = 0
    warning_count = 0
    info_count = 0
    other_count = 0
    
    for line in lines:
        line_upper = line.upper()
        
        if "ERROR" in line_upper or "EXCEPTION" in line_upper:
            error_count += 1
            error_lines.append(line)
            # Extract a pattern (first 100 chars after ERROR/EXCEPTION)
            pattern = line[max(0, line_upper.find("ERROR") - 20):min(len(line), line_upper.find("ERROR") + 80)]
            error_patterns[pattern.strip()] += 1
        
        elif "WARNING" in line_upper or "WARN" in line_upper:
            warning_count += 1
            warning_lines.append(line)
        
        elif "INFO" in line_upper:
            info_count += 1
        
        else:
            other_count += 1
    
    # Sort error patterns by frequency
    top_patterns = sorted(error_patterns.items(), key=lambda x: x[1], reverse=True)[:5]
    
    return {
        "total_lines": len(lines),
        "error_count": error_count,
        "warning_count": warning_count,
        "info_count": info_count,
        "other_count": other_count,
        "error_lines": error_lines[-10:],  # Last 10 errors
        "warning_lines": warning_lines[-5:],  # Last 5 warnings
        "top_error_patterns": top_patterns,
    }
