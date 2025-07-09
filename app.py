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
    dcc.RadioItems(
        options=["total_cases", "new_cases", "new_cases_smoothed_per_million"],
        value="total_cases",
        id="controls-and-radio-item",
    ),
    dcc.Graph(id="graph-content"),
]


@callback(
    Output("graph-content", "figure"),
    Input("dropdown-selection", "value"),
    Input("controls-and-radio-item", "value"),
)
def update_graph(country, radio_value):
    dff = df[df.country == country]
    return px.line(
        dff,
        x="date",
        y=radio_value,
    )


app.run(debug=True)
