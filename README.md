# pandas-notion

pandas-notion is a Python package that retrieves data from a Notion database and converts it into a pandas DataFrame. It simplifies the process of extracting and transforming data from Notion, allowing for easy data analysis and manipulation using pandas.

## Usage

To use pandas-notion, you need to have:

- A Notion integration token.
- The ID of the Notion database you want to access.
- Permission to connect to the database for such token

Set the Environment Variable

Set the `NOTION_SECRET` environment variable with your Notion integration token. You can do this in your terminal or include it in a `.env` file (if using python-dotenv or similar).

Example (Terminal):

```bash
export NOTION_SECRET='your_notion_integration_token'
```

Code Example

```python
import pandas-notion

# Replace 'your_database_id' with your actual Notion database ID
df_notion = pandas-notion.read_database('your_database_id')

print(df_notion.head())
```

This code will:

- Connect to the specified Notion database.
- Retrieve all the data.
- Convert it into a pandas DataFrame.
- Display the first few rows of the DataFrame.

## Development

### Project structure

The package consists of three main Python scripts:

1. `__init__.py`
    - Purpose: Serves as entry point to read data from a Notion database.

2. `connection.py`
    - Purpose: Handles the connection to the Notion API.
    - Contains:
        - Constants for API URLs and headers.
        - The get_database function, which retrieves raw JSON data from the Notion API.
        - Features:
        - Supports pagination and filtering via parameters.
        - Manages authentication using the `NOTION_SECRET` environment variable.

3. `parser.py`
    - Purpose: Parses the raw JSON data from Notion into a pandas DataFrame.
    - Contains:
        - The parse_notion_json function, which processes the raw data.
        - The parse_property function, which determines the type of each property and calls the appropriate parser.
        - Specialized parse_<type> functions for each supported Notion property type (e.g., parse_title, parse_select).
        - Functionality:
        - Converts various Notion data types into suitable pandas data types.
        - Handles different property types like text, numbers, dates, selects, and more.
