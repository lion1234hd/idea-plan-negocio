import streamlit as st
import openai

# Configurar tu clave de API de OpenAI
st.sidebar.header("Configuración de API")
api_key = st.sidebar.text_input("Clave de API de OpenAI", type="password")

# Configurar el capital inicial y el tiempo de retorno
st.sidebar.header("Configuración del Negocio")
capital_inicial = st.sidebar.number_input("Capital Inicial (en dólares)", min_value=0)
tiempo_retorno = st.sidebar.number_input("Tiempo para obtener dividendos (en meses)", min_value=1)

# Verificar si se han ingresado datos de configuración
if api_key and capital_inicial > 0 and tiempo_retorno >= 1:
    # Inicializar la API de OpenAI
    openai.api_key = api_key

    # Título de la aplicación
    st.title("Generador de Plan de Negocio")

    # Generar una idea de negocio utilizando GPT-3 de OpenAI
    st.header("Sugerencia de Idea de Negocio:")
    try:
        respuesta_gpt3_idea = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Genera una idea de negocio innovadora y factible.",
            max_tokens=100
        )
        idea_negocio = respuesta_gpt3_idea.choices[0].text.strip()
        st.write(idea_negocio)
    except Exception as e:
        st.error("Se produjo un error al generar la idea de negocio. Verifica tu clave de API y vuelve a intentarlo.")

    # Analizar la idea de negocio utilizando GPT-3 de OpenAI
    st.header("Análisis de la Idea de Negocio:")
    try:
        respuesta_gpt3_analisis = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Analiza la idea de negocio: '{idea_negocio}'",
            max_tokens=2500
        )
        analisis_negocio = respuesta_gpt3_analisis.choices[0].text.strip()
        st.write(analisis_negocio)
    except Exception as e:
        st.error("Se produjo un error al analizar la idea de negocio. Verifica tu clave de API y vuelve a intentarlo.")

else:
    st.warning("Por favor, completa la configuración de API, el capital inicial y el tiempo de retorno en el panel izquierdo.")
