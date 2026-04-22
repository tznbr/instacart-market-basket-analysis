# I am working on an Instacart analysis project using pandas and Plotly.

# I have a CSV file called "final_instacart_pipeline.csv" that contains the following columns:

# order_dow (day of week, values 0–6)
# order_hour_of_day (values 0–23)

# Please generate Python code that:

# Uses pandas and plotly.express (no matplotlib)
# Defines a function called make_chart_4() that returns a Plotly figure
# Loads the CSV into a dataframe called df
# Groups the data by order_dow and order_hour_of_day
# Calculates the total number of orders for each combination
# Converts the numeric day of week (0–6) into readable labels:
# 0 → Sunday
# 1 → Monday
# 2 → Tuesday
# 3 → Wednesday
# 4 → Thursday
# 5 → Friday
# 6 → Saturday
# Creates a heatmap using plotly.express.density_heatmap:
# x-axis: order_hour_of_day
# y-axis: day of week (as readable names)
# color: order count
# Uses a clean, professional color scale (e.g., "Blues")
# Ensures:
# hours are displayed clearly from 0–23 on the x-axis
# days are ordered correctly from Sunday to Saturday on the y-axis
# Applies a clean layout using the "plotly_white" template
# Includes a clear title and axis labels
# Sets an appropriate chart height for dashboard display
# Returns the figure (do not display it and do not create a Dash app)

# Return only clean, runnable Python code.

import pandas as pd
import plotly.express as px

def make_chart_4():
    df = pd.read_csv("final_instacart_pipeline.csv")

    order_counts = (
        df.groupby(["order_dow", "order_hour_of_day"])
        .size()
        .reset_index(name="order_count")
    )

    order_counts["order_dow_name"] = order_counts["order_dow"].map(
        {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    )

    fig = px.density_heatmap(
        order_counts,
        x="order_hour_of_day",
        y="order_dow_name",
        z="order_count",
        color_continuous_scale="Blues",
        labels={
            "order_hour_of_day": "Hour of Day",
            "order_dow_name": "Day of Week",
            "order_count": "Order Count",
        },
        title="Order Volume by Day of Week and Hour",
        template="plotly_white"
    )

    fig.update_layout(
        xaxis=dict(tickmode="linear", tick0=0, dtick=1),
        yaxis=dict(categoryorder="array", categoryarray=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]),
        height=500
    )

    return fig
