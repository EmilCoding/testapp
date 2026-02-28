import pytest
from app import func


def test_message(monkeypatch) -> None:
    givenargs = None
    givenkwargs = None
    def mockprint(*args, **kwargs) -> None:
        nonlocal givenargs, givenkwargs
        givenargs = args    
        givenkwargs = kwargs   

    monkeypatch.setattr('builtins.print', mockprint)
    func()
    
    assert givenargs == ('Hello, World!', )
    assert not givenkwargs
