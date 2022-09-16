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

from plotly.graph_objects import Figure # type: ignore
from dash import Dash, dcc, html # type: ignore
from dash.dependencies import Input, Output # type: ignore

from graphs import migration, population, fertility, average, urban_population

from data_migrator import df
from utils import filter_values


app = Dash(__name__)

# Layout
app.layout = html.Div(children=[
    html.H1(children="População em Nível Continental"),

    # Taxa de Migração
    html.Div(children=[
        dcc.Graph(id="migration-rate", figure=migration.chart), # type: ignore
        dcc.RangeSlider(
            min=1955, # type: ignore
            max=2020, # type: ignore
            id="migration-rate-slider", # type: ignore
            step=1, # type: ignore
            marks=None, # type: ignore
            pushable=True, # type: ignore
            value=[1955, 2020], # type: ignore
            tooltip={ # type: ignore
                "placement": "bottom",
                "always_visible": True,
            },
        )
    ]),
])


# Callbacks
@app.callback( # type: ignore
    Output(component_id="migration-rate", component_property="figure"),
    Input(component_id="migration-rate-slider", component_property="value"),
)
def update_migration_rate(value: list[int]) -> Figure: # type: ignore
    # Filtramos o DataFrame com os valores do intervalo escolhido.
    new_df = filter_values(df, "year", *list(range(*value)))

    # Criamos e retornamos o gráfico com os novos valores.
    return migration.create_chart(new_df) # type: ignore


if __name__ == "__main__":
    app.run_server(debug=True) # type: ignore
