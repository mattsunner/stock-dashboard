"""
Dash (Plotly) Stock Price Dashboard 

Author: Matthew Sunner, 2021
"""

import dash
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

    dcc.Graph(
        id='basic-plot',
        figure=fig1
    ),

    dcc.Graph(
        id='candle-plot',
        figure=fig2
    ),

    dcc.Graph(
        id='moving-avg',
        figure=fig3
    ),

    dcc.Graph(
        id='matrix-view',
        figure=fig4
    ),
])

# App Server
if __name__ == '__main__':
    app.run_server(debug=True)
