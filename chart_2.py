# I have a CSV file called "final_instacart_pipeline.csv" that already contains the following columns:

# reorder_type (values: Weekly, Bi-Weekly, Other)
# product_name
# reordered (0 or 1)

# Please generate Python code that:

# Loads the CSV into a dataframe called df
# Filters the data to only include "Weekly" and "Bi-Weekly" reorder types
# Filters to only include reordered products (where reordered = 1)
# Identifies the top 5 most frequently reordered products for each group (Weekly and Bi-Weekly)
# Creates two clean horizontal bar charts:
# One for Weekly users
# One for Bi-Weekly users
# Uses matplotlib only (no seaborn)
# Includes clear titles, axis labels, and good spacing
# Keeps the visualizations simple and presentation-ready

# Return only clean, runnable Python code.

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV into a dataframe
df = pd.read_csv("final_instacart_pipeline.csv")

# Filter to only include "Weekly" and "Bi-Weekly" reorder types and reordered products
subset = df[
    df["reorder_type"].isin(["Weekly", "Bi-Weekly"]) & (df["reordered"] == 1)
]

# Get top 5 most frequently reordered products for Weekly
weekly_top5 = (
    subset[subset["reorder_type"] == "Weekly"]["product_name"]
    .value_counts()
    .head(5)
)

# Get top 5 most frequently reordered products for Bi-Weekly
biweekly_top5 = (
    subset[subset["reorder_type"] == "Bi-Weekly"]["product_name"]
    .value_counts()
    .head(5)
)

# Create subplots for the two charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Weekly chart
ax1.barh(weekly_top5.index, weekly_top5.values, color="#4C72B0")
ax1.set_title("Top 5 Reordered Products - Weekly Users", fontsize=14, weight="semibold", pad=10)
ax1.set_xlabel("Reorder Count", fontsize=12)
ax1.invert_yaxis()  # To have the highest at the top

# Bi-Weekly chart
ax2.barh(biweekly_top5.index, biweekly_top5.values, color="#55A868")
ax2.set_title("Top 5 Reordered Products - Bi-Weekly Users", fontsize=14, weight="semibold", pad=10)
ax2.set_xlabel("Reorder Count", fontsize=12)
ax2.invert_yaxis()

# Adjust layout
plt.tight_layout()
plt.show()
