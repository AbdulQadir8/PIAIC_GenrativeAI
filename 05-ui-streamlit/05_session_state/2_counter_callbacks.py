import streamlit as st

st.title('Counter Example using Callbacks')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('Increment',on_click=increment_counter)
st.button('Increment1',on_click=increment_counter)
st.button('Inrement2',on_click=increment_counter)
st.button('Increment3',on_click=increment_counter)          
st.write('Count :',st.session_state.count)