import streamlit as st
import pandas as pd

df = pd.read_csv('ucl-finals.csv')

def main():
    st.title('Finales de Champions League')
    st.header('Dataframe')
    st.dataframe(df)

main()