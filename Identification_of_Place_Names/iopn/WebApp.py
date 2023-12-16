import streamlit as st

import Fuzzer
import NewModel
import Translator

st.title("Identification of Place Names")
text = ''
message = st.text_area("Type your message here:", height=100)
submit_button = st.button("Submit")

if submit_button:
    if message:
        text = message
        st.write("Message submitted successfully.")
    else:
        st.write("Please enter a message.")

translated = Translator.translator(text)

result = NewModel.identify_place_names(translated)

for word_to_search in result:
    result = Fuzzer.fuzzy_search("places.csv", word_to_search)
    st.write(f'The word {result[0]} is found and its canonical name is {result[1]} and is in the {result[2]} table.')
