---
title: "Programmatic Data Operations"
teaching: 10
exercises: 50
questions:
- "Why use programming to operate on data?"
objectives:
- "Students inspect Python objects with dir()."
- "Students learn the basics of *data wrangling*."
- "Students use DataFrames in Pandas to investigate and operate upon data."
keypoints:
- "You may need to *wrangle* your data before you can use it."
- "Pandas DataFrames give you a lot of power to inspect and analyze data."
---

Many of us first learned how to work with data using spreadsheet software, such
as Excel. While such tools have a low barrier to entry, they are 1. Relatively
difficult to use for more advanced operations, and 2. Make a lot of assumptions
about data that can be *catastrophic* to data entry & analysis.

> ## A Scary Story
> There are [numerous
> instances](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1044-7)
> of Excel *automatically* converting (biological) gene names into dates or floating-point
> numbers. The prospect of having Excel automatically corrupt your data should be
> reason enough to avoid doing data analysis in spreadsheet programs, at least for
> all but the *very simplest* cases.
{: .callout}

In this lesson, we will learn how to interact with data *programmatically*; that
is, using a computer programming language. We will use an *application
programming interface* to obtain data from a web server (Citrination), and the
Python package [Pandas](https://pandas.pydata.org/) to operate on those data. We
will represent data in *DataFrames*, and use Pandas to investigate and operate
on data in ways that would be challenging or impossible in spreadsheet programs.

## Data Wrangling
<!-- -------------------------------------------------- -->
*Technically* we now have the data in `query_result`, but we are far from done.
From this point, we need to *wrangle* the data into a usable form. If we try to
use the data in its current form:

~~~
query_result.hits[:5]
~~~
{: .language-python}

We will find some unintelligible object references:

~~~
[<citrination_client.search.pif.result.pif_search_hit.PifSearchHit at 0x115798f60>,
 <citrination_client.search.pif.result.pif_search_hit.PifSearchHit at 0x115813e80>,
 <citrination_client.search.pif.result.pif_search_hit.PifSearchHit at 0x115813080>,
 <citrination_client.search.pif.result.pif_search_hit.PifSearchHit at 0x11729af28>,
 <citrination_client.search.pif.result.pif_search_hit.PifSearchHit at 0x11729a278>]
~~~
{: .language-bash}

In order to do visualization or machine learning, we need to extract the data
from these Python objects. In other words, we need to wrangle and
[tidy](https://vita.had.co.nz/papers/tidy-data.pdf) our data. [Hadley
Wickham](http://hadley.nz/) -- author of the `tidyverse` and data science
superstar -- notes that "wrangling data is 80% boredom and 20% screaming". Since
wrangling data is a course all on its own, we will punt the details of this
topic. I wrote a Python utility function to take care of the wrangling steps.[^2]

~~~
pifs = [x.system for x in query_result.hits]
df_data = pifs2df(pifs)
~~~
{: .language-python}

The exercise below will illustrate some of the steps involved in wrangling data,
but will shortcut a lot of the screaming so we can get to more enjoyable topics.
The function `pifs2df` will return a Pandas *DataFrame*, which will allow us to
analyze our data.

## DataFrames in Pandas
<!-- -------------------------------------------------- -->
A *DataFrame* is a rectangular representation of data provided by the
[Pandas](https://pandas.pydata.org/) package. A DataFrame is much like a
spreadsheet -- it is composed of columns and rows of cells. Each column defines
a variable, while each row is an observation of the data. Pandas also provides a
row-id column which uniquely identifies each observation. For instance, the
following is an example of a simple DataFrame.

| id | X1 | X2  |
|----|----|-----|
|  1 | 0  | "a" |
|  2 | 1  | "b" |
|  3 | 0  | "c" |
|  4 | 1  | "d" |

I'll refer to this as `df_simple` below. Once we have our data in a DataFrame,
we may leverage the package to carry out a number of useful data operations.
Pandas provides a number of built-in operations:

~~~
df_data.describe() # Computes summary statistics
df_data.head(10)   # Show the first 10 rows of the DataFrame
df_data.tail(10)   # Show the last 10 rows of the DataFrame
df_data.shape      # Return the dimensions of the data, (rows, columns)
df_data.columns    # List the columns in the data
~~~
{: .language-python}

These simple programmatic tools help us to *get a handle* on the data quickly;
quickly check what variables (columns) the DataFrame has, assess the variability
in the data (using `describe()`), inspect a few observations to check the
datatypes and typical values (using `head()` or `tail()`).

However, there are even *more powerful* operations we can carry out using
Pandas. We can select individual columns using indexing syntax:

~~~
df_simple["X1"]
~~~
{: .language-python}

| id | X1 |
|----|----|
|  1 | 0  |
|  2 | 1  |
|  3 | 0  |
|  4 | 1  |

We can also check which elements meet particular criteria

~~~
df_simple["X1"] == 0
~~~
{: .language-python}

~~~
[True, False, True, False]
~~~
{: .language-python}

We can *chain* these operations to filter rows that correspond to particular criteria:

~~~
df_simple[df_simple["X1"] == 0]
~~~
{: .language-python}

| id | X1 | X2  |
|----|----|-----|
|  1 | 0  | "a" |
|  3 | 0  | "c" |

This can be extremely useful for manually assessing patterns in data; you can
filter on one variable to see how other quantities co-vary.

We can also *sort* rows by particular columns.

~~~
df_simple.sort_values(by = "X1")
~~~
{: .language-python}

| id | X1 | X2  |
|----|----|-----|
|  1 | 0  | "a" |
|  3 | 0  | "c" |
|  2 | 1  | "b" |
|  4 | 1  | "d" |

We may also create new derived columns based on existing variables.

~~~
df_simple.assign(
	X3 = 10 ** df_simple["X1"]
)
~~~
{: .language-python}

| id | X1 | X2  | X3 |
|----|----|-----|----|
|  1 | 0  | "a" | 1  |
|  2 | 1  | "b" | 10 |
|  3 | 0  | "c" | 1  |
|  4 | 1  | "d" | 10 |

There are many more things we can do in Pandas, to learn more, you can check out
the Pandas [documentation](https://pandas.pydata.org/pandas-docs/stable/) and
some of the
[tutorials](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#min).

## Exercise
<!-- -------------------------------------------------- -->

> ## Exercise: Programmatic Data Operations
>
> Complete [04_data_exercise.ipynb](../files/exercises/04_data_exercise.ipynb)
{: .challenge}

[^1]: If you were to share a script with your API key, you will have shared your key with someone else. Game over!
[^2]: Since `pifs2df` was purpose-built for this exercise, it's not guaranteed to work for arbitrary cases. Your mileage may vary!

{% include links.md %}
