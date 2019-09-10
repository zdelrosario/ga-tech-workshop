---
title: Setup
---

In short, you'll need:

- Python and Jupyter (recommended: Anaconda)
- Exercise files
- API key

**If you have any issues with these steps**: Please ask a TA! We will gladly
help you set up your environment.

## Software Tools
<!-- -------------------------------------------------- -->

### Python
<!-- ------------------------- -->

We recommend [Anaconda
python](https://www.anaconda.com/distribution/#download-section), which will
provide *almost* everything you need. Make sure to install python version `>=
3.0`.

### Python Modules
<!-- ------------------------- -->

Once you have installed python, you will need to install a handful of python
modules to complete all the workshop exercises. Anaconda provides a package
installer called `pip`; from the command line, you can simply execute the
following commands.

> ## Install Modules
> Execute the following commands in your terminal.
> ~~~
> pip install citrination_client # For accessing Citrination database
> pip install pypif_sdk          # For working with PIFs
> pip install matminer           # For featurizing inorganic materials
> ~~~
> {: .language-bash}
{: .callout}

### Tabula
<!-- ------------------------- -->

[Tabula](https://tabula.technology) is a free program for *liberating* data from
PDF's. Please follow the previous link and install Tabula before the workshop.

## Exercises Files
<!-- ------------------------- -->

We will work through a number of programming exercises in this workshop. We have
consolidated the exercise notebooks in a single zip; download this and unzip.

- [Exercises](https://github.com/CitrineInformatics/ga-tech-workshop/raw/master/files/exercises/exercises.zip) - Zipped files

## API Key Setup
<!-- -------------------------------------------------- -->

To access Citrination, you will need to provide your API key. **However, we
strongly discourage you from copy-pasting this key into scripts that you
write**. Instead, we will configure your computer to store your API key in an
operating system-wide variable, and write our scripts to load that variable.
This section will describe how to do this.

First, log into Citrination, and click on `Account Settings` to find your API
key. Copy this, and follow either of the Two Options listed below.

<img src="./fig/find_api_key.png" style="width:400px;">

### Simple option: Text file
Create a text (.txt) file *in the same folder as your workshop files* with the
name `api.txt`. In this file, paste your API key. This value will be loaded by
the workshop exercises, and will allow you to access Citrination.

- In Windows, you can do this with Notepad
- In Mac OSX, you can use TextExit; make sure to enable plain text
  - Format > Make Plain Text; OR
  - press Command + Shift + T
- In Linux, you can use whatever you want (vim, emacs, nano, you got this)

Note that this is a **simplified** way to provide your API key to the workshop
materials. In practice, we recommend the following advanced option when doing
any kind of serious work. **While it is not required for you to use the advanced
option for this workshop, we strongly suggest you get the following working
before doing any serious work with your API key.**

### Advanced option: Environment variable
In OS X or Linux, the following instructions will work:

- In Terminal, type vim ~/.bash_profile (or use an editor of your choice).
- In that file, press i (edit mode) and add the line export CITRINATION_API_KEY="your_api_key".
  - Replace "your_api_key" with your actual API key; ensure this has no extra whitespace (spaces, tabs, etc.)
- Save and exit (Esc, :wq, Enter).
- Open up a new Terminal and load this notebook one more time.

On Windows, this is [*more
complicated*](https://www.computerhope.com/issues/ch000549.htm), but still
manageable.

## Final Check
<!-- -------------------------------------------------- -->

To check that you've successfully set up your computer for the workshop, please
run the following jupyter notebook.

> ## Test your installation
>
> Download and run
> [check_install.ipynb](https://github.com/CitrineInformatics/ga-tech-workshop/raw/master/files/exercises/check_install.ipynb).
> This is also included in the `exercises.zip` file above.
>
> Navigate to the folder where you downloaded `check_install.ipynb`,
> execute the command `jupyter notebook`, open `check_install.ipynb`,
> and click on `Cells > Run All`. If you can successfully run the
> notebook (without errors), then you are ready for the workshop!
{: .challenge}

{% include links.md %}
