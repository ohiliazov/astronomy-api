from collections import defaultdict
from copy import deepcopy

from utils import normalize_degrees

ASPECTS = {
    0: "conjunction",
    30: "semisextile",
    60: "sextile",
    90: "quadrature",
    120: "trigone",
    150: "quincunx",
    180: "opposition",
}

DEFAULT_ORBS = {
    "luminary": {0: 10, 30: 3, 60: 5, 90: 6, 120: 8, 150: 5, 180: 10},
    "personal": {0: 7, 30: 2, 60: 4, 90: 5, 120: 6, 150: 2, 180: 7},
    "social": {0: 6, 30: 1.5, 60: 3, 90: 4, 120: 5, 150: 3, 180: 6},
    "transpersonal": {0: 5, 30: 1, 60: 2, 90: 3, 120: 4, 150: 2, 180: 5},
    "other": {0: 5, 30: 1, 60: 2, 90: 3, 120: 4, 150: 2, 180: 5},
}


def calculate_aspect(first, second, orbs) -> int:
    first_lon = normalize_degrees(first.position.longitude)
    second_lon = normalize_degrees(second.position.longitude)
    diff = abs(first_lon - second_lon)

    for a in ASPECTS:
        if -orbs[a] / 2 <= diff - a <= orbs[a] / 2:
            return a


def aspect(first, second, orbs=None):
    if not orbs:
        orbs = deepcopy(DEFAULT_ORBS)

    aspects_first = calculate_aspect(first, second, orbs[first.type])
    aspects_second = calculate_aspect(first, second, orbs[second.type])

    if aspects_first is None and aspects_second is None:
        return None

    if aspects_first is not None and aspects_second is not None:
        direction = "bidirectional"
    else:
        direction = "unidirectional"

    return {
        "name": ASPECTS[aspects_first],
        "direction": direction,
        "first": {
            "name": first.name,
            "exist": aspects_first is not None,
        },
        "second": {
            "name": second.name,
            "exist": aspects_second is not None,
        },
    }


def aspects(planets: dict):
    acc = defaultdict(list)

    for planet1_key, planet1 in planets.items():
        for planet2_key, planet2 in planets.items():
            if planet1_key != planet2_key:
                if not acc[planet2_key]:
                    aspects_found = aspect(planets[planet1], planets[planet2])
                    acc[planet1_key].append(aspects_found)

    return acc
