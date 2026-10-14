# Nominations

STATE: **DRAFT**

The Rupee Fund exists to find and fund great projects via democractic methods.

Only contributors are voters, and only contributors can nominate projects.
This document uses the words contributor, voter, and member interchangably at
different places.

## Ideal System

In an ideal system, we have to assume a 100% fair and unbiased voter. Fair in the
sense of the ideal that they believe in an equal opportunity for all.  And unbiased
in the sense that they only evaluate the project nomination at "face value" - i.e.
as submitted to our system, without considering any additional context which may be
available for evaluation - which may be from various sources - online platforms,
direct or indirect knowledge of the project and its contributors, their history,
impacts of social media campaigns and influencers and so on.

As TRF community grows, the number of projects may increase, and so we also assume that
to do a great job, the ideal voter has adequate time available for evaluating projects
and voting on them.

This ideal system, as any reader will appreciate, is not practical.  A project
nomination has two effects:

1. Creates visibility for the project
2. Adds additional load for every voter for evaluation.

## Indian Election System

The Indian Election System is hosted in the largest democracy in the world. It has scaled
from a population of 35 crore at independence to almost 150 crore in 2026. Every voter
has one vote. Voting happens independently for all states, and the Union (There is no
"center"). Elections happen at lower levels as well.

Anybody who is not a citizen may not be nominated for an election. Specifically, nomination
requires that anyone contesting an election be registered as a voter.

Depending on the affiliation of the candidate, the nomination process has additional requirements:

1. Members of recognized National/State level parties need 1 proposer
2. An independent candidate needs 10 proposers - voters from the constituency where the
   candidate has applied.

### Lok Sabha Election

Every candidate has to pay a security deposit - 25k for general category, and 12.5k for SC/STs.

### State Assembly Election

The security deposit is 10k INR for general candidates, and 5k for SC/STs.

According to the [ECI website](https://www.eci.gov.in/faq/1/7), Q18:

> In Modakurichi Assembly Constituency of Tamil Nadu there were 1033 contesting candidates
> during the general election to Tamil Nadu Legislative Assembly in 1996. The ballot papers
> were in the form of a booklet.

A defeated candidate who fails to secure more than one sixth of the valid votes polled loses
the deposit. According to news reports, 86% of the candidates who contested the 2024 Lok
Sabha Polls lost their deposit, which is roughly 7200 candidates losing 16.4 crore rupees.
State level statistics seem similar - e.g. the 2026 Tamil Nadu State elections saw 83%
candidates lose their deposit!

The timeline for filing nominations is approximately one month, following by scrutiny,
a last date for withdrawal of candidature, and the eventual election.

Election results follow a first-past-the-post model. The candidate with the highest number
of votes wins.  A voter may only vote for one candidate.

Voting happens in consituencies - where the number of voters may range from two lakh to
38 lakhs, with few constituencies with even lower numbers down to 58 thousand.

An average voting turnout is closer to 65%.

## How our Communities operate

In real world politics, people spend a significant amount on time on the process. Voters
are passive consumers of a daily stream of information courtesy newspapers, media channels,
and so on. There is an implicit hierarchy in the news reportage - and the media plays an
interesting role, creating its own dynamics. The relatively recent emergence of social
media has caused a sea change in campaigning and voter engagement.

Our communities are mostly involved in building great things. Time spent on organizational
activities is relatively low. A relatively small number of projects and organizations have
governance boards and elections, etc

Communities are engaged/enraged on forums, Mastodon, Twitter, LinkedIn, Hacker News, blogs, etc.
Networks are generally informal. People are generally allowed to hide their identity
using features such as usernames. This also enables trolls and bots to operate, generating
significantly more overhead for people trying to manage communities - moderation can be
tiring, and some may even view volunteering as a thankless job. With the rise of AI coding,
there has been much debate on handling volumes of contribution, etc as well.

Our communities run on various ideas of merit, including relevance - potential and actual
adoption. Commit counts, Stars, downloads, upvotes, reddit "karma", etc Some proudly wear
the badges of sponsoring entities - amplifying their own brand as well as those of sponsors.

Projects have generally larger user community, and smaller contributor communities. Projects
and individuals raise funds using sponsors and avenues like direct fundraising (e.g. Blender),
GitHub sponsor, Kickstarter/Indiegogo, various other channel.

Other notable efforts for funding include the Zerodha [FLOSS/Fund](https://floss.fund/)
(1M$ a year globally), [Open Source Pledge](https://opensourcepledge.com/)(strictly speaking
this is a reporting system - 7.5 million $ noted as of Oct, 2026),
thanks.dev([172k USD](https://opencollective.com/thanks-dev) as of Oct, 2026).

## TRF Nomination System Requirements

A good system has to strike a balance. How much time should we expect contributors to
spend on voting ? Remember a contributor may contribute Rs 15, Rs 1024, or anything
else - and independent of all that everyone has exactly one vote.

Any contributor may be considered to have a "right" to nominate a project - i.e.
their own project. 

If they think somebody else's project is a good fit for our community, then they need
to be able to convince at-least one representative from that project to become a member,
so that this new member can nominate their own project. Overall, the right to self
nominate ensures that only believers of the core idea of TRF get funded - and that
belief must be demonstrated by becoming a member.

The right to nominate must be balanced against the tendency in our community to scratch
an "itch" - which is of course healthy at an individual level, but shouldn't end up
adding to overhead for all voters, w.r.t. time required to make a choice.

TRF intends to be lean and efficient by relying entirely on the contributor community
to manage itself. To achieve this, we have the concept of [karma](KARMA.md)
which helps contributors regulate self and collective behaviour.

## Proposed Nomination System

The following process is a reasonable way to solve for these requirements:

1. Initially, voters collectively decide on how many projects they want to vote on.
   Any more projects beyond this consensus get "queued"
2. Everyone gets to nominate only their own project
3. Every nominated project needs 5 contributors to back it. After the required
   backers are secured, the project gets enqueued for acceptance.
4. When a project is enqueued, it may be withdrawn.
5. When the project gets accepted, a small deposit needs to be paid to secure
   listing for voting - say 1024 rupees. The deposit may be paid by either the
   nominator, or the backers, or any other member
6. A listed project has a "time to live" of two seasons. If it does not get
   funded in the first season, it gets listed in the next season as well.
   If it remains unfunded for 2 seasons, without securing a sufficient threshold
   of votes across seasons, then the deposit is lost. Else it gets refunded.
   When a project gets funded, or secures enough votes, the deposit gets refunded.
7. For 4 seasons following the acceptance, the nominator is not allowed to nominate
   another project. Similarly, a project that remains unfunded would have a cooling
   period of 2 seasons to get listed again. These limits may be voted upon in the
   beginning, and potentially come up for review every 2 years.

The limit on the maximum number of projects in a "Theme" is revised every 4 seasons,
in a pre-season poll.

So, how does the number of projects scale with the community size ? When proposers
find that there is no room in the "General Theme", that should not be the end
of the road.  Once the "General Theme" gets maxed out, "Special Themes",
described in [REAL-VOTING.md](REAL-VOTING.md) will naturally emerge. "Special Themes"
must necessarily follow specific, well defined themes in some ways to cater to various
voter preferences. Voters can allocate votes flexibly across Themes, so they are not
restricted in any way.

Projects may be allowed to move across Themes once, after listing.  This may temporarily
cause a Theme to exceed its limit.

With multiple themes, there will a queue per Theme. When a project in a queue wants to
switch Themes, it will get enqueued in the target Theme's queue.

# Who Gets Funded

Notionally, TRF funds only individuals. However, in many cases the money may not end
up directly in the account of the individual, and instead be sent to a "fiscal host"
for management:

1. If the project has an associated bank account, and the funds are intended to be
   spent through the project, then the money will go there. For examples beyond the
   regular projects, think of: trust accounts, college clubs/departments,
   not-for-profits, etc.
2. If the individual is a minor, then the money may goto the parent/guardian, or
   an organization which may be assisting the minor.

Individuals who don't have independent finances are listed as a "Dependent Member",
and as such do not possess voting rights on the platform. They must be added by the
Fiscal Host, who must be a contributing member, and may collect karma.

FIXME - check rules for minors. We may need to list parents/guardians for students
in all cases.

# Listed Project

A Listed project must have:

0. Proposer - is a TRF member, and owner OR fiscal host of the project
1. Title
2. Description of Project
3. Scope of activities for which funding is sought
4. Timeline in which activities will be completed (after funding)
6. Reusable deliverables generated - clear description of artifacts generated that are reusable
7. Utility of deliverables - OR how they are useful to voters or to anybody !
8. License - under which reusable deliverables are released.
9. Campaign page - URL (campaign page, blog, video etc etc)
10. Socials of project. Optional - but if any are used by the project, then they must be specified here.
11. Who will the Funds Go To: list of
    - TRF member reference. This could be a self reference as well. Nickname will be rendered
      if the member has one in their profile.
    - Clear recognizable photograph of the member. Must be taken at or close to time of
      the submission. Avoid "driver license" and "adhaar" photos :)
      This is an essential trust building measure in our community.
    - Fiscal host reference (TRF member)
    - Socials of the member w.r.t. this project. Optional - but if the member uses or intends to
      use any for this project (e.g. personal socials) then best to provide them here.
    - Role that this member will play in the project
    - How is this member qualified to play this particular role?
    - How will the funds be used
    - Timeline of usage of funds
12. Frequency of progress update posts after funding. Funded projects are required to make
    periodic updates at-least at this set frequency. Once a month is a nominal recommended
    update frequency, but could be higher for projects as they choose.
13. List of fund matching members:
    - TRF Member reference
    - Fund matching ratio (1:1, 2:1, etc)
    - Minimum and Maximum matching contribution
    - Reasons for the member matching funds
    - Timeline of disbursement of matching funds

A listed project is NOT allowed to be raising funds for same purposes elsewhere TBD. Why?
This is undesirable, as it can result in a lot of confusing scenarios. In short, we reward
clear planning and purpose. A listed project is NOT allowed to raise funds for dependent
steps, without resolution of this project's funding status. For exactly the same reason.
E.g. for a software project, if feature B will get implemented after feature A, and there
is a running campaign for feature A, then the project must not be raising funds for feature
B publicly. (the publicly part is important - does that capture the intent?)

It's easier to explain this with hardware projects. They consist of one to three phases :
prototyping (including validation), getting ready for mass production(certification),
and mass production. If the project is raising funds for prototyping phase in TRF, it can't
be seeking public funds via campaigns elsewhere either to implement part of the prototyping
phase, or follow-on phases.

## Matching funds

The fund matching mechanism ensures that we can support this popular concept. However, we
do require the fund matching agency to be a member as well.

One of the fund matching agency can be the project itself as well, or even its own members. 
This could be a way to say, "ah the community believes in this, so I will also put money into it".

A fund matching agency can be an individual or an org! A clear plan for usage of matching
funds is a must in the plan. Matching funds must have signoff both from the project proposer
and the matching fund proposer.

# Reviews

Projects that ask to raise more than a specified threshold of funds may need an expert
review. We need to have a mechanism for this, where volunteers can sign up and give
their inputs, which will be featured on the project. Reviewers would be picked randomly
from a pool based on their areas of expertise.

Projects that don't find reviewers may get dropped after a few seasons in the queue.

Project reviews may fetch the reviewer positive or negative karma! Funded projects
that failed to meet expectations might fetch reviewers negative karma too. Positive
karma is likely for excellent reviews, pointing out project improvements/corrections,
derisking.

# Long Life Projects

After being funded, and delivering the goods expected, a project may be turned into a long
life project as well. This is a steady source of funding to the project, backed by the
community.  This funding is outside the voting mechanism, but keeps the project inside the
community, and keeps it regulated with the rules of the community - i.e. the karma system.

Long life projects need to have "funding members" with a min/max committed per month.
A long life project needs to define a reasonable minimum threshold of monthly funds -
comparable to the smallest allowed project on TRF? (TBD). Must also have a minimum
number of members backing it - say 100.

From the TRF perspective, costs overheads of supporting Long Life Projects must be maintained
separately. Long Life Projects can happen not earlier than Season 2.

# Side effects of going beyond voting

Purely voting members remain anonymous and invisible.

However, that changes when members becomes active in various ways:

- Participating in discussions in TRF spaces
- When a member nominates their project, their profile becomes visible (inside TRF)
  irrevocably. (should we have a right to be forgotten and what timeline?)
- When a member backs a project nomination, their profile becomes visible
- When a member reviews a project, their profile becomes visible.
- If a member gives non-anonymous karma, their profile becomes visible.

# Authors

Shree Kumar

# License

CC-BY-SA-4.0
