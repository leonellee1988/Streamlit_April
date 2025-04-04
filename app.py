# Cargar paquetes:
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar generalidades de la App:
st.set_page_config(page_title='Data Science Project 01', page_icon='lee_logo.png')

# Cargar la información del dataFrame:
df = pd.read_excel('final_champions_league.xlsx')

# Renombrar columnas:
df_1 = df.copy().rename(columns={
    'season': 'Season', 'winner-country': 'Winner Country', 'winner': 'Winner',
    'score-winner': 'Score Winner', 'score-runner-up': 'Score Runner Up',
    'runner-up': 'Runner Up', 'runner-up-country': 'Runner Up Country',
    'stadium': 'Stadium', 'final-city': 'Final City', 'final-country': 'Final Country',
    'attendance': 'Attendance', 'normal-time': 'Regular Time',
    'extra-time': 'Extra Time', 'penalty': 'Penalties'
})

# Funciones auxiliares:
def compute_stats(series):
    return [
        round(series.sum(), 2), round(series.mean(), 2),
        round(series.min(), 2), round(series.max(), 2),
        round(series.var(), 2), round(series.std(), 2)
    ]

def create_statistics_table(df):
    df['total-score'] = df['score-winner'] + df['score-runner-up']
    stats = {
        'Metric': ['Total', 'Average', 'Min', 'Max', 'Var', 'Std'],
        'Goals': compute_stats(df['total-score']),
        'Attendance': compute_stats(df['attendance'])
    }
    st.dataframe(pd.DataFrame(stats))

def create_goals_histogram(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    color = sns.color_palette("viridis")[0]
    sns.histplot(df['score-winner'] + df['score-runner-up'], bins=10, kde=True, color=color, ax=ax)
    ax.set_xlabel('Total Goals in Final', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    st.pyplot(fig)

def create_bar_chart(data, xlabel, ylabel, horizontal=False):
    data = data.sort_values(ascending=horizontal)
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette("viridis", len(data))
    kind = 'barh' if horizontal else 'bar'
    data.plot(kind=kind, ax=ax, color=colors, edgecolor='black')
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    st.pyplot(fig)

def create_pie_chart(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette("viridis", len(data))
    labels = [f'{country} {pct:.1f}% ({count})' for country, pct, count in zip(
        data.index, data / data.sum() * 100, data
    )]
    ax.pie(data, labels=labels, colors=colors, startangle=90,
           wedgeprops={'edgecolor': 'black'}, pctdistance=0.85, labeldistance=1.1)
    st.pyplot(fig)

def create_ring_chart(df):
    resolved = df[['normal-time', 'extra-time', 'penalty']].sum()
    labels = ['Regular Time', 'Extra Time', 'Penalties']
    percentages = (resolved / resolved.sum()) * 100
    label_text = [f'{lbl}\n{cnt} ({pct:.1f}%)' for lbl, cnt, pct in zip(labels, resolved, percentages)]
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette("viridis", len(resolved))
    wedges, _ = ax.pie(resolved, labels=label_text, colors=colors,
                       startangle=90, wedgeprops={'edgecolor': 'black'}, pctdistance=0.85)
    centre_circle = plt.Circle((0, 0), 0.60, facecolor='white', edgecolor='black', linewidth=1.5, zorder=10)
    ax.add_artist(centre_circle)
    st.pyplot(fig)

# Función principal:
def main():

    # Filtro en el sidebar:
    selected_country = st.sidebar.selectbox('Filter by Winner Country:', ['All countries'] + sorted(df['winner-country'].dropna().unique().tolist()))
    if selected_country == 'All countries':
        df_filtrado = df
    else:
        df_filtrado = df[df['winner-country'] == selected_country]

    # Encabezado de la App:
    st.image(r'C:\Users\Usuario\Desktop\ciencia_de_datos\streamlit\champions-league.svg', width=150)
    st.title('UEFA Champions League')
    st.header('Final statistics in the UEFA Champions League')
    st.subheader(f'Summary table: Finals from 1955 to 2023 season')

    # Dataframe:
    st.dataframe(df_filtrado)

    # Estadísticas
    st.subheader(f'Basic descriptive statistics')
    create_statistics_table(df_filtrado)

    # Histograma
    st.subheader(f'Distribution of goals in UEFA Champions League finals')
    create_goals_histogram(df_filtrado)

    # Top 10 equipos más ganadores (dentro del país seleccionado)
    st.subheader(f'Top 10: UEFA Champions League champion clubs')
    top_teams = df_filtrado['winner'].value_counts().head(10)
    create_bar_chart(top_teams, 'Club', 'Cups')

    # Top 5 países más ganadores:
    if selected_country == 'All countries':
        st.subheader('Top 5: Countries with most Champions League titles')
        top_countries = df['winner-country'].value_counts().head(5)
        create_pie_chart(top_countries)

    # Distribución de finales por resolución
    st.subheader(f'Distribution of finals by type of resolution')
    create_ring_chart(df_filtrado)

    # Estadios más usados en ese país
    st.subheader(f'Top 10: Stadiums that hosted UEFA Champions League finals')
    top_stadiums = df_filtrado['stadium'].value_counts().head(10)
    create_bar_chart(top_stadiums, 'Finals', 'Stadium', horizontal=True)

main()