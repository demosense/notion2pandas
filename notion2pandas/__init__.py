import pandas as pd
from .connection import get_database
from .parser import parse_notion_json

def read_database(database_id: str, num_pages: int = -1) -> pd.DataFrame:
    """
    Reads a Notion database and returns a pandas DataFrame.

    Parameters:
    - database_id (str): The ID of the Notion database.
    - num_pages (int, optional): Number of pages to retrieve. Defaults to -1 (all pages).

    Returns:
    - pd.DataFrame: DataFrame containing the Notion database content.
    """
    raw = get_database(database_id, num_pages)
    df = parse_notion_json(raw)
    return df