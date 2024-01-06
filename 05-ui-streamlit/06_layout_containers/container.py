# https://docs.streamlit.io/library/api-reference/layout/st.container

import streamlit as st
import numpy as np

with st.container():
    st.write("This is inside the conatiner")

    # you can call any streamlit command, including custom components:
    st.bar_chart(np.random.randn(50,3))

st.write("This is outside the container")
