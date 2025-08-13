import marimo

__generated_with = "0.14.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import duckdb
    import pandas as pd
    return duckdb, mo


@app.cell
def _(duckdb):
    conn = duckdb.connect()

    conn.execute('''
        CREATE TABLE flights
        as
        SELECT * FROM read_csv_auto('data/flights.csv')
        LIMIT 1000
        ''').df()
    return (conn,)


@app.cell
def _(conn):
    conn.execute('''
        CREATE OR REPLACE TABLE airports(
            IATA_CODE VARCHAR, AIRPORT VARCHAR, CITY VARCHAR,
            STATE VARCHAR, COUNTRY VARCHAR, LATITUDE VARCHAR,
            LONGITUDE VARCHAR);
        COPY airports FROM 'data/airports.csv' (AUTO_DETECT TRUE);
    ''')

    df = conn.execute('SELECT * FROM airports').df()
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// attention | Attention!

    This is important
    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
