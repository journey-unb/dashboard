import plotly.express as px
from functions import *
from data_migrator import df

# Aqui definimos as configurações de layout do gráfico.
config = {"title": {"text": "Média de Idades (1955-2020)"}}
labels = {"median_age": "Média das idades", "region": "Região", "year": "Ano"}

# `facet_col`: informação que vai aparecer em cada coluna.
# `facet_col_wrap`: quantas colunas vão aparecer por linha.
filtered_df = filter_columns(df, "year", "region", "median_age")
fig = px.area(filtered_df, facet_col="region", facet_col_wrap=3, x="year", y="median_age", color="region", labels=labels, markers=True)

fig.update_layout(config)
