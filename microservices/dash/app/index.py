from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
from apps import app1, home

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

# application route goes here
def display_page(pathname):
    if pathname == '/':
         return home.layout
    elif pathname == '/app1':
         return app1.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(host="0.0.0.0",debug=True)
