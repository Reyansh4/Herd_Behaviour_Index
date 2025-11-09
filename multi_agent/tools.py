"""LangChain tool definitions for interacting with the herd mentality dataset."""
from __future__ import annotations

import json
from inspect import cleandoc
from typing import Any, Dict, Iterable

import pandas as pd
from langchain_core.tools import tool

from . import data_utils


@tool("herd_dataset_columns")
def herd_dataset_columns(_: str = "") -> str:
    """Return the list of columns available in the herd mentality dataset."""
    columns = data_utils.list_columns()
    return "Available columns:\n- " + "\n- ".join(columns)


@tool("herd_dataset_preview")
def herd_dataset_preview(limit_text: str = "5") -> str:
    """Return a markdown preview of the first N rows of the dataset."""
    try:
        limit = int(limit_text.strip()) if limit_text else 5
    except ValueError:
        limit = 5
    df = data_utils.load_raw_dataset()
    preview_md = data_utils.dataframe_to_markdown(df, limit=limit)
    return cleandoc(
        f"""
        Preview of the herd mentality dataset (first {limit} rows):

        {preview_md}
        """
    )


@tool("herd_dataset_summary")
def herd_dataset_summary(_: str = "") -> str:
    """Return descriptive statistics for the dataset."""
    df = data_utils.load_raw_dataset()
    summary = data_utils.summary_statistics(df)
    return summary.to_string()


def _records_to_dataframe(records: Iterable[Dict[str, Any]]) -> pd.DataFrame:
    """Convert iterable of record dictionaries into a DataFrame."""
    dataframe = pd.DataFrame.from_records(list(records))
    if dataframe.empty:
        raise ValueError("No records provided to create a DataFrame.")
    return dataframe


@tool("save_processed_dataset")
def save_processed_dataset(payload: str) -> str:
    """Persist a set of records to data/processed and return the output path.

    Args:
        payload: JSON string with fields:
            - "records": array[object] representing rows
            - "filename": optional string for the output file name
    """
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ValueError("Payload must be valid JSON.") from exc

    if "records" not in data:
        raise ValueError("Payload must include a 'records' field.")

    dataframe = _records_to_dataframe(data["records"])
    filename = data.get("filename", "herd_mentality_processed.csv")
    output_path = data_utils.save_processed_dataframe(dataframe, filename=filename)
    return f"Saved {len(dataframe)} rows to {output_path.as_posix()}"


@tool("filter_herd_dataset")
def filter_herd_dataset(payload: str) -> str:
    """Filter the dataset by column equality and return a markdown preview.

    Args:
        payload: JSON string with fields:
            - "column": column name to filter on
            - "equals": desired value (case sensitive)
            - "limit": optional int limiting rows in the preview (default 5)
    """
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ValueError("Payload must be valid JSON.") from exc

    column = data.get("column")
    value = data.get("equals")
    limit = int(data.get("limit", 5))

    if not column or value is None:
        raise ValueError("Payload must include both 'column' and 'equals'.")

    df = data_utils.load_raw_dataset()
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset.")

    filtered = df[df[column] == value]
    if filtered.empty:
        return f"No rows found where {column} == {value!r}."

    preview_md = data_utils.dataframe_to_markdown(filtered, limit=limit)
    return cleandoc(
        f"""
        Filtered rows where {column} == {value!r} (showing up to {limit} rows):

        {preview_md}
        """
    )

