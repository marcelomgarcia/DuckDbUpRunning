# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains learning materials and examples from "DuckDB Up and Running" by Wei-Meng Lee (O'Reilly Media). The project demonstrates DuckDB functionality through interactive notebooks using Marimo.

## Environment Setup

**Python Version**: 3.11 (specified in `.python-version`)

**Package Management**: Uses `uv` for dependency management (note: `uv.lock` present)

Install dependencies:
```bash
uv sync
```

## Running Notebooks

The primary development approach uses Marimo notebooks for interactive exploration:

```bash
# Run a specific notebook
uv run marimo edit public_sector_network.py
uv run marimo edit duckdb_flights.py

# Run in view mode
uv run marimo run public_sector_network.py
```

## Data Organization

The repository uses two main datasets:

1. **Public Sector Network** (`data/public_net/`)
   - Primary dataset used in examples
   - Contains: nodes.csv, energy_usage.csv, traffic.csv, environment.csv, maintenance.csv, procurement.csv, recommendations.csv
   - Used in `public_sector_network.py`

2. **World Population** (`data/world_pop/`)
   - Contains: countries_of_the_world.csv

3. **Flight Data** (referenced but not included)
   - Original book uses 2015 Flight Delays dataset (too large for GitHub)
   - Example code references `data_flights/flights.csv`

## Architecture

**Notebook Structure**: Marimo notebooks are Python files with decorated cells using the `@app.cell` decorator pattern. Each cell is a function that returns the variables it creates, enabling reactive execution.

**DuckDB Connection Pattern**: Notebooks typically establish a DuckDB connection in an early cell (`conn = duckdb.connect()`) and use SQL queries via `read_csv_auto()` to load CSV data directly into queries or tables.

**Data Loading**: The codebase demonstrates loading CSV files using DuckDB's `read_csv_auto()` function directly in SQL queries rather than pre-loading into pandas or other frameworks.

## Key Dependencies

- **duckdb**: Core database engine
- **marimo**: Interactive notebook environment (reactive Python notebooks)
- **polars**: DataFrame library used in examples
- **fastparquet**: Parquet file support
- **mysql-connector-python**: MySQL integration examples
