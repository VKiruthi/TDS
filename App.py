import streamlit as st

st.header('TDS Assignment')
st.subheader('Find the largest among the 3 given numbers')

with st.form(key='form1'):
    n1 = st.number_input("Enter the First Number :")
    n2 =st.number_input("Enter the Second Number :")
    n3 =st.number_input("Enter the Third Number :")
    button = st.form_submit_button("Find the maximum")
if button:
    st.success(f"The maximum number is {max([n1,n2,n3])} ")
