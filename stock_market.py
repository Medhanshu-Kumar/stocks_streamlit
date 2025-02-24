import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Stock Market App!")
st.write('This is my hope of getting a hike!')

ticker_symbol='AAPL'

import datetime
start_date = st.date_input("Please enter Starting Date",
                           datetime.date(2019,1,1))
end_date = st.date_input("Please enter Ending Date",datetime.date(2022,12,31))

ticker_symbol=st.text_input("Enter the stock ticker symbol")

ticker_data = yf.Ticker(ticker_symbol)

ticker_df=ticker_data.history(period='1d',start=f"{start_date}",
                              end=f"{end_date}")
st.dataframe(ticker_df)
st.line_chart(ticker_df.Close)

col1,col2 = st.columns(2)

with col1:
    st.write(
        """
            ## Daily Closing Price Chart
        """
    )
    st.line_chart(ticker_df.Close)

with col2:
    st.write(
        """
            ## Daily Volume Price Chart
        """
    )
    st.line_chart(ticker_df.Volume)
