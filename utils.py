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

from pandas import DataFrame


def filter_columns(df: DataFrame, *filters: Any) -> DataFrame:
    """
    Esta função filtra as colunas do dataframe através dos parâmetros
    `filters`.
    """
    rows = df.values.tolist() # type: ignore
    columns: list[str] = list(df.columns)

    indexes: list[int] = []
    new_df: list[list[int]] = []

    for value in filters:
        indexes.append(columns.index(value))

    for row in rows:
        values: list[int] = []

        for index in indexes:
            values.append(row[index])

        new_df.append(values)

    return DataFrame(new_df, columns=filters) # type: ignore


def filter_values(df: DataFrame, column: str, *values: Any) -> DataFrame:
    """
    Esta função filtra as linhas do dataframe de acordo com os valores
    de uma coluna.
    """
    rows = df.values.tolist() # type: ignore
    columns: list[str] = list(df.columns)

    index = columns.index(column)
    new_df: list[list[int]] = []

    for row in rows:
        if row[index] in values:
            new_df.append(row)
  
    return DataFrame(new_df, columns=columns)

def filter_fertility(df: DataFrame):
    fertility_value = filter_columns(df, "fertility_rate", "region", "year").values.tolist()
    fertility_list_big = []
    fertility_list_small = []
    
    for value in fertility_value:
        if value[0] >= 2.2:
            fertility_list_big.append(value)
        else:
            fertility_list_small.append(value)
    #print(fertility_list_small)
def closest_value(values: list[int], number: int) -> int:
  aux: list[int] = []

  for value in values:
    aux.append(abs(number - value))
    
  return values[aux.index(min(aux))]

def get_specific_continent(df: DataFrame, *continents: Any) -> DataFrame:
    """
    Esta função filtra as linhas do dataframe e retorna apenas os valores
    específicos do continente escolhido. O diferencial é a utilização do
    filtro de forma única através da sua posição na lista.
    """
    rows = df.values.tolist() # type: ignore
    columns: list[str] = list(df.columns)

    new_df: list[list[str | int]] = []

    for row in rows:
        if row[1] in continents:
            new_df.append(row)
    
    return DataFrame(new_df, columns=columns)
