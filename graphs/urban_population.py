import plotly.express as px
from functions import *
from data_migrator import df

# Aqui definimos as configurações de layout do gráfico.
config = {"title": {"text": "População Urbana (1955 - 2020)"}}
labels = {"urban_population": "População Urbana", "region": "Região", "year": "Ano", "urban_population_percentage": "% de população urbana"}
hover_data = ["urban_population_percentage", "urban_population"]

# `animation_frame`: critério para animação.
# `animatiou_group`: o que vai ser animado.
# `hover_data`: informações que vão aparecer ao passar o mouse em cima das barras.
filtered_df = filter_columns(df, "urban_population", "urban_population_percentage", "year", "region")
fig = px.bar(filtered_df, x="region", y="urban_population", color="region", animation_frame="year", animation_group="region", hover_data=hover_data, labels=labels)

fig.update_layout(config)
