# Configuration Files

This directory includes example projects are illustrated with their corresponding
[HUML](https://huml.io/) configuration files.

Three type of configuration files are used:

- Project description, in the projects directory. These describe individual projects,
  their members, funding needs, who the funding goes to, where funding comes from
  (including e.g. matching grants), deliverables, etc
- Member specific. Includes various bits of information about a member, to be used
  in public facing information. Note that the actual visibility of various parts of
  this information is dependent on the activities of the member in TRF. Those who
  purely vote without getting involved in anything else are not made visible.
- Member secrets information. Private information of members is stored here.

Configuration files are used here to illustrate concepts, and do not represent how
data will ultimately be stored.  Use the files to understand and critique what sort
of data the system might store, and subject to what uses.

The configuration files may not be exhaustive and inclusive of every need. This is
on purpose. Most of the examples serve to illustrate the kind of projects we might
be looking for.  They focus on the creative side of things to a certain extent,
like emotions in the campaign, motivations of people seeking funding, persona of
people who might seek funds, etc.

# Project Description

The following keys are used in each project file:

- project_id
- proposer : reference to a member, notional owner. May or may not get funds.
- title
- desc - description
- funding_range : minimum and maximum funding requested.
- campaign_url : Link to project video, webpage, etc
- categories : list of buckets this project this fall into, in the general theme.
  It is an error to include more than one bucket of the same type.
- licenses : SPDX license identifiers used in the project
- deliverables : list of deliverables that will be generated from funded activities,
  and license for each.
- members : List of project members, each consisting of
  - uid
  - funding_range : min, max that will go to this member
  - role : role of the member in the project
  - fund_usage : description of how this member will use (whole/part of) the funds.
- matching_grants : List of members matching grants, each consisting of
  - uid
  - matching_ratio : "crowd:me-gives" ratio - numerator and denominator whole numbers
  - funding_range : min, max that can be raised through this.

# Members

member.public.huml has public info for members - including individuals, fiscal hosts,
matching grant providers, etc

## Member Secrets

member.secret.huml has private info - personal identification etc which will never be
visible.
