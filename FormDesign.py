import streamlit as st

name = st.text_input("Enter your Name: ")
fname = st.text_input("Enter Your Father Name: ")
adr = st.text_area("Enter Your Address: ")
classdata = st.selectbox("Enter your Class :", (1,2,3,4,5))

button = st.button("Done")
if button:
    st.markdown(f"""
    Name: {name}
    Father Name: {fname}
    Address: {adr}
    Class: {classdata}
        """)