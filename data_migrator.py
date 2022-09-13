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

import os
import sqlite3
from typing import List

import pandas


def format_number(value: str) -> int:
    return int(value.replace(",", ""))


def format_percentage(value: str) -> float:
    return float(value[:-1])


def initialize_database() -> None:
    """
    Esta função executa a criação e migração dos dados para o banco de
    dados. Ela deve ser executada apenas uma vez.
    """
    columns = [
        "year",
        "population",
        "yearly_change_percentage",
        "yearly_change",
        "net_migrants",
        "median_age",
        "fertility_rate",
        "population_density",
        "urban_population_percentage",
        "urban_population",
        "relative_population_percentage",
        "relative_population",
        "rank",
        "region",
    ]

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    encoding = "unicode_escape"

    # Fazer formatação de strings dentro de uma query SQL é uma má
    # prática pois é inseguro (permite SQL Injection). Como neste caso
    # é um projeto acadêmico simples e vai ser executado em um ambiente
    # controlado, não há problemas. Para mais informações, veja:
    # <https://en.wikipedia.org/wiki/SQL_injection>
    cursor.execute(f"CREATE TABLE IF NOT EXISTS data ({', '.join(columns)})")    

    for file in os.listdir("data/"):
        filename, ext = os.path.splitext(file)

        if ext != ".csv":
            continue

        path = f"data/{file}"
        csv_df = pandas.read_csv(path, encoding=encoding) # type: ignore

        rows: List[List[int | float]] = []

        for row in csv_df.values.tolist(): # type: ignore
            # Alguns valores precisam ser tratados antes de serem inseridos
            # no banco de dados.
            row[1] = format_number(row[1])
            row[2] = format_percentage(row[2])
            row[3] = format_number(row[3])
            row[4] = format_number(row[4])
            row[8] = format_percentage(row[8])
            row[9] = format_number(row[9])
            row[10] = format_percentage(row[10])
            row[11] = format_number(row[11])

            row.append(filename)
            rows.append(row)

        # Aqui também há SQL Injection, mas pelo mesmo motivo que anterior,
        # não haverá problemas aqui.
        sql = f"INSERT INTO data VALUES ({', '.join(['?'] * len(columns))})"

        cursor.executemany(sql, rows)
        conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    initialize_database()
else:
    # Caso o módulo seja importado, o banco de dados já deve ter sido
    # inicializado. Então, basta carregar os dados para um `DataFrame`.
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    sql = "SELECT * FROM data"
    df = pandas.read_sql(sql, conn) # type: ignore

    cursor.close()
    conn.close()
