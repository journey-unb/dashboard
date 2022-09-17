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

from typing import Any

import plotly.express as px # type: ignore
from plotly.graph_objects import Figure # type: ignore
from pandas import DataFrame

from data_migrator import df
from utils import filter_values


# Aqui definimos as configurações de layout do gráfico.
current_year: int = 2000
config = {"title": {"text": f"População Urbana ({current_year})", "x": 0.5}}
labels = {
    "year": "Ano",
    "region": "Região",
    "urban_population": "População Urbana",
}


def create_chart(
    df: DataFrame,
    labels: dict[str, str] = labels,
    config: dict[str, Any] = config,
) -> Figure:
    chart = px.bar( # type: ignore
        df,
        x="region",
        y="urban_population",
        color="region",
        labels=labels,
    )

    chart.update_layout(config) # type: ignore
    chart.update_yaxes(range=[9_000_000, 2_400_000_000]) # type: ignore
    return chart


# Aqui criamos o gráfico utilizando a função `create_chart`.
filtered_df = filter_values(df, "year", current_year)
chart = create_chart(filtered_df)
