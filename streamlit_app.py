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
            engine="text-davinci-002",
            prompt="Genera una idea de negocio innovadora y factible.",
            max_tokens=100
        )
        idea_negocio = respuesta_gpt3_idea.choices[0].text.strip()
        st.write(idea_negocio)
    except Exception as e:
        st.error("Se produjo un error al generar la idea de negocio. Verifica tu clave de API y vuelve a intentarlo.")

    # Analizar la idea de negocio utilizando GPT-3 de OpenAI
    st.header("Análisis de la Idea de Negocio:")

    # Sección de Análisis de Mercado
    try:
        respuesta_gpt3_analisis_mercado = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Realiza un análisis de mercado para la idea de negocio: '{idea_negocio}'",
            max_tokens=500
        )
        analisis_mercado = respuesta_gpt3_analisis_mercado.choices[0].text.strip()
        st.subheader("Análisis de Mercado:")
        st.write(analisis_mercado)
    except Exception as e:
        st.error("Se produjo un error al realizar el análisis de mercado. Verifica tu clave de API y vuelve a intentarlo.")

    # Sección de Estrategias de Marketing
    try:
        respuesta_gpt3_estrategias_marketing = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Define las estrategias de marketing para la idea de negocio: '{idea_negocio}'",
            max_tokens=500
        )
        estrategias_marketing = respuesta_gpt3_estrategias_marketing.choices[0].text.strip()
        st.subheader("Estrategias de Marketing:")
        st.write(estrategias_marketing)
    except Exception as e:
        st.error("Se produjo un error al definir las estrategias de marketing. Verifica tu clave de API y vuelve a intentarlo.")

    # Sección de Estructura Organizacional
    try:
        respuesta_gpt3_estructura_organizacional = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Describe la estructura organizacional para la idea de negocio: '{idea_negocio}'",
            max_tokens=500
        )
        estructura_organizacional = respuesta_gpt3_estructura_organizacional.choices[0].text.strip()
        st.subheader("Estructura Organizacional:")
        st.write(estructura_organizacional)
    except Exception as e:
        st.error("Se produjo un error al describir la estructura organizacional. Verifica tu clave de API y vuelve a intentarlo.")

    # Sección de Proyecciones Financieras
    try:
        respuesta_gpt3_proyecciones_financieras = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Establece proyecciones financieras para la idea de negocio: '{idea_negocio}'",
            max_tokens=500
        )
        proyecciones_financieras = respuesta_gpt3_proyecciones_financieras.choices[0].text.strip()
        st.subheader("Proyecciones Financieras:")
        st.write(proyecciones_financieras)
    except Exception as e:
        st.error("Se produjo un error al establecer las proyecciones financieras. Verifica tu clave de API y vuelve a intentarlo.")

    # Sección de Plan de Contingencia
    try:
        respuesta_gpt3_plan_contingencia = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Propón un plan de contingencia para la idea de negocio: '{idea_negocio}'",
            max_tokens=500
        )
        plan_contingencia = respuesta_gpt3_plan_contingencia.choices[0].text.strip()
        st.subheader("Plan de Contingencia:")
        st.write(plan_contingencia)
    except Exception as e:
        st.error("Se produjo un error al proponer el plan de contingencia. Verifica tu clave de API y vuelve a intentarlo.")

else:
    st.warning("Por favor, completa la configuración de API, el capital inicial y el tiempo de retorno en el panel izquierdo.")
