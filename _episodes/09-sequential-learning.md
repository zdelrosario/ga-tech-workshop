---
title: "Introduction to Sequential Learning"
teaching: 10
exercises: 50
questions:
- "What is sequential learning?"
objectives:
- "Students design a machine learning model for sequential learning on materials science data."
- "Students learn about featurizing, particularly for materials."
keypoints:
- "Additional features can be computed from the 'raw' features, including polynomial terms and chemical compositions. This process is called featurization."
---

![Sequential learning schematic](../../fig/sequential-learning.png)

## Exercise
<!-- -------------------------------------------------- -->

> ## Exercise: Sequential Learning Simulation
>
> Complete [07_sl_exercise.ipynb](../files/exercises/07_sl_exercise.ipynb)
{: .challenge}

## Further Study
<!-- -------------------------------------------------- -->

The following are suggested directions for further study in Materials Informatics.

### A Proper Introduction
<!-- ------------------------- -->

If I had to recommend a single book for this area, I would point you to [An
Introduction to Statistical
Learning](http://faculty.marshall.usc.edu/gareth-james/ISL/), by James, Witten,
Hastie, and Tibshirani. This text is freely available in PDF form, and covers
all the basics of fitting regression and classification models.

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

{% include links.md %}
