"""
HBI segment assignment: Mode inference and segment classification.

Canonical logic from docs/HBI_index_and_segment_matrix.md.
Mode is inferred from Spread (S): 1-3 -> Co-Present, 4-10 -> Diffusive.
Segments are evaluated in order: S4, S2, S3, S1, S5 (S5 only when Mode = Diffusive).
"""

from typing import Union


def infer_mode(S: Union[int, float]) -> str:
    """
    Infer Herd Mode from Spread (S).
    S 1-3: Co-Present (local to city-level).
    S 4-10: Diffusive (regional to global).
    """
    s = float(S)
    return "Diffusive" if s >= 4 else "Co-Present"


def _is_low(val: float) -> bool:
    return 1 <= val <= 3


def _is_medium(val: float) -> bool:
    return 4 <= val <= 6


def _is_high(val: float) -> bool:
    return 7 <= val <= 10


def _is_medium_or_above(val: float) -> bool:
    return val >= 4


def classify_segment(
    M: Union[int, float],
    S: Union[int, float],
    I: Union[int, float],
    D: Union[int, float],
    mode: str,
) -> str:
    """
    Classify an event into a segment based on dimension values.

    Parameters
    ----------
    M : Magnitude (1-10)
    S : Spread (1-10)
    I : Intensity (1-10)
    D : Duration (1-10)
    mode : "Co-Present" or "Diffusive" (use infer_mode(S) if unknown)

    Returns
    -------
    Segment string, e.g. "S1 - Aligned Expansion", or "Unclassified".
    """
    m, s, i, d = float(M), float(S), float(I), float(D)

    # S4 – Persistent Friction
    if _is_high(i) and _is_high(d):
        return "S4 - Persistent Friction"

    # S2 – Emotion-Driven
    if _is_high(i) and not _is_high(d):
        return "S2 - Emotion-Driven"

    # S3 – Volatile Expansion
    if _is_medium_or_above(m) and _is_medium_or_above(s) and _is_low(d):
        return "S3 - Volatile Expansion"

    # S1 – Aligned Expansion
    if (
        _is_medium_or_above(m)
        and _is_medium_or_above(s)
        and _is_medium_or_above(d)
        and _is_medium(i)
    ):
        return "S1 - Aligned Expansion"

    # S5 – Low Energy Diffusion (only when Diffusive)
    if _is_low(i) and mode == "Diffusive":
        return "S5 - Low Energy Diffusion"

    return "Unclassified"


def assign_segment_row(
    row: dict,
    m_col: str = "Magnitude(M)",
    s_col: str = "Spread(S)",
    i_col: str = "Intensity(I)",
    d_col: str = "Duration(D)",
) -> str:
    """
    Assign segment for a single row (dict or pandas Series-like).
    Infers Mode from Spread, then classifies.
    """
    M = row.get(m_col, row.get("M"))
    S = row.get(s_col, row.get("S"))
    I = row.get(i_col, row.get("I"))
    D = row.get(d_col, row.get("D"))
    mode = infer_mode(S)
    return classify_segment(M, S, I, D, mode)
