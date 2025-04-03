import streamlit as st
import pandas as pd

df = pd.read_excel('final_champions_league.xlsx')

def main():
    st.title('Finales de Champions League')
    st.header('Dataframe')
    st.dataframe(df)

main()