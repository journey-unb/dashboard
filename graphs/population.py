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

from data_migrator import df
from utils import filter_columns, filter_values


# Aqui definimos as configurações de layout do gráfico.
labels = {"population": "População", "region": "Região", "year": "Ano"}

filtered_df = filter_columns(df, "year", "region", "population")
valid_years: list[str | int] = []

# Aqui inserimos, de maneira provisória, um sistema para escolha
# dos anos a ser mostrado. Na próxima etapa do trabalho, utilizaremos
# a função "Range Slider" do Dash.
for year in input("Insira o ano desejado:").split():
  if year.isnumeric():
    valid_years.append(int(year))

# Caso não insira um ano válido, será mostrado a população de todos os anos.
# Caso contrário, utilizaremos o filtro de valores para mostrar os dados
# do ano específico.
if not valid_years:
  filtered_year = filtered_df
  valid_years.append("todos os anos")
else:
  filtered_year = filter_values(filtered_df, "year", *valid_years)

chart = px.pie( # type: ignore
  filtered_year,
  values="population",
  names="region",
  labels=labels,
)

# TODO: Utilizar títulos dinâmicos e seguir a PEP-8.
chart.update_layout(title_text=f'Percentual populacional por continente de {", ".join([str(year) for year in valid_years])}', title_x=0.5) # type: ignore
