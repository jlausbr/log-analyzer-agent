"""Tests for the log analysis tools."""

import pytest
import tempfile
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from tools.log_reader import read_log_file
from tools.log_processor import process_log_events


class TestLogReader:
    """Tests for read_log_file tool."""
    
    def test_read_valid_log_file(self):
        """Test reading a valid log file."""
        # Create a temporary log file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.log', delete=False) as f:
            f.write("2024-01-15 10:23:45 [INFO] Application started\n")
            f.write("2024-01-15 10:23:46 [ERROR] Error occurred\n")
            temp_path = f.name
        
        try:
            result = read_log_file(temp_path)
            
            assert result["success"] is True
            assert result["error"] is None
            assert len(result["content"]) > 0
            assert result["total_lines"] == 2
            assert result["lines_read"] == 2
            assert result["file_size"] > 0
        finally:
            Path(temp_path).unlink()
    
    def test_read_with_max_lines(self):
        """Test reading with max lines limit."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.log', delete=False) as f:
            for i in range(10):
                f.write(f"Line {i}\n")
            temp_path = f.name
        
        try:
            result = read_log_file(temp_path, max_lines=5)
            
            assert result["success"] is True
            assert result["total_lines"] == 10
            assert result["lines_read"] == 5
            assert result["content"].count("\n") == 5
        finally:
            Path(temp_path).unlink()
    
    def test_file_not_found(self):
        """Test handling of non-existent file."""
        result = read_log_file("nonexistent_file.log")
        
        assert result["success"] is False
        assert "not found" in result["error"].lower()
        assert result["content"] == ""
        assert result["total_lines"] == 0
    
    def test_empty_path(self):
        """Test handling of empty file path."""
        result = read_log_file("")
        
        assert result["success"] is False
        assert result["error"] is not None
    
    def test_path_traversal_prevention(self):
        """Test prevention of path traversal attacks."""
        result = read_log_file("../../etc/passwd")
        
        assert result["success"] is False
        assert "path traversal" in result["error"].lower()
    
    def test_directory_instead_of_file(self):
        """Test handling when path is a directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            result = read_log_file(temp_dir)
            
            assert result["success"] is False
            assert "not a file" in result["error"].lower()


class TestLogProcessor:
    """Tests for process_log_events tool."""
    
    def test_categorization(self):
        """Test log event categorization."""
        log_content = """
2024-01-15 10:23:45 [INFO] Application started
2024-01-15 10:23:46 [WARNING] High memory usage
2024-01-15 10:23:47 [ERROR] Connection failed
2024-01-15 10:23:48 [ERROR] Connection timeout
2024-01-15 10:23:49 [INFO] Retrying connection
        """.strip()
        
        result = process_log_events(log_content)
        
        assert result["total_lines"] == 5
        assert result["error_count"] == 2
        assert result["warning_count"] == 1
        assert result["info_count"] == 2
    
    def test_pattern_extraction(self):
        """Test extraction of error patterns."""
        log_content = """
[ERROR] Connection failed: timeout
[ERROR] Connection failed: timeout
[ERROR] Connection failed: refused
        """.strip()
        
        result = process_log_events(log_content)
        
        assert result["error_count"] == 3
        assert len(result["top_error_patterns"]) > 0
        # Most frequent pattern should be listed
        assert result["top_error_patterns"][0][1] >= 1
    
    def test_empty_content(self):
        """Test handling of empty log content."""
        result = process_log_events("")
        
        assert result["total_lines"] == 0
        assert result["error_count"] == 0
        assert result["warning_count"] == 0
        assert result["info_count"] == 0
        assert result["error_lines"] == []
        assert result["top_error_patterns"] == []
    
    def test_recent_errors_limit(self):
        """Test that only recent errors are included."""
        lines = [f"[ERROR] Error {i}\n" for i in range(20)]
        log_content = "".join(lines)
        
        result = process_log_events(log_content)
        
        # Should only include last 10 errors
        assert len(result["error_lines"]) <= 10
    
    def test_pattern_ranking(self):
        """Test that patterns are ranked by frequency."""
        log_content = """
[ERROR] Pattern A
[ERROR] Pattern A
[ERROR] Pattern A
[ERROR] Pattern B
[ERROR] Pattern B
[ERROR] Pattern C
        """.strip()
        
        result = process_log_events(log_content)
        
        # Top pattern should have highest count
        top_patterns = result["top_error_patterns"]
        if len(top_patterns) >= 2:
            assert top_patterns[0][1] >= top_patterns[1][1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
