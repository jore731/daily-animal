import streamlit as st
from pygbif import species, occurrences
import random
import kagglehub
import os

if 'data_path' not in st.session_state:
    st.session_state.data_path = ""
if 'animals' not in st.session_state:
    st.session_state.animals = []
if 'selected_animals' not in st.session_state:
    st.session_state.selected_animals = []
if 'images' not in st.session_state:
    st.session_state.images = []

def init():
    st.session_state.data_path = kagglehub.dataset_download("iamsouravbanerjee/animal-image-dataset-90-different-animals")

    with open(f"{st.session_state.data_path}/name of the animals.txt", "r") as open_file:
        st.session_state.animals = [animal[:-1] for animal in open_file.readlines()]

init()

def refresh():
    images = []
    for animal in st.session_state.selected_animals:
        for image in os.listdir(f"{st.session_state.data_path}/animals/animals/{animal}"):
            images.append(f"{st.session_state.data_path}/animals/animals/{animal}/{image}")
    random.shuffle(images)
    st.session_state.images = images


st.multiselect("Select an animal", key="selected_animals", options=st.session_state.animals, on_change=refresh)

number_of_rows = 5
cells = []
for row_number in range(number_of_rows):
    cells +=st.columns(3)

for index, col in enumerate(cells):
    tile = col.container()
    with tile:
        try:
            st.image(st.session_state.images[index], use_container_width=True)
        except IndexError:
            pass


# def refresh():
#     while True:
#         st.session_state.found_specie = species.name_suggest(q="", offset=random.randint(0,10000), limit=1)[0]
#         st.session_state.found_occurrences = occurrences.search(taxonKey=st.session_state.found_specie["key"], mediatype="StillImage")["results"]
    
#         if len(st.session_state.found_occurrences)>=6:
#             return
    

# st.button("Refresh", type="tertiary", on_click=refresh)

# st.title(st.session_state.found_specie["scientificName"])

# row1 = st.columns(3)
# row2 = st.columns(3)

# for index, col in enumerate(row1 + row2):
#     tile = col.container()
#     with tile:
#         st.image(st.session_state.found_occurrences[index]["media"][0]["identifier"], use_container_width=True)