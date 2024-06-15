import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("Meet the Team")

(col7, col8, col9) = st.columns([1.5, 1.5, 1.5])
df = pandas.read_csv("heetsec-team.csv")
with col7:
    for index, row in df[:2].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.info(row["position"])
        st.write(row["info"])
        st.image("images/team/" + row["image"])

with col8:
    for index, row in df[2:4].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.info(row["position"])
        st.write(row["info"])
        st.image("images/team/" + row["image"])

with col9:
    for index, row in df[4:6].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.info(row["position"])
        st.write(row["info"])
        st.image("images/team/" + row["image"])