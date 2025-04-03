import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar la información del Dataframe:
df = pd.read_excel('final_champions_league.xlsx')

def main():

    # Encabezado de la App:
    st.title('UEFA Champions League')
    st.header('Histórico de finales Champions League')
    st.subheader('Temporadas: de 1955 a 2023')
    st.dataframe(df)
    
    # Top 10 equipos más ganadores en Champions:
    top_teams = df['winner'].value_counts().head(10)

    # Gráfica s/Top 10 equipos más ganadores en Champions:
    sns.set(style="whitegrid")
    colors = sns.color_palette("viridis", len(top_teams))
    fig, ax = plt.subplots(figsize=(10, 6))
    top_teams.plot(kind='bar', ax=ax, color=colors)
    ax.set_title('Top 10 Equipos más Ganadores de la UEFA Champions League', fontsize=16, fontweight='bold')
    ax.set_xlabel('Equipo', fontsize=12)
    ax.set_ylabel('Copas', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)

main()