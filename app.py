from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv(
    "data/ourworldindata_covid.csv",
)

app = Dash()

# Requires Dash 2.17.0 or later
app.layout = [
    html.H1(children="Covid Dashboard", style={"textAlign": "center"}),
    dcc.Dropdown(df.country.unique(), "Canada", id="dropdown-selection"),
    dcc.Graph(id="graph-content"),
]


@callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    dff = df[df.country == value]
    return px.line(
        dff,
        x="date",
        y="new_cases_smoothed_per_million",
    )


app.run(debug=True)
