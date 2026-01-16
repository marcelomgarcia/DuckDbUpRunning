import marimo

__generated_with = "0.19.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import duckdb
    import polars as pl
    return duckdb, mo


@app.cell
def _(mo):
    mo.md(r"""
    Learning DuckDB
    ===============

    The dataset is [Public Sector Network](https://www.kaggle.com/datasets/mirzamilanfarabi/public-sector-network) because it seems to be enough complex with a few files and still small enough to be uploaded to GitHub.
    """)
    return


@app.cell
def _(duckdb):
    conn = duckdb.connect()
    query = '''
      SELECT Node_ID,Type,Region 
      FROM read_csv_auto('data/nodes.csv')
      '''
    df = conn.execute(query).df()
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
