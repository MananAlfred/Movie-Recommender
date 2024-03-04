import streamlit as st

st.set_page_config(
    page_title="Site Developer Details",
    page_icon="🙂"
)

st.header("Manan Alfred")

st.sidebar.success("Select a page from above")

tab1, tab2, tab3, tab4= st.tabs(["Description", "Photo", "GitHub", "LinkedIn"])

with tab1:
    st.title("Iam a hardworking and smart AI enthusiast! \nCurrently a Student in an esteemed university!")
    st.subheader("\nPlease refer my Github for more projects!")
with tab2:
    st.header("[My Photo](https://media.licdn.com/dms/image/D4E03AQGUnklON7V0gw/profile-displayphoto-shrink_400_400/0/1695374883885?e=1715212800&v=beta&t=SfND9KRcEmlytyqPhvqQLls8ylv3j2rM1p4_Ji5G-w8)")

with tab3:
    st.header("My Github Link is :-")
    st.write("[Github Link](https://github.com/MananAlfred)")

with tab4:
    st.header("My LinkedIn is :- ")
    st.write("[LinkedIn Link](https://www.linkedin.com/in/manan-alfred/)")