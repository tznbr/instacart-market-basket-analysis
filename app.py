# I am working on an Instacart analysis project using Dash and Plotly.

# I already have four separate Python chart files:

# chart_1.py with a function called make_chart_1()
# chart_2.py with a function called make_chart_2()
# chart_3.py with a function called make_chart_3()
# chart_4.py with a function called make_chart_4()

# Each function already returns a Plotly figure.

# Please generate Python code for a single file called app.py that:

# Imports Dash, html, and dcc
# Imports the four chart functions from their respective files
# Creates a Dash app
# Builds a clean, professional dashboard layout for a classroom presentation
# Includes:
# A main dashboard title at the top
# A short subtitle describing the project focus on Weekly vs Bi-Weekly reorder behavior
# All four charts displayed in a neat layout
# Arrange the charts in a 2x2 grid:
# Top left: chart 1
# Top right: chart 3
# Bottom left: chart 2
# Bottom right: chart 4
# Uses simple inline styling for spacing, margins, font, and alignment
# Keeps the layout clean and presentation-ready
# Runs locally with:
# if __name__ == "__main__":
#     app.run(debug=True)
# Returns only clean, runnable Python code for app.py


import dash
from dash import html, dcc
from chart_1 import make_chart_1
from chart_2 import make_chart_2
from chart_3 import make_chart_3
from chart_4 import make_chart_4

app = dash.Dash(__name__)
app.title = "Instacart Reorder Dashboard"

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Instacart Reorder Insights",
                    style={"margin": "0", "fontSize": "32px", "textAlign": "center"},
                ),
                html.P(
                    "Comparing Weekly and Bi-Weekly reorder behavior across product popularity and order timing.",
                    style={"margin": "8px 0 24px", "fontSize": "16px", "textAlign": "center", "color": "#555"},
                ),
            ],
            style={"padding": "24px 16px", "maxWidth": "1200px", "margin": "0 auto"},
        ),
        html.Div(
            [
                html.Div(
                    dcc.Graph(figure=make_chart_1()),
                    style={"width": "48%", "marginBottom": "24px"},
                ),
                html.Div(
                    dcc.Graph(figure=make_chart_3()),
                    style={"width": "48%", "marginBottom": "24px"},
                ),
            ],
            style={"display": "flex", "justifyContent": "space-between", "flexWrap": "wrap", "gap": "24px", "maxWidth": "1200px", "margin": "0 auto"},
        ),
        html.Div(
            [
                html.Div(
                    dcc.Graph(figure=make_chart_2()),
                    style={"width": "48%", "marginBottom": "24px"},
                ),
                html.Div(
                    dcc.Graph(figure=make_chart_4()),
                    style={"width": "48%", "marginBottom": "24px"},
                ),
            ],
            style={"display": "flex", "justifyContent": "space-between", "flexWrap": "wrap", "gap": "24px", "maxWidth": "1200px", "margin": "0 auto"},
        ),
    ],
    style={"fontFamily": "Arial, sans-serif", "backgroundColor": "#F8F9FB", "color": "#111", "paddingBottom": "32px"},
)

if __name__ == "__main__":
    app.run(debug=True)
