def normalize_degrees(degrees: float) -> float:
    if degrees < -180:
        return degrees + 360
    if degrees > 180:
        return degrees - 360
