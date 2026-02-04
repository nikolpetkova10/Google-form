import streamlit as st
st.title("Geography")
answer1 = st.text_input("Коя е столицата на България?")
if st.button("Провери"):
  if answer1 == "София":
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")

answer2 = st.text_input("Коя е столицата на Япония?")
if st.button("Провери"):
  if answer2 == "Токио":
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")

answer3 = st.text_input("Коя е столицата на Белгия?")
if st.button("Провери"):
  if answer3 == "Брюксел":
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")

answer4 = st.text_input("Коя е столицата на Германия?")
if st.button("Провери"):
  if answer4 == "Берлин":
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")
    
answer5 = st.text_input("Коя е столицата на Гърция?")
if st.button("Провери"):
  if answer5 == "Атина":
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")
