import pytest

from src.scoring import scoring


@pytest.mark.parametrize(
    "correction,answer",
    [
        (["mathylde", "maureen"], ["mathylde", "maureen"]),
        (["charles"], ["charles"]),
    ],
)
def test_scoring_perfect(correction, answer):
    score_ = scoring(correction, answer)
    assert score_ == 1


@pytest.mark.parametrize(
    "correction,answer",
    [
        (["mathylde", "maureen"], ["charles"]),
        (["mathylde", "maureen"], None),
        (["mathylde", "maureen"], []),
        (["charles"], None),
        (["charles"], ["mathylde", "maureen"]),
        (["charles"], []),
    ],
)
def test_scoring_zero(correction, answer):
    score_ = scoring(correction, answer)
    assert score_ == 0


@pytest.mark.parametrize(
    "correction, answer",
    [
        (["mathylde", "maureen"], ["mathylde"]),
        (["mathylde", "maureen"], ["maureen"]),
        (["charles"], ["charles", "maureen"]),
    ],
)
def test_scoring_not_complete(correction, answer):
    score_ = scoring(correction, answer)
    assert score_ == 0.5
