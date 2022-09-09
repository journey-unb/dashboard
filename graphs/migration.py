import plotly.express as px
from functions import *
from data_migrator import df

# Aqui definimos as configurações de layout do gráfico.
config = {"title": {"text": "Taxa de Migração (1955 - 2020)"}}
labels = {"year": "Ano", "net_migrants": "Migrantes", "region": "Região"}

# A criação do gráfico utiliza o modo "linear" do Plotly.
# Alguns itens básicos foram alterados, como a representação
# das "etiquetas" de ano, imigrantes e região.
filtered_df = filter_columns(df, "year", "net_migrants", "region")
fig = px.line(filtered_df, x="year", y="net_migrants", color="region", line_shape="spline", labels=labels, markers=True)

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