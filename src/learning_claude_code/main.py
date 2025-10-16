"""Main FastAPI application."""

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI

from learning_claude_code import __version__
from learning_claude_code.api import router as api_router
from learning_claude_code.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application lifespan events."""
    # Create database tables on startup
    Base.metadata.create_all(bind=engine)
    yield
    # Cleanup on shutdown (if needed)


app = FastAPI(
    title="Learning Claude Code API",
    description="A FastAPI web service for learning Claude Code",
    version=__version__,
    lifespan=lifespan,
)

# Include API router
app.include_router(api_router, prefix="/api")


@app.get("/")
def read_root() -> dict[str, str]:
    """Root endpoint returning API information."""
    return {
        "name": "Learning Claude Code API",
        "version": __version__,
        "docs": "/docs",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
