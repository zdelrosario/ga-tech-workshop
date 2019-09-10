import numpy as np
import os
import pandas as pd
import re
import matplotlib.pyplot as plt

from pypif_sdk.readview import ReadView
from functools import reduce
from sklearn.linear_model import LinearRegression

# Set multiple functions' default value
N_INIT = 20

## API Key Setup
##################################################
# Automates loading a Citrination API key
def getAPIKey(evar = "CITRINATION_API_KEY", filename = "./api.txt"):
    # Try environment variable first
    res = os.environ.get(evar)
    if res is not None:
        print("Loaded environment variable {0:}".format(evar))
    # Fallback to text file
    else:
        print("Environment variable {0:} not found, searching for {1:}...".format(
            evar,
            filename
        ))
        with open(filename, "r") as myfile:
            res = myfile.readline().strip()

    return res

## Parsing
##################################################
# Filtered dir()
def ddir(object):
    return list(filter(lambda s: s[0] != "_", dir(object)))

# Get a PIF scalar
def parsePifKey(pif, key):
    """Parse a single pif key for single scalar values;
    return nan if no scalar found.
    """
    if (key in ReadView(pif).keys()):
        if 'scalars' in dir(ReadView(pif)[key]):
            try:
                return ReadView(pif)[key].scalars[0].value
            except IndexError:
                return np.nan
        else:
            return np.nan
    else:
        return np.nan

# Flatten a collection of PIFs
def pifs2df(pifs):
    """Converts a collection of PIFs to tabular data
    Very simple, purpose-built utility script. Converts an iterable of PIFs
    to a dataframe. Returns the superset of all PIF keys as the set of columns.
    Non-scalar values are converted to nan.

    Usage
        df = pifs2df(pifs)
    Arguments
        pifs = an iterable of PIFs
    Returns
        df = Pandas DataFrame

    examples
        import os
        from citrination_client import CitrinationClient
        from citrination_client import PifSystemReturningQuery, DatasetQuery
        from citrination_client import DataQuery, Filter

        ## Set-up citrination search client
        site = "https://citrination.com"
        client = CitrinationClient(api_key = os.environ["CITRINATION_API_KEY"], site = site)
        search_client = client.search

        ## Query the Agrawal (2014) dataset
        system_query = \
            PifSystemReturningQuery(
                size = 500,
                query = DataQuery(
                    dataset = DatasetQuery(id = Filter(equal = "150670"))
                )
            )
        query_result = search_client.pif_search(system_query)
        pifs = [x.system for x in query_results.hits]

        ## Rectangularize the pifs
        df = pifs2df(pifs)
    """
    ## Consolidate superset of keys
    key_sets = [set(ReadView(pif).keys()) for pif in pifs]
    keys_ref = reduce(
        lambda s1, s2: s1.union(s2),
        key_sets
    )

    ## Rectangularize
    ## TODO: Append dataframes, rather than using a comprehension
    df_data = \
        pd.DataFrame(
            columns = keys_ref,
            data = [
                [
                    parsePifKey(pif, key) \
                    for key in keys_ref
                ] for pif in pifs
            ]
        )

    return df_data

# Formula to dict
def parse_formula(formula):
    """Parse a formula string
    Usage
        d = parse_formula(formula)
    Arguments
        formula = chemical formula; string
    Returns
        d = python dict of element keys and compositional fractions
    """
    composition = dict(map(
        lambda s: (
            re.search(r'\D+', s).group(),
            float(re.search(r'[\d\.]+', s).group())
        ),
        re.findall(
            r'\w+[\d\.]+',
            formula
            #ReadView(pifs[0]).chemical_formula
        )
    ))
    return composition

# Parse formulas, return a DataFrame
def formulas2df(formulas):
    """Convert an iterable of formulas to a DataFrame
    Usage
        df = formulas2df(formulas)
    Arguments
        formulas = chemical formulas; iterable of strings
    Returns
        df = DataFrame of chemical compositions; keys are elements, entries are
             composition fractions
    """

    # Parse all the formulas
    all_compositions = [
        parse_formula(formula) \
        for formula in formulas
    ]
    all_formulas = [set(d.keys()) for d in all_compositions]

    # Determine the superset of elements
    all_elements = reduce(
        lambda s1, s2: s1.union(s2),
        all_formulas
    )

    # Join all formulas
    df_composition = pd.DataFrame(columns = all_elements)

    for ind in range(len(all_compositions)):
        df_composition = df_composition.append(
            pd.DataFrame(
                columns = all_compositions[ind].keys(),
                data = [all_compositions[ind].values()]
            ),
            ignore_index = True,
            sort = True
        )
        df_composition = df_composition.fillna(0)

    return df_composition

## Sequential Learning Simulator
##################################################
def sequentialLearningSimulator(
        X, Y,
        n_init = N_INIT,
        n_iter = 40,
        n_repl = 50,
        model  = LinearRegression()
):
    """Perform simulated sequential learning on a given dataset

    :param X: Feature dataset
    :type X: numpy array
    :param Y: Response dataset
    :type Y: numpy array
    :param acq: acquisition strategy
    :returns: acquisition history
    :rtype: numpy array
    """
    np.random.seed(101)

    n_total = Y.shape[0]

    acq_history = np.zeros((n_repl, n_iter + n_init))
    ind_all = range(n_total)

    ## Replication loop
    for ind in range(n_repl):
        ## Random initial selection
        ind_train = np.random.choice(n_total, n_init, replace = False)
        acq_history[ind, :n_init] = ind_train

        ## Iteration loop
        for jnd in range(n_iter):
            ## Train model
            reg = model.fit(X[ind_train], Y[ind_train])

            ## Predict on test data
            ind_test    = np.setxor1d(ind_all, ind_train)
            Y_pred_test = reg.predict(X[ind_test])

            ## Select best candidate
            ind_best = ind_test[np.argmax(Y_pred_test)]

            ## Record and advance
            ind_train = np.concatenate((ind_train, [ind_best]))
            acq_history[ind, n_init + jnd] = ind_best

    return acq_history

def plotHistory(acq_history, Y, label, n_init = N_INIT, color = "black"):
    """Plot the results of a sequential learning simulation

    :param acq_history: Output from sequentialLearningSimulator()
    :type acq_history: numpy array
    :param Y: Response values
    :param label: Text label for plotted history
    :type label: string
    :param n_init: Number of initial candidates
    :type n_init: integer
    :param color: Color for plotted history
    :type color: string
    :type Y: numpy array
    """
    n_iter = acq_history.shape[1] - n_init
    Y_hist = np.array([Y[acq_history[i, :]] for i in range(acq_history.shape[0])])

    max_value   = np.max(Y)

    ## Average the initial points
    Y_hist = np.concatenate(
        (np.atleast_2d(np.mean(Y_hist[:, :n_init], axis = 1)).T, Y_hist[:, n_init:]),
        axis = 1
    )
    ## Take cumulative maximum
    Y_max = np.maximum.accumulate(Y_hist, axis = 1)
    ## Statistics over replications
    Y_mean    = np.mean(Y_max, axis = 0)
    Y_median  = np.median(Y_max, axis = 0)
    Y_upper   = np.quantile(Y_max, 0.9, axis = 0)
    Iter      = np.arange(n_iter + 1)

    plt.plot(Iter, [max_value] * (n_iter + 1), "k:")
    # Median of maxes
    plt.plot(Iter, Y_median, color = color, linewidth = 3, label = label)
    plt.legend(loc = 0)


## Data cleaning workshop helpers
##################################################
def create_mapping_from_table(header_csv):
    '''
    This function takes a CSV file defining header abbreviations and creates
    a dictionary mapping the abbreviation to the full name in a way that is
    commensurate with the Citrine CSV Template Ingester.

    :param header_csv: A string filepath to the CSV file.
    :return mapping: A dictionary mapping abbreviation to full name.
    '''
    mapping = {}
    df = pd.read_csv(header_csv)

    # Read each row of the df
    for index, row in df.iterrows():
        # Check for composition column; keep as is
        if row['Details'].startswith('%'):
            mapping[row['Abbreviation']] = 'ACTUAL COMPOSITION: {} (wt %)'.format(
                row['Abbreviation'])

        # Otherwise it's a Property name
        else:
            mapping[row['Abbreviation']] = 'PROPERTY: {}'.format(row['Details'])

    print('Mapping dictionary successfully created.')
    return mapping


def rename_columns_in_df(df, mapping):
    '''
    This function takes a DataFrame with abbreviated header names and renames
    the columns.

    :param df: A pandas DataFrame with the data and abbreviated column names.
    :param mapping: A dictionary mapping abbreviated to detailed names.
    :return df: A pandas DataFrame with the columns renamed.
    '''
    # Create new column names from supplied mapping by adding to empty list
    new_cols = []
    for abbreviation in list(df):
        new_cols.append(mapping[abbreviation])

    # Change the columns of the DataFrame to the new names
    df.columns = new_cols
    print('Columns are renamed and the DataFrame is saved to a new CSV file.')
    return df


def add_iron_composition(df):
    '''
    This function takes a DataFrame with alloy elements and adds a column for
    the weight percent of iron, the base metal.

    :param df: A pandas DataFrame missing composition of iron.
    :return df: A pandas DataFrame with composition of iron added in a new column.
    '''
    # Get only the columns that have composition
    # This called a "list comprehension" and it's a powerful Python paradigm
    comp_cols = [col for col in list(df) if 'ACTUAL COMP' in col]
    df_ = df[comp_cols]

    # Sum across columns
    col_sum = df_.sum(axis=1)

    # Compute iron composition as 100 - sum
    iron_comp = col_sum.mul(-1).add(100)

    # Add the composition as a new column to the DataFrame
    df['ACTUAL COMPOSITION: Fe (wt %)'] = iron_comp
    print('Iron composition column was added to the dataset.')
    return df


def add_chemical_formula(df):
    '''
    This function takes in a pandas DataFrame and adds a column for the
    chemical formula by combining the constituent compositions.

    :param df: A pandas DataFrame with compositions and missing a formula.
    :return df: A pandas DataFrame with chemical formula added in a new column.
    '''
    # Get only the columns that have composition
    comp_cols = [col for col in list(df) if 'ACTUAL COMP' in col]
    df_ = df[comp_cols]

    # Generate a list of chemical formulas
    formulas_list = []
    for index, row in df_.iterrows():
        # Loop through the compositions and add to the formula
        formula = ''
        for col in comp_cols:
            # Only add the element if it has a non-zero composition
            if row[col] > 1e-3:
                # A little complicated to account for floats to string conversion
                formula += col.split(' ')[2] + '{0:.5f}'.format(row[col]/100).rstrip('0')

        formulas_list.append(formula)

    # Add the chemical formula as a new column
    df['FORMULA'] = formulas_list
    print('Chemical formula column was added to the dataset.')
    return df


def fix_fatigue_strength(df):
    '''
    This function takes in a pandas DataFrame and multiplies cells where the
    Fatigue Strength is too small by 1000.

    :param df: A pandas DataFrame with erroneous values for Fatigue Strength.
    :return df: A pandas DataFrame with corrected values.
    '''
    prop_name = 'PROPERTY: Fatigue Strength'
    for index, row in df.iterrows():
        if row[prop_name] < 10.0:
            df.at[index, prop_name] *= 1000
    print('{} values have been corrected.'.format(prop_name))
    return df


def csv_to_pifs(df, fpath):
    '''
    This function takes in a pandas DataFrame and filepath writes a PIF
    with the data from the DataFrame to the filepath.

    :param df: A pandas DataFrame with cleaned data.
    :return: None
    '''
    # Create empty list to store ChemicalSystem objects
    systems = []

    # Loop through rows to create a ChemicalSystem for each entry
    for i, row in df.iterrows():
        system = ChemicalSystem()
        system.chemical_formula = row['FORMULA']

        # Empty lists to store composition and properties
        composition = []
        properties = []
        for col in list(df):
            # Parse non-zero compositions
            if 'ACTUAL COMP' in col:
                if row[col] > 1e-3:
                    comp = Composition()
                    comp.element = col.split(' ')[2]
                    comp.actual_weight_percent = Scalar(value=row[col])
                    composition.append(comp)
            # Parse all remaining properties
            elif 'PROPERTY' in col:
                prop = Property()
                prop.name = ' '.join(col.split(' ')[1:])
                prop.scalars = [Scalar(value=row[col])]
                properties.append(prop)
        system.composition = composition
        system.properties = properties

        systems.append(system)

    with open(fpath, 'w') as f:
        pif.dump(systems, f, indent=4)

    print('PIFs created and saved!')


def create_and_upload_data(client, fpath, dataset_name, dataset_desc,
                           public_flag=False):
    '''
    This function creates a dataset on Citrination and uploads the data
    stored in PIF format at the specified filepath.

    :param client: A CitrinationClient instance.
    :param fpath: A string filepath for the PIF on the local system.
    :param dataset_name: The string name for the dataset.
    :param dataset_desc: The string description for the dataset.
    :return: None
    '''
    # Create dataset and obtain ID
    dataset = client.data.create_dataset(name=dataset_name,
                                         description=dataset_desc,
                                         public=public_flag)
    dataset_id = dataset.id

    # Upload data to dataset; guard against AWS timeout
    start = time()
    timeout = 240
    while time() - start < timeout:
        sleep(1)
        try:
            print('Uploading data...')
            client.data.upload(dataset_id, fpath)
            break
        except:
            if time() - start>=timeout:
                raise RuntimeError("Possible AWS timeout, try re-running.")
            continue

    assert (client.data.matched_file_count(dataset_id) >= 1), "Upload failed."
    return dataset_id



# Extra function; not used
def create_mapping_from_table_w_units(header_csv):
    '''
    This function takes a CSV file defining header abbreviations and creates
    a dictionary mapping the abbreviation to the full name in a way that is
    commensurate with the Citrine CSV Template Ingester.

    :param header_csv: A string filepath to the CSV file.
    :return mapping: A dictionary mapping abbreviation to full name.
    '''
    mapping = {}
    df = pd.read_csv(header_csv)

    # Read each row of the df
    for index, row in df.iterrows():
        # Check for composition column; keep as is
        if row['Details'].startswith('%'):
            mapping[row['Abbreviation']] = 'ACTUAL COMPOSITION: {} (wt %)'.format(
                row['Abbreviation'])

        # Check for fatigue strength column
        elif 'fatigue' in row['Details'].lower():
            mapping[row['Abbreviation']] = 'PROPERTY: {} (MPa)'.format(row['Details'])

        # Check for temperature column
        elif 'temperature' in row['Details'].lower():
            mapping[row['Abbreviation']] = 'PROPERTY: {} (C)'.format(row['Details'])

        # Check for time column
        elif 'time' in row['Details'].lower():
            mapping[row['Abbreviation']] = 'PROPERTY: {} (min)'.format(row['Details'])

        # Check for rate column
        elif 'rate' in row['Details'].lower():
            mapping[row['Abbreviation']] = 'PROPERTY: {} (C/hr)'.format(row['Details'])

        else:
            mapping[row['Abbreviation']] = 'PROPERTY: {}'.format(row['Details'])

    print('Mapping dictionary successfully created.')
   eturn mapping
