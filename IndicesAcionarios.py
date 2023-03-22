import streamlit as st
import yfinance as yf
import pandas as pd
import sgs

st.title('Dados Abertos')

st.subheader('Criado por André Luiz Greboge, com base em dados abertos da CVM. Se conecte comigo em meu LinkedIn: ')

indices = ('^FTSE','^GSPC','^DJI','^IXIC','^GDAXI','^N225','','')

dropdown = st.multiselect("Escolha seu índice", indices)

start= st.date_input('Start', value = pd.to_datetime('2022-01-01'))
end= st.date_input('End', value = pd.to_datetime('today'))

if len(dropdown) > 0:
    df = yf.download(dropdown,start,end)['Adj Close']
    st.line_chart(df)