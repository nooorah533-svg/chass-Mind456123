import streamlit as st
import google.generativeai as genai
import time

# إعدادات الصفحة
st.set_page_config(page_title="Gemini Dashboard", layout="wide")

# القائمة الجانبية
with st.sidebar:
    st.title("⚙️ الإعدادات")
    api_key = st.text_input("أدخل مفتاح API الخاص بك:", type="password")

st.title("🤖 داش بورد جيمني للذكاء الاصطناعي")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("اسأل جيمني أي شيء..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.warning("الرجاء إدخال مفتاح الـ API في القائمة الجانبية للبدء.")