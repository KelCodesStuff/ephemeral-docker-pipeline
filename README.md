# Ephemeral Docker Testing Pipeline

This repository demonstrates a containerized testing architecture using Docker multi-stage builds.

## Architecture Highlights

**State Isolation:** Tests are executed inside a disposable Docker container (`--rm`), ensuring zero state leakage between runs and eliminating environmental flakiness.

**Multi-Stage Builds:** Separates the production payload from testing dependencies, keeping the base image lean while providing a fully featured ephemeral environment for validation.

**CI/CD Ready:** The included Makefile provides a standardized entry point for pipeline runners like CircleCI or Buildkite to trigger automated validation.

## Directory Structure

```
ephemeral-docker-pipeline/
├── src/
│   └── math_ops.py
├── tests/
│   └── test_math_ops.py
├── Dockerfile
├── Makefile
├── requirements-test.txt
└── README.md
```

## Usage

Run the full ephemeral test suite with a single command:

```bash
make test
```

This will:
1. Build a Docker image targeting the `test` stage
2. Spin up a disposable container
3. Execute the pytest suite inside the container
4. Automatically remove the container on exit (`--rm`)