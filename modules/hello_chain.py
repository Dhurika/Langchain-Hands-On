import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

def run():
    st.title("Hello chain")
    st.markdown("""
    ### What's happening here?
    - `PromptTemplate` → a prompt with a **variable** inside it
    - `ChatGroq` → your connection to the **Groq LLM**
    """)

    topic = st.text_input("Topic",placeholder="eg.Neural Networks")
    prompt = PromptTemplate(input_variables=[topic],template="Explain a few lines about this {topic}")

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7
    )
    chain = prompt | llm #LCEL
    if st.button("Run Chain"):
         if topic:
            with st.spinner("Thinking..."):
                result = chain.invoke({"topic": topic})
                st.success(result.content)
         else:
            st.warning("Enter a topic first!")
