from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: Another example graph with different data
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 1, 1], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 1, 1], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

