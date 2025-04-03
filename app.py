# Carga de paquetes:
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

    # Mostrar el dataframe en Streamlit:
    st.dataframe(df)
    
    # Conteo de triunfos en finales por equipo o club:
    top_teams = df['winner'].value_counts().head(10)

    # Gráfica s/Top 10 equipos más ganadores en Champions:
    # Elegir estilo y paleta de colores Seaborn:
    sns.set(style="whitegrid")                                                      
    colors = sns.color_palette("viridis", len(top_teams))                           
    fig, ax = plt.subplots(figsize=(10, 6))                                         
    # Crear gráfico de barras:
    top_teams.plot(kind='bar', ax=ax, color=colors)
    ax.set_title('Top 10: Campeones de UEFA Champions League', fontsize=16, fontweight='bold')
    # Configuración de titulos y etiquetas:
    ax.set_xlabel('Equipo', fontsize=12)
    ax.set_ylabel('Copas', fontsize=12)
    # Rotación de las etiquetas del eje X:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    # Mostrar el gráfico en Streamlit:
    st.pyplot(fig)

main()