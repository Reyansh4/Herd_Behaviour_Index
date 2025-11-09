"""Shared data access helpers for the herd mentality events dataset."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Iterable, Sequence

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "herd_mentality_events.csv"
PROCESSED_DIR = DATA_DIR / "processed"


class DatasetNotFoundError(FileNotFoundError):
    """Raised when the herd mentality dataset cannot be located on disk."""


def ensure_processed_dir() -> Path:
    """Ensure the processed data directory exists and return it."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    return PROCESSED_DIR


@lru_cache(maxsize=1)
def load_raw_dataset() -> pd.DataFrame:
    """Load the canonical dataset from disk (cached)."""
    if not RAW_DATA_PATH.exists():
        raise DatasetNotFoundError(f"Dataset not found at {RAW_DATA_PATH}")
    return pd.read_csv(RAW_DATA_PATH)


def refresh_raw_dataset() -> pd.DataFrame:
    """Load the canonical dataset without touching the cache."""
    if not RAW_DATA_PATH.exists():
        raise DatasetNotFoundError(f"Dataset not found at {RAW_DATA_PATH}")
    return pd.read_csv(RAW_DATA_PATH)


def list_columns(df: pd.DataFrame | None = None) -> list[str]:
    """Return the column names for the provided dataframe (or the raw dataset)."""
    target = df if df is not None else load_raw_dataset()
    return list(target.columns)


def dataframe_preview(df: pd.DataFrame, limit: int = 5) -> pd.DataFrame:
    """Return a head preview of a dataframe."""
    return df.head(limit)


def add_or_replace_column(
    df: pd.DataFrame, column_name: str, values: Sequence | Iterable
) -> pd.DataFrame:
    """Return a copy of the dataframe with a new or updated column."""
    result = df.copy()
    result[column_name] = list(values)
    return result


def save_processed_dataframe(
    df: pd.DataFrame, filename: str = "herd_mentality_processed.csv"
) -> Path:
    """Persist the dataframe under data/processed and return the written path."""
    ensure_processed_dir()
    safe_name = filename.strip() or "herd_mentality_processed.csv"
    if not safe_name.endswith(".csv"):
        safe_name = f"{safe_name}.csv"
    output_path = PROCESSED_DIR / safe_name
    df.to_csv(output_path, index=False)
    return output_path


def dataframe_to_markdown(df: pd.DataFrame, limit: int = 5) -> str:
    """Render a dataframe preview as Markdown."""
    preview_df = dataframe_preview(df, limit=limit)
    return preview_df.to_markdown(index=False)


def summary_statistics(df: pd.DataFrame) -> pd.Series:
    """Return summary statistics for numeric columns."""
    return df.describe(include="all")

