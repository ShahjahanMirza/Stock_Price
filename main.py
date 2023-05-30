
import yfinance as yf
import streamlit as st
import datetime
import numpy as np

st.write("""
         # Stock Prices :-
            Shown are the stock closing price and volume!
         """)

symbols = [
'NVDA	(NVIDIA Corporation)',
'AI	(C3.ai, Inc.)',
'PLTR	(Palantir Technologies Inc.)',
'TSLA	(Tesla, Inc.)',
'AAPL	(Apple Inc.)',
'CHPT	(ChargePoint Holdings, Inc.)',
'AVGO	(Broadcom Inc.)',
'AMD	(Advanced Micro Devices, Inc.)',
'UPST	(Upstart Holdings, Inc.)',
'NIO	(NIO Inc.)',
'F	(Ford Motor Company)',
'NFLX	(Netflix, Inc.)',
'SNOW	(Snowflake Inc.)',
'GME	(GameStop Corp.)',
'SPY	(SPDR S&P 500 ETF Trust)',
'CVNA	(Carvana Co.)',
'QQQ	(Invesco QQQ Trust)',
'DNA	(Ginkgo Bioworks Holdings, Inc.)',
'RIOT	(Riot Platforms, Inc.)',
'SOFI	(SoFi Technologies, Inc.)',
'VALE	(Vale S.A.)',
'TGT	(Target Corporation)',
'IXIC	(NASDAQ Composite)',
'GEVO	(Gevo, Inc.)',
'COIN	(Coinbase Global, Inc.)',
'WLDS	(Wearable Devices Ltd.)',
'ETRN	(Equitrans Midstream Corporation)',
'PYPL	(PayPal Holdings, Inc.)',
'META	(Meta Platforms, Inc.)',
'SOXL (Direxion Daily Semiconductor Bull 3X Shares)',
'GOOGL (Google)']

tickerSymbol = st.selectbox("Select Symbol: ",symbols)
tickerSymbol = (tickerSymbol.split('(')[0]).strip()

tickerData = yf.Ticker(tickerSymbol)

col1, col2 = st.columns([1, 2])
star = col1.date_input("From: ",datetime.date(2015, 1,1))
en = col2.date_input("Till: ", datetime.datetime.now())

time_period = ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo']

period = st.selectbox("Choose Time Period: ",time_period)

tickerDf = tickerData.history(period = period, start=star, end=en)

st.write("""
         ## CLOSING :""")
st.line_chart(tickerDf.Close)
st.write("""
         ## VOLUME :""")
st.line_chart(tickerDf.Volume) 
