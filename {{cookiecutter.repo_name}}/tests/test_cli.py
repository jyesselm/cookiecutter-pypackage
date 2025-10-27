"""Tests for the CLI module."""

import pytest
from click.testing import CliRunner

from {{ cookiecutter.repo_name }}.cli import cli


class TestCLI:
    """Test cases for the CLI."""

    def test_cli_help(self) -> None:
        """Test that the CLI shows help."""
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "{{ cookiecutter.project_short_description }}" in result.output

    def test_hello_command(self) -> None:
        """Test the hello command."""
        runner = CliRunner()
        result = runner.invoke(cli, ["hello"])
        assert result.exit_code == 0
        assert "Hello, world!" in result.output

    def test_hello_verbose(self) -> None:
        """Test the hello command with verbose flag."""
        runner = CliRunner()
        result = runner.invoke(cli, ["hello", "--verbose"])
        assert result.exit_code == 0
        assert "Hello, world! (verbose mode)" in result.output
