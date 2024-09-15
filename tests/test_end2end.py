2# tests/test_end2end.py

import os
import pandas as pd

# Import the package
import pandas_notion

def test_read_database():
    """
    End-to-end test for the pandas-notion package.
    """
    # Retrieve environment variables
    NOTION_SECRET = os.getenv("NOTION_SECRET")
    DATABASE_ID = os.getenv("DATABASE_ID")

    # Check that environment variables are set
    assert NOTION_SECRET is not None, "NOTION_SECRET is not set in the environment."
    assert DATABASE_ID is not None, "DATABASE_ID is not set in the environment."

    # Call the function to read the Notion database
    df = pandas_notion.read_database(database_id=DATABASE_ID)

    # Basic assertions
    assert isinstance(df, pd.DataFrame), "The result is not a pandas DataFrame."
    assert not df.empty, "The DataFrame is empty."

    # Optionally, print the DataFrame head (for debugging purposes)
    print(df.head())