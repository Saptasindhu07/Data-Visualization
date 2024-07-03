import dash
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
from dash import html
from dash import dcc

data = pd.read_csv('./DATASETS/gapminder.csv')

app = dash.Dash()

app.layout = html.Div([
    html.Div(children=[
        html.H1(children='MY FIRST DASHBOARD')
    ], style={'border': '2px solid red', 'float': 'left', 'width': '99%', 'height': '50px', 'text-align': 'center', 'justify-content': 'center'}),
    html.Div(children=[
        dcc.Graph(id='scatter-plot',
                  figure={'data': [go.Scatter(x=data['pop'], y=data['gdpPercap'], mode='markers')]}
                  )
    ], style={'border': '2px solid red', 'float': 'left', 'width': '49.5%', 'height': '350px'}),
    html.Div(children=[
        dcc.Graph(id='box-plot',
                  figure=go.Box(x=data['gdpPercap']))
    ], style={'border': '2px solid black', 'float': 'left', 'width': '49.5%', 'height': '350px'}),
])

if __name__ == '__main__':
    app.run_server()
