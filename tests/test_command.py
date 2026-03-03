"""Test if the command works"""
import subprocess


def test_running_module() -> None:
    assert subprocess.run(['python', '-m', 'app']), "Error was raised during module run"


def test_using_command() -> None:
    assert subprocess.run(["app"]), "Error was raised during 'app' command."
