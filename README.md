# Ephemeral Docker Testing Pipeline

This repository demonstrates a containerized testing architecture using Docker multi-stage builds.

## Architecture Highlights:

*   **State Isolation**: Tests are executed inside a disposable Docker container (`--rm`), ensuring zero state leakage between runs and eliminating environmental flakiness.
*   **Multi-Stage Builds**: Separates the production payload from testing dependencies, keeping the base image lean while providing a fully featured ephemeral environment for validation.
*   **CI/CD Ready**: The included Makefile provides a standardized entry point for pipeline runners like CircleCI or Buildkite to trigger automated validation.

## How to Run

1.  Ensure you have Docker installed and running on your system.
2.  In the root of the repository, execute the following command:

```bash
make test
```

This will automatically build the ephemeral testing environment and run the test suite inside the container. Once the tests complete, the container will automatically be removed.

## Test Suite Structure

The testing suite is located in the `tests/` directory and is segmented by physical domain to mirror the source code structure.

*   `tests/physics/test_kinematics.py`: Validates motion formulas (velocity, acceleration, momentum, displacement).
*   `tests/physics/test_dynamics.py`: Validates force formulas (Newton's laws, friction, centripetal/gravitational forces).
*   `tests/physics/test_energy.py`: Validates energy and work functions (kinetic, potential, power, work done).
*   `tests/physics/test_thermo_elec.py`: Validates thermodynamic and electrical calculations (Ideal Gas Law, Ohm's Law, Coulomb's Law).

All tests utilize `pytest` to ensure accurate mathematical calculations and proper boundary/exception handling (e.g., preventing divide-by-zero errors).