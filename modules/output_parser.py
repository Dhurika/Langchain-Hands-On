import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

load_dotenv()

def run():
    st.title("✍️ Module 3 — Output Parser")

    st.markdown("""
        ### What's new?
        - `StrOutputParser` → converts `AIMessage` to plain **string**
        - `JsonOutputParser` → converts response to a python **dict**
        - `prompt | llm | parser` → full **3 step LCEL chain**

        ### Why parsers?
        | Without Parser | With Parser |
        |---|---|
        | `result.content` | `result` |
        | `AIMessage object` | `plain string / dict` |
        """)
    
    parser = st.radio("Select Parser",["String parser","Json Parser"])
    
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7
    )

    topic = st.text_input("What topic",placeholder="eg.Groq")
    if parser == "String parser":
            prompt = ChatPromptTemplate.from_messages([
                ("system","You are a helpful assistant."),
                ("human","Explain the {topic} in three lines")
            ])
            chain = prompt | llm | StrOutputParser()
            if st.button("Run Prompt"):
                  if topic:
                    with st.spinner("Thinking..."):
                        result = chain.invoke({"topic":topic})
                        st.success(result)
                        st.code(type(result).__name__)  # shows → str

    elif parser == "Json Parser":

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Always respond in valid JSON only. No extra text."),
            ("human", "Give me 3 facts about {topic} as JSON like: {{\"facts\": [\"fact1\", \"fact2\", \"fact3\"]}}")
        ])

        chain = prompt | llm | JsonOutputParser()

        if st.button("Run Prompt"):
            if topic:
                with st.spinner("Thinking..."):
                    result = chain.invoke({"topic": topic})
                    st.json(result)         # renders as JSON!
                    st.code(type(result).__name__) 