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

import plotly.express as px # type: ignore
from pandas import DataFrame

from data_migrator import df
from utils import filter_columns

def create_chart(df: DataFrame, labels: dict, config: dict = {}): # type: ignore
    hover_data = ["urban_population_percentage", "urban_population"]
    chart = px.bar( # type: ignore
        df,
        x="region",
        y="urban_population",
        color="region",
        animation_frame="year",
        animation_group="region",
        hover_data=hover_data,
        labels=labels,
    )

    chart.update_layout(config)
    return chart

# Aqui definimos as configurações de layout do gráfico.
config = {"title": {"text": "População Urbana (1955-2020)", "x": 0.5}}
labels = {
    "urban_population": "População Urbana",
    "region": "Região",
    "year": "Ano",
    "urban_population_percentage": "% de população urbana",
}

# `animation_frame`: critério para animação.
# `animatiou_group`: o que vai ser animado.
# `hover_data`: informações que vão aparecer ao passar o mouse em cima 
# das barras.
filtered_df = filter_columns(
    df,
    "urban_population",
    "urban_population_percentage",
    "year",
    "region",
)

# Aqui criamos o gráfico utilizando a função `create_chart`
chart = create_chart(filtered_df, labels, config)
