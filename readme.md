# SPX AI Backend V1

FastAPI backend for the SPX AI Trading Dashboard.

## Important

This V1 uses DEMO SPX/options data by default.

It is intended for development, testing, and paper-trading workflows.

It does not yet connect to live Robinhood SPX/options data.

## Features

- FastAPI API
- Demo SPX market snapshot
- Demo technical indicators
- Demo support/resistance levels
- Demo 0DTE strategy candidates
- Hard risk-management filter
- OpenAI analysis endpoint
- Safe fallback mode when OpenAI is not configured
- In-memory paper trading
- Base44-compatible CORS
- Render deployment configuration

## Run locally

Install Python 3.13.

Create a virtual environment:

```bash
python -m venv .venv
