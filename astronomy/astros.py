import swisseph as swe
from pathlib import Path

swe.set_ephe_path(str(Path(__file__).parent.parent / "eph"))
JD = swe.julday(1992, 1, 22, 10 + 1 / 12)
print(swe.utc_to_jd(1992, 1, 22, 10, 5, 0, 1))
print(JD)

PLANETS = {
    "sun": swe.SUN,
    "moon": swe.MOON,
    "mercury": swe.MERCURY,
    "venus": swe.VENUS,
    "mars": swe.MARS,
    "jupiter": swe.JUPITER,
    "saturn": swe.SATURN,
    "uranus": swe.URANUS,
    "neptune": swe.NEPTUNE,
    "pluto": swe.PLUTO,
    "chiron": swe.CHIRON,
    "lilith": swe.MEAN_APOG,
    "ceres": swe.CERES,
    "vesta": swe.VESTA,
    "pallas": swe.PALLAS,
    "juno": swe.JUNO,
}

PLANETS_BY_TYPE = {
    "sun": "luminary",
    "moon": "luminary",
    "mercury": "personal",
    "venus": "personal",
    "mars": "personal",
    "jupiter": "social",
    "saturn": "social",
    "uranus": "transpersonal",
    "neptune": "transpersonal",
    "pluto": "transpersonal",
    "chiron": "other",
    "lilith": "other",
    "ceres": "other",
    "vesta": "other",
    "pallas": "other",
    "juno": "other",
}
