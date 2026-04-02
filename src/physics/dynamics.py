def calculate_newtons_second_law(m: float, a: float) -> float:
    return m * a

def calculate_centripetal_force(m: float, v: float, r: float) -> float:
    if r == 0:
        raise ValueError("Radius cannot be zero.")
    return (m * (v ** 2)) / r

def calculate_friction_force(mu: float, normal_force: float) -> float:
    return mu * normal_force

def calculate_gravitational_force(m1: float, m2: float, r: float) -> float:
    if r == 0:
        raise ValueError("Radius cannot be zero.")
    G = 6.67430e-11 # Gravitational constant in m^3 kg^-1 s^-2
    return G * (m1 * m2) / (r ** 2)
