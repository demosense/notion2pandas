# notion2pandas/parser.py

import pandas as pd

def parse_notion_json(raw: list) -> pd.DataFrame:
    """
    Parses raw Notion JSON data into a pandas DataFrame.

    Parameters:
    - raw (list): A list of Notion page objects.

    Returns:
    - pd.DataFrame: DataFrame containing the parsed data.
    """
    records = []

    for page in raw:
        properties = page.get("properties", {})
        record = {}
        for prop_name, prop_value in properties.items():
            parsed_value = parse_property(prop_value)
            record[prop_name] = parsed_value
        record["id"] = page.get("id", None)
        records.append(record)

    df = pd.DataFrame(records)
    return df

def parse_property(prop: dict):
    """
    Parses a Notion property value into a Python data type.

    Parameters:
    - prop (dict): The property value dictionary from Notion.

    Returns:
    - The parsed value.
    """
    prop_type = prop.get("type")
    if prop_type == "title":
        return parse_title(prop.get("title", []))
    elif prop_type == "rich_text":
        return parse_rich_text(prop.get("rich_text", []))
    elif prop_type == "select":
        return parse_select(prop.get("select"))
    elif prop_type == "multi_select":
        return parse_multi_select(prop.get("multi_select"))
    elif prop_type == "number":
        return parse_number(prop.get("number"))
    elif prop_type == "date":
        return parse_date(prop.get("date"))
    elif prop_type == "checkbox":
        return parse_checkbox(prop.get("checkbox"))
    elif prop_type == "url":
        return parse_url(prop.get("url"))
    elif prop_type == "email":
        return parse_email(prop.get("email"))
    elif prop_type == "phone_number":
        return parse_phone_number(prop.get("phone_number"))
    elif prop_type == "formula":
        return parse_formula(prop.get("formula"))
    elif prop_type == "relation":
        return parse_relation(prop.get("relation"))
    elif prop_type == "rollup":
        return parse_rollup(prop.get("rollup"))
    elif prop_type == "people":
        return parse_people(prop.get("people"))
    elif prop_type == "files":
        return parse_files(prop.get("files"))
    elif prop_type == "created_time":
        return parse_created_time(prop.get("created_time"))
    elif prop_type == "last_edited_time":
        return parse_last_edited_time(prop.get("last_edited_time"))
    elif prop_type == "status":
        return parse_status(prop.get("status"))
    else:
        # Log that the type of field is not supported
        print(f"Property type '{prop_type}' is not supported.")
        return None

def parse_title(value: list) -> str:
    """
    Parses a Notion 'title' property.

    Parameters:
    - value (list): List of title text objects.

    Returns:
    - str: The concatenated plain text of the title.
    """
    if not value:
        return ''
    texts = [v.get('plain_text', '') for v in value]
    return ''.join(texts)

def parse_rich_text(value: list) -> str:
    """
    Parses a Notion 'rich_text' property.

    Parameters:
    - value (list): List of rich text objects.

    Returns:
    - str: The concatenated plain text.
    """
    if not value:
        return ''
    texts = [v.get('plain_text', '') for v in value]
    return ''.join(texts)

def parse_select(value: dict) -> str:
    """
    Parses a Notion 'select' property.

    Parameters:
    - value (dict): The select object.

    Returns:
    - str: The name of the selected option.
    """
    if value:
        return value.get('name', '')
    else:
        return ''

def parse_multi_select(value: list) -> list:
    """
    Parses a Notion 'multi_select' property.

    Parameters:
    - value (list): List of selected options.

    Returns:
    - list: List of selected option names.
    """
    if value:
        return [v.get('name', '') for v in value]
    else:
        return []

def parse_number(value):
    """
    Parses a Notion 'number' property.

    Parameters:
    - value (float): The number value.

    Returns:
    - float: The number.
    """
    return value  # Could be None

def parse_date(value: dict):
    """
    Parses a Notion 'date' property.

    Parameters:
    - value (dict): The date object.

    Returns:
    - pd.Timestamp or dict: The start date (and end date if available).
    """
    if value:
        start = value.get('start')
        end = value.get('end')
        try:
            start_date = pd.to_datetime(start)
            if end:
                end_date = pd.to_datetime(end)
                return {'start': start_date, 'end': end_date}
            else:
                return start_date
        except Exception as e:
            print(f"Error parsing date: {e}")
            return None
    else:
        return None

def parse_checkbox(value: bool) -> bool:
    """
    Parses a Notion 'checkbox' property.

    Parameters:
    - value (bool): The checkbox value.

    Returns:
    - bool: The checkbox state.
    """
    return value

def parse_url(value: str) -> str:
    """
    Parses a Notion 'url' property.

    Parameters:
    - value (str): The URL.

    Returns:
    - str: The URL string.
    """
    return value

def parse_email(value: str) -> str:
    """
    Parses a Notion 'email' property.

    Parameters:
    - value (str): The email address.

    Returns:
    - str: The email address.
    """
    return value

def parse_phone_number(value: str) -> str:
    """
    Parses a Notion 'phone_number' property.

    Parameters:
    - value (str): The phone number.

    Returns:
    - str: The phone number.
    """
    return value

def parse_formula(value: dict):
    """
    Parses a Notion 'formula' property.

    Parameters:
    - value (dict): The formula object.

    Returns:
    - The computed value of the formula.
    """
    formula_type = value.get('type')
    formula_value = value.get(formula_type)
    return formula_value

def parse_relation(value: list) -> list:
    """
    Parses a Notion 'relation' property.

    Parameters:
    - value (list): List of related page references.

    Returns:
    - list: List of related page IDs.
    """
    if value:
        return [v.get('id') for v in value]
    else:
        return []

def parse_rollup(value: dict):
    """
    Parses a Notion 'rollup' property.

    Parameters:
    - value (dict): The rollup object.

    Returns:
    - The computed rollup value.
    """
    rollup_type = value.get('type')
    rollup_value = value.get(rollup_type)
    return rollup_value

def parse_people(value: list) -> list:
    """
    Parses a Notion 'people' property.

    Parameters:
    - value (list): List of person objects.

    Returns:
    - list: List of person names or IDs.
    """
    if value:
        return [v.get('name', v.get('id')) for v in value]
    else:
        return []

def parse_files(value: list) -> list:
    """
    Parses a Notion 'files' property.

    Parameters:
    - value (list): List of file objects.

    Returns:
    - list: List of file URLs.
    """
    files = []
    for v in value:
        if v.get('type') == 'file':
            files.append(v.get('file', {}).get('url', ''))
        elif v.get('type') == 'external':
            files.append(v.get('external', {}).get('url', ''))
    return files

def parse_created_time(value: str):
    """
    Parses a Notion 'created_time' property.

    Parameters:
    - value (str): The creation timestamp.

    Returns:
    - pd.Timestamp: The creation time.
    """
    try:
        return pd.to_datetime(value)
    except Exception as e:
        print(f"Error parsing created_time: {e}")
        return None

def parse_last_edited_time(value: str):
    """
    Parses a Notion 'last_edited_time' property.

    Parameters:
    - value (str): The last edited timestamp.

    Returns:
    - pd.Timestamp: The last edited time.
    """
    try:
        return pd.to_datetime(value)
    except Exception as e:
        print(f"Error parsing last_edited_time: {e}")
        return None
    

def parse_status(value: str):
    """
    Parses a Notion 'status' property.

    Parameters:
    - value (dict): The status value.

    Returns:
    - str: The status name.
    """
    try:
        return value.get("name", None)
    except Exception as e:
        print(f"Invalid status property: {e}")
        return None