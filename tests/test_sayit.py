#!/usr/bin/env python

"""Tests for `sayit` package."""

import pytest

from click.testing import CliRunner

from sayit import sayit
from sayit import cli


@pytest.mark.parametrize("number, human_text",[
    (0,'zero'),
    (1,'one'),
    (2,'two'),
    (3,'three'),
    (4,'four'),
    (5,'five'),
    (6,'six'),
    (7,'seven'),
    (8,'eight'),
    (9,'nine'),
])
def test_up_to_single_digit(number, human_text):
    assert sayit(number) == human_text



# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'sayit.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
