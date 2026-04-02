"""
Unit tests for dynamics physics formulas.
Tests core force calculations including Newton's laws, centripetal force, friction, and gravity.
"""
import pytest
from src.physics.dynamics import calculate_newtons_second_law, calculate_centripetal_force, calculate_friction_force, calculate_gravitational_force

def test_calculate_newtons_second_law():
    # 5kg mass * 9.8m/s^2 acceleration = 49.0N force
    assert calculate_newtons_second_law(5, 9.8) == 49.0

def test_calculate_centripetal_force():
    # Centripetal force of 2kg mass moving 5m/s in 10m radius path
    assert calculate_centripetal_force(2, 5, 10) == 5.0
    
    # Ensure radius of 0 raises a ValueError
    with pytest.raises(ValueError):
        calculate_centripetal_force(2, 5, 0)

def test_calculate_friction_force():
    # Friction with mu=0.5 and Normal force=100N
    assert calculate_friction_force(0.5, 100) == 50.0

def test_calculate_gravitational_force():
    # Approximate gravitational force on a 1kg mass at Earth's surface
    assert 9.8 < calculate_gravitational_force(1, 5.972e24, 6371000) < 9.83
