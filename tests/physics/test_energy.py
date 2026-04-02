"""
Unit tests for energy and work physics formulas.
Tests potential energy, kinetic energy, work done, and power consumption.
"""
import pytest
import math
from src.physics.energy import calculate_potential_energy, calculate_work_done, calculate_power, calculate_kinetic_energy

def test_calculate_potential_energy():
    # Potential energy of a 10kg mass 5m off the ground
    assert calculate_potential_energy(10, 5) == 490.0

def test_calculate_work_done():
    # Work done by 10N force over 5m at 60 degrees. Cos(60) is roughly 0.5
    assert math.isclose(calculate_work_done(10, 5, 60), 25.0)

def test_calculate_power():
    # Power generated from 100 Joules over 10 seconds
    assert calculate_power(100, 10) == 10.0
    
    # Time equal to zero should raise error
    with pytest.raises(ValueError):
        calculate_power(100, 0)

def test_calculate_kinetic_energy():
    # Kinetic energy of a 2kg mass moving at 3m/s
    assert calculate_kinetic_energy(2, 3) == 9.0
