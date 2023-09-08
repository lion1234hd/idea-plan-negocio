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

    # Botón para generar el plan de negocio
    if st.button("Generar Plan de Negocio"):
        # Combinar la información del usuario en un solo texto
        informacion_usuario = f"**Idea de Negocio:**\n{idea_negocio}\n\n" \
                              f"**Capital Inicial:** {capital_inicial} dólares\n" \
                              f"**Tiempo de Retorno:** {tiempo_retorno} meses\n\n"

        # Generar el plan de negocio utilizando GPT-3 de OpenAI
        try:
            respuesta_gpt3 = openai.Completion.create(
                engine="text-davinci-003",
                prompt=informacion_usuario,
                max_tokens=500  # Aumentar si es necesario
            )
            st.subheader("Plan de Negocio Generado:")
            st.write(respuesta_gpt3.choices[0].text)
        except Exception as e:
            st.error("Se produjo un error al generar el plan de negocio. Verifica tu clave de API y vuelve a intentarlo.")
else:
    st.warning("Por favor, completa la configuración de API y la información del negocio en el panel izquierdo.")

