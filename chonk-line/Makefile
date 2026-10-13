.PHONY: start-worker execute

start-worker:
	python -m src.entrypoints.worker

# Usage: make execute MESSAGE="Hello, le Chonk." CALLER="Vibe (Mistral)"
execute:
	python scripts/execute.py --message "$(MESSAGE)" --caller "$(CALLER)"
