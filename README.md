# Modern Python Package Cookiecutter

A modern cookiecutter template for Python packages with all the latest best practices.

## Features

- **Modern Python packaging** with `pyproject.toml`
- **Type hints and mypy support** for better code quality
- **Comprehensive testing** with pytest and coverage
- **Code formatting** with Black and isort
- **Fast linting** with Ruff
- **Pre-commit hooks** for automated code quality
- **GitHub Actions CI/CD** with multi-Python testing
- **Professional project structure** with src layout
- **Automatic user detection** - no need to enter personal info every time!

## Quick Start

1. **Setup your personal information** (one-time setup):
   ```bash
   python setup.py
   ```
   This will automatically detect your name, email, and GitHub username from git config.

2. **Create a new Python package**:
   ```bash
   cookiecutter .
   ```

3. **Follow the prompts** - you only need to provide:
   - Project name
   - Repository name (auto-generated from project name)
   - Project description

## What's Included

### Project Structure
```
your-package/
├── src/your_package/          # Source code in modern src layout
├── tests/                     # Test directory
├── docs/                      # Documentation directory
├── .github/
│   ├── workflows/ci.yml       # GitHub Actions CI/CD
│   ├── ISSUE_TEMPLATE/        # Issue templates
│   └── pull_request_template.md
├── pyproject.toml             # Modern Python packaging
├── .pre-commit-config.yaml    # Pre-commit hooks
├── Makefile                   # Common development tasks
├── LICENSE                    # MIT license
├── CHANGELOG.md               # Changelog
└── README.md                  # Project documentation
```

### Development Tools
- **Black** - Code formatting
- **isort** - Import sorting
- **Ruff** - Fast linting
- **mypy** - Type checking
- **pytest** - Testing framework
- **pre-commit** - Git hooks for code quality

### CI/CD
- **GitHub Actions** with multi-Python testing (3.8, 3.9, 3.10, 3.11, 3.12)
- **Automated testing, linting, and building**
- **Code coverage reporting** with Codecov

## Customization

### Personal Information
The template automatically detects your personal information from:
1. Git configuration (`git config user.name`, `git config user.email`)
2. Environment variables (`AUTHOR_NAME`, `AUTHOR_EMAIL`, `GITHUB_USERNAME`)
3. System username (fallback)

To update your information later:
```bash
python setup.py
```

### Environment Variables
You can set these environment variables to override automatic detection:
```bash
export AUTHOR_NAME="Your Name"
export AUTHOR_EMAIL="your.email@example.com"
export GITHUB_USERNAME="yourusername"
```

## Development

After creating a package, you can:

1. **Install in development mode**:
   ```bash
   cd your-package
   pip install -e ".[dev]"
   pre-commit install
   ```

2. **Run tests**:
   ```bash
   make test
   # or
   pytest
   ```

3. **Format code**:
   ```bash
   make format
   # or
   black src/ tests/
   isort src/ tests/
   ```

4. **Lint code**:
   ```bash
   make lint
   # or
   ruff check src/ tests/
   mypy src/
   ```

5. **Run all checks**:
   ```bash
   make check
   ```

## Available Make Commands

- `make help` - Show all available commands
- `make install` - Install the package
- `make install-dev` - Install in development mode
- `make test` - Run tests
- `make test-cov` - Run tests with coverage
- `make lint` - Run linting
- `make format` - Format code
- `make format-check` - Check code formatting
- `make clean` - Clean build artifacts
- `make build` - Build the package
- `make publish` - Publish to PyPI
- `make check` - Run all checks
- `make pre-commit` - Run pre-commit on all files

## License

This template is licensed under the MIT License.
