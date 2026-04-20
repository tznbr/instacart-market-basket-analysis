# I am working on an Instacart analysis project using pandas and Plotly Dash.

# I have a CSV file called "final_instacart_pipeline.csv" that contains the following columns:

# reorder_type (values: Weekly, Bi-Weekly, Other)
# product_name
# reordered (0 or 1)

# I already created two analyses:

# Reorder rate comparison for Weekly vs Bi-Weekly users
# Top 5 most reordered products

# Please generate Python code that:

# Uses Plotly (not matplotlib)
# Loads the CSV into a dataframe called df
# Filters the data to only include "Weekly" and "Bi-Weekly" reorder types
# Groups by reorder_type and calculates the average reorder rate
# Creates a clean bar chart comparing Weekly vs Bi-Weekly reorder rates
import pandas as pd
import plotly.express as px

def make_chart_1():
    df = pd.read_csv("final_instacart_pipeline.csv")

    filtered = df[df["reorder_type"].isin(["Weekly", "Bi-Weekly"])]

    summary = (
        filtered.groupby("reorder_type")["reordered"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        summary,
        x="reorder_type",
        y="reordered",
        title="Reorder Rate: Weekly vs Bi-Weekly"
    )

    return fig