"""Test if the command works"""
import os
import pytest


def test_running_module() -> None:
    assert not os.system('python -m app'), "Error was raised during module run"


def test_using_command() -> None:
    assert not os.system('app'), "Error was raised during 'app' command."
