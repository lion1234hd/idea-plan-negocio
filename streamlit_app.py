import streamlit as st
import openai

# Función para generar un análisis completo de factibilidad
def generar_analisis_factibilidad(idea_negocio, capital_inicial, tiempo_retorno):
    # Realizar un análisis completo de factibilidad utilizando GPT-3 de OpenAI
    try:
        respuesta_gpt3_analisis_factibilidad = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Analiza la factibilidad de la siguiente idea de negocio:\n\n'{idea_negocio}'\n\nCapital Inicial: ${capital_inicial}\nTiempo de Retorno Esperado: {tiempo_retorno} meses.",
            max_tokens=1000
        )
        analisis_factibilidad = respuesta_gpt3_analisis_factibilidad.choices[0].text.strip()
        return analisis_factibilidad
    except Exception as e:
        st.error("Se produjo un error al realizar el análisis de factibilidad. Verifica tu clave de API y vuelve a intentarlo.")
        return ""

# Configurar tu clave de API de OpenAI
st.sidebar.header("Configuración de API")
api_key = st.sidebar.text_input("Clave de API de OpenAI", type="password")

# Configurar el capital inicial y el tiempo de retorno
st.sidebar.header("Configuración del Negocio")
capital_inicial = st.sidebar.number_input("Capital Inicial (en dólares)", min_value=0)
tiempo_retorno = st.sidebar.number_input("Tiempo de Retorno Esperado (en meses)", min_value=1)

# Verificar si se ha ingresado una clave de API válida y se han proporcionado valores para capital inicial y tiempo de retorno
if api_key and capital_inicial > 0 and tiempo_retorno >= 1:
    # Inicializar la API de OpenAI
    openai.api_key = api_key

    # Título de la aplicación
    st.title("Generador de Análisis de Factibilidad de Negocio")

    # Generar una idea de negocio utilizando GPT-3 de OpenAI
    st.header("Sugerencia de Idea de Negocio:")
    try:
        respuesta_gpt3_idea = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Genera una idea de negocio innovadora y factible.",
            max_tokens=1000
        )
        idea_negocio = respuesta_gpt3_idea.choices[0].text.strip()
        st.write(idea_negocio)
    except Exception as e:
        st.error("Se produjo un error al generar la idea de negocio. Verifica tu clave de API y vuelve a intentarlo.")

    # Botón para generar un análisis completo de factibilidad
    if st.button("Generar Análisis de Factibilidad"):
        analisis_factibilidad = generar_analisis_factibilidad(idea_negocio, capital_inicial, tiempo_retorno)

        # Mostrar el análisis completo de factibilidad
        st.header("Análisis Completo de Factibilidad de la Idea de Negocio:")
        st.write(analisis_factibilidad)

else:
    st.warning("Por favor, completa la configuración de API, el capital inicial y el tiempo de retorno en el panel izquierdo.")
