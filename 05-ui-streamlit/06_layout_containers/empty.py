# https://docs.streamlit.io/library/api-reference/layout/st.empty

# Inserts a container into your app that can be used to hold a single element. 

import streamlit as st
import time

st.title("Pakistan")


with st.empty():
    for second in range(10):
        st.write(f"⏳ {second} seconds have passed")
        time.sleep(1)
    st.write("✔️ 10 seconds over!")

st.write("Pakistan Zinda bad")