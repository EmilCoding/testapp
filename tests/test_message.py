import io
import sys
from app import func


def test_message(monkeypatch) -> None:
    fake_out = io.StringIO()
    monkeypatch.setattr(sys, "stdout", fake_out)

    func()
    assert fake_out.getvalue() == 'Hello, World!\n'
