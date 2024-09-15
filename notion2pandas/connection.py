import os
import requests
import time

# Retrieve the Notion integration token from environment variables
NOTION_SECRET = os.getenv("NOTION_SECRET")
if NOTION_SECRET is None:
    raise ValueError("Environment variable 'NOTION_SECRET' is not set.")

API_URL = "https://api.notion.com/v1"

HEADERS = {
    "Authorization": f"Bearer {NOTION_SECRET}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def get_database(database_id: str, num_pages: int = -1) -> list:
    """
    Retrieves the contents of a Notion database using the Notion API.

    Parameters:
    - database_id (str): The ID of the Notion database.
    - num_pages (int, optional): Maximum number of pages to retrieve. Defaults to -1 (all pages).

    Returns:
    - list: A list of page objects from the Notion database.
    """
    results = []
    has_more = True
    start_cursor = None
    page = 1

    while has_more and (num_pages == -1 or page <= num_pages):
        print(f"Downloading page {page} (start_cursor: {start_cursor})")

        data = {}
        if start_cursor:
            data["start_cursor"] = start_cursor

        response = requests.post(
            f"{API_URL}/databases/{database_id}/query",
            headers=HEADERS,
            json=data
        )

        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from Notion API: {response.text}")

        res_json = response.json()
        results.extend(res_json.get("results", []))
        has_more = res_json.get("has_more", False)
        start_cursor = res_json.get("next_cursor", None)

        # Avoid being throttled by the API limits
        time.sleep(0.5)
        page += 1

    return results