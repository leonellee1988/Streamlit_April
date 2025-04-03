import streamlit as st

def main():
    st.title('Curso de Streamlit')
    st.header('Este es mi primer encabezado')
    st.subheader('Este es mi primer sub-encabezado')
    st.text('Hola mundo, estoy aprendiendo a crear Apps con Streamlit')

    nombre = 'Edwin Lee'

    st.text(f'Hola, mi nombre es {nombre}, y me encanta Python')
    st.markdown('### Esto es un markdown')
    st.success('Exito')
    st.warning('Esto es una advertencia')
    st.info('Esto es una información')
    st.error('Error')

    st.text('Esto es un texto normal')
    st.text('### Pero también le puedo aplicar markdown')

main()