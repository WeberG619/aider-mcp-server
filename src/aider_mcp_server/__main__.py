import argparse
import asyncio
import logging
import sys
from aider_mcp_server.server import serve
from aider_mcp_server.atoms.utils import DEFAULT_EDITOR_MODEL

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    try:
        # Create the argument parser
        parser = argparse.ArgumentParser(description="Aider MCP Server - Offload AI coding tasks to Aider")

        # Add arguments
        parser.add_argument(
            "--editor-model",
            type=str,
            default=DEFAULT_EDITOR_MODEL,
            help=f"Editor model to use (default: {DEFAULT_EDITOR_MODEL})"
        )
        parser.add_argument(
            "--current-working-dir",
            type=str,
            required=True,
            help="Current working directory (must be a valid git repository)"
        )

        args = parser.parse_args()

        logger.info(f"Starting aider-mcp-server with model={args.editor_model}, cwd={args.current_working_dir}")

        # Run the server asynchronously
        asyncio.run(serve(
            editor_model=args.editor_model,
            current_working_dir=args.current_working_dir
        ))
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server crashed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()