import os
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI


st.set_page_config(page_title="Convo Chatbot")
st.header("Hey, Let's Chat !!")

api_key = os.getenv('OPENAI_API_KEY', 'Your_API_KEY')

chat = ChatOpenAI(api_key=api_key, temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant")
    ]

def getresponse(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input_text = st.text_input("Input", key='input')
submit = st.button("Ask the question")

if submit:
    response = getresponse(input_text)
    st.subheader("The Response is:")
    st.write(response)
