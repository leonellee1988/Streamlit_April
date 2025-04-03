# Carga de paquetes:
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar la información del Dataframe:
df = pd.read_excel('final_champions_league.xlsx')

# Crear un Dataframe con columnas modificadas:
df_1 = df.copy()
df_1 = df_1.rename(columns = {
    'season':'Season',
    'winner-country':'Winner Country',
    'winner':'Winner',
    'score-winner':'Score Winner',
    'score-runner-up':'Score Runner Up',
    'runner-up':'Runner Up',
    'runner-up-country':'Runner Up Country',
    'stadium':'Stadium',
    'final-city':'Final City',
    'final-country':'Final Country',
    'attendance':'Attendance',
    'normal-time':'Regular Time',
    'extra-time':'Extra Time',
    'penalty':'Penaties'
})

# Función para calcular las estadísticas
def create_statistics_table(df):
    df['total-score'] = df['score-winner'] + df['score-runner-up']
    stats = {
        'Metric': ['Total', 'Average', 'Min', 'Max', 'Var', 'Std'],
        'Goals': [
            round(df['total-score'].sum(),2),
            round(df['total-score'].mean(),2),   
            round(df['total-score'].min(),2),    
            round(df['total-score'].max(),2),
            round(df['total-score'].var(),2),    
            round(df['total-score'].std(),2)    
        ],
        'Attendance': [
            round(df['attendance'].sum(),2),
            round(df['attendance'].mean(),2),    
            round(df['attendance'].min(),2),     
            round(df['attendance'].max(),2),
            round(df['attendance'].var(),2),     
            round(df['attendance'].std(),2)
        ]
    }
    stats_df = pd.DataFrame(stats)
    st.dataframe(stats_df)

# Función para crear gráficos:
def create_bar_chart(data, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette("viridis", len(data))
    data.plot(kind='bar', ax=ax, color=colors, edgecolor='black')
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

def create_ring_chart(df):
    resolved_data = df[['normal-time', 'extra-time', 'penalty']].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette("viridis", len(resolved_data))
    wedges, texts, autotexts = ax.pie(
        resolved_data,
        labels=['Regular Time', 'Extra Time', 'Penalties'],
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'linestyle': 'solid'},
        pctdistance=0.85
    )
    centre_circle = plt.Circle((0, 0), 0.60, color='white', fc='white', linewidth=1)
    ax.add_artist(centre_circle)
    for w in wedges:
        w.set_edgecolor('white')
    st.pyplot(fig)

# Función principal Streamlit:
def main():

    # Logo UEFA Champions League:
    st.image(r'C:\Users\Usuario\Desktop\ciencia_de_datos\streamlit\champions-league.svg', width=150)

    # Encabezado de la App:
    st.title('UEFA Champions League')
    st.header('Final statistics in the UEFA Champions League')
    st.subheader('Summary table: from 1955 to 2023 season')

    # Mostrar el dataframe en Streamlit:
    st.dataframe(df_1)

    #Mostrar el dataframe de estadísticas básicas en Streamlit:
    st.subheader('Basic descriptive statistics')
    create_statistics_table(df)

    # Conteo de triunfos en finales por equipo o club:
    top_teams = df['winner'].value_counts().head(10)
    st.subheader('Top 10: UEFA Champions League champion clubs')
    create_bar_chart(top_teams, 'Club', 'Cups')

    # Conteo de triunfos en finales por país:
    top_countries = df['winner-country'].value_counts().head(5)
    st.subheader('Top 5: UEFA Champions League champion countries')
    create_pie_chart(top_countries)

    # Distribución de finales por medio de resolución (tiempo regular, tiempo extra o penales):
    st.subheader('Distribution of finals by type of resolution')
    create_ring_chart(df)

main()