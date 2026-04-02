import math

def calculate_potential_energy(m: float, h: float, g: float = 9.8) -> float:
    return m * g * h

def calculate_work_done(f: float, d: float, theta_degrees: float) -> float:
    theta_radians = math.radians(theta_degrees)
    return f * d * math.cos(theta_radians)

def calculate_power(w: float, t: float) -> float:
    if t == 0:
        raise ValueError("Time cannot be zero.")
    return w / t

def calculate_kinetic_energy(m: float, v: float) -> float:
    return 0.5 * m * (v ** 2)
