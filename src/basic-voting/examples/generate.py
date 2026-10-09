#!/usr/bin/env python3
"""Generate sample projects-30.csv and votes-300.csv for tally.py.

Usage:
    generate.py [OUT_DIR]

OUT_DIR defaults to the directory containing this script. A fixed random
seed is used, so the output is identical on every run.
"""

import csv
import random
import sys
from pathlib import Path

NAMES = [
    "Open-source Indic OCR engine", "Open hardware water quality sensor",
    "Libre 3D-printable prosthetic hand", "FOSS clinic records system",
    "Open-design solar charge controller", "3D-printable lab equipment library",
    "Open-source farm weather station", "Libre Kannada speech dataset",
    "Open-source school timetable app", "Open hardware air quality monitor",
    "Libre screen reader voice for Tamil", "Open-design bus stop wayfinding signs",
    "Open-source rainwater harvesting designs", "Open hardware low-cost microscope",
    "FOSS offline learning server", "Open-source waste collection route planner",
    "3D-printable playground parts", "Libre textbook translation toolkit",
    "Open-design cargo bicycle frame", "CC-BY-SA illustration library",
    "Community mesh Wi-Fi firmware", "Open-source animal shelter tracker",
    "Open-design menstrual cup mould", "FOSS flood alert SMS gateway",
    "Open seed variety database", "Libre Braille embosser",
    "Open-source theatre lighting controller", "Open first-aid training manual",
    "Open-design composting unit", "Libre point-of-sale app for vendors",
]
NUM_VOTES = 300
DENOMINATORS = [1, 2, 3, 4, 5, 10, 100]
CARRY_OVER_CHOICES = [0] * 3 + [10000, 25000, 50000, 75000, 100000]


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    out = Path(argv[0]) if argv else Path(__file__).resolve().parent
    rng = random.Random(42)

    projects = []
    for i, name in enumerate(NAMES, 1):
        lo = rng.randrange(5, 60) * 1000
        hi = lo + rng.randrange(0, 50) * 1000
        projects.append((f"P{i:02d}", name, lo, hi))
    with open(out / "projects-30.csv", "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["PID", "name", "min", "max"])
        w.writerows(projects)

    # Skew popularity so some projects clearly lead the vote.
    weights = [rng.choice([1, 2, 3, 5, 8, 13]) for _ in projects]
    with open(out / "votes-300.csv", "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["VID", "carry-over", "denominator", "shares"])
        for v in range(1, NUM_VOTES + 1):
            denom = rng.choice(DENOMINATORS)
            k = rng.randint(1, 5)
            pids = []
            while len(pids) < k:
                pid = rng.choices(projects, weights)[0][0]
                if pid not in pids:
                    pids.append(pid)
            # Split up to the whole denominator; sometimes leave part unused.
            budget = denom - (rng.randrange(denom) if rng.random() < 0.1 else 0)
            cuts = sorted(rng.randint(0, budget) for _ in range(len(pids) - 1))
            parts = [b - a for a, b in zip([0] + cuts, cuts + [budget])]
            shares = "|".join(f"{n}/{p}" for n, p in zip(parts, pids) if n > 0)
            w.writerow([f"V{v:03d}", rng.choice(CARRY_OVER_CHOICES), denom, shares])


if __name__ == "__main__":
    main()
