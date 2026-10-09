# Vote tally

`tally.py` tallies votes and allocates the funding pool to
projects, following the rules in [doc/VOTING-BASICS.md](../../doc/VOTING-BASICS.md).

The examples illustrate the basic voting mechanism. Here,
we do not cover the user interface aspects of voting, including
how the projects are arranged, how their details are shown to
users etc.

Treat this as a testbed to generate voting scenarios to match
expected/anticipated voter behaviour. This can be used to
support ideas for evolution of the voting mechanism.

## Requirements

Python 3.7 or later. No other packages are needed.

## Usage

```
python3 tally.py PROJECTS_CSV VOTES_CSV FUND_TOTAL
```

- `PROJECTS_CSV`: one row per project, `PID,name,min,max`
- `VOTES_CSV`: one row per vote, `VID,carry-over,denominator,"num1/pid1|num2/pid2|..."`
- `FUND_TOTAL`: size of the funding pool, as a whole number

A header row is optional in both files.

The output is:

1. **Carried over fund**: the median carry-over vote, plus whatever was
   left unallocated.
2. **Funded projects**: a CSV list of `PID,name,cumulative-vote,allocated-fund`,
   with the most-voted project first.

If an input file has a problem, such as an unknown project ID or numerators
that add up to more than the denominator, the script prints the file and
line number and exits with status 1.

## Running the examples

Run these commands from this directory (`src/voting`).

### Small example: 5 projects, 4 votes

```
python3 tally.py examples/projects.csv examples/votes.csv 30000
```

Expected output:

```
Carried over fund: 750
  (median carry-over vote: 750, unallocated remainder: 0)

Funded projects:
PID,name,cumulative-vote,allocated-fund
P2,Water filter,130,8000
P3,Tree planting,100,6000
P1,School library,95,15250
```

₹750 (the median of the carry-over votes 0, 500, 1000 and 2000) is set
aside. P2 and P3 are funded in full. P1 gets the remaining ₹15,250, which
is between its minimum and maximum. P4 gets nothing, and P5 received no
votes.

### Larger example: 30 projects, 300 votes

```
python3 tally.py examples/projects-30.csv examples/votes-300.csv 500000
```

Expected output:

```
Carried over fund: 35000
  (median carry-over vote: 25000, unallocated remainder: 10000)

Funded projects:
PID,name,cumulative-vote,allocated-fund
P10,Open hardware air quality monitor,9020,23000
P22,Open-source animal shelter tracker,8516,27000
P13,Open-source rainwater harvesting designs,7107,52000
P30,Libre point-of-sale app for vendors,6988,46000
P28,Open first-aid training manual,6724,58000
P05,Open-design solar charge controller,6246,58000
P08,Libre Kannada speech dataset,4961,69000
P06,3D-printable lab equipment library,3286,95000
P03,Libre 3D-printable prosthetic hand,3238,37000
```

Try other pool sizes to see how the allocation changes.

### Regenerating the larger example

`examples/projects-30.csv` and `examples/votes-300.csv` are produced by
`examples/generate.py`. It uses a fixed random seed, so it writes the same
files every time:

```
python3 examples/generate.py              # overwrites the files in examples/
python3 examples/generate.py /some/dir    # writes them to another directory
```
