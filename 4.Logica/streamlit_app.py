import streamlit as st
import pandas as pd
import info

# Title of the app
st.title("Animales")


# Elefante al inicio
if "animal_actual" not in st.session_state:
    st.session_state.animal_actual = "elefante"

# Extraer datos

nombre = info.animales[st.session_state.animal_actual]["nombre"]
descripcion = info.animales[st.session_state.animal_actual]["descripcion"]
pais = info.animales[st.session_state.animal_actual]["paises"]
coordenadas = info.animales[st.session_state.animal_actual]["coordenadas"]
foto = info.animales[st.session_state.animal_actual]["foto"]

# Display animal details
st.header(nombre)

with st.container():
    columna1, columna2 = st.columns(2)

    with columna1:
        st.image(foto, caption=nombre.title(), use_container_width=True)

    with columna2:
        # Descripción
        st.write(f"**Descripción:** {descripcion}")

        # Banderas
        columnas = st.columns(len(pais))
        for index, columna in enumerate(columnas):
            with columna:
                st.image(info.banderas[pais[index]],
                         caption=pais[index], use_container_width=True)

        # Mapa
        st.map(coordenadas, use_container_width=True,
               height=300, zoom=0, size=1000000)

# Botones
for index, columna_boton in enumerate(st.columns(len(info.animales))):
    animal = list(info.animales.keys())[index]
    with columna_boton:
        if st.button(animal.title(), use_container_width=True):
            st.session_state.animal_actual = animal
            st.rerun()
