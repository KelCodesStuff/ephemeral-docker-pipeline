# Stage 1: Base Application Environment
FROM python:3.11-slim as base

# Set the working directory inside the container
WORKDIR /app

# Copy the application source code
COPY src/ /app/src/

# Stage 2: Ephemeral Testing Environment
FROM base as test

# Copy test files and testing requirements
COPY tests/ /app/tests/
COPY requirements-test.txt /app/

# Install testing dependencies (e.g., pytest)
RUN pip install --no-cache-dir -r requirements-test.txt

# Set the default command to run the test suite
# This executes automatically when the container runs
ENV PYTHONPATH=/app
CMD ["pytest", "tests/"]
