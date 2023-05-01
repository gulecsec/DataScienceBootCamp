
from google.cloud import bigquery

import pandas as pd

from colorama import Fore, Style

from taxifare.ml_logic.params import PROJECT, DATASET


def get_bq_chunk(table: str,
                 index: int,
                 chunk_size: int,
                 dtypes: dict = None,
                 verbose=True) -> pd.DataFrame:
    """
    return a chunk of a big query dataset table
    format the output dataframe according to the provided data types
    """

    table_complete = f"{PROJECT}.{DATASET}.{table}"

    client = bigquery.Client()
    rows = client.list_rows(table_complete, start_index=index, max_results=chunk_size)
    df = rows.to_dataframe()

    df = df.astype(dtypes)

    if verbose:
        print(Fore.MAGENTA + f"Source data from big query {table}: {chunk_size if chunk_size is not None else 'all'} rows (from row {index})" + Style.RESET_ALL)

    return df

def save_bq_chunk(table: str,
                  data: pd.DataFrame,
                  is_first: bool):
    """
    save a chunk of the raw dataset to big query
    empty the table beforehands if `is_first` is True
    """

    print(Fore.BLUE + f"\nSave data to big query {table}:" + Style.RESET_ALL)

    # pass  # YOUR CODE HERE
