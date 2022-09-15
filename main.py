"""
MIT License

Copyright (c) 2022 UnB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from dash import Dash, dcc, html # type: ignore
from dash.dependencies import Input, Output # type: ignore
import plotly.express as px # type: ignore

from graphs import migration, population, fertility, average, urban_population

from data_migrator import df
from utils import filter_values


app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("População em Nível Continental"),

    # Taxa de Migração
    html.Div(children=[ # type: ignore
        dcc.Graph(
            id="migration-rate", # type: ignore
            figure=migration.chart # type: ignore
        )
    ]),

    # População
    html.Div(children=[ # type: ignore
        dcc.Graph(
            id="population", # type: ignore
            figure=population.chart # type: ignore
        )
    ]),

    # Taxa de Fertilidade
    html.Div(children=[ # type: ignore
        dcc.Graph(
            id="fertility-rate", # type: ignore
            figure=fertility.chart # type: ignore
        ),
         dcc.RangeSlider(
            id="fertility-range-slider",
            step=1,
            min = 1955,
            max = 2020,
            value=[1955, 2020],
            pushable=1,
            marks=None,
            tooltip={"placement": "bottom", "always_visible": True}
        )
    ]),

    # Média de Idades
    html.Div(children=[ # type: ignore
        dcc.Graph(
            id="average-age", # type: ignore
            figure=average.chart # type: ignore
        )
    ]),

    # População Urbana
    html.Div(children=[
        dcc.Graph(
            id="urban-population", # type: ignore
            figure=urban_population.chart # type: ignore
        )
    ]),
])
@app.callback(
    Output(component_id="fertility-rate", component_property="figure"),
    Input(component_id="fertility-range-slider", component_property="value")
)

def update_fertility_rate(input_value: list[int]): # type: ignore
    new_df = filter_values(df, "year", *list(range(*input_value)))
    chart = fertility.create_chart(new_df, fertility.labels, fertility.config)
    
    return chart


if __name__ == "__main__":
    app.run_server(debug=True) # type: ignore
