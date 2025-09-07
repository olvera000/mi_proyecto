import builtins

import pytest

from src.main import greet, main


def test_greet_default():
    assert greet() == "Hola, Mundo!"


@pytest.mark.parametrize("name,expected", [
    ("Ana", "Hola, Ana!"),
    ("Carlos", "Hola, Carlos!"),
])
def test_greet_with_name(name, expected):
    assert greet(name) == expected


def test_cli_outputs_name(capsys):
    # call main() with args to avoid exiting the interpreter
    rc = main(["--name", "CLI"])
    captured = capsys.readouterr().out.strip()
    assert rc == 0
    assert captured == "Hola, CLI!"
