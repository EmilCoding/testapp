"""
Make a few initial tests to make sure pytest works and the package can be installed.
"""


def test_trivial() -> None:
    assert True, "This test must never fail"


def test_import() -> None:
    import app as _
