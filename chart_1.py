#  i am working on an Instacart analysis project using pandas and matplotlib.

# I have a CSV file called "final_instacart_pipeline.csv" that already contains a column called:
# - reorder_type (values: Weekly, Bi-Weekly, Other)
# - reordered (0 or 1)

# Please generate Python code that:

# 1. Loads the CSV into a dataframe called df
# 2. Filters the data to only include "Weekly" and "Bi-Weekly"
# 3. Calculates the average reorder rate for each group
# 4. Creates a clean, executive-level bar chart comparing Weekly vs Bi-Weekly reorder rates
# 5. Uses matplotlib only (no seaborn)
# 6. Includes clear titles, axis labels, and good spacing
# 7. Keeps the visualization simple and presentation-ready

# Return only clean, runnable Python code.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

df = pd.read_csv("final_instacart_pipeline.csv")

subset = df[df["reorder_type"].isin(["Weekly", "Bi-Weekly"])]

rates = (
subset.groupby("reorder_type")["reordered"]
.mean()
.reindex(["Weekly", "Bi-Weekly"])
* 100
)

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(
rates.index,
rates.values,
color=["#4C72B0", "#55A868"],
width=0.5,
edgecolor="none",
)

ax.set_title("Weekly vs Bi-Weekly Reorder Rates", fontsize=16, weight="semibold", pad=14)
ax.set_ylabel("Reorder Rate (%)", fontsize=12)
ax.set_xlabel("")
ax.set_ylim(0, max(rates.values) * 1.15)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(True)
ax.spines["bottom"].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.3)

ax.bar_label(bars, labels=[f"{value:.1f}%" for value in rates.values], padding=6, fontsize=11)
plt.tight_layout()
plt.show()