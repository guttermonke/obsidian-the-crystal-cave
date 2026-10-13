"""Trigger the chonk-line workflow and print le Chonk's reply.

Usage:
    python scripts/execute.py --message "Hello, le Chonk." --caller "Vibe (Mistral)"
"""
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mistralai import Mistral


def main() -> None:
    parser = argparse.ArgumentParser(description="Send a message to le Chonk and wait for the reply.")
    parser.add_argument("--message", required=True, help="What to say to le Chonk.")
    parser.add_argument("--caller", default="an ensemble agent", help="Who is calling.")
    parser.add_argument("--workflow", default="chonk-line", help="Workflow to trigger.")
    args = parser.parse_args()

    client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
    execution = client.workflows.execute_workflow_and_wait(
        workflow_identifier=args.workflow,
        input={"message": args.message, "caller": args.caller},
    )
    print(execution.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
