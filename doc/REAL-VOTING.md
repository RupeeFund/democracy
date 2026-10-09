# Voting Mechanism

Document Status: **DRAFT**. Comments are open

This is the proposed voting mechanism for The Rupee Fund (TRF).

TRF pools funds from contributors over a season (3 months). Contributors nominate
projects. Contributors also vote on the projects to decide which projects must
get funded. Thus, we refer to contributors as voters.

Each voter has equal weight, independent of their contribution to the fund.
Whether someone contributes Rs 15 or Rs 1024 or more - they get only exactly
one vote.

## Voters Vote On These

Each voter primarily helps make decisions at two levels:

1. Selects zero, one or projects for funding.  A voter can contribute their full
   vote, or a fraction to any project, flexibly.
2. Indicate how much of the pool must be carried over to the next season without
   being used to fund ANY projects in the current season.

## Two Phase Voting

Voting happens in two phases:

1. Phase 1 : voters are unaware of each other's choices. Projects are listed at
   random for every voter. This voting phase lasts 1 week. Voters are allowed
   to vote as many times as they want - only the last vote of every voter is
   considered as the valid vote. At the end of phase 1, the results are
   published as a "pulse of the result".
2. Phase 2 : With the "pulse" results out. Projects are now rearranged in order
   of the accrued votes. Voters have 1 more week to change their vote. As in phase
   1, a voter may vote multiple times, with only the last vote considered valid.
   Folks who did not participate in the first phase also can vote till the end of
   phase 2.

The results at the end of phase 2 are the final result of the voting.

The two phase result is designed to enhance the overall feeling of satisfaction for
the entire group: sometimes, voters assume that the group thinks something else.
Voters may also be unaware of what others think are promising projects - as they
would not have floated up at the time of their vote. The second phase is designed
to fix this. As a side effect, this overall allows voters a maximum of 2 weeks to
vote.

For details of how votes are tallied, refer [this document](VOTING-BASICS.md)

## Voting User Interface

Categories are a way for individuals to think about projects. A project may
belong to more than one category. Projects self classify themselves based on
various limits (to be documented later).

Projects are grouped into a few categories for ease of selection:

1. Categories organized by community/adopter size: nascent, small-mid size, and large
   projects
2. Categories based on the timeline for which the funding is requested - "immediate",
   "short to mid term" and "long term". 

When a user selects a project, they also get the option to specify what fraction
of their vote must go to the project - typically a percentage, but they could enter
a generic N/M fractional vote. This is the default. If they select say 3 projects,
then each would get 1/3 of the vote, unless changed on the user interface.

Voters can also specify a part of the pool that will be carried over to the
next season. The user interface will ensure that the total of all the funded
projects and the carry-over funds don't exceed the pool size.

## Communities

In Season 1, everyone votes on all the projects.  We call this the "General Community"
vote. At this point, the will of the community wouldn't be known, so voting is kept
generic.

"General Community" based voting would adequately represent our community initially.
However, we are a pluralistic society.  As the number of contributors grows, and the
funding grows, formal and ad-hoc communities may form, and become interested in creating
their own causes/projects, campaign for them, etc.  Such groups will be termed
"Special Communities".

Any project may be part of only one Community - the "General Community" or one of the
"Special Communities". A project may move to a Special Community, only on invitation/
permission of that community. A project may return to the General Community at any point
without permission.

Formation of a Community may need endorsements from multiple community members, or
making a contribution relative to the popularity of the proposer (we don't want to
be hijacked by money power!), or a mix of both. If a community fails to attract
enough voters, it may get dissolved after a set number of seasons - say 4 seasons.
The exact rules and limits have to be discussed, and maybe voted upon and finalized.
Limits may be revised every year.

## What's a "Project"

A project is a specific activity for which funds are sought - either done in the past,
or to be done in the future.  A project is associated with one or more individuals -
who will receive funds.  For a project nomination to complete, TRF will require approval
from every individual in the project to be listed under it. 

Each individual listed under a project must be listed with their complete legal
name. Alias/Nickname is allowed as an add-on, not as the primary identity.

A project requires the following:

1. Title
2. Description
3. Funds Requested (a maximum value, and a minimum value)
4. Overall purpose of funds
5. Campaign page/video
5. Categories
6. Team - one or more individuals, affliation, each with a clear photograph,
   split of fund for each, and how they will use the funds . Plus any relevant
   social media handles, or blog links etc. Idea is to have enough info here to
   build trust. The split of funds can be a range. This range allows us to
   flexibly allocate the funds, when the project gets selected in the vote.

Funds may go the the actual team members identified, or to one or more "fiscal
hosts".  A fiscal host may be a hosting organization (e.g. deparatment or club
account in a college, registered project account, company, etc), or a
parent/guardian/teacher (for students), etc.

Any project may not request the entire pool.  Exact limits may need community
feedback (initial voting!). Nominally, not than 1/4 of a season pool. Why this
restriction? Choosing a sole winner is probably not a good idea. Multiple winners
acts as a pressure release, compared to a winner takes all vote.

We will also need to decide on the minimum funding that a project is allowed to
request.  Should this be 10k, 20k, 25k, etc ? This may also get voted upon by
the initial community prior to season 1.

A team member may be part of more than one project. During voting, the user interface
is expected to clearly show members that may get funding from multiple projects, based
on the selected projects.

## Timeline

Tentatively, we can shoot for the below timeline. Season begins at T0

1. T0 : fund pooling starts
2. T0 + 1 months : nominations window open for projects
3. T0 + 3 months + 2 days : nominations window close (1 month + 2 days)
3. T0 + 4 months : projects final
4. T0 + 4 months + 2 day : voting phase 1 start
5. T0 + 4 months + 9 days : voting phase 2 start
6. T0 + 4 months + 16 days : voting results final
7. T0 + 4 months + 23 days : funds transferred out

The timeline for a season is kept relaxed, to account for the voluntary nature of
reviews and approvals.

## Creating, Retaining and Multiplying Trust

We are in India - the world's most populous country. We have to design for scale
from day 1. The single largest challenge for us it to maintain trust.  There is
no guarantee that we'll grow massive.  If we do treat Trust as a Day 0 requirement,
and design for it - then we may well have a better chance.  The downside is potentially
higher friction in early days of the fund.  But this would also mean that whoever starts
and stays with us for the journey may not move away as easily - if and when controversies
arise. It would naive to think that we will one fine day be successful in making
27 million people (or 50 million, or whatever that number is in the future) believe in
this idea - without some hiccups along the way.

How do we do all this? We carefully design for trust.  We don't have to do everything
during Season 1, but it's important to understand as many aspects of this as possible

1. Voters must not feel cheated. And if they do, there may be consequences. But
   we have to be mindful of people misusing various mechanisms. With careful
   design, we may be able to reduce possibility for misuse of the platform.
2. Any funded individuals history will be visible. E.g. during voting, voters will
   see for how many times they have been funded, and total funding raised.  The
   individual may want to use this as "badge" of sorts elsewhere too.
3. We might want to provide other ways in which funded individuals can build trust,
   without getting noisy in emails or on the pages.  We must also lay clear guidelines
   for these.

We will need to have an "allegation" mechanism.  We will listen to external feedback,
and will make all reasonable attempts to explain our stance.  However, only contributors
will be able to raise allegations. Any allegations must be supported by "data" in it.
Allegations not supported by data may be junked.

## Visibility is Trust

Scale we want to reach. And fraud we want to stay away from. And trust we want to inspire.
In ourselves, and The Rupee Fund.

That's our biggest challenge. Let's use data as our shield.

What data do we need to keep?

1. Phone numbers of those who nominate projects. Why? Our contribution threshold is low. So any
   fraudster can get in for less than the price of a cup of tea :) Appropriate measures we have
   to take, so that we don't get caught unawares.  This might start becoming a problem starting
   when we hit even a modest measure of success.

2. Phone numbers of everyone who is part of a project.  Student contributors under 18 must be
   represented by someone else - a parent, guardian, teacher, school/college department, etc
   with a contact number. We need to tread carefully here, and maybe even set the right limits

3. Emails are a must for all non students !?

4. Clear, high resuolution photographs of any real person.  If somebody is requesting funds,
   or suggesting that somebody else is a good candidate, then we deserve to know exactly who
   we are dealing with.

5. As the project scales, so will the risk of fraud. How do we ensure we are dealing with
   genuine people ? Build a trust system. Manual verification by volunteers may work. We
   may also require nominators to volunteer to verify randomly selected people. Our processes
   could require logged video recordings. In today's world of sophisticated spoofing, all
   this may not necessarily guarantee anything.

6. We can't give our contributors an absolute guarantee that we won't every get frauded,
   but we will try our level best. That's one reason to keep more data around than what
   we absolutely need.  And a good verification trail. Our fund transfers will be based
   on UPI IDs or Bank Transfers, that can act as useful identification too - as financial
   institutions locally have strict KYC norms for compliance purposes.

Ideas from here will be distilled to create our Governance document.

## Vote Database

An anonymized voting database may be made available. Availability will be restricted
to contributors. We don't want random people showing up and asking for data.  Data
may not be available for general download.  Must be requested by email, with the right
formatting, by contributors?  Why all these restrictions ? Our database may grow pretty
quickly, and we shouldn't create structures that will add to our burden.  Now you may ask
- isn't looking at emails burden ? No - not if this can be done automatically without
human intervention in most cases. We will be essentially following good practices here
- know who you are giving data to, and how they will be using it. Data will continue to
be licensed under CC-BY-SA-4.0, requiring attribution to The Rupee Fund.

## Anonymity in Voting

Most systems try to implement this by default.  But we are an online system.  So, no matter
what we'd have some notion of "traceability" to "identity", unless we outsource the voting
itself to third parties.

Is anonymity a good default choice for most voting systems ? Yes. But from a point of
view of "giving", visibility is not necessarily a bad end goal.  Many forms of giving try
to setup tiers of visibility based on the magnitude of the contribution. But, we are The
Rupee Fund. We can't operate that way.

Not being anonymous could broadly have three applications:

1. Verification. Is the system correctly accounting for my vote ?
2. Proving to somebody else that "I voted for you".
3. Public show support in the winning cause. But we aren't a "social" network at this
   point. Else we could have shown "Supported by Venkatraman Kartik Balakrishnan and
   978 others (show list)". At this point, for funded projects, we'd show "Supported by 
   979 rupee funders"

There is a case to not having this option altogether.  Technically, in a relationship
involving power - somebody could coerce somebody else to reveal their identity this way.
But it could also be argued that if the enforcer has so much coercive power, then any
voting method that is "online" not work.  But this "identity proving business" does add
an additional detriment - even privately done voting isn't safe, as the coercive boundary
stretches outside the bounds of privacy.

So - here's what we can do. Whether to remain anonymous is a user's choice, exercised during
the vote.  By default the checkbox will be "ON".  But if the checkboox is turned "OFF",
what should happen? The user will have the option of providing an "anonymizing key".
The hash of the voter is computed using SHA256 for this string: secret-key+uppercase(PAN)+email

"secret-key" is stored in the system. However, it will not be known to others.

For verification, we must still pass through the hash to the voting database. We can use a
two pass approach for this:

1. Pass 1: for all votes, compute SHA256 hash on full string. If it's a non-anonymous vote,
   add prefix "nan-"
2. Pass 2: deduplicate hashes, without touching the "nan-" votes. By assigning a sequence number,
   we can significantly reduce the size of the voting database.

These two steps merely illustrate the scheme. There are more efficient ways of implementing
this :)

## Overall Vision

The Rupee Fund is a democratic movement designed for anyone who wants to encourage the creation
of all types of projects based on Free and Open ideas. Contributors help identify/discover and
recognize/fund projects. And each project is ultimately a set of individuals. In this sense,
The Rupee Fund is "by the people and for the people".
 
The underlying theme of the Fund is that we have all benefitted from the Free and Open world.
We believe that only the goodness in everyone can build a world that is more Free and more Open,
than it was in the past. And for this mission, we seek collective action. Not for ourselves,
but for the Whole Wide World.

# License

CC-BY-SA-4.0
