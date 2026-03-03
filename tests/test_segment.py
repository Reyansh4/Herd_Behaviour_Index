"""Tests for segment assignment (canonical rules from docs)."""
import pytest
from methodology.segment import infer_mode, classify_segment, assign_segment_row

# --- Mode ---
@pytest.mark.parametrize("S,expected", [(1, "Co-Present"), (3, "Co-Present"), (4, "Diffusive"), (10, "Diffusive")])
def test_infer_mode(S, expected):
    assert infer_mode(S) == expected

# --- Segment: S4 Persistent Friction (I high, D high) ---
@pytest.mark.parametrize("M,S,I,D", [(5, 5, 8, 8), (1, 1, 7, 10)])
def test_segment_s4(M, S, I, D):
    assert classify_segment(M, S, I, D, "Diffusive") == "S4 - Persistent Friction"
    assert classify_segment(M, S, I, D, "Co-Present") == "S4 - Persistent Friction"

# --- Segment: S2 Emotion-Driven (I high, D not high) ---
def test_segment_s2():
    # Berlin Wall: M=9, S=9, I=8, D=2 -> S3 (M,S>=med, D low) takes precedence? No: S2 is before S3 in order. S2: I high and D not high. I=8 high, D=2 not high -> S2.
    assert classify_segment(9, 9, 8, 2, "Diffusive") == "S2 - Emotion-Driven"
    assert classify_segment(5, 5, 7, 3, "Diffusive") == "S2 - Emotion-Driven"

# --- Segment: S3 Volatile Expansion (M,S >= medium, D low) ---
def test_segment_s3():
    # I must not be high (else S2/S4). So I medium or low. M=9,S=9,D=2 -> S3
    assert classify_segment(9, 9, 5, 2, "Diffusive") == "S3 - Volatile Expansion"
    assert classify_segment(4, 4, 4, 1, "Diffusive") == "S3 - Volatile Expansion"

# --- Segment: S1 Aligned Expansion (M,S,D >= medium, I medium) ---
def test_segment_s1():
    assert classify_segment(5, 5, 5, 5, "Diffusive") == "S1 - Aligned Expansion"
    assert classify_segment(4, 6, 5, 6, "Diffusive") == "S1 - Aligned Expansion"

# --- Segment: S5 Low-Energy Diffusion (I low, Mode = Diffusive) ---
def test_segment_s5():
    assert classify_segment(4, 6, 2, 8, "Diffusive") == "S5 - Low Energy Diffusion"
    assert classify_segment(3, 5, 1, 5, "Diffusive") == "S5 - Low Energy Diffusion"

# --- S5 not applied for Co-Present ---
def test_segment_s5_co_present_unchanged():
    # I low but Co-Present -> Unclassified (S5 only for Diffusive)
    assert classify_segment(3, 2, 2, 4, "Co-Present") == "Unclassified"

# --- Unclassified ---
def test_segment_unclassified():
    # I medium, D low, but M or S low -> no S3. M=2,S=2,I=5,D=2 -> Unclassified
    assert classify_segment(2, 2, 5, 2, "Diffusive") == "Unclassified"

# --- assign_segment_row ---
def test_assign_segment_row():
    row = {"Magnitude(M)": 9, "Spread(S)": 9, "Intensity(I)": 8, "Duration(D)": 2}
    assert assign_segment_row(row) == "S2 - Emotion-Driven"
    row_s1 = {"Magnitude(M)": 5, "Spread(S)": 5, "Intensity(I)": 5, "Duration(D)": 5}
    assert assign_segment_row(row_s1) == "S1 - Aligned Expansion"
