from collections import defaultdict

import plotly.express as px
from functions import *
from data_migrator import df

# Aqui definimos as configurações de layout do gráfico.
config = {"title": {"text": "Taxa de Fertilidade (1955 - 2020)"}}
labels = {"year": "Ano", "fertility_rate": "Taxa de Fertilidade", "region": "Região"}

# A criação do gráfico utiliza o modo "linear" do Plotly.
# Alguns itens básicos foram alterados, como a representação
# das "etiquetas" de ano, imigrantes e região.
filtered_df = filter_columns(df, "year", "region", "fertility_rate")

rows = filtered_df.values.tolist()
average = defaultdict(int)

for row in rows:
    # `row[0]` é garantidamente um ano, e `row[2]` é garantidamente a taxa de fertilidade.
    # `average` é um dicionário; então estamos fazendo basicamente, por exemplo:
    # `row[2020] += 5.50`
    average[row[0]] += row[2]

# Agora adicionamos os itens da média no dicionário.
# Dividimos o `value` por 6 para obter a média aritmética, já que existem 6 regiões.
for key, value in average.items():
    rows.append([key, "all", value / 6])

changed_df = DataFrame(rows, columns=list(filtered_df.columns))
fig = px.line(changed_df, x="year", y="fertility_rate", color="region", line_shape="spline", labels=labels, markers=True)

# Aqui adicionamos as funções de selecionar o intervalo
# de tempo através de botões e um "controle deslizante".
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=[
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=5, label="5y", step="year", stepmode="backward"),
                dict(count=10, label="10y", step="year", stepmode="backward"),
                dict(count=20, label="20y", step="year", stepmode="backward"),
                dict(count=50, label = "50y", step = "year", stepmode = "backward"),
                dict(step="all"),
            ],
        ),
        rangeslider=dict(visible=True),
        type="date",
    )
)

fig.update_layout(config)
fig.show()