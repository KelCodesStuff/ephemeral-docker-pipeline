"""
Unit tests for kinematics physics formulas.
Tests core motion calculations including acceleration, displacement, momentum, and velocity.
Includes error bound checking for invalid zero inputs.
"""
import pytest
from src.physics.kinematics import calculate_acceleration, calculate_displacement, calculate_momentum, calculate_velocity

def test_calculate_acceleration():
    # Test valid acceleration: (10 - 0) / 2 = 5.0
    assert calculate_acceleration(0, 10, 2) == 5.0
    
    # Test zero-time exception handling to prevent ZeroDivisionError
    with pytest.raises(ValueError):
        calculate_acceleration(0, 10, 0)

def test_calculate_displacement():
    # Displacement from rest with a=9.8 over 2 seconds
    assert calculate_displacement(0, 9.8, 2) == 19.6

def test_calculate_momentum():
    # Momentum of 5kg object moving at 10m/s
    assert calculate_momentum(5, 10) == 50.0

def test_calculate_velocity():
    # Velocity of object traveling 100m in 10s
    assert calculate_velocity(100, 10) == 10.0
