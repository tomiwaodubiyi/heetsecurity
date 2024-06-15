import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("Contact us")
form = st.form(key="contact_form")
form.text_input(label="First name")
form.text_input(label="Last name")
form.text_input(label="Email")
form.text_input(label="Phone")
form.text_area(label="Message")
submit_button = form.form_submit_button(label="Send Message")

if submit_button:
    print("Let's go")

