.PHONY: help install install-dev test lint format clean build publish

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package
	pip install .

install-dev: ## Install the package in development mode
	pip install -e ".[dev,test]"
	pre-commit install

test: ## Run tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=src/{{ cookiecutter.repo_name }} --cov-report=html --cov-report=term

lint: ## Run linting
	ruff check src/ tests/
	mypy src/

format: ## Format code
	black src/ tests/
	isort src/ tests/

format-check: ## Check code formatting
	black --check src/ tests/
	isort --check-only src/ tests/

clean: ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: clean ## Build the package
	python -m build

publish: build ## Publish to PyPI
	twine upload dist/*

check: format-check lint test ## Run all checks

pre-commit: ## Run pre-commit on all files
	pre-commit run --all-files
