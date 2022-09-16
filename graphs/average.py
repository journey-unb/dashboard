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


# Aqui definimos as configurações de layout do gráfico.
config = {"title": {"text": "Média de Idades (1955-2020)", "x": 0.5}}
labels = {"median_age": "Média das idades", "region": "Região", "year": "Ano"}

#Função responsável por fazer a filtragem por continentes. 
def retornar_lista(df):
    df_list = df.values.tolist()
    colunas = df.columns
    continente_escolhido = []

    for lista in df_list:
        if 'africa' == lista[1]: # O Botão será responsavel por mudar esse parametro, criando assim um novo gráfico ao escolher um continente diferente.
            continente_escolhido.append(lista)
    
    return DataFrame(columns = colunas, data = continente_escolhido)

filtered_df = filter_columns(df, "year", "region", "median_age")

df = retornar_lista(filtered_df)
chart = px.area(df, x="year", y="median_age", color="region", labels=labels, markers=True)

chart.update_layout(config)
