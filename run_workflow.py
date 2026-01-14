"""
Runner script for the AI-Proposal Engine POC Workflow
"""

import asyncio
import sys
from pathlib import Path

# Add the poc_implementation directory to the path
sys.path.insert(0, str(Path(__file__).parent / "poc_implementation"))

def run_workflow():
    """
    Run the POC workflow
    """
    try:
        from workflow import run_proposal_engine_poc
        
        print("Running AI-Proposal Engine POC Workflow...")
        print("="*50)
        
        # Run the async workflow
        result = asyncio.run(run_proposal_engine_poc())
        
        print("\n" + "="*50)
        print("POC WORKFLOW EXECUTION COMPLETE")
        print("="*50)
        
        if result and result.get("status") == "success":
            print("✅ POC was successful!")
            print(f"📄 Output generated: {result.get('output_path', 'N/A')}")
        else:
            print("⚠️  POC completed with some issues")
            
        return result
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure you're running from the correct directory")
        return None
    except Exception as e:
        print(f"Error running workflow: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    run_workflow()