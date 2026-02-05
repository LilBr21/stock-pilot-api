# Stock Pilot API

Backend API for Stock Pilot - a market analysis and portfolio tracking application.

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL with async SQLAlchemy 2.0
- **Migrations**: Alembic
- **Auth**: JWT (access + refresh tokens)
- **Validation**: Pydantic v2
- **Stock Data**: Finnhub API

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL 16+
- Finnhub API key (free at [finnhub.io](https://finnhub.io))

### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Copy environment file and configure
cp .env.example .env
```

### Environment Variables

Edit `.env` with your values:

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/stockpilot
SECRET_KEY=your-secret-key-min-32-chars
FINNHUB_API_KEY=your-finnhub-api-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

### Database Setup

```bash
# Start PostgreSQL (Docker example)
docker run -d --name stockpilot-db \
  -p 5432:5432 \
  -e POSTGRES_USER=stockpilot \
  -e POSTGRES_PASSWORD=stockpilot \
  -e POSTGRES_DB=stockpilot \
  postgres:16

# Run migrations
alembic upgrade head
```

### Running the Server

```bash
# Development with hot reload
uvicorn app.main:app --reload

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

API will be available at `http://localhost:8000`

### API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Auth
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login (returns JWT tokens)
- `POST /api/v1/auth/refresh` - Refresh access token
- `POST /api/v1/auth/logout` - Logout

### Users
- `GET /api/v1/users/me` - Get current user
- `PATCH /api/v1/users/me` - Update profile

### Stocks
- `GET /api/v1/stocks/search?q={query}` - Search stocks
- `GET /api/v1/stocks/{symbol}` - Get stock quote
- `GET /api/v1/stocks/{symbol}/chart` - Get chart data

### Watchlists
- `GET /api/v1/watchlists` - List watchlists
- `POST /api/v1/watchlists` - Create watchlist
- `GET /api/v1/watchlists/{id}` - Get watchlist
- `DELETE /api/v1/watchlists/{id}` - Delete watchlist
- `POST /api/v1/watchlists/{id}/items` - Add stock
- `DELETE /api/v1/watchlists/{id}/items/{symbol}` - Remove stock

## Project Structure

```
app/
├── main.py              # FastAPI app entry point
├── core/
│   ├── config.py        # Settings (pydantic-settings)
│   └── security.py      # JWT & password hashing
├── db/
│   ├── base.py          # SQLAlchemy base
│   └── session.py       # Async session
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── services/            # Business logic
└── api/
    ├── deps.py          # Dependencies (auth, db)
    └── v1/              # API routes
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_auth.py -v
```

## Development

### Creating Migrations

```bash
# Auto-generate migration from model changes
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1
```
