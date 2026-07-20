"""State definition for the log analyzer agent."""

from typing import Optional, List
from dataclasses import field
from pydantic import BaseModel


class LogAnalysisState(BaseModel):
    """
    State object that tracks the log analysis workflow.
    
    This state is shared across all nodes in the LangGraph and maintains
    information needed for the agent to process logs and generate reports.
    """
    
    # Input
    log_file_path: str
    
    # Processing stages
    log_file_content: Optional[str] = None
    log_metadata: Optional[dict] = None
    parsed_events: Optional[dict] = None
    analysis_result: Optional[dict] = None
    
    # Validation and errors
    validation_errors: List[str] = field(default_factory=list)
    is_valid: bool = True
    
    # Final output
    report: Optional[str] = None
    
    class Config:
        arbitrary_types_allowed = True
