import streamlit as st
import info

st.title("Animales")
st.header("elefante")

columna_izquierda, columna_derecha = st.columns(2)

with columna_izquierda:
  st.image(info.foto_elefante)
with columna_derecha:
  pais1, pais2, pais3, pais4 = st.columns(4, vertical_alignment="center")
  
  with pais1:
      st.image(info.bandera_kenya, caption="Kenya")
  with pais2:
      st.image(info.bandera_tanzania, caption="Tanzania")
  with pais3:
      st.image(info.bandera_zimbabwe, caption="Zimbabwe")
  with pais4:
      st.image(info.bandera_bostwana, caption="Botswana")

  st.write(f"**Descripción** {info.descripcion_elefante}")
  st.map(info.coordenadas_elefante,height=300,zoom=1,size=1000000)