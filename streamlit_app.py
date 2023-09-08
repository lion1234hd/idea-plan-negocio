import streamlit as st
import openai

# Función para generar un análisis completo
def generar_analisis(idea_negocio):
    # Realizar un análisis completo utilizando GPT-3 de OpenAI
    try:
        respuesta_gpt3_analisis = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Realiza un análisis completo de la siguiente idea de negocio:\n\n'{idea_negocio}'\n\nIncluye el análisis de mercado, estrategias de marketing, estructura organizacional, proyecciones financieras y plan de contingencia.",
            max_tokens=1000
        )
        analisis_completo = respuesta_gpt3_analisis.choices[0].text.strip()
        return analisis_completo
    except Exception as e:
        st.error("Se produjo un error al realizar el análisis completo. Verifica tu clave de API y vuelve a intentarlo.")
        return ""

# Configurar tu clave de API de OpenAI
st.sidebar.header("Configuración de API")
api_key = st.sidebar.text_input("Clave de API de OpenAI", type="password")

# Verificar si se ha ingresado una clave de API válida
if api_key:
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
            max_tokens=1100
        )
        idea_negocio = respuesta_gpt3_idea.choices[0].text.strip()
        st.write(idea_negocio)
    except Exception as e:
        st.error("Se produjo un error al generar la idea de negocio. Verifica tu clave de API y vuelve a intentarlo.")

    # Botón para generar un análisis completo
    if st.button("Generar Análisis Completo"):
        analisis_completo = generar_analisis(idea_negocio)

        # Mostrar el análisis completo
        st.header("Análisis Completo de la Idea de Negocio:")
        st.write(analisis_completo)

else:
    st.warning("Por favor, completa la configuración de API en el panel izquierdo.")
