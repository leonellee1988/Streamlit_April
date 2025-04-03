import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('final_champions_league.xlsx')

def main():
    st.title('UEFA Champions League')
    st.header('Histórico de finales Champions League')
    st.subheader('Temporadas: de 1955 a 2023')
    st.dataframe(df)

    top_teams = df['winner'].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    top_teams.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title('Top 10 Equipos más Ganadores de la UEFA Champions League', fontsize=16)
    ax.set_xlabel('Equipo', fontsize=12)
    ax.set_ylabel('Número de Victorias', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)

main()