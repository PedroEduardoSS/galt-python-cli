"""
Esse módulo testa cenários de argumentos do módulo argumentos.py.
Cenários:
    1 - Testa a criação da instância do argumentparser
    2 - Testa os argumentos já definidos por padrão
    3 - Testa os argumentos simulando valores passados pelo usuário
    4 - Testa o argumento ops customizado

NOTA: No argumento ops é necessário colocar o sinal '=' antes e depois devido algum erro nos casos
de colocar '-' ou '-*' como operadores.
"""

import pytest
import sys
from argparse import ArgumentParser
from mathquiz import get_parser

def test_get_parser_returns_argumentparser():
    parser = get_parser()
    assert isinstance(parser, ArgumentParser)

def test_default_arguments():
    parser = get_parser()
    args = parser.parse_args([])
    assert args.num == 10
    assert args.ops == "=+-*/="
    assert args.min == 1
    assert args.max == 10
    assert args.decimals is False
    assert args.places == 2

def test_all_arguments():
    parser = get_parser()
    argv = [
        "--num", "5",
        "--ops", "=+-=",
        "--min", "3",
        "--max", "15",
        "--decimals",
        "--places", "4"
    ]
    args = parser.parse_args(argv)
    assert args.num == 5
    assert args.ops == "=+-="
    assert args.min == "3"
    assert args.max == "15"
    assert args.decimals is True
    assert args.places == 4

def test_invalid_num_argument(monkeypatch):
    parser = get_parser()
    testargs = ["prog", "--num", "abc"]
    monkeypatch.setattr(sys, "argv", testargs)
    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(testargs[1:])
    assert excinfo.value.code == 2

def test_ops_argument_custom():
    parser = get_parser()
    args = parser.parse_args(["--ops", "=+="])
    assert args.ops == "=+="