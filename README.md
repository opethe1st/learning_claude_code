# Learning Claude Code

A Python library for learning Claude Code.

## Features

- Modern Python package structure with `src/` layout
- FastAPI web service with RESTful API endpoints
- PostgreSQL database with SQLAlchemy ORM
- Docker and Docker Compose setup for easy deployment
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

## Usage

### Running with Docker (Recommended)

The easiest way to run the application is with Docker Compose, which sets up both the app and PostgreSQL database:

```bash
docker-compose up --build
```

This will:
- Start a PostgreSQL database container
- Build and start the FastAPI application container
- Create database tables automatically
- Enable hot-reload for development

The API will be available at:
- API: http://localhost:8000
- Interactive API docs (Swagger UI): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc

To stop the services:
```bash
docker-compose down
```

To stop and remove volumes (clears database data):
```bash
docker-compose down -v
```

### Running Locally (Without Docker)

If you prefer to run without Docker, you'll need PostgreSQL installed locally.

1. Start PostgreSQL and create a database:
```bash
createdb learning_claude_code
```

2. Set the database URL environment variable:
```bash
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/learning_claude_code"
```

3. Start the development server:
```bash
uvicorn learning_claude_code.main:app --reload
```

### API Endpoints

The service includes the following endpoints:

- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint
- `GET /api/items` - List all items
- `GET /api/items/{item_id}` - Get a specific item
- `POST /api/items` - Create a new item
- `PUT /api/items/{item_id}` - Update an item
- `DELETE /api/items/{item_id}` - Delete an item

### Example API Usage

Create an item:
```bash
curl -X POST "http://localhost:8000/api/items" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Example Item",
    "description": "An example item",
    "price": 29.99,
    "quantity": 10
  }'
```

List all items:
```bash
curl "http://localhost:8000/api/items"
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
