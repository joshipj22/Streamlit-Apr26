import streamlit as st

st.title("This is a title")
st.header("_Streamlit_ is :blue[cool] ")
st.checkbox("select fuel type" , ['Diesel','Petrol','CNG','LPG','Electric'])
st.selectbox("select fuel type" , ['Diesel','Petrol','CNG','LPG','Electric'])
st.multiselect("select fuel type" , ['Diesel','Petrol','CNG','LPG','Electric'])
st.text_input("select fuel type" , ['Diesel','Petrol','CNG','LPG','Electric'])
st.set_page_config 