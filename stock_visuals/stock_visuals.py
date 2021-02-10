"""
Stock Visuals

Set of functions to generate all visuals in the dashboard applications

Author: Matthew Sunner,  2021
"""

import pandas as pd
import numpy as np
import datapane as dp
import plotly.figure_factory as ff
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px
import pandas_datareader.data as web

import datetime


def stock_price_dod(ticker, start_date, end_date):
    """stock_price_dod: Day over day stock price for a given stock_ticker

    Args:
        ticker (str): String representation of ticker symbol
        start_date (datetime obj): Python Datetime start date
        end_date (datetime obj): Python Datetime end date

    Returns:
        Object: Plotly figure object
    """

    stock_object = web.DataReader(
        ticker, 'yahoo', start_date, end_date).reset_index()

    trace = go.Scatter(x=stock_object.Date, y=stock_object.Close, name=ticker)
    fig = go.Figure([trace])
    fig.update_layout(
        title={
            'text': f'{ticker} Stock Price',
            'x': 0.5,
            'xanchor': 'center'
        }
    )

    return fig


def stock_price_ma(ticker, avg_days, start_date, end_date):
    """stock_price_ma: Moving Average Value by Day

    Args:
        ticker (str): String stock ticker
        avg_days (int): Number of days to include in the average
        start_date (obj): Python Datetime start date
        end_date (datetime obj): Python Datetime end date

    Returns:
        Object: Plotly figure object
    """

    stock_object = web.DataReader(
        ticker, 'yahoo', start_date, end_date).reset_index()

    stock_object['MAvg'] = stock_object['Close'].rolling(
        window=avg_days).mean()

    trace_base = go.Scatter(x=stock_object.Date,
                            y=stock_object.Close, name=ticker)
    trace_ma = go.Scatter(
        x=stock_object.Date, y=stock_object['MAvg'], name=f'Moving Average - {avg_days} days')

    fig = go.Figure([trace_base, trace_ma])
    fig.update_layout(
        title={
            'text': f"{ticker} Stock Price with {avg_days} Day Moving Average",
            'x': 0.5,
            'xanchor': 'center'})

    return fig


def stock_price_candle(ticker, start_date, end_date):
    """stock_price_dod: Day over day stock price for a given stock_ticker

    Args:
        ticker (str): String representation of ticker symbol
        start_date (datetime obj): Python Datetime start date
        end_date (datetime obj): Python Datetime end date

    Returns:
        Object: Plotly figure object
    """

    stock_object = web.DataReader(
        ticker, 'yahoo', start_date, end_date).reset_index()

    fig = go.Figure(go.Candlestick(x=stock_object.Date, open=stock_object.Open,
                                   high=stock_object.High, low=stock_object.Low, close=stock_object.Close))
    fig.update_layout(
        title={
            'text': f"{ticker} Stock Price (Candle Stick)",
            'x': 0.5,
            'xanchor': 'center'})

    return fig


def stock_price_matrix(ticker, start_date, end_date):
    """stock_price_dod: Day over day stock price for a given stock_ticker

    Args:
        ticker (str): String representation of ticker symbol
        start_date (datetime obj): Python Datetime start date
        end_date (datetime obj): Python Datetime end date

    Returns:
        Object: Plotly figure object
    """

    stock_object = web.DataReader(
        ticker, 'yahoo', start_date, end_date).reset_index()

    stock_object = stock_object[['Open', 'Close', 'Volume']]

    stock_object["index"] = np.arange(len(stock_object))

    fig = go.Figure(ff.create_scatterplotmatrix(stock_object, diag='box', index='index', size=3,
                                                height=600, width=1150, colormap='RdBu',
                                                title={
                                                    'text': f"{ticker} Stock Price (Scatterplot Matrix)",
                                                    'x': 0.5,
                                                    'xanchor': 'center'}))
    return fig