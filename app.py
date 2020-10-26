from dash.react import dash

my_app = dash('my app')

from dash_components import h1, PlotlyGraph

my_app.layout = h1("testing the app")

my_app.server.run(debug=True)