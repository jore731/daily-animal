import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.title("Tutorial Streamlit")

left_column, right_column = st.columns([1, 20])

with right_column:
    with st.container():
        st.write(
            "**Instalación de Streamlit**: Para instalar streamlit en python utilizaremos el gestor de paquetes pip. Para ello, ejecutaremos el siguiente comando en la terminal:"
        )
        st.code("""pip install streamlit""", language="bash")
    st.divider()

    with st.container():
        st.write(
            "**Arranque app Streamlit**: Para arrancar una aplicación de Streamlit, ejecutaremos el siguiente comando en la terminal:"
        )
        st.code("""streamlit run app.py""", language="bash")
    st.divider()
    with st.container():
        st.write("st.title: crea un título para un texto dado")
        st.code("""st.title(\"Esto es un título\")""", language="python")
        st.title("Esto es un título")
    st.divider()

    with st.container():
        st.write("st.header: crea un encabezado para un texto dado")
        st.code("""st.header(\"Esto es un encabezado\")""", language="python")
        st.header("Esto es un encabezado")
    st.divider()

    with st.container():
        st.write("st.subheader: crea un subencabezado para un texto dado")
        st.code("""st.subheader(\"Esto es un subencabezado\")""",
                language="python")
        st.subheader("Esto es un subencabezado")
    st.divider()

    with st.container():
        st.write("st.text: crea un texto para un texto dado")
        st.code(
            """st.text(\"Esto es un texto donde los enlaces como [prueba](google.com) no funcionan\")""",
            language="python",
        )
        st.text(
            "Esto es un texto donde los enlaces como [prueba](google.com) no funcionan"
        )
    st.divider()

    with st.container():
        st.write("st.markdown: crea un texto en markdown para un texto dado")
        st.code(
            """st.markdown(\"### Esto es un texto en markdown\")""", language="python"
        )
        st.markdown(
            "Esto es un texto donde los enlaces como [prueba](google.com) sí funcionan"
        )
    st.divider()

    with st.container():
        st.write("st.code: crea un bloque de código para un texto dado")
        st.code("""st.code(\"print('Hola Mundo')\")""", language="python")
        st.code("print('Hola Mundo')")
    st.divider()

    with st.container():
        st.write("st.image: muestra una imagen en la aplicación")
        st.code(
            """st.image(\"https://docs.streamlit.io/logo.svg\")""", language="python"
        )
        st.image("https://docs.streamlit.io/logo.svg")
    st.divider()

    with st.container():
        st.write("st.audio: muestra un audio en la aplicación")
        st.code(
            """audio_file = open('https://assets.mixkit.co/active_storage/sfx/213/213.wav', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/wav')""",
            language="python",
        )
        audio_file = open("2.Bases/audio.wav", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/wav")
    st.divider()

    with st.container():
        st.write("st.latex: muestra una fórmula en la aplicación")
        st.code("""st.latex(\"f(x) = x^2\")""", language="python")
        st.latex("f(x) = x^2")
    st.divider()

    with st.container():
        st.write("st.map: muestra un mapa en la aplicación")
        st.code(
            """
data = [{"latitude": 40.41, "longitude": -3.70}]
st.map(data)""",
            language="python",
        )
        data = [{"latitude": 40.41, "longitude": -3.70}]
        st.map(data)
    st.divider()

    with st.container():
        st.write("st.table: muestra una tabla en la aplicación")
        st.code(
            """
data = [[1, 2, 3],[4, 5, 6]]
st.table(data)""",
            language="python",
        )
        data = [[1, 2, 3], [4, 5, 6]]
        st.table(data)
    st.divider()

    with st.container():
        st.write("st.dataframe: muestra un dataframe en la aplicación")
        st.code(
            """
import pandas as pd
data = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})
st.dataframe(data)""",
            language="python",
        )
        data = pd.DataFrame({"column1": [1, 2, 3], "column2": [4, 5, 6]})
        st.dataframe(data)
    st.divider()

    with st.container():
        st.write("st.json: muestra un json en la aplicación")
        st.code(
            """
data = {'key1': 'value1', 'key2': 'value2'}
st.json(data)""",
            language="python",
        )
        data = {"key1": "value1", "key2": "value2"}
        st.json(data)
    st.divider()

    with st.container():
        st.write("st.button: muestra un botón en la aplicación")
        st.code(
            """if st.button('Click me'):
    st.write('Clicked')""",
            language="python",
        )
        if st.button("Click me"):
            st.write("Clicked")
    st.divider()

    with st.container():
        st.write("st.checkbox: muestra un checkbox en la aplicación")
        st.code(
            """if st.checkbox('Check me'):
    st.write('Checked')""",
            language="python",
        )
        if st.checkbox("Check me"):
            st.write("Checked")
    st.divider()

    with st.container():
        st.write("st.radio: muestra un radio button en la aplicación")
        st.code(
            """option = st.radio('Radio', ['option 1', 'option 2'])
if option == 'option 1':
    st.write('option 1 selected')
else:
    st.write('option 2 selected')""",
            language="python",
        )
        option = st.radio("Radio", ["option 1", "option 2"])
        if option == "option 1":
            st.write("option 1 selected")
        else:
            st.write("option 2 selected")
    st.divider()

    with st.container():
        st.write("st.text_input: muestra un input en la aplicación")
        st.code(
            """name = st.text_input('Enter your name')
st.write('Hello', name)""",
            language="python",
        )
        name = st.text_input("Enter your name")
        st.write("Hello", name)
        st.divider()

    with st.container():
        st.write("st.session_state: guarda el estado de la aplicación en la sesión. Esto permite cambiar valores sin que se reseteen al ejecutar la aplicación de nuevo.")
        st.code(
            """if 'counter' not in st.session_state:
    st.session_state.counter = 0
if st.button('Increment'):
    st.session_state.counter += 1
st.write('Counter:', st.session_state.counter)""",
            language="python",
        )
        if "counter" not in st.session_state:
            st.session_state.counter = 0
        if st.button("Increment"):
            st.session_state.counter += 1
        st.write("Counter:", st.session_state.counter)
    st.divider()
