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
