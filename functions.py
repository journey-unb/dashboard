import pandas
from pandas import DataFrame

def filter_columns(df, *filters):
    """
    Essa função filtra as colunas do dataframe através do parâmetro `filters`.
    """
    rows = df.values.tolist()
    columns = list(df.columns)

    indexes = []
    new_df = []

    for filter in filters:
        indexes.append(columns.index(filter))

    for row in rows:
        values = []

        for index in indexes:
            values.append(row[index])

        new_df.append(values)

    return DataFrame(new_df, columns=filters)

def filter_values(df, column, *values):
    """
    Essa função filtra as linhas do dataframe através dos parâmetros `column` e `values`.
    """
    rows = df.values.tolist()
    columns = list(df.columns)

    index = columns.index(column)
    new_df = []

    for row in rows:
        if row[index] in values:
            new_df.append(row)
  
    return DataFrame(new_df, columns=columns)