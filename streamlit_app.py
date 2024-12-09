import streamlit as st

st.title("🎈 My new app")

conn = st.connection("snowflake")
df = conn.query("SELECT * FROM mytable;", ttl="10m")

for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
