import streamlit as st
import tester

st.title("Unit Tester")



api_key = st.sidebar.text_input("Enter Your Google API key:")
api_key_button = st.sidebar.button("Submit", key="api_button")
if api_key_button:
    st.session_state.google_api_key = api_key
    st.sidebar.write("Success ")



input_code = st.text_area("Enter the Code", height=20*15)
submit  = st.button("Submit", key="submit_button")
if submit:
    result =  tester.write_test_function(input_code, st.session_state.google_api_key)
    st.write(result)
clear_button = st.button("Clear")
main_content = st.empty()
if clear_button:
    main_content.empty()
