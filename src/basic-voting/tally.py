#!/usr/bin/env python3
"""Tally Rupee Fund votes and allocate the funding pool.

Implements the process described in doc/VOTING-BASICS.md, using only
integer arithmetic.

Usage:
    tally.py projects.csv votes.csv FUND_TOTAL

projects.csv rows:  PID,name,min-funding,max-funding
votes.csv rows:     VID,carry-over-fund,denominator,"num1/pid1|num2/pid2|..."

A header row is optional in both files (detected by a non-numeric
funding/denominator column). Blank lines and lines starting with '#'
are ignored.
"""

import argparse
import csv
import sys
from dataclasses import dataclass
from math import gcd


class InputError(Exception):
    pass


@dataclass
class Project:
    pid: str
    name: str
    min_fund: int
    max_fund: int


@dataclass
class Vote:
    vid: str
    carry_over: int
    denominator: int
    shares: list  # [(numerator, pid), ...]


def _rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        for lineno, row in enumerate(csv.reader(f), start=1):
            row = [c.strip() for c in row]
            if not row or not any(row) or row[0].startswith("#"):
                continue
            yield lineno, row


def _int(value, what, path, lineno):
    try:
        return int(value)
    except ValueError:
        raise InputError(f"{path}:{lineno}: {what} must be an integer, got {value!r}")


def read_projects(path):
    projects = {}
    for lineno, row in _rows(path):
        if len(row) < 4:
            raise InputError(f"{path}:{lineno}: expected PID,name,min,max")
        pid, name, lo, hi = row[:4]
        if not projects and not lo.lstrip("-").isdigit():
            continue  # header
        lo = _int(lo, "min funding", path, lineno)
        hi = _int(hi, "max funding", path, lineno)
        if lo < 0 or hi < lo:
            raise InputError(f"{path}:{lineno}: need 0 <= min <= max, got {lo}, {hi}")
        if pid in projects:
            raise InputError(f"{path}:{lineno}: duplicate project ID {pid!r}")
        projects[pid] = Project(pid, name, lo, hi)
    return projects


def read_votes(path, projects):
    votes = []
    seen = set()
    for lineno, row in _rows(path):
        if len(row) < 3:
            raise InputError(f"{path}:{lineno}: expected VID,carry-over,denominator,shares")
        vid, carry, denom = row[:3]
        if not votes and not denom.isdigit():
            continue  # header
        carry = _int(carry, "carry-over fund", path, lineno)
        denom = _int(denom, "denominator", path, lineno)
        if carry < 0:
            raise InputError(f"{path}:{lineno}: carry-over fund may not be negative")
        if denom <= 0:
            raise InputError(f"{path}:{lineno}: denominator must be positive")
        if vid in seen:
            raise InputError(f"{path}:{lineno}: duplicate voter ID {vid!r}")
        seen.add(vid)

        shares = []
        spec = row[3] if len(row) > 3 else ""
        for part in filter(None, (p.strip() for p in spec.split("|"))):
            num, sep, pid = part.partition("/")
            if not sep:
                raise InputError(f"{path}:{lineno}: bad share {part!r}, expected numerator/pid")
            num = _int(num.strip(), "numerator", path, lineno)
            pid = pid.strip()
            if num < 0:
                raise InputError(f"{path}:{lineno}: numerator may not be negative")
            if pid not in projects:
                raise InputError(f"{path}:{lineno}: unknown project ID {pid!r}")
            shares.append((num, pid))
        if sum(n for n, _ in shares) > denom:
            raise InputError(f"{path}:{lineno}: numerators exceed denominator {denom}")
        votes.append(Vote(vid, carry, denom, shares))
    return votes


def tally_votes(projects, votes):
    """Sum normalized votes per project.

    Each numerator is scaled by LCM/denominator, where LCM is the least
    common multiple of all denominators, so that votes with different
    denominators carry equal weight and every value stays an integer.
    """
    common = 1
    for v in votes:
        common = common * v.denominator // gcd(common, v.denominator)
    totals = {pid: 0 for pid in projects}
    for v in votes:
        scale = common // v.denominator
        for num, pid in v.shares:
            totals[pid] += num * scale
    return totals, common


def median_carry_over(votes):
    values = sorted(v.carry_over for v in votes)
    if not values:
        return 0
    mid = len(values) // 2
    if len(values) % 2:
        return values[mid]
    return (values[mid - 1] + values[mid]) // 2


def allocate(projects, totals, available):
    """Allocate `available` across vote buckets. Returns (allocations, unspent)."""
    # Projects with no votes are not eligible for funding.
    buckets = {}
    for pid, total in totals.items():
        if total > 0:
            buckets.setdefault(total, []).append(projects[pid])

    allocations = {}
    remaining = available
    for total in sorted(buckets, reverse=True):
        bucket = buckets[total]
        bucket_max = sum(p.max_fund for p in bucket)
        bucket_min = sum(p.min_fund for p in bucket)
        if remaining >= bucket_max:
            for p in bucket:
                allocations[p.pid] = p.max_fund
            remaining -= bucket_max
        elif remaining < bucket_min:
            break
        else:
            # Fund every project its minimum, then share what's left across
            # the bucket in proportion to each project's (max - min) range.
            # bucket_range > 0 here, since bucket_min <= remaining < bucket_max.
            bucket_range = bucket_max - bucket_min
            extra = remaining - bucket_min
            for p in bucket:
                amount = p.min_fund + (p.max_fund - p.min_fund) * extra // bucket_range
                allocations[p.pid] = amount
                remaining -= amount
            break
    return allocations, remaining


def main(argv=None):
    ap = argparse.ArgumentParser(description="Tally Rupee Fund votes and allocate funds.")
    ap.add_argument("projects", help="projects CSV: PID,name,min,max")
    ap.add_argument("votes", help='votes CSV: VID,carry-over,denominator,"num/pid|..."')
    ap.add_argument("fund", type=int, help="total size of the funding pool (integer)")
    args = ap.parse_args(argv)

    if args.fund < 0:
        ap.error("fund must be non-negative")

    try:
        projects = read_projects(args.projects)
        votes = read_votes(args.votes, projects)
    except (InputError, OSError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    totals, _ = tally_votes(projects, votes)
    carry = min(median_carry_over(votes), args.fund)
    allocations, unspent = allocate(projects, totals, args.fund - carry)

    print(f"Carried over fund: {carry + unspent}")
    print(f"  (median carry-over vote: {carry}, unallocated remainder: {unspent})")
    print()
    print("Funded projects:")
    w = csv.writer(sys.stdout, lineterminator="\n")
    w.writerow(["PID", "name", "cumulative-vote", "allocated-fund"])
    for pid in sorted(allocations, key=lambda p: (-totals[p], p)):
        w.writerow([pid, projects[pid].name, totals[pid], allocations[pid]])
    return 0


if __name__ == "__main__":
    sys.exit(main())
