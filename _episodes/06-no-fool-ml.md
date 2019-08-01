---
title: "How To Not Get Fooled by Machine Learning"
teaching: 10
exercises: 50
questions:
- "What is the danger zone?"
- "How do I train a machine learning model?"
- "Why should I learn some statistics to do machine learning?"
objectives:
- "Students fit machine learning models using scikit-learn."
- "Students learn about underfitting and overfitting."
- "Students use cross-validation to support hyperparameter tuning."
- "Students learn about featurizing, particularly for materials."
keypoints:
- "The danger zone is doing machine learning without any math or statistics knowledge!"
- "Training a machine learning model is accomplished by tuning model parameters to minimize error on a training set."
- "Features are facts about an observation used to inform a model. The way the model uses the features is controlled by the parameters."
- "Hyperparameters are tunable settings in a model that are held constant during training. An example includes polynomial order."
- "A model tends to underfit when it is not flexible enough to capture genuine trends in the data."
- "A model tends to overfit when it is so flexible that it fits spurious patterns in the data."
- "Cross-validation gives more accurate error estimates than naive training error, which can help with tuning hyperparameters."
- "Additional features can be computed from the 'raw' features, including polynomial terms and chemical compositions. This process is called featurization."
---

[Drew Conway](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram)
writes of people with "hacking skills plus substantive expertise" as living in
the _danger zone_.

![Data Science
Triangle](https://images.squarespace-cdn.com/content/v1/5150aec6e4b0e340ec52710a/1364352051365-HZAS3CLBF7ABLE3F5OBY/ke17ZwdGBToddI8pDm48kB2M2-8_3EzuSSXvzQBRsa1Zw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpxPe_8B-x4gq2tfVez1FwLYYZXud0o-3jV-FAs7tmkMHY-a7GzQZKbHRGZboWC-fOc/Data_Science_VD.png?format=750w)

The idea here is that applying machine learning models without any understanding
of math or statistics is _dangerous_, in the sense that someone in the _danger
zone_ can easily build and apply models without realizing they've made a grave
mistake.[^1] Of course, we're not going to be able to teach you everything you
need to know about math and statistics in a one-day workshop. But we can pick
out an important slice of content, and lay a foundation for further study.

## Fitting a Machine Learning Model
<!-- -------------------------------------------------- -->


## Underfitting and Overfitting
<!-- -------------------------------------------------- -->

## Cross-Validation
<!-- -------------------------------------------------- -->

## Further Study
<!-- -------------------------------------------------- -->

### A Proper Introduction
<!-- ------------------------- -->

If I had to recommend a single book for this area, I would point you to [An
Introduction to Statistical
Learning](http://faculty.marshall.usc.edu/gareth-james/ISL/), by James, Witten,
Hastie, and Tibshirani. This text is freely available in PDF form, and covers
all the basics of fitting regression and classification models.

[^1]: Mistakes of the sort for which software does not have an error message, like p-hacking or abusing the interpretation of regression coefficients.

{% include links.md %}
