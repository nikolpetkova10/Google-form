import streamlit as st
st.title("Geography")
answer = st.text_input("Коя е столицата на България?")
if st.button("Провери"):
  if answer == "София":
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")

answer = st.text_input("Коя е столицата на Япония?")
if st.button("Провери"):
  if answer == "Токио":
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")

answer = st.text_input("Коя е столицата на Белгия?")
if st.button("Провери"):
  if answer == "Брюксел":
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")

answer = st.text_input("Коя е столицата на Германия?")
if st.button("Провери"):
  if answer == "Берлин":
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")
    
answer = st.text_input("Коя е столицата на Гърция?")
if st.button("Провери"):
  if answer == "Атина":
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")
