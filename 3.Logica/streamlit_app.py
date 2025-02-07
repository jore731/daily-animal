import streamlit as st
import pandas as pd
import informacion

# Title of the app
st.title("Animales")

nombre: str
descripcion: str
pais: str
foto: str


# Función para cambiar el animal
def cambiar_animal(nuevo_animal):
    print(nuevo_animal)
    st.session_state.nombre = nuevo_animal.title()
    st.session_state.descripcion = informacion.animales[nuevo_animal]["descripcion"]
    st.session_state.pais = informacion.animales[nuevo_animal]["paises"]
    st.session_state.foto = informacion.animales[nuevo_animal]["foto"]
    st.session_state.coordenadas = informacion.animales[nuevo_animal]["coordenadas"]


# Elefante al inicio
if "init" not in st.session_state:
    cambiar_animal("elefante")
    st.session_state.init = True

# Display animal details
st.header(st.session_state.nombre)

with st.container():
    columna1, columna2 = st.columns(2)

    with columna1:
        st.image(
            st.session_state.foto,
            caption=st.session_state.nombre.title(),
            use_container_width=True,
        )

    with columna2:
        st.write(f"**Descripción:** {st.session_state.descripcion}")
        columnas = st.columns(len(st.session_state.pais))
        for index, columna in enumerate(columnas):
            with columna:
                st.image(
                    informacion.banderas[st.session_state.pais[index]],
                    caption=st.session_state.pais[index],
                    use_container_width=True,
                )
        st.map(
            pd.DataFrame(
                st.session_state.coordenadas, columns=["latitude", "longitude"]
            ),
            use_container_width=True,
            height=300,
            zoom=0,
            size=1000000,
        )
columna1, columna2, columna3, columna4 = st.columns(4)

with columna1:
    st.button(
        "Elefante",
        on_click=cambiar_animal,
        args=("elefante",),
        use_container_width=True,
    )
with columna2:
    st.button(
        "Pingüinos",
        on_click=cambiar_animal,
        args=("pingüino",),
        use_container_width=True,
    )
with columna3:
    st.button(
        "Jirafa", on_click=cambiar_animal, args=("jirafa",), use_container_width=True
    )
with columna4:
    st.button(
        "Cebra", on_click=cambiar_animal, args=("cebra",), use_container_width=True
    )
