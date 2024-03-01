import streamlit as st

# Title
st.title('Here is the 1st page')

# create a text input

name = st.text_input('Your name')

if st.button("Click"):
    st.write(f'Hello *{name}* :sunglasses:')