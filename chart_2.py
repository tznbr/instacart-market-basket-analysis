# I have a CSV file called "final_instacart_pipeline.csv" that contains the following columns:

# reorder_type (values: Weekly, Bi-Weekly, Other)
# product_name
# reordered (0 or 1)

# Please generate Python code that:

# Uses pandas and plotly.express (no matplotlib)
# Defines a function called make_chart_2() that returns a Plotly figure
# Loads the CSV into a dataframe called df
# Filters the data to only include "Weekly" and "Bi-Weekly" reorder types
# Filters to only include reordered items (where reordered = 1)
# Groups the data by product_name and calculates the total number of reorders
# Identifies the top 5 most frequently reordered products
# Creates a clean horizontal bar chart showing these products
# x-axis: reorder count
# y-axis: product_name
# Uses a simple, professional style (e.g., plotly_white template)
# Includes a clear title and axis labels
# Returns the figure (do not display it and do not create a Dash app)

# Return only clean, runnable Python code.

import pandas as pd
import plotly.express as px

def make_chart_2():
    # Load the CSV into a dataframe
    df = pd.read_csv("final_instacart_pipeline.csv")
    
    # Filter to only include "Weekly" and "Bi-Weekly" reorder types and reordered items
    subset = df[
        df["reorder_type"].isin(["Weekly", "Bi-Weekly"]) & (df["reordered"] == 1)
    ]
    
    # Group by product_name and count total reorders
    product_reorders = subset.groupby("product_name").size().reset_index(name="reorder_count")
    
    # Get the top 5 most frequently reordered products
    top_5 = product_reorders.nlargest(5, "reorder_count")
    
    # Create the horizontal bar chart
    fig = px.bar(
        top_5,
        x="reorder_count",
        y="product_name",
        orientation="h",
        title="Top 5 Most Frequently Reordered Products",
        labels={"reorder_count": "Reorder Count", "product_name": "Product Name"},
        template="plotly_white"
    )
    
    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        xaxis_title="Reorder Count",
        yaxis_title="Product Name",
        height=400
    )
    
    return fig
