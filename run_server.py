#!/usr/bin/env python3
"""
Standalone runner for aider-mcp-server without UV dependency
"""
import sys
import os
import subprocess
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    # Get the directory containing this script
    script_dir = Path(__file__).parent
    
    # Add the src directory to Python path
    src_dir = script_dir / "src"
    sys.path.insert(0, str(src_dir))
    
    try:
        # Import and run the aider MCP server
        from aider_mcp_server import main as aider_main
        aider_main()
    except ImportError as e:
        logger.error(f"Failed to import aider_mcp_server: {e}", exc_info=True)
        logger.error("Make sure dependencies are installed: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error running aider-mcp-server: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()