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