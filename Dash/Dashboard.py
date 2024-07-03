import dash
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
from dash import html
from dash import dcc

data = pd.read_csv('./DATASETS/gapminder.csv')

app = dash.Dash()

app.layout = html.Div([
    html.Div(style={'border': '2px solid red'}),
    html.Div(style={'border': '2px solid red'}),
    html.Div(style={'border': '2px solid red'})
])

if __name__ == '__main__':
    app.run_server()
