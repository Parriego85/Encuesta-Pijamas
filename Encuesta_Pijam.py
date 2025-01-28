import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_image_select import image_select

# Links de imágenes como variables
img_negro = "https://www.wearfigs.com/i/contentful/5j6wpslh72e4/1WlkcV0JKNu0fJ5gvK5u61/cf0be2e0ca2e9019fb730a82fb36a9c4/HP_Color_Carousel_288x288__BLACK.jpg?fm=webp&w=180"
img_azul_marino = "https://www.wearfigs.com/i/contentful/5j6wpslh72e4/62uiKWOuTkOnA6xYq9K66z/40d1ba60a5aade3867e91c8bb84c871e/HP_Color_Carousel_288x288__NAVY.jpg?fm=webp&w=180"
img_azul_rey = "https://www.wearfigs.com/i/contentful/5j6wpslh72e4/30wBlJjLCiJkgZcIrlngQ0/6ec23b4990733065a36ab2ed8c1dd312/HP_Color_Carousel_288x288__ROYAL_BLUE.jpg?fm=webp&w=180"
img_carbon = "https://www.wearfigs.com/i/contentful/5j6wpslh72e4/2d0Fmv4diHBiL1noIITvro/fdb960f7fd5541c496be34caa635549a/HP_Color_Carousel_288x288__CHARCOAL.jpg?fm=webp&w=180"
img_musgo = "https://www.wearfigs.com/i/contentful/5j6wpslh72e4/36yRkvkTsQWIlrp2ym1Tlj/67090d57a723e4fa3c322cc793e97c5d/HP_Color_Carousel_288x288__MOSS.jpg?fm=webp&w=180"
img_malbec = "https://www.wearfigs.com/i/contentful/5j6wpslh72e4/zLNryDMamecpB7vOuNakn/83a27f0f135af2757726d90404d7074d/HP_Color_Carousel_288x288__BURGUNDY.jpg?fm=webp&w=180"
img_cotton_candy = "https://www.wearfigs.com/i/contentful/5j6wpslh72e4/5aUA3vKIrHRMqTyUKxkg4U/8543c26b92d7be6890ebe3d2112def89/HP_Color_Carousel_288x288__MAUVE.jpg?fm=webp&w=180"
img_azul_cielo = "https://www.wearfigs.com/i/contentful/5j6wpslh72e4/3QE3oKMDCz3gHLcMaeM3RH/d7ba5ad4694d14b905ba9449d04beb35/HP_Color_Carousel_288x288__CEIL_BLUE.jpg?fm=webp&w=180"
img_grafito = "https://www.wearfigs.com/i/contentful/5j6wpslh72e4/5mznRvwmEt2pGPEIzcLpxt/0b3720e587c9c83c81ae6dc56b48d0d8/HP_Color_Carousel_288x288__GRAPHITE.jpg?fm=webp&w=180"

# Estilo personalizado
st.markdown(
    """
    <style>
        .stApp {
            padding: 20px;
            border-radius: 20px;
            margin: 15px;
        }
        .title {
            font-size: 30px;
            color: #00796b;
            text-align: center;
            font-weight: bold;
        }
        .subtitle {
            font-size: 20px;
            color: #004d40;
            text-align: center;
        }
        .topic {
            font-size: 18px;
            color: #00796b;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .question {
            font-size: 15px;
            font-weight: bold;
        }
        div.stButton > button {
            background-color: #00796b;
            color: white;
            border-radius: 10px;
            border: 2px solid #004d40;
            font-size: 16px;
            padding: 10px 20px;
        }
        div.stButton > button:hover {
            background-color: #004d40;
            color: white;
        }
        div.stButton > button:focus {
            background-color: #00796b !important;
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Configurar estado inicial
if 'mostrar_encuesta' not in st.session_state:
    st.session_state.mostrar_encuesta = False

# Título e introducción
st.markdown('<div class="title">Encuesta de Pijamas Quirúrgicas</div>', unsafe_allow_html=True)
st.write("""
Estamos diseñando prendas que se ajusten a las necesidades reales de quienes trabajan o estudian en el sector médico.
Tu opinión será clave para crear productos únicos, prácticos y personalizados.
""")
st.markdown('<div class="subtitle">¡Participa en nuestra encuesta y sé parte del cambio!</div>', unsafe_allow_html=True)

# Botón de inicio
if st.button("Comenzar"):
    st.session_state.mostrar_encuesta = True

if st.session_state.mostrar_encuesta:
    st.write("---")
        
    # Perfil del participante
    with st.expander("**1. Perfil del Participante**", expanded=True):
        area = st.selectbox("¿A qué área de la salud te dedicas o estás estudiando?", [
            "Medicina General", "Especialidad Médica", "Enfermería", "Anestesiología", 
            "Medicina Estética", "Odontología", "Otro"
        ], index=0, help="Selecciona tu área de especialización.")

        if area == "Otro":
            st.text_input("Especifica tu área:", placeholder="Escribe aquí...")

        if area == "Especialidad Médica":
            st.text_input("Especifica tu área de especialidad:", placeholder="Escribe aquí...")

        rol = st.radio("¿Cuál es tu rol actual?", [
            "Médico", "Residente", "Enfermero/a", "Estudiante", "Otro"
        ])

        if rol == "Estudiante":
            st.text_input("¿En qué institución o universidad estudias?", placeholder="Escribe aquí...")
        else:
            st.text_input("¿En qué institución u hospital trabajas?", placeholder="Escribe aquí...")

        frecuencia = st.radio("¿Con qué frecuencia usas pijamas quirúrgicas?", [
            "Diariamente", "Varias veces por semana", "Ocasionalmente", "Nunca"
        ])

        if frecuencia == "Nunca":
            st.markdown('<div class="subtitle">¡Gracias por tu tiempo! No necesitas responder más preguntas.</div>',
                         unsafe_allow_html=True)
            st.stop()
        else:
            wearing = st.text_area("¿Qué marca(s) de pijamas usas regularmente?", 
                                   placeholder="Nombra todas las que consideres.")
        # Preferencias sobre pijamas quirúrgicas
    with st.expander("**2. Preferencias sobre Pijamas Quirúrgicas**", expanded=True):
        identify = st.selectbox("Cuando piensas en uniforme médico, ¿qué marca es la primera que se te viene a la mente?", [
            "Skechers", "Grey's Anatomy", "Cherokee", "Figs", "Clinic Dress", 
            "Med Couture", "Healing Hands", "Dickies Medical", "Barco"
        ], index=0)

        most = st.radio("¿Qué consideras más importante en pijamas quirúrgicas?", [
            "Precio", "Comodidad para largas horas de trabajo", "Diseño atractivo", 
            "Apariencia profesional", "Durabilidad", "Otro"
        ])

        if most == "Otro":
            st.text_input("Especifica:", placeholder="Escribe aquí...")

        caracteristicas = st.multiselect(
            "¿Qué características valoras más en las pijamas quirúrgicas?", [
                "Comodidad", "Durabilidad", "Diseño moderno", 
                "Tejidos tecnológicos (antibacteriales, regulación térmica)", 
                "Personalización (nombre, especialidad, etc.)"
            ]
        )

        if "Tejidos tecnológicos (antibacteriales, regulación térmica)" in caracteristicas:
            innovaciones = st.multiselect(
                "¿Qué innovaciones te interesan más?", [
                    "Tejidos que repelen líquidos", "Antibacteriales", 
                    "Regulación térmica", "Bolsillos especializados", "Ajuste anatómico"
                ], default=["Antibacteriales", "Regulación térmica"]
            )

                # Variable para almacenar la selección
        if "selected_colors" not in st.session_state:
            st.session_state.selected_colors = []

        st.markdown('<div class="topic">¿Cuál es tu top 3 de colores favoritos?</div>', unsafe_allow_html=True)

        # Mostrar las imágenes para seleccionar
        selected_color = image_select(
            "", 
            images=[
                img_negro, 
                img_azul_marino, 
                img_azul_rey, 
                img_carbon, 
                img_musgo, 
                img_malbec, 
                img_cotton_candy, 
                img_azul_cielo, 
                img_grafito
            ],
            captions=[
                "Negro", 
                "Azul Marino", 
                "Azul Rey", 
                "Carbón", 
                "Verde Musgo", 
                "Malbec", 
                "Cotton Candy", 
                "Azul Cielo", 
                "Grafito"
            ],
            key="color_selection"
        )

        # Agregar el color seleccionado al listado si no excede de 3
        def add_color_to_selection(color):
            if color and color not in st.session_state.selected_colors:
                if len(st.session_state.selected_colors) < 3:
                    st.session_state.selected_colors.append(color)
                else:
                    st.warning("Solo puedes seleccionar hasta 3 colores. Si deseas cambiar tu selección, reinicia la app.")

        if selected_color:
            add_color_to_selection(selected_color)

        # Mostrar las imágenes seleccionadas
        if st.session_state.selected_colors:
            st.write("<div class='question'>Has seleccionado:</div>", unsafe_allow_html=True)
            cols = st.columns(len(st.session_state.selected_colors))
            for i, color in enumerate(st.session_state.selected_colors):
                with cols[i]:
                    st.image(color, width=100)


        # Cantidad y frecuencia de compra
    with st.expander("**3. Cantidad y Frecuencia de Compra**", expanded=True):
        where = st.selectbox("¿Dónde compras normalmente tus pijamas quirúrgicas?", [
            "Tiendas físicas", "On line (Amazon, eBay, Mercado Libre, etc.)", 
            "Proveedores de hospital", "Otro"
        ])

        cantidad = st.radio("¿Cuántos juegos de pijamas quirúrgicas compras al año?", [
            "Menos de 2", "2-4", "5-7", "Más de 7"
        ])

        frecuencia_compra = st.radio("¿Con qué frecuencia compras pijamas quirúrgicas?", [
            "Cada 1-3 meses", "Cada 4-6 meses", "Una vez al año", "Solo cuando es necesario (reemplazo)"
        ])

        costo = st.radio("¿Cuál es el precio promedio que pagas por un conjunto de pijamas quirúrgicas?", [
            "Menos de \$500", "\$500 - \$700", "\$700 - \$1,000", "Más de \$1,000"
        ])

        ## Interés en el modelo de suscripción
    with st.expander("**4. Interés en el Modelo de Suscripción**", expanded=True):
        interes_suscripcion = st.select_slider(
            "¿Qué tan interesad@ estarías en un modelo de suscripción que te envíe pijamas quirúrgicas periódicamente?",
            options=["No me interesa", "Poco interesad@", "Interesad@", "Muy interesad@"]
        )
        

        # Embajadores
        st.markdown('<div class="topic">5. Colaboración y Embajadores</div>', unsafe_allow_html=True)
        embajador = st.radio("¿Te gustaría ser embajador de nuestra marca?", [
            "Sí",
            "No",
            "Tal vez",
        ])
        if embajador in ["Sí", "Tal vez"]:
            st.write("<div class='question'>Compártenos tu contacto</div>", unsafe_allow_html=True)
            name = st.text_input("", placeholder="Nombre y Apellido(s):")
            mail = st.text_input("", placeholder="Correo:")
            if mail and "@" not in mail:
                st.error("Por favor, introduce un correo válido")
            phone = st.text_input("", placeholder="Teléfono:")
            if phone and not phone.isdigit():
                st.error("Por favor, introduce solo números en el campo de teléfono.")
            redes_sociales = st.text_input("", placeholder="Redes sociales:")
            if redes_sociales and "@" not in redes_sociales:
                st.error("Por favor, incluye '@' en tus redes sociales (por ejemplo, @usuario).")

            beneficios = st.text_area(
                "¿Qué beneficios esperarías al ser embajador?"
            )

        # Agradecimiento
        st.write("---")
        st.write(
            """<div class="subtitle">¡Gracias por participar! Tu opinión es muy valiosa para nosotros.</div>""", 
            unsafe_allow_html=True)
        





#st.checkbox('yes')
#st.radio('Pick your gender',['Male','Female'])



#st.selectbox('Pick your gender',['Male','Female'])
#st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
#st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
#st.slider('Pick a number', 0,50)