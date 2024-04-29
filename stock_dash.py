from dash import Dash, dcc, callback, Input, Output
import plotly.express as px
import dash_design_kit as ddk
import plotly.graph_obs as go

df = px.data.stocks()

app = Dash(__name__)

app.layout = ddk.App([
    ddk.Header('Weekly Analytics'),

    ddk.Card([
        ddk.Graph(figure=go.Figure(data=go.Surface(z=df.values))),
        width=100
    ], )


    ddk.Card(
        ddk.Graph(figure=go.Figure(data=go.Surface(z=df.values))),
        width=50),

    ddk.Card(
        ddk.DataTable(data=df.round(2).round(2).to_dict('r'))
    )
    
])


@callback(
    Output('graph-1', 'figure'),
    Input('dropdown', 'value'))
def update(stock_ticker):
    return px.scatter(
        df, y=stock_ticker,
        trendline='rolling',
        trendline_options=dict(window=5),
    )
)

app.run(debug=True)