import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()

def run():
    st.title("Study Buddy")

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7
        )
    prompt = ChatPromptTemplate.from_messages([
        ("system","You are study helper buddy for students"),
        MessagesPlaceholder(variable_name="history"),
        ("user","{user_message}")
    ])

    chain = prompt | llm | StrOutputParser()

    if "history" not in st.session_state:
        st.session_state.history = []

    for msg in st.session_state.history:
        if(isinstance(msg,HumanMessage)):
            st.chat_message("student").write(msg)
        else:
            st.chat_message("study buddy").write(msg)
    
    user_message = st.chat_input("Ask your question to the agent")
    if user_message:
        st.chat_message("student").write(user_message)
        with st.spinner("Thinking"):
            result = chain.invoke({
                "history":st.session_state.history,
                "user_message":user_message
                })
            st.chat_message("study buddy").write(result)
        st.session_state.history.append(HumanMessage(content=user_message))
        st.session_state.history.append(AIMessage(content=result))