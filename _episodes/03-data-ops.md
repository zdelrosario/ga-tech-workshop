---
title: "Programmatic Data Operations"
teaching: 10
exercises: 50
questions:
- "Why use programming to operate on data?"
objectives:
- "Students use an application programming interface (API)."
- "Students inspect Python objects with dir()."
- "Students learn the basics of *data wrangling*."
- "Students use DataFrames in Pandas to investigate and operate upon data."
keypoints:
- "Don't share your API key!"
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
> of Excel *automatically* converting gene names into dates or floating-point
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

## Application Programming Interfaces (APIs)
<!-- -------------------------------------------------- -->
An *application programming interface* (API) is a kind of [software
link](https://www.mulesoft.com/resources/api/what-is-an-api); it provides a
programmer with access to a server or other software service. In our case, we
will use the API for
[Citrination](https://citrination.com/search/simple?searchMatchOption=fuzzyMatch)
to search for and access materials data.

We will start by
[setting-up](https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/clients_sequence/1_data_client_api_tutorial.ipynb)
the Citrination API. You will first need to [sign
up](https://citrination.com/users/sign_in) for an account. After creating an
account, navigate to "Account Settings" to find your API key.

<img src="../../fig/citrination_account_settings.png" style="width:800px;height:400px;">

> ## Protip: Don't share your API key!
> An *API key* is like a password -- it is a secret access code that grants you entry
> to a system. In this workshop this is not such an issue, but if you were to upload
> secret or sensitive data to Citrination (or another database) and gave your API
> key to someone else (accidentally or otherwise), that person could use your key
> to access your data.
{: .callout}

### Setting up your API key
<!-- -------------------------------------------------- -->
To access Citrination, you will need to provide your API key. **However, we
strongly discourage you from copy-pasting this key into scripts that you
write**.[^1] Instead, we will configure your computer to store your API key in
an operating system-wide variable, and write our scripts to load that variable.
This section will describe how to do this.

In OS X or Linux, the following instructions will work:

- In Terminal, type vim ~/.bash_profile (or use an editor of your choice).
- In that file, press i (edit mode) and add the line export CITRINATION_API_KEY="your_api_key".
- Save and exit (Esc, :wq, Enter).
- Open up a new Terminal and load this notebook one more time.

On Windows, this is [*more
complicated*](https://www.computerhope.com/issues/ch000549.htm), but still
manageable.

### Initializing the API
<!-- -------------------------------------------------- -->
After you have saved your API key and restarted your terminal, you can set about
using your key to access Citrination. The following packages will be necessary
to do so.

~~~
# Standard packages
import os # To read your API key from the environment variable

# Third-party packages
from citrination_client import * # To use the API function calls

# Initialize client
~~~
{: .language-python}

The following code will read the environment variable `CITRINATION_API_KEY` and
use it to access Citrination.

~~~
site = "https://citrination.com"
client = CitrinationClient(
    api_key = os.environ.get('CITRINATION_API_KEY'),
    site = site
)
client # reveal the attributes
~~~
{: .language-python}

### Accessing data
<!-- -------------------------------------------------- -->
Next, we will use the client to initialize the *search client*. This will enable
us to search Citrination for data, and load it onto our computer for local
analysis.

The search client is very powerful, but is also rather complex. We will build up
a simple search below for illustrative purposes, but see the [search client
tutorial](https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/clients_sequence/4_search_client_api_tutorial.ipynb)
for more information.

In practice, I recommend using the Citrination
[Search](https://citrination.com/search/simple?searchMatchOption=fuzzyMatch) or
[Datasets](https://citrination.com/datasets) tab to find what you're interested
in, then start constructing an API call to match. For instance, I searched for
materials with the "strength" property, found a ceramic with strength values,
then navigated to its parent dataset.

<img src="../../fig/citrination_search_strength.png" style="width:800px;height:400px;">

Searching for materials with a "strength" property.

<img src="../../fig/citrination_material-2-dataset.png" style="width:800px;height:400px;">

Inspecting a ceramic with "strength" properties, following the parent dataset.

<img src="../../fig/citrination_nist_ceramics.png" style="width:800px;height:400px;">

Below I took the NIST Ceramics dataset ID above and assigned it to a Python
variable for later access.

~~~
## Identify desired dataset's ID number
dataset_id = 151803 # NIST structural ceramics dataset
~~~
{: .language-python}

Using an initialized `client`, one can then call `client.search` along with a
structured query to access data. I give an example of this syntax below -- the
following code accesses a specific database by an id number, and returns up to
`5000` results.

~~~
## Build search query
search_client = client.search
query = \
    PifSystemReturningQuery(
        size = 5000,                              # Maximum number of results to return
        query=DataQuery(
            dataset=DatasetQuery(                 # Search among datasets
                id=Filter(equal=str(dataset_id))  # Match the dataset ID
            )
        )
    )

## Inspect results
query_result = search_client.pif_search(query)
print("Found {} PIFs in dataset.".format(query_result.total_num_hits, dataset_id))
~~~
{: .language-python}

We may access results through the `query_result` object. You will learn how to
do this in the Exercise at the end of this lesson.

Citrination stores data in the form of [*physical information
files*](http://citrineinformatics.github.io/pif-documentation/) (PIFs) -- an
open-source standard for storing data about physical objects. While PIFs are
convenient for storing information, they are less convenient for data analysis
and machine learning. Below, we'll discuss *data wrangling* -- transforming data
from one form to another desired format.

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
{: .language-bas}

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
> Complete this [jupyter notebook]()
{: .challenge}

[^1]: If you were to share a script with your API key, you will have shared your
    key with someone else. Game over!
[^2]: Since `pifs2df` was purpose-built for this exercise, it's not guaranteed
    to work for arbitrary cases. Your mileage may vary!

{% include links.md %}
