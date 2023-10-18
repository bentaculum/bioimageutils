import pytest
from bioimageutils import str2bool


@pytest.mark.parametrize(
    "inp, out",
    [
        ("False", False),
        ("FAlse", False),
        ("f", False),
        ("0", False),
    ],
)
def test_str2bool_valid(inp, out):
    assert str2bool(inp) == out


@pytest.mark.parametrize("x", ["hello", "Fals", "1.0", False, 0])
def test_str2bool_invalid(x):
    with pytest.raises((TypeError, ValueError)):
        str2bool(x)
