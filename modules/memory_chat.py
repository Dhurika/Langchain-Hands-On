import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()

def run():
    st.title("Memory Chat")

    st.markdown("""
    ### What's new?
    - `MessagesPlaceholder` → a slot in the prompt for **chat history**
    - `HumanMessage` / `AIMessage` → message objects stored in history
    - `st.session_state` → Streamlit's way of **remembering** across reruns

    ### How memory works?
    | Without Memory | With Memory |
    |---|---|
    | Only current message sent | Full history sent every time |
    | AI forgets everything | AI remembers context |
    """)

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system","you are a helpful assistant"),
        MessagesPlaceholder(variable_name="history"),
        ("user","{input}")
    ])

    chain = prompt | llm | StrOutputParser()

    if "history" not in st.session_state:
        st.session_state.history = []

    # Display chat history
    for msg in st.session_state.history:
        if isinstance(msg, HumanMessage):
            st.chat_message("user").write(msg.content)
        else:
            st.chat_message("assistant").write(msg.content)

    # Chat input
    user_input = st.chat_input("Say something...")

    if user_input:
        st.chat_message("user").write(user_input)

        with st.spinner("Thinking..."):
            result = chain.invoke({
                "history": st.session_state.history,
                "input": user_input
            })

        st.chat_message("assistant").write(result)

        # Save to history
        st.session_state.history.append(HumanMessage(content=user_input))
        st.session_state.history.append(AIMessage(content=result))