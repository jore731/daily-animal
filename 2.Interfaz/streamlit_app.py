import streamlit as st
import pandas as pd

# Title of the app
st.title("Animales")

# Animal details
nombre = "elefante"
descripcion = "Los elefantes son los animales terrestres más grandes del mundo, conocidos por su inteligencia y fuertes lazos sociales."
paises = ["Kenya", "Tanzania", "Zimbabwe", "Botswana"]
coordenadas = [
    {"latitude": -1.2921, "longitude": 36.8219},
    {"latitude": -6.369028, "longitude": 34.888822},
    {"latitude": -19.015438, "longitude": 29.154857},
    {"latitude": -22.328474, "longitude": 24.684866},
]
foto = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"


bandera_kenya = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Kenya.svg/1920px-Flag_of_Kenya.svg.png"
bandera_tanzania = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Tanzania.svg/1920px-Flag_of_Tanzania.svg.png"
bandera_zimbabwe = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Flag_of_Zimbabwe.svg/1920px-Flag_of_Zimbabwe.svg.png"
bandera_bostwana = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_Botswana.svg/1920px-Flag_of_Botswana.svg.png"

# Coordinates for Nairobi, Kenya
animal_location = {"latitude": -1.2921, "longitude": 36.8219}


# Display animal details
st.header(nombre)

with st.container():
    columna1, columna2 = st.columns(2)

    with columna1:
        st.image(foto, caption=nombre.title(), use_container_width=True)

    with columna2:
        st.write(f"**Descripción:** {descripcion}")
        columnas = st.columns(len(paises))
        pais1, pais2, pais3, pais4 = st.columns(4)
        with pais1:
            st.image(bandera_kenya, caption="Kenya", use_container_width=True)
        with pais2:
            st.image(bandera_tanzania, caption="Tanzania", use_container_width=True)
        with pais3:
            st.image(bandera_zimbabwe, caption="Zimbabwe", use_container_width=True)
        with pais4:
            st.image(bandera_bostwana, caption="Botswana", use_container_width=True)

        st.map(
            pd.DataFrame(coordenadas, columns=["latitude", "longitude"]),
            use_container_width=True,
            height=300,
            zoom=0,
            size=1000000,
        )
