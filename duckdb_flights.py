import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import duckdb as ddb
    from pathlib import Path
    return ddb, mo


@app.cell
def _(mo):
    mo.md(r"""
    # Chapter 2: Importing Data into DuckDB

    Loading from different data sources

    ## Loadinf CSV File
    """)
    return


@app.cell
def _(ddb):
    conn = ddb.connect()

    query = '''
      DROP TABLE IF EXISTS flights;
      CREATE TABLE flights 
      as FROM read_csv_auto('data_flights/flights.csv')
      LIMIT 1000
    '''

    df_flights = conn.execute(query).df()
    return (conn,)


@app.cell
def _(conn, mo):
    mo.plain(conn.execute('SELECT * FROM flights').df())
    return


if __name__ == "__main__":
    app.run()
