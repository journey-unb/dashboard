import plotly.express as px
from functions import *
from data_migrator import df

# Aqui definimos as configurações de layout do gráfico.
labels = {"population": "População", "region": "Região", "year": "Ano"}

filtered_df = filter_columns(df, "year", "region", "population")
valid_years = []

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

fig = px.pie(filtered_year, values="population", names="region", labels=labels)
fig.update_layout(title_text=f'Percentual populacional por continente de {", ".join([str(year) for year in valid_years])}', title_x=0.5)
fig.show()