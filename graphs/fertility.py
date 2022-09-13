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

from collections import defaultdict
from typing import DefaultDict

import plotly.express as px # type: ignore
from pandas import DataFrame

from data_migrator import df
from utils import filter_columns, filter_fertility

# Aqui definimos as configurações de layout do gráfico.
config = {"title": {"text": "Taxa de Fertilidade (1955-2020)", "x": 0.5}}
labels = {
    "year": "Ano",
    "fertility_rate": "Taxa de Fertilidade",
    "region": "Região",
}

# A criação do gráfico utiliza o modo "linear" do Plotly.
# Alguns itens básicos foram alterados, como a representação
# das "etiquetas" de ano, imigrantes e região.
filtered_df = filter_columns(df, "year", "region", "fertility_rate")
filter_fertility(filtered_df)

rows = filtered_df.values.tolist() # type: ignore
average: DefaultDict[str, int] = defaultdict(int)

for row in rows:
    # `row[0]` é garantidamente um ano e `row[2]` é garantidamente a
    # taxa de fertilidade. `average` é um dicionário; então estamos
    # fazendo basicamente, por exemplo: `row[2020] += 5.50`
    average[row[0]] += row[2]

# Agora adicionamos os itens da média no dicionário.
# Dividimos o `value` por 6 para obter a média aritmética, já que
# existem 6 regiões.
for key, value in average.items():
    rows.append([key, "all", value / 6])

changed_df = DataFrame(rows, columns=list(filtered_df.columns))
chart = px.line( # type: ignore
    changed_df,
    x="year",
    y="fertility_rate",
    color="region",
    labels=labels,
    markers=True,
)

chart.update_layout(config) # type: ignore
