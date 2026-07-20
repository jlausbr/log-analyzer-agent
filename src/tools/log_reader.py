"""Tool for reading and validating log files."""

from pathlib import Path
from typing import Optional


def read_log_file(file_path: str, max_lines: Optional[int] = None) -> dict:
    """
    Read a log file and return its contents with metadata.
    
    Args:
        file_path: Path to the log file to read
        max_lines: Maximum number of lines to read (None = all lines)
    
    Returns:
        dict with keys:
            - success: bool indicating if read was successful
            - content: str with file contents (truncated if needed)
            - total_lines: int total number of lines in file
            - lines_read: int number of lines actually read
            - file_size: int file size in bytes
            - error: Optional[str] error message if unsuccessful
    
    Raises:
        ValueError: if file_path is empty or contains suspicious patterns
    """
    
    # Validation
    if not file_path:
        return {
            "success": False,
            "error": "File path cannot be empty",
            "content": "",
            "total_lines": 0,
            "lines_read": 0,
            "file_size": 0,
        }
    
    # Security: prevent path traversal attacks
    if ".." in file_path or file_path.startswith("/etc"):
        return {
            "success": False,
            "error": "Invalid file path: path traversal detected",
            "content": "",
            "total_lines": 0,
            "lines_read": 0,
            "file_size": 0,
        }
    
    try:
        path = Path(file_path)
        
        # Check if file exists
        if not path.exists():
            return {
                "success": False,
                "error": f"File not found: {file_path}",
                "content": "",
                "total_lines": 0,
                "lines_read": 0,
                "file_size": 0,
            }
        
        # Check if it's a file (not a directory)
        if not path.is_file():
            return {
                "success": False,
                "error": f"Path is not a file: {file_path}",
                "content": "",
                "total_lines": 0,
                "lines_read": 0,
                "file_size": 0,
            }
        
        # Get file size
        file_size = path.stat().st_size
        
        # Read file
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        
        # Apply max_lines limit if specified
        if max_lines and max_lines > 0:
            lines_to_return = lines[:max_lines]
            lines_read = len(lines_to_return)
        else:
            lines_to_return = lines
            lines_read = total_lines
        
        content = "".join(lines_to_return)
        
        return {
            "success": True,
            "content": content,
            "total_lines": total_lines,
            "lines_read": lines_read,
            "file_size": file_size,
            "error": None,
        }
    
    except PermissionError:
        return {
            "success": False,
            "error": f"Permission denied reading file: {file_path}",
            "content": "",
            "total_lines": 0,
            "lines_read": 0,
            "file_size": 0,
        }
    
    except Exception as e:
        return {
            "success": False,
            "error": f"Error reading file: {str(e)}",
            "content": "",
            "total_lines": 0,
            "lines_read": 0,
            "file_size": 0,
        }
