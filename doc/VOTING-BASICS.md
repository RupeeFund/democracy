# Basics of Voting

The Rupee Fund pools funds from many contributors over a few months.
Contributors nominate projects. The minimum attributes of a project
are an ID, name, and a range of funding requested(minimum, maximum).

Contributors then vote for their projects. A contributor may vote
for one or more projects, and split their single vote across them
flexibly - e.g. 10% to project A, 70% to project D, and 20% to
project Z.  As part of the vote, a contributor can suggest 
that a portion of the fund be carried over to the next season.

Each vote includes a denominator component, and for every project
there is a numerator. Sum of all numerators in a vote may not
exceed the denominator. To avoid pitfalls of floating point
numbers, we use only integer arithmetic. 

In a CSV representation, a vote looks like this:

VID,carry-over-fund,denominator,"numerator1/pid1|numerator2/pid2|...|numeratorN/pidN"

Here: VID is the voter ID, pid1-N are project IDs

# Tallying votes

To normalize the voting numbers, the LCM of all the denominators
is used. LCM/denominator is used as the scaling factor for all
the numerators.

The scaled numerators for each project are then summed
separately - giving us the aggregate vote for each project.

The median value of the carry-over fund is kept aside, and excluded
from the fund allocated to projects. The remaining amount is available
for allocation to the winners of the vote.

The projects are then sorted by descending order of votes to give
us the funding order. Two or more projects could end up getting the
same number of votes. To deal with this, the sorted project list is
grouped into buckets, where each bucket holds projects with exactly
the same number of votes.

Let bucket(0..n) be the buckets of grouped projects, sorted in
descending order of votes. Each bucket consists of a set of projects,
each of which has a minimum and maximum funding requirement.

We start the allocation loop with Funused =  Ftotal - Fcarry

Loop over each bucket:

1. Fbucketmax = sum of max funding of all projects in bucket
2. Fbucketmin = sum of min funding of all projects in bucket
3. if Funused >= Fbucketmax:
     fund all projects in bucket, to their max requested
     Funused -= Fbucketmax
   elif Funused < Fbucketmin:
     done with processing all buckets
   else:
     Fbucketrange = sum of (max-min) funding of all projects in bucket
     factor = (Funused-Fbucketmin)/Fbucketrange
     fund all projects in bucket, to the range of their minimum requested + ((max-min) x factor)
     reduce Funused by the fund spent
     done with processing all buckets

# Authors

Shree Kumar

# License

CC-BY-SA-4.0
