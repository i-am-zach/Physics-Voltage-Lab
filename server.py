import dash
import dash_core_components as dcc
import dash_html_components as html

from utils import generate_formatted_dataframe, scatter_plot, generate_numpy, surface_plot

external_stylesheets = ['https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(className="content container", children=[
    html.H1(children="Group 1: Zach Lefkovitz, Aidan Morrison, Nathan Oleari, Nick Larson"),
    html.Div(className="columns", children=[
        html.Div(className="column", children=[
            dcc.Graph(id="group-1-surf", figure=surface_plot(*generate_numpy("group_1.csv"))),
        ]),
        html.Div(className="column", children=[
            dcc.Graph(id="group-1-scat", figure=scatter_plot(generate_formatted_dataframe("group_1.csv"))),
        ])
    ]),

    html.H1(children="Group 2: Meghan Stancliff, Adam Jankelowitz, Nick Larson, Michelle Chen, Zach Lefkovitz"),
    html.Div(className="columns", children=[
        html.Div(className="column", children=[
            dcc.Graph(id="group-2-surf", figure=surface_plot(*generate_numpy("group_2.csv"))),
        ]),
        html.Div(className="column", children=[
            dcc.Graph(id="group-2-scat", figure=scatter_plot(generate_formatted_dataframe("group_2.csv"))),
        ])
    ]),

    html.H1(children="Group 3: Ari Wainer, Javi Espanosa, Nathan Oleari, Daniel Malis"),
    html.Div(className="columns", children=[
        html.Div(className="column", children=[
            dcc.Graph(id="group-3-surf", figure=surface_plot(*generate_numpy("group_3.csv"))),
        ]),
        html.Div(className="column", children=[
            dcc.Graph(id="group-3-scat", figure=scatter_plot(generate_formatted_dataframe("group_3.csv"))),
        ])
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)