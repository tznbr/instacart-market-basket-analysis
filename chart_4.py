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
