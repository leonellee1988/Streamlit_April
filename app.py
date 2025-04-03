import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://es.uefa.com/uefachampionsleague/history/winners/finals/'
response = requests.get(url)
table = BeautifulSoup.find('table')

def main():
    st.title('Finales de Champions League')
    st.header('Dataframe')
    st.dataframe(table)

main()