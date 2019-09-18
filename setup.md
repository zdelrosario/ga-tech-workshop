---
title: Setup
---

In short, you'll need:

- Exercise files (Download)
- Python and Jupyter (Recommended: Anaconda)
- Tabula (Free software)
- API key (Create a Citrination account)

**If you have any issues with these steps**: Please ask a TA! We will gladly
help you set up your environment.

## Exercises Files
<!-- ------------------------- -->

We will work through a number of programming exercises in this workshop. We have
consolidated the exercise notebooks and installation files in a single zip;
download the following and unzip.

- [Exercises](https://github.com/CitrineInformatics/ga-tech-workshop/raw/master/files/exercises/exercises.zip) - Zipped files

## Tutorial: Using a Terminal
<!-- -------------------------------------------------- -->

Many software tools are most easily accessed through a programmatic interface
called a *terminal*. This section is a brief tutorial on using a terminal. We
will make minimal use of the terminal in this workshop, but it will be
absolutely essential for setting up your computer for the workshop. Please ask a
TA if you have any issues using a terminal.

### Opening a terminal

- Mac: `terminal.app` is your terminal -- you can find this through Spotlight
  search (Command + Spacebar).
- Windows: **After** you have installed Anaconda python, you will have access to
  `Anaconda prompt` -- use this as your terminal for the workshop.
- Linux: If you're on Linux, you probably already use a terminal regularly. On
  Ubuntu the shortcut to open a terminal is `Ctrl + Alt + T`.

After opening your terminal, you should see a window that looks something like
the following.

<img src="./fig/terminal_example.png" style="width:600px;">

To use the terminal, you manually type commands, then press Enter to execute.

### Changing directory

When looking for files (Mac: Finder, Windows: Explorer, Linux: e.g. Nautilus),
we use a program to look at *directories*. Your terminal does something similar
-- at any point it is *located* in a particular *directory*. The following
screenshot illustrates `c`hanging `d`irectories (`cd`) to my `Downloads` folder,
then `l`i`s`ting (`ls`) the contents of said directory. This is where I placed
the `exercises.zip` archive for the workshop. (Note: On Windows, you must use
the command `dir`, rather than `ls`.)

<img src="./fig/terminal_cd.png" style="width:600px;">

I unzip the archive `exercises.zip` from within terminal with the command `unzip
exercises.zip -d exercises`, which results in the following:

<img src="./fig/terminal_unzip.png" style="width:600px;">

I can then `cd` into the unzipped folder and install the required Python
packages with `pip install -r requirements.txt`. However, I can only do this
after I've installed Anaconda!

## Python and Jupyter
<!-- ------------------------- -->

We recommend [Anaconda
python](https://www.anaconda.com/distribution/#download-section), which will
provide *almost* everything you need. Make sure to install python version `>=
3.0`.

### Windows Installation
<!-- ------------------------- -->

If you are on Windows, you may need to install [Visual C++
Studio](https://go.microsoft.com/fwlink/?LinkId=691126). Click the
aforementioned link and install the tools.

### Python Modules
<!-- ------------------------- -->

Once you have installed python, you will need to install a handful of python
modules to complete all the workshop exercises. Anaconda provides a package
installer called `pip`; from the command line, you can simply execute the
following commands.

> ## Install Modules
> In your terminal, change directory to where you unzipped the exercises,
> and execute the command:
> ~~~
> pip install -r requirements.txt
> ~~~
> {: .language-bash}
> This will install the requirements for the workshop.
{: .callout}

<img src="./fig/terminal_pip.png" style="width:600px;">

### Opening Jupyter Notebooks
<!-- ------------------------- -->

Jupyter notebooks are a particular way of working with Python code. They are
designated with the file extension `.ipynb`. Unfortunately, you cannot simply
double-click on a Jupyter notebook to open it. Instead, you must launch the
Jupyter client from your terminal. Navigate to the directory where you want
Jupyter to launch (for the workshop, this is where you unzipped the contents of
`exercises.zip`), and execute the command `jupyter notebook`.

<img src="./fig/terminal_jupyter.png" style="width:600px;">

This will open a webpage in your browser with a file explorer-like view; you can
then click on the notebooks in that directory to open them. Go ahead and open
`check_install.ipynb`, which you will run at the end of installation to check if
everything is set up correctly.

## Tabula
<!-- ------------------------- -->

[Tabula](https://tabula.technology) is a free program for *liberating* data from
PDF's. Please follow the previous link and install Tabula before the workshop.

## API Key Setup
<!-- -------------------------------------------------- -->

To access Citrination, you will need to provide your API key. **However, we
strongly discourage you from copy-pasting this key into scripts that you
write**. Instead, we will configure your computer to store your API key in an
operating system-wide variable, and write our scripts to load that variable.
This section will describe how to do this.

First, log into
[Citrination](https://citrination.com/search/simple?searchMatchOption=fuzzyMatch)
-- create an account if you have not already. Click on `Account Settings` to
find your API key. Copy this, and follow either of the Two Options listed below.

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
