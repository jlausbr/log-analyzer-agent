"""Main entry point for the log analyzer agent."""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from agent.state import LogAnalysisState
from agent.graph import create_log_analyzer_agent


def main():
    """
    Main function to run the log analyzer agent.
    """
    load_dotenv()
    
    # Validate API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set in .env file")
        print("Please create a .env file with your OpenAI API key.")
        sys.exit(1)
    
    # Create the agent
    print("Initializing Log Analyzer Agent...")
    agent = create_log_analyzer_agent()
    
    # Example input: use the sample log file
    log_file = "examples/logs/app.log"
    
    if not Path(log_file).exists():
        print(f"ERROR: Log file not found: {log_file}")
        sys.exit(1)
    
    print(f"\nAnalyzing log file: {log_file}")
    print("=" * 60)
    
    # Create initial state
    initial_state = LogAnalysisState(log_file_path=log_file)
    
    # Run the agent
    try:
        result = agent.invoke(input=initial_state)
        
        # Display results
        print("\n" + "=" * 60)
        print("ANALYSIS COMPLETE")
        print("=" * 60)
        
        if result.validation_errors:
            print(f"\nValidation Errors: {result.validation_errors}")
        
        if result.report:
            print(f"\n{result.report}")
            
            # Save report to file
            output_path = os.getenv("REPORT_OUTPUT_PATH", "examples/reports/")
            Path(output_path).mkdir(parents=True, exist_ok=True)
            
            report_file = Path(output_path) / "latest_report.md"
            report_file.write_text(result.report)
            print(f"\nReport saved to: {report_file}")
        else:
            print("\nNo report generated.")
    
    except Exception as e:
        print(f"\nERROR: Agent execution failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
