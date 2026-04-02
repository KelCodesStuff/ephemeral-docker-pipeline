def calculate_acceleration(vi: float, vf: float, t: float) -> float:
    if t == 0:
        raise ValueError("Time cannot be zero.")
    return (vf - vi) / t

def calculate_displacement(vi: float, a: float, t: float) -> float:
    return (vi * t) + (0.5 * a * (t ** 2))

def calculate_momentum(m: float, v: float) -> float:
    return m * v

def calculate_velocity(d: float, t: float) -> float:
    if t == 0:
        raise ValueError("Time cannot be zero.")
    return d / t
