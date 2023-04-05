import pytest
from series.series import fibonacci,lucas,sum_series


def test_fibonacci():
    actual=fibonacci(4)
    expected=3
    assert actual == expected

def test_lucas():
    actual=lucas(4)
    expected=7
    assert actual == expected

