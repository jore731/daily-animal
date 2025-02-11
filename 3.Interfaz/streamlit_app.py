import streamlit as st
import pandas as pd
import info

# Title of the app
st.title("Animales")

# Display animal details
st.header(info.nombre_elefante)

columna1, columna2 = st.columns(2)

with columna1:
    st.image(info.foto_elefante, caption=info.nombre_elefante.title(),
             use_container_width=True)

with columna2:
    st.write(f"**Descripción:** {info.descripcion_elefante}")

    pais1, pais2, pais3, pais4 = st.columns(4, vertical_alignment="center")
    with pais1:
        st.image(info.bandera_kenya, caption="Kenya",
                 use_container_width=True)
    with pais2:
        st.image(info.bandera_tanzania, caption="Tanzania",
                 use_container_width=True)
    with pais3:
        st.image(info.bandera_zimbabwe, caption="Zimbabwe",
                 use_container_width=True)
    with pais4:
        st.image(info.bandera_bostwana, caption="Botswana",
                 use_container_width=True)

    st.map(info.coordenadas_elefante, use_container_width=True,
           height=300, zoom=0, size=1000000)
