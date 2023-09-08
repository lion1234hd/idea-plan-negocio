import streamlit as st
import openai

# Función para analizar la factibilidad de la idea de negocio
def analizar_factibilidad(idea_negocio, capital_inicial, tiempo_retorno):
    # Analizar la factibilidad utilizando GPT-3 de OpenAI
    try:
        respuesta_gpt3_factibilidad = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Analiza la factibilidad de la siguiente idea de negocio:\n\n'{idea_negocio}'\n\nCapital Inicial: ${capital_inicial}\nTiempo de Retorno Esperado: {tiempo_retorno} meses.",
            max_tokens=500
        )
        factibilidad = respuesta_gpt3_factibilidad.choices[0].text.strip()
        return factibilidad
    except Exception as e:
        st.error("Se produjo un error al analizar la factibilidad. Verifica tu clave de API y vuelve a intentarlo.")
        return ""

# Función para generar un plan de negocios completo
def generar_plan_negocios(idea_negocio):
    # Generar un plan de negocios completo utilizando GPT-3 de OpenAI
    try:
        respuesta_gpt3_plan_negocios = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Desarrolla un plan de negocios completo para la siguiente idea de negocio:\n\n'{idea_negocio}'",
            max_tokens=3000
        )
        plan_negocios_completo = respuesta_gpt3_plan_negocios.choices[0].text.strip()
        return plan_negocios_completo
    except Exception as e:
        st.error("Se produjo un error al generar el plan de negocios completo. Verifica tu clave de API y vuelve a intentarlo.")
        return ""

# Configurar tu clave de API de OpenAI
st.sidebar.header("Configuración de API")
api_key = st.sidebar.text_input("Clave de API de OpenAI", type="password")

# Permitir al usuario ingresar su propia idea de negocio
st.sidebar.header("Ingresar Idea de Negocio")
idea_negocio = st.sidebar.text_area("Ingresa tu Idea de Negocio")

# Configurar el capital inicial y el tiempo de retorno
st.sidebar.header("Configuración del Negocio")
capital_inicial = st.sidebar.number_input("Capital Inicial (en dólares)", min_value=0)
tiempo_retorno = st.sidebar.number_input("Tiempo de Retorno Esperado (en meses)", min_value=1)

# Verificar si se ha ingresado una clave de API válida y una idea de negocio
if api_key and idea_negocio:
    # Inicializar la API de OpenAI
    openai.api_key = api_key

    # Título de la aplicación
    st.title("Analizador de Idea de Negocio")

    # Botón para analizar la factibilidad de la idea de negocio
    if st.button("Analizar Factibilidad"):
        factibilidad = analizar_factibilidad(idea_negocio, capital_inicial, tiempo_retorno)

        # Mostrar la factibilidad de la idea de negocio
        st.header("Factibilidad de la Idea de Negocio:")
        st.write(factibilidad)

        # Si no es factible, proporcionar razones
        if "factible" not in factibilidad.lower():
            st.header("Razones por las que no es factible:")
            st.write(factibilidad)

        # Si es factible, generar un plan de negocios completo
        else:
            # Generar un plan de negocios completo
            plan_negocios_completo = generar_plan_negocios(idea_negocio)

            # Mostrar el plan de negocios completo
            st.header("Plan de Negocios Completo:")
            st.write(plan_negocios_completo)

else:
    st.warning("Por favor, completa la configuración de API y proporciona una idea de negocio en el panel izquierdo.")
