#!/usr/bin/env python3
"""Pre-generation hook to automatically detect user information."""

import os
import subprocess
import sys
from datetime import datetime


def get_git_config(key):
    """Get git configuration value."""
    try:
        result = subprocess.run(
            ["git", "config", "--get", key], capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def get_github_username():
    """Try to get GitHub username from git config or environment."""
    # Try git config first
    username = get_git_config("github.user")
    if username:
        return username

    # Try environment variable
    username = os.environ.get("GITHUB_USERNAME")
    if username:
        return username

    # Try to extract from git remote if available
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True,
        )
        remote_url = result.stdout.strip()
        if "github.com" in remote_url:
            # Extract username from URL like https://github.com/username/repo.git
            parts = remote_url.split("/")
            if len(parts) >= 4:
                return parts[3]
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    return None


def get_author_name():
    """Get author name from git config or environment."""
    # Try git config first
    name = get_git_config("user.name")
    if name:
        return name

    # Try environment variable
    name = os.environ.get("AUTHOR_NAME")
    if name:
        return name

    # Try system username
    name = os.environ.get("USER") or os.environ.get("USERNAME")
    if name:
        return name.title()

    return "Your Name"


def get_author_email():
    """Get author email from git config or environment."""
    # Try git config first
    email = get_git_config("user.email")
    if email:
        return email

    # Try environment variable
    email = os.environ.get("AUTHOR_EMAIL")
    if email:
        return email

    return "your.email@example.com"


def get_current_year():
    """Get current year."""
    return datetime.now().year


def get_current_date():
    """Get current date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")


def main():
    """Main function to set cookiecutter context variables."""
    # Set the context variables that will be available in templates
    context = {
        "author_name": get_author_name(),
        "author_email": get_author_email(),
        "github_username": get_github_username(),
        "year": get_current_year(),
        "release_date": get_current_date(),
    }

    # Write to a file that can be read by cookiecutter
    with open("cookiecutter_context.json", "w") as f:
        import json

        json.dump(context, f, indent=2)

    print("Detected user information:")
    for key, value in context.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
