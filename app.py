import streamlit as st
st.title("Geography")
answer = st.number_input("Коя е столицата на България?", step=1)
if st.button("Провери"):
  if answer == София:
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")


