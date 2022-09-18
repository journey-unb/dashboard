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

import dash_daq as daq # type: ignore

from graphs import migration, population, fertility, average, urban_population

from data_migrator import df
from utils import filter_columns, filter_values, filter_range, closest_value


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

    # Percentual Populacional
    html.Div(children=[
        dcc.Graph(id="population-percentage", figure=population.chart), # type: ignore
        daq.NumericInput( # type: ignore
            min=1955, # type: ignore
            max=2020, # type: ignore
            id="population-percentage-input", # type: ignore
            label="Alterar ano", # type: ignore
            labelPosition="top", # type: ignore
            size=80, # type: ignore
            value=population.current_year, # type: ignore
        )
    ]),

    # Média de Idades
    html.Div(children=[
        dcc.Graph(id="age-average", figure=average.chart),

    ])
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


@app.callback( # type: ignore
    Output(component_id="population-percentage", component_property="figure"),
    Input(
        component_id="population-percentage-input",
        component_property="value",
    ),
)
def update_population_percentage(value: int) -> Figure:
    population_df = population.filtered_columns
    config = population.config

    rows = population_df.values.tolist() # type: ignore

    # Criamos uma lista com todos os anos disponíveis no DataFrame.
    years_list: list[int] = []
    
    for row in rows:
        row_year: int = row[0]

        if not row_year in years_list:
            years_list.append(row[0])
    
    # Verificamos se o ano escolhido pelo usuário é valido.
    # Caso não esteja na lista `years_list`, retornará o ano mais próximo.
    year: int = closest_value(years_list, value)

    # Filtramos o DataFrame para o ano escolhido.
    new_df = filter_values(population_df, "year", year)

    # Atualizamos o parâmetro `ano` para as configurações do gráfico.
    title_text = f"Percentual populacional por continente de {year}"
    config["title"]["text"] = title_text

    # Retornamos o gráfico com os novos valores.
    return population.create_chart(new_df)


if __name__ == "__main__":
    app.run_server(debug=True) # type: ignore
