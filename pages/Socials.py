import streamlit as st
import pandas

st.set_page_config(layout="wide")

df = pandas.read_csv("heetsec-socials.csv")
st.header("Socials")
social_links = "Follow us on our social media media pages to stay updated"
st.write(social_links)
for index, row in df[:5].iterrows():
    st.header(row["pages"])
    st.write(f"[Follow]({row['url']})")
    #st.image("images/socials/" + row["image"])