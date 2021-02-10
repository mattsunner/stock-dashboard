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


# Layout
app.layout = html.Div(children=[
    html.H1(children='Stock Dashboard'),

    html.Div(children='''
        A Plotly Dash powered dashboard to view daily stock data.
    '''),

    html.Div(["Stock Ticker Input: ",
              dcc.Input(id='stock-text-box', value='AAPL', type='text')]),

    html.Div(["Moving Average Days: ",
              dcc.Input(id='ma-days-box', value=30, type='number')]),

    html.Div([
        "Start Date Selection: ",
        dcc.DatePickerSingle(
            id='start-date-picker',
            date='2020-01-01',
            display_format='MMM Do, YY'
        )
    ]),

    html.Div([
        "End Date Selection: ",
        dcc.DatePickerSingle(
            id='end-date-picker',
            date='2021-01-01',
            display_format='MMM Do, YY'
        )
    ]),

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
    Input(component_id='stock-text-box', component_property='value'),
    Input(component_id='start-date-picker', component_property='date'),
    Input(component_id='end-date-picker', component_property='date'),
)
def update_figure1(selected_ticker, start_date_pick, end_date_pick):
    fig = stock_price_dod(selected_ticker, start_date_pick, end_date_pick)

    return fig


@app.callback(
    Output(component_id='candle-plot', component_property='figure'),
    Input(component_id='stock-text-box', component_property='value'),
    Input(component_id='start-date-picker', component_property='date'),
    Input(component_id='end-date-picker', component_property='date'),
)
def update_figure2(selected_ticker, start_date_pick, end_date_pick):
    fig = stock_price_candle(selected_ticker, start_date_pick, end_date_pick)

    return fig


@app.callback(
    Output(component_id='moving-avg', component_property='figure'),
    Input(component_id='stock-text-box', component_property='value'),
    Input(component_id='ma-days-box', component_property='value'),
    Input(component_id='start-date-picker', component_property='date'),
    Input(component_id='end-date-picker', component_property='date'),
)
def update_figure3(selected_ticker, ma_days, start_date_pick, end_date_pick):
    fig = stock_price_ma(selected_ticker, ma_days,
                         start_date_pick, end_date_pick)

    return fig


@app.callback(
    Output(component_id='matrix-view', component_property='figure'),
    Input(component_id='stock-text-box', component_property='value'),
    Input(component_id='start-date-picker', component_property='date'),
    Input(component_id='end-date-picker', component_property='date'),
)
def update_figure4(selected_ticker, start_date_pick, end_date_pick):
    fig = stock_price_matrix(selected_ticker, start_date_pick, end_date_pick)

    return fig


# App Server
if __name__ == '__main__':
    app.run_server(debug=True)
