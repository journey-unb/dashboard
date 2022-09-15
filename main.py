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

from dash import Dash, dcc, html, ctx # type: ignore
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
        ),
        dcc.RangeSlider(
            id="migration-range-slider",
            step=1,
            min = 1955,
            max = 2020,
            value=[1955, 2020],
            pushable=1,
            marks=None,
            tooltip={"placement": "bottom", "always_visible": True}
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
        ),
        html.Button('Voltar', id='backward', n_clicks=0), # type: ignore
        html.Button('Avançar', id='forward', n_clicks=0) # type: ignore
    ]),
])

@app.callback(
    Output(component_id="urban-population", component_property="figure"), 
    Input(component_id="forward", component_property="n_clicks"),
    Input(component_id="backward", component_property="n_clicks")
)

def update_urban_population(first_button, second_button): # type: ignore
    # Definimos os valores para os botões `forward` e `backward`.
    button_values: dict[str, int] = {
        "forward": 5,
        "backward": -5
    }

    # Aqui verificamos se o callback retorna valores diferentes de `None`
    # e realizamos a ação apenas caso esta esteja no intervalo entre `1955` e `2020`.
    if ctx.triggered_id and 1955 <= urban_population.current_year + button_values[ctx.triggered_id] <= 2020:
       urban_population.current_year += button_values[ctx.triggered_id]

    # Atualizamos o título para o gráfico e filtramos o valor para o ano desejado.
    urban_population.config["title"]["text"] = f"População Urbana ({urban_population.current_year})"
    new_df = filter_values(urban_population.filtered_columns, "year", urban_population.current_year)
    
    # Criamos e retornamos o gráfico com os novos falores.
    chart = urban_population.create_chart(new_df, urban_population.labels, urban_population.config) # type: ignore
    return chart

@app.callback(
    Output(component_id="migration-rate", component_property="figure"),
    Input(component_id="migration-range-slider", component_property="value")
)

def update_migration_rate(input_value: list[int]): # type: ignore
    # Filtramos o DataFrame com os valores do intervalo escolhido.
    new_df = filter_values(df, "year", *list(range(*input_value)))

    # Criamos e retornamos o gráfico com os novos valores.
    chart = migration.create_chart(new_df, migration.labels, migration.config) # type: ignore
    return chart

if __name__ == "__main__":
    app.run_server(debug=True) # type: ignore
