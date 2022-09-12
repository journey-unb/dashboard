from dash import Dash, dcc, html

# Aqui atualizamos a database
import data_migrator

# Aqui importamos os gráficos
from graphs.average import average_graph
from graphs.fertility import fertility_graph
from graphs.migration import migration_graph
from graphs.population import population_graph
from graphs.urban_population import urban_population_graph

app = Dash(__name__)

app.layout = html.Div([
    html.H1('População em nível continental'),
    html.Div([
        html.H2('Taxa de Migração'),
        dcc.Graph(
        id='migration-graph',
        figure = migration_graph
    )
    ])
])

app.run_server(debug=True)