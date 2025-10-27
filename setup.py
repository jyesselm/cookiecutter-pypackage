#!/usr/bin/env python3
"""Setup script to automatically detect user information and update cookiecutter.json."""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


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


def update_cookiecutter_json():
    """Update cookiecutter.json with detected user information."""
    cookiecutter_path = Path("cookiecutter.json")

    if not cookiecutter_path.exists():
        print("Error: cookiecutter.json not found!")
        return False

    # Load existing cookiecutter.json
    with open(cookiecutter_path, "r") as f:
        config = json.load(f)

    # Detect user information
    author_name = get_author_name()
    author_email = get_author_email()
    github_username = get_github_username()
    year = get_current_year()
    release_date = get_current_date()

    # Update the configuration
    config["author_name"] = author_name
    config["author_email"] = author_email
    config["year"] = str(year)
    config["release_date"] = release_date

    if github_username:
        config["github_username"] = github_username

    # Save updated configuration
    with open(cookiecutter_path, "w") as f:
        json.dump(config, f, indent=2)

    print("Updated cookiecutter.json with detected information:")
    print(f"  Author Name: {author_name}")
    print(f"  Author Email: {author_email}")
    print(f"  GitHub Username: {github_username or 'Not detected'}")
    print(f"  Year: {year}")
    print(f"  Release Date: {release_date}")

    return True


def main():
    """Main function."""
    if update_cookiecutter_json():
        print("\n✅ Setup complete! You can now use the cookiecutter template.")
        print("\nTo use the template:")
        print("  cookiecutter .")
        print("\nTo update your information later:")
        print("  python setup.py")
    else:
        print("❌ Setup failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
