# Learning Claude Code

A Python library for learning Claude Code.

## Features

- Modern Python package structure with `src/` layout
- Type checking with mypy
- Linting and formatting with ruff
- Testing with pytest
- Pre-commit hooks for code quality
- CI/CD with GitHub Actions

## Installation

### From source

```bash
git clone https://github.com/opethe1st/learning_claude_code.git
cd learning_claude_code
pip install -e ".[dev]"
```

## Development

### Setup

1. Clone the repository
2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -e ".[dev]"
```

4. Install pre-commit hooks:

```bash
pre-commit install
```

### Running Tests

```bash
pytest
```

### Code Quality

Run linting:

```bash
ruff check src tests
```

Run formatting:

```bash
ruff format src tests
```

Run type checking:

```bash
mypy src
```

## License

MIT License - see LICENSE file for details
