"""Worker entrypoint for the Chonk Line.

Connects outbound to the Mistral Workflows API, registers the chonk-line
workflow, and waits for executions. While this process runs, the line is up.
"""
import asyncio
import sys
from pathlib import Path

# Make 'src' importable regardless of working directory.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from mistralai_workflows import discover_workflows, run_worker


async def main() -> None:
    print("Chonk Line worker starting...")
    discovered = discover_workflows()
    print("Discovered workflows:", discovered)
    await run_worker(discovered)


if __name__ == "__main__":
    asyncio.run(main())
