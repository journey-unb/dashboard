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
from dash import Dash, dcc, html, ctx # type: ignore
from dash.dependencies import Input, Output # type: ignore

from graphs import migration, population, fertility, average, urban_population

from data_migrator import df
from utils import filter_columns, filter_values, filter_range


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
        ),
    ]),

    # População Urbana
    html.Div(children=[
        dcc.Graph(
            id="urban-population", # type: ignore
            figure=urban_population.chart, # type: ignore
        ),
        html.Button("<",id="backward", n_clicks=0), # type: ignore
        html.Button(">", id="forward", n_clicks=0), # type: ignore
    ]),

    # Taxa de Fertilidade
    html.Div(children=[
        dcc.Graph(id="fertility-rate", figure=fertility.chart), # type: ignore
        dcc.RangeSlider(
            min=1955, # type: ignore
            max=2020, # type: ignore
            id="fertility-rate-year-slider", # type: ignore
            step=1, # type: ignore
            marks=None, # type: ignore
            pushable=True, # type: ignore
            value=[1955, 2020], # type: ignore
            tooltip={ # type: ignore
                "placement": "bottom",
                "always_visible": True,
            },
        ),
        dcc.RangeSlider(
            min=1, # type: ignore
            max=7, # type: ignore
            id="fertility-rate-slider", # type: ignore
            step=1, # type: ignore
            marks=None, # type: ignore
            pushable=True, # type: ignore
            value=[1.43, 6.71], # type: ignore
            tooltip={ # type: ignore
                "placement": "bottom",
                "always_visible": True,
            },
        ),
    ]),
])


# Callbacks
@app.callback( # type: ignore
    Output(component_id="migration-rate", component_property="figure"),
    Input(component_id="migration-rate-slider", component_property="value"),
)
def update_migration_rate(value: list[int]) -> Figure: # type: ignore
    # Filtramos o `DataFrame` com os valores do intervalo escolhido.
    new_df = filter_values(df, "year", *list(range(*value)))

    # Criamos e retornamos o gráfico com os novos valores.
    return migration.create_chart(new_df) # type: ignore


@app.callback( # type: ignore
    Output(component_id="urban-population", component_property="figure"),
    Input(component_id="backward", component_property="n_clicks"),
    Input(component_id="forward", component_property="n_clicks"),
)
def update_urban_population(
    backward: int,
    forward: int,
) -> Figure: # type: ignore
    # Definimos os valores para os botões `forward` e `backward`.
    values: dict[str | None, int] = {"backward": -5, "forward": 5, None: 0}
    triggered_id = ctx.triggered_id # type: ignore

    current_year = urban_population.current_year
    config = urban_population.config

    if 1955 <= current_year + values[triggered_id] <= 2020: # type: ignore
        urban_population.current_year += values[triggered_id] # type: ignore

    title_text = f"População Urbana ({current_year})"
    config["title"]["text"] = title_text
    
    filtered_df = filter_values(df, "year", current_year)
    return urban_population.create_chart(filtered_df, config=config) # type: ignore
    

@app.callback( # type: ignore
    Output(component_id="fertility-rate", component_property="figure"),
    Input(
        component_id="fertility-rate-year-slider",
        component_property="value",
    ),
    Input(component_id="fertility-rate-slider", component_property="value"),
)
def update_fertility_rate(
    years_values: list[int],
    rate_values: list[int],
) -> Figure: # type: ignore
    # Filtramos o `DataFrame` com os valores do intervalo escolhido.
    filtered_df = filter_columns(df, "year", "region", "fertility_rate")
    new_df = filter_range(filtered_df, "year", years_values)
    new_df = filter_range(new_df, "fertility_rate", rate_values)

    # Criamos e retornamos o gráfico com os novos valores.
    return fertility.create_chart(new_df) # type: ignore


if __name__ == "__main__":
    app.run_server(debug=True) # type: ignore
