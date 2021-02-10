"""
Dash (Plotly) Stock Price Dashboard 

Author: Matthew Sunner, 2021
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

import datetime

from stock_visuals import stock_price_dod, stock_price_ma, stock_price_candle, stock_price_matrix

app = dash.Dash(__name__)


# Stock Ticker Information
start_date = datetime.datetime(2020, 1, 1)
end_date = datetime.datetime.now()
ticker = 'AAPL'
ma_value = 30

# Figures
fig1 = stock_price_dod(ticker, start_date, end_date)
fig2 = stock_price_candle(ticker, start_date, end_date)
fig3 = stock_price_ma(ticker, ma_value, start_date, end_date)
fig4 = stock_price_matrix(ticker, start_date, end_date)

# Layout
app.layout = html.Div(children=[
    html.H1(children='Stock Dashboard'),

    html.Div(children='''
        A Plotly Dash powered dashboard to view daily stock data.
    '''),

    html.Div(["Stock Ticker Input: ",
              dcc.Input(id='stock-text-box', value='AAPL', type='text')]),

    dcc.Graph(
        id='basic-plot',
    ),

    dcc.Graph(
        id='candle-plot',
    ),

    dcc.Graph(
        id='moving-avg',
    ),

    dcc.Graph(
        id='matrix-view',
    ),
])

# Callbacks


@app.callback(
    Output(component_id='basic-plot', component_property='figure'),
    Input(component_id='stock-text-box', component_property='value')
)
def update_figure1(selected_ticker):
    fig = stock_price_dod(selected_ticker, start_date, end_date)

    return fig


@app.callback(
    Output(component_id='candle-plot', component_property='figure'),
    Input(component_id='stock-text-box', component_property='value')
)
def update_figure2(selected_ticker):
    fig = stock_price_candle(selected_ticker, start_date, end_date)

    return fig


@app.callback(
    Output(component_id='moving-avg', component_property='figure'),
    Input(component_id='stock-text-box', component_property='value')
)
def update_figure3(selected_ticker):
    fig = stock_price_ma(selected_ticker, ma_value, start_date, end_date)

    return fig


@app.callback(
    Output(component_id='matrix-view', component_property='figure'),
    Input(component_id='stock-text-box', component_property='value')
)
def update_figure4(selected_ticker):
    fig = stock_price_matrix(selected_ticker, start_date, end_date)

    return fig


# App Server
if __name__ == '__main__':
    app.run_server(debug=True)
