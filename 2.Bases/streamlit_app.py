import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Title of the app
st.title("Streamlit Components Example")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is a simple text")

# Markdown
st.markdown("### This is a markdown text")

# Displaying code
st.code("""
def hello_world():
    print("Hello, World!")
""", language='python')

# Displaying JSON
st.json({
    'name': 'Streamlit',
    'type': 'Web App Framework',
    'language': 'Python'
})

# Displaying a dataframe
data = {
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
st.dataframe(df)

# Displaying a chart

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 30, 40])
st.pyplot(fig)

# Input widgets
name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")

age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is: {age}")

# Button
if st.button("Click me"):
    st.write("Button clicked!")

# Sidebar
st.sidebar.title("Sidebar Title")
st.sidebar.write("This is the sidebar")

# File uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")
