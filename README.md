# Programmatic Materials Informatics

[![Create a Slack Account with us](https://img.shields.io/badge/Create_Slack_Account-The_Carpentries-071159.svg)](https://swc-slack-invite.herokuapp.com/)

This repository generates the corresponding lesson website from [The Carpentries](https://carpentries.org/) repertoire of lessons.

## Contributing

We welcome all contributions to improve the lesson! Maintainers will do their best to help you if you have any
questions, concerns, or experience any difficulties along the way.

We'd like to ask you to familiarize yourself with our [Contribution Guide](CONTRIBUTING.md) and have a look at
the [more detailed guidelines][lesson-example] on proper formatting, ways to render the lesson locally, and even
how to write new episodes.

Please see the current list of
[issues](https://github.com/zdelrosario/gatw-citrine-day2/issues) for ideas for
contributing to this repository. For making your contribution, we use the GitHub
flow, which is nicely explained in the chapter [Contributing to a
Project](http://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project) in Pro
Git by Scott Chacon. Look for the tag
![good_first_issue](https://img.shields.io/badge/-good%20first%20issue-gold.svg).
This indicates that the mantainers will welcome a pull request fixing this
issue.

## Maintenance Plan (DRAFT)

### System
The infrastructure of this lesson is cloned from the [software
carpentries](https://github.com/carpentries/styles) template. While updating
from the upstream repo is possible, this should be unnecessary unless critical
issues are identified & fixed.

The lessons themselves teach Python and a number of packages: matplotlib and the
Citrination API (pycc). These are important upstream dependencies to keep the
lessons updated and relevant.

There are no downstream dependencies of this software.

### Status
Under development.

### Maintainer(s)
* Zachary del Rosario (zdelrosario@citrine.io) "Maintainer"

### Maintenance Concept
The Maintainer will be responsible for ensuring that lessons accurately teach
concepts from up-to-date versions of upstream dependencies. This includes both
executable example codes, and teaching materials that reflect current syntax.
Maintanence will be accomplished by ensuring example calls execute correctly,
and adapting lesson materials as necessary to reflect API changes.

It is not yet clear if we will employ unit tests for this repo -- most of the
example code is in Jupyter notebooks. I (Zach) will have to consult with the
rest of the Citrine team to determine if this will be possible.

Maintenance of this repo will continue until the delivery of this workshop
(scheduled for 2019, September 18 - 19). At this point, exercises and materials
should be extracted and maintained in a more general repository.

### Transfer
The ability to transfer the role of Maintainer will be vested in the Sr.
Community Manager. Transfer will entail giving access to this repo to the new
Maintainer, as well as a transfer of all responsibilities listed under
Maintenance Concept.

## Authors

A list of contributors to the lesson can be found in [AUTHORS](AUTHORS)

## Citation

To cite this lesson, please consult with [CITATION](CITATION)

[lesson-example]: https://carpentries.github.io/lesson-example
