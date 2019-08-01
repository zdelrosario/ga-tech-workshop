import pandas as pd
import numpy as np
import re
from pypif_sdk.readview import ReadView
from functools import reduce

## Parsing
##################################################
# Filtered dir()
def ddir(object):
    return list(filter(lambda s: s[0] != "_", dir(object)))

## Parsing
##################################################
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
