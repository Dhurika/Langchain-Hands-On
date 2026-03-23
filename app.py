import streamlit as st

st.set_page_config(page_title="Langchain learnings",page_icon="🦜")
st.sidebar.title("Langchain Learning")

module = st.sidebar.radio("Choose Module", [
    "01 - Hello Chain",
    "02 - Prompt Engineer",
    "03 - Output Parser",
    "04 - Memory Chat",
    "05 - Study Buddy(A Overall Recall)",
    "06 - RAG (Doc Q&A)",
    "07 - Agent",
])

if module == "01 - Hello Chain":
    from modules import hello_chain
    hello_chain.run()
elif module == "02 - Prompt Engineer":
    from modules import prompt_engineering
    prompt_engineering.run()
elif module == "03 - Output Parser":
    from modules import output_parser
    output_parser.run()
elif module == "04 - Memory Chat":
    from modules import memory_chat
    memory_chat.run()
elif module == "05 - Study Buddy(A Overall Recall)":
    from modules import study_buddy
    study_buddy.run()