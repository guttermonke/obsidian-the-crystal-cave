# For a future Mistral managed deployment.
# NOTE: managed deployments require pay-as-you-go billing on the Mistral org;
# the Free plan cannot run them. The self-hosted worker path (see README) is
# the zero-cost route and is what the ensemble uses today.
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./
COPY src ./src
COPY scripts ./scripts

RUN pip install --no-cache-dir .

CMD ["python", "-m", "src.entrypoints.worker"]
