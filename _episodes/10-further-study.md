---
title: "Suggestions for Further Study"
teaching: 0
exercises: 0
questions:
- "How do I learn more?"
objectives:
- "Students become aware of new tools they could learn and use."
- "Students become aware of resources they can use for further study."
keypoints:
- "There's a lot more to know -- keep studying!"
---

This workshop is intended to give you an *introduction* to materials informatics
-- it is unreasonable to think you could learn everything you need in two days!
The following are suggested directions for further study in materials
informatics.

## Formal Coursework
<!-- -------------------------------------------------- -->

The first version of this workshop was taught at Georgia Tech. If you are a
GATech student, the following classes are a great next step for adding more to
your toolkit.

- Data Analytics for (Chemical) Engineers (COE 3803, ChBE 4803)
- Data and Visual Analytics (CSE 6242),
- Machine Learning/Computational Data Analytics (CS 7641 or CSE/IYSE 6740)
- Regression Analysis (ISYE 6414)
- Data Mining and Statistical Learning (ISYE 7406)

## Software
<!-- -------------------------------------------------- -->

Software is a key component of materials informatics -- the more fluent you are
with your tools, the easier it will be to try many ideas quickly and arrive at
better solutions. The following are suggestions on new software you might learn.

### More Python
<!-- ------------------------- -->

I learned Python by reading the **free** book [Think
Python](https://greenteapress.com/wp/think-python-2e/), by Allen B. Downey. If
you want a more complete introduction to programming in Python, I would start
here.

### R / Tidyverse
<!-- ------------------------- -->

I am a personal fan of the R programming language, especially the
[Tidyverse](https://www.tidyverse.org/) -- a set of R packages meant to
facilitate data analysis. The [Data Challenge
Lab](http://dcl-docs.stanford.edu/home/) at Stanford has worked with Hadley
Wickham to develop curricula teaching the Tidyverse and *exploratory data
analysis* concepts.


### R or Python?
<!-- ------------------------- -->

TL;DR: Why not both? I use Python for scientific computing, and switch to
R/Tidyverse for data analysis.

Different languages tend to be popular in different circles. Python is favored
by those doing scientific computing (people running large simulations), where it
is used for mid-performance and "glue code" applications (scientists tend to use
C++ / Fortran for high-performance code). Python has also gained a *very large*
"market share" in terms of general language adoption.

R is favored by statisticians, who played a large role in defining the language.
The most advanced statistical methods tend to be implemented first in R, then
percolate to other langauges.

### Tabula
<!-- ------------------------- -->

Don't forget that we learned to use [Tabula](https://tabula.technology)! *You
don't need to copy-paste or hand-copy data from PDF's anymore!*

### WebPlotDigitizer
<!-- ------------------------- -->

Similar to Tabula, [WebPlotDigitizer](https://automeris.io/WebPlotDigitizer/) is
a free piece of software to help you extract data from inconvenient formats; in
this case, plots.

## Machine Learning
<!-- -------------------------------------------------- -->

Remember the [*danger
zone*](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram)! If
you intend to keep using machine learning for your work, then you need a *proper
and complete* introduction to ML.

### More Stats
<!-- ------------------------- -->

One key idea we did not cover in this workshop is *exploratory data analysis*
(EDA) -- the process of exploring and understanding a dataset before pursuing
more complicated analyses. This step is crucial to doing machine learning well,
as lessons will inform building effective machine learning models.

Allen Downey has written [Think
Stats](https://greenteapress.com/wp/think-stats-2e/), which covers this topic in
Python. The Data Challenge Lab's
[curriculum](http://dcl-docs.stanford.edu/home/) covers this in R.

### A Proper Introduction to Machine Learning
<!-- ------------------------- -->

If I had to recommend a single book for this area, I would point you to [An
Introduction to Statistical
Learning](http://faculty.marshall.usc.edu/gareth-james/ISL/), by James, Witten,
Hastie, and Tibshirani. This text is freely available in PDF form, and covers
all the basics of fitting regression and classification models.

## Materials Informatics-Specific Knowledge
<!-- -------------------------------------------------- -->

Materials informatics is more specialized than general machine learning.
Consequently, there are some important tools that are not covered in a more
generic ML course.

### Materials Featurization
<!-- ------------------------- -->

The following sources provide tools for featurizing materials data. Note that
these packages tend to provide a lot more than _just_ featurization.

[Matminer](https://hackingmaterials.lbl.gov/matminer/) provides a number of
featurizing tools for inorganic compounds.

[RDKit](https://www.rdkit.org/docs/GettingStartedInPython.html#descriptor-calculation)
provides a number of "descriptors" (features) for organic molecules, taking
[SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)
inputs.
