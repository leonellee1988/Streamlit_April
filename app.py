import streamlit as st
import pandas as pd

df = pd.read_excel('final_champions_league.xlsx')

def main():
    st.title('UEFA Champions League')
    st.header('Histórico de finales Champions League')
    st.subheader('Temporadas: de 1955 a 2023')
    st.dataframe(df)

main()