import dash
from dash import dcc, html  # Import directly from the main Dash package
import plotly
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div(children = [
    html.H2(children = 'Helllo Dash!'),

    dcc.Graph(
        figure = go.Figure([
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[100, 280, 350],
                name = 'lokalnie'
            ),
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[140, 200, 390],
                name = 'online'
            )
        ])
    )
])

if __name__ == "__main__":  # jesli bezpośrednio uruchomimy nasz skrypt to uruchomimy aplikacje run server
    app.run_server(debug=True)  