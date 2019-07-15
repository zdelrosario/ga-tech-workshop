import pandas as pd
from pypif_sdk.readview import ReadView

def pifs2df(pifs):
    """Converts a collection of PIFs to tabular data
    Very simple, purpose-built utility script. Assumes the top-level keys
    contain the relevant data, and flattens those keys to rectangular data.

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
    ## Perform some checks
    keys_ref = set(ReadView(pifs[0]).keys())
    if not all([keys_ref == set(ReadView(pif).keys()) for pif in pifs]):
        raise ValueError("PIFs do not have same top-level keys!")

    ## Rectangularize
    df_data = \
        pd.DataFrame(
            columns = keys_ref,
            data = [
                [
                    ReadView(pif)[key].scalars[0].value \
                    for key in keys_ref
                ] for pif in pifs
            ]
        )

    return df_data
