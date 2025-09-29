import streamlit as st

conn = st.connection("streamlit_db")
df = conn.query("select * from users")
st.dataframe(df)
