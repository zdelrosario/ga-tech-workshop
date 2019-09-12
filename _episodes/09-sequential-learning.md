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
- "Sequential learning is an *iterative* process, balancing human intuition and model predictions to select promising experimental candidates."
---

*Sequential learning* (SL) is one of the most exciting applications of machine
learning to materials science. The concept is to use ML as a "lab partner" --
given experimental data, the scientist trains a ML model to predict material
properties of interest, then uses this trained model to rank untested
candidates. The scientist can use a combination of model output[^1] and physical
intuition to choose new candidates to test experimentally, then add the new data
to a database, retrain the model, and repeat the cycle until satisfied. The
figure below illustrates this loop.

![Sequential learning schematic](../../fig/sequential-learning.png)

In the **final exercise** of the workshop, you will use all you have learned to
design and train a machine learning model for sequential learning, and study its
performance on the Agrawal et al. steel alloy data we studied previously. Of
course, we will not have time to carry out real experiments, so *we will
**simulate** sequential learning on a known dataset*. This simulation proceeds
in the following steps:
1. Select a random subset of the data
1. Train the model on selected data
1. Use the model to rank the remaining candidates
1. Select the top *predicted* candidate, add to the dataset
1. Repeat from Step (2) for a fixed number of iterations

The exercise notebook has a guided tutorial to setting up this exercise, and
suggestions on ideas you may try to improve your model.

## Exercise
<!-- -------------------------------------------------- -->

> ## Exercise: Sequential Learning Simulation
>
> Complete [07_sl_exercise.ipynb](../files/exercises/07_sl_exercise.ipynb)
{: .challenge}


[^1]: With *quantified uncertainties*, see [Ling et al. 2017](https://arxiv.org/pdf/1704.07423.pdf)

{% include links.md %}
