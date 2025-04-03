# Carga de paquetes:
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar la información del Dataframe:
df = pd.read_excel('final_champions_league.xlsx')

# Función para crear gráficos:
def create_bar_chart(data, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette("viridis", len(data))
    data.plot(kind='bar', ax=ax, color=colors)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)

def create_pie_chart(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette("viridis", len(data))
    labels = [f'{country} {pct:.1f}% ({count})' for country, pct, count in zip(
        data.index, 
        data.values / data.sum() * 100, 
        data.values
    )]
    ax.pie(
        data,
        labels=labels,
        colors=colors, 
        startangle=90, 
        wedgeprops={'edgecolor': 'black'},
        pctdistance=0.85,
        labeldistance=1.1
    )
    st.pyplot(fig)

# Función principal Streamlit:
def main():

    # Logo UEFA Champions League:
    st.image(r'C:\Users\Usuario\Desktop\ciencia_de_datos\streamlit\champions-league.svg', width=150)

    # Encabezado de la App:
    st.title('UEFA Champions League')
    st.header('Estadísticas finales Champions League')
    st.subheader('Tabla de resumen: temporada 1955 a 2023')

    # Mostrar el dataframe en Streamlit:
    st.dataframe(df)

    # Conteo de triunfos en finales por equipo o club:
    top_teams = df['winner'].value_counts().head(10)
    st.subheader('Top 10: clubes campeones UEFA Champions League')
    create_bar_chart(top_teams, 'Club', 'Copas')

    # Conteo de triunfos en finales por país:
    top_countries = df['winner-country'].value_counts().head(5)
    st.subheader('Top 5: países campeones UEFA Champions League')
    create_pie_chart(top_countries)

main()