from unittest.mock import patch
from calculator.repl import run_calculator


def test_exit():
    with patch("builtins.input", side_effect=["exit"]):
        run_calculator()


def test_invalid_operation():
    with patch("builtins.input", side_effect=["x", "exit"]):
        run_calculator()


def test_addition():
    with patch("builtins.input", side_effect=["+", "2", "3", "exit"]):
        run_calculator()


def test_subtraction():
    with patch("builtins.input", side_effect=["-", "5", "2", "exit"]):
        run_calculator()


def test_multiplication():
    with patch("builtins.input", side_effect=["*", "3", "4", "exit"]):
        run_calculator()


def test_division():
    with patch("builtins.input", side_effect=["/", "10", "2", "exit"]):
        run_calculator()


def test_divide_by_zero():
    with patch("builtins.input", side_effect=["/", "10", "0", "exit"]):
        run_calculator()


def test_invalid_number():
    with patch("builtins.input", side_effect=["+", "abc", "5", "exit"]):
        run_calculator()
