# I have a CSV file called "final_instacart_pipeline.csv" that contains the following column:

# days_since_prior_order

# Please generate Python code that:

# Uses pandas and plotly.express (no matplotlib)
# Defines a function called make_chart_3() that returns a Plotly figure
# Loads the CSV into a dataframe called df
# Filters out null values in days_since_prior_order
# Filters the data to only include values between 0 and 30 days
# Creates a histogram showing the distribution of days_since_prior_order
# Uses an appropriate number of bins (e.g., 30) to clearly show patterns
# Adds vertical reference lines at 7 and 14 days to highlight weekly and bi-weekly cycles
# Uses a clean, professional style (plotly_white template)
# Includes a clear title and axis labels
# Returns the figure (do not display it and do not create a Dash app)

# Return only clean, runnable Python code.

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def make_chart_3():
    df = pd.read_csv("final_instacart_pipeline.csv")
    subset = df[df["days_since_prior_order"].notna()]
    subset = subset[(subset["days_since_prior_order"] >= 0) & (subset["days_since_prior_order"] <= 30)]

    fig = px.histogram(
        subset,
        x="days_since_prior_order",
        nbins=30,
        title="Distribution of Days Since Prior Order",
        labels={"days_since_prior_order": "Days Since Prior Order", "count": "Order Count"},
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title="Days Since Prior Order",
        yaxis_title="Count",
        bargap=0.1,
        height=450
    )

    fig.add_vline(x=7, line_dash="dash", line_color="#636EFA", annotation_text="7 days", annotation_position="top left")
    fig.add_vline(x=14, line_dash="dash", line_color="#EF553B", annotation_text="14 days", annotation_position="top left")

    return fig
