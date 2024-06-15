import pandas
import streamlit as st

st.set_page_config(layout="wide")
(col1, empty, col2) = st.columns([1.5, 0.5, 1.5])

with col1:
    st.title("HeetSecurity")
    st.caption("One stop for your cybersecurity solutions")

with col2:
    st.header("About")
    content = """
    HeetSecurity is a digital platform offering cybersecurity solutions such as training, offensive penetration testing, auditing and compliance, web application security testing, and security operations center.
    """
    st.write(content)

col3, empty, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    st.header("Blog")
    st.write("Read our exciting blog posts.")
    st.info("Zero-day vulnerability discovered on Microsoft's Azure.")
    st.info("We just released a free linux strength training video on Youtube")

with col4:
    st.header("Services")
    st.write("Below are the list of services that we offer.")
    st.text("Penetration testing")
    st.text("Security Operations Center")
    st.text("Education")
    st.text("Auditing & Compliance")

col5, empty, col6 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("heetsec-socials.csv")
with col5:
    st.header("Socials")
    social_links = "Follow us on our social media media pages to stay updated"
    st.write(social_links)
    for index, row in df[:5].iterrows():
        st.header(row["pages"])
        st.write(f"[Follow]({row['url']})")
        #st.image("images/socials/" + row["image"])
with col6:
    st.header("Contact")
    form = st.form(key="contact_form")
    form.text_input(label="First name")
    form.text_input(label="Last name")
    form.text_input(label="Email")
    form.text_input(label="Phone")
    form.text_input(label="Message")
    submit_button = form.form_submit_button(label="Send Message")

st.header("Meet the Team")

(col7, col8, col9) = st.columns(3)
df = pandas.read_csv("heetsec-team.csv")
with col7:
    for index, row in df[:2].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.info(row["position"])
        st.write(row["info"])
        #st.image("images/team/" + row["image"])

with col8:
    #st.header("Meet the Team")
    for index, row in df[2:4].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.info(row["position"])
        st.write(row["info"])
        #st.image("images/team/" + row["image"])

with col9:
    for index, row in df[4:6].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.info(row["position"])
        st.write(row["info"])
        #st.image("images/team/" + row["image"])