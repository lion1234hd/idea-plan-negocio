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

    # Crear un formulario para recopilar información del usuario
    st.header("Ingresa la información del negocio:")
    idea_negocio = st.text_area("Describe tu idea de negocio:")
    
    # Análisis de mercado
    st.header("1. Análisis de Mercado:")
    st.write("Identificar tamaño del mercado, competidores, tendencias y oportunidades.")
    analisis_mercado = st.text_area("Análisis de Mercado:")
    
    # Estrategias de marketing
    st.header("2. Estrategias de Marketing:")
    st.write("Definición de cómo atraer y retener clientes.")
    estrategias_marketing = st.text_area("Estrategias de Marketing:")
    
    # Estructura organizacional
    st.header("3. Estructura Organizacional:")
    st.write("Describir la estructura de tu equipo y responsabilidades clave.")
    estructura_organizacional = st.text_area("Estructura Organizacional:")
    
    # Proyecciones financieras
    st.header("4. Proyecciones Financieras:")
    st.write("Establecer expectativas de ingresos, costos y rentabilidad.")
    proyecciones_financieras = st.text_area("Proyecciones Financieras:")
    
    # Plan de contingencia
    st.header("5. Plan de Contingencia:")
    st.write("Proponer soluciones a posibles problemas.")
    plan_contingencia = st.text_area("Plan de Contingencia:")

    # Botón para generar el plan de negocio
    if st.button("Generar Plan de Negocio"):
        # Combinar todos los datos ingresados por el usuario
        plan_completo = f"**Idea de Negocio:**\n{idea_negocio}\n\n" \
                        f"**1. Análisis de Mercado:**\n{analisis_mercado}\n\n" \
                        f"**2. Estrategias de Marketing:**\n{estrategias_marketing}\n\n" \
                        f"**3. Estructura Organizacional:**\n{estructura_organizacional}\n\n" \
                        f"**4. Proyecciones Financieras:**\n{proyecciones_financieras}\n\n" \
                        f"**5. Plan de Contingencia:**\n{plan_contingencia}\n\n"

        # Generar el plan de negocio utilizando GPT-3 de OpenAI
        try:
            respuesta_gpt3 = openai.Completion.create(
                engine="text-davinci-002",
                prompt=plan_completo,
                max_tokens=200
            )
            st.subheader("Plan de Negocio Generado:")
            st.write(respuesta_gpt3.choices[0].text)
        except Exception as e:
            st.error("Se produjo un error al generar el plan de negocio. Verifica tu clave de API y vuelve a intentarlo.")
else:
    st.warning("Por favor, completa la configuración de API y la información del negocio en el panel izquierdo.")

