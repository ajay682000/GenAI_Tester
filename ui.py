import streamlit as st
import tester

st.title("Unit Tester")

input_code = st.text_area("Enter the Code", height=20*15)
submit  = st.button("Submit")
if submit:
    # st.write(text_box)
    result =  tester.write_test_function(input_code)
    st.write(result)