import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
def run():
    st.title("✍️ Module 2 — Prompt Engineer")

    st.markdown("""
    ### What's new?
    - `ChatPromptTemplate` → separate **system** and **human** messages
    - `system` → tells the LLM who it is
    - `human` → the actual user input
    """)

    #persona = st.text_input("Give the AI a persona", value="You are a sarcastic tech bro who explains things with startup buzzwords.")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a sarcastic tech bro who explains things with startup buzzwords."),
        ("human", "Explain {topic} in 4 lines.")
    ])

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7
    )
    chain = prompt | llm

    topic = st.text_input("Topic to explain", placeholder="e.g. blockchain")

    if st.button("Run"):
        if topic:
            with st.spinner("Thinking..."):
                result = chain.invoke({"topic": topic})
                st.success(result.content)
        else:
            st.warning("Fill both fields!")

