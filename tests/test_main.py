import sys

from src.main import greet, main


def test_greet_default():
    assert greet() == "Hola, Mundo!"


def test_greet_uppercase():
    assert greet("Mundo", uppercase=True) == "HOLA, MUNDO!"


def test_greet_with_name():
    assert greet("Ana") == "Hola, Ana!"


def test_cli_times(monkeypatch, capsys):
    # Simular llamada de CLI: 2 repeticiones con nombre "Ana"
    monkeypatch.setattr(sys, "argv", ["prog", "--name", "Ana", "--times", "2"])
    rc = main()
    out_lines = capsys.readouterr().out.strip().splitlines()
    assert rc == 0
    assert out_lines == ["Hola, Ana!", "Hola, Ana!"]
