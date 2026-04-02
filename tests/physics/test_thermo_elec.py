"""
Unit tests for thermodynamics and electromagnetism physics formulas.
Tests Ideal Gas Law, Ohm's law, and Coulomb's law.
"""
import pytest
import math
from src.physics.thermo_elec import calculate_ideal_gas_pressure, calculate_ohms_law_voltage, calculate_coulombs_law_force

def test_calculate_ideal_gas_pressure():
    # Ideal gas law validation for Standard Temperature and Pressure parameters
    pressure = calculate_ideal_gas_pressure(1, 273.15, 22.4)
    assert 101 < pressure < 102
    
    # Validation against division by zero volume
    with pytest.raises(ValueError):
         calculate_ideal_gas_pressure(1, 273.15, 0)

def test_calculate_ohms_law_voltage():
    # Voltage calculation for 2 Amps through 50 Ohms
    assert calculate_ohms_law_voltage(2, 50) == 100

def test_calculate_coulombs_law_force():
    # Electrostatic force between two 1 Coulomb charges separated by 1 meter
    force = calculate_coulombs_law_force(1, 1, 1)
    assert math.isclose(force, 8.98755e9)
