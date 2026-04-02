def calculate_ideal_gas_pressure(n: float, t_kelvin: float, v: float) -> float:
    if v == 0:
        raise ValueError("Volume cannot be zero.")
    R = 8.314 # Ideal gas constant in J/(mol K)
    return (n * R * t_kelvin) / v

def calculate_ohms_law_voltage(i: float, r: float) -> float:
    return i * r

def calculate_coulombs_law_force(q1: float, q2: float, r: float) -> float:
    if r == 0:
        raise ValueError("Radius cannot be zero.")
    k_e = 8.98755e9 # Coulomb's constant
    return k_e * (q1 * q2) / (r ** 2)
