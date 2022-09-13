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

from graphs import migration, population, fertility, average


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
        )
    ]),

    # Média de Idades
    html.Div(children=[ # type: ignore
        dcc.Graph(
            id="average-age", # type: ignore
            figure=average.chart # type: ignore
        )
    ]),
])


if __name__ == "__main__":
    app.run_server(debug=True) # type: ignore
