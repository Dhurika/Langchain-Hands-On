# 🦜 LangChain Mastery — Learn by Building

A hands-on LangChain learning project built with **Streamlit + Groq**, covering everything from basic chains to RAG and Agents. Each module teaches one core concept with a working interactive demo.

---

## 🚀 Tech Stack

- **LangChain v1.2** — AI framework
- **Groq** — Free, fast LLM inference (`llama-3.1-8b-instant`)
- **Streamlit** — UI
- **Python 3.10+**

---

## 📦 Setup

### 1. Clone the repo
```bash
git clone https://github.com/Dhurika/Langchain-Hands-On.git
cd Langchain-Hands-On
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key
Create a `.env` file in the root:
```
GROQ_API_KEY=your_key_here
```
Get your free key at → https://console.groq.com

### 5. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
langchain-hands-on/
├── app.py                  # Streamlit navigation shell
├── modules/
│   ├── __init__.py
│   ├── hello_chain.py      # Module 1
│   ├── prompt_engineer.py  # Module 2
│   ├── output_parser.py    # Module 3
│   ├── memory_chat.py      # Module 4
│   ├── rag.py              # Module 5 (coming soon)
│   └── agent.py            # Module 6 (coming soon)
├── requirements.txt
└── .env                    # never commit this!
```

---

## 🧠 Modules

### ✅ Module 1 — Hello Chain
> **Concepts:** `PromptTemplate`, `ChatGroq`, LCEL `|` pipe operator

The absolute basics. Learn how to connect a prompt to an LLM using the pipe operator.

```python
chain = prompt | llm
result = chain.invoke({"topic": "neural networks"})
```

---

### ✅ Module 2 — Prompt Engineer
> **Concepts:** `ChatPromptTemplate`, system messages, human messages, dynamic personas

Learn the difference between `PromptTemplate` and `ChatPromptTemplate`. Control the AI's personality with system messages.

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "{persona}"),
    ("human", "Explain {topic} in 4 lines.")
])
```

---

### ✅ Module 3 — Output Parsers
> **Concepts:** `StrOutputParser`, `JsonOutputParser`

Stop doing `result.content` manually. Parsers clean up the LLM output into usable Python types.

```python
# plain string
chain = prompt | llm | StrOutputParser()

# python dict
chain = prompt | llm | JsonOutputParser()
```

---

### ✅ Module 4 — Memory Chat
> **Concepts:** `MessagesPlaceholder`, `HumanMessage`, `AIMessage`, `st.session_state`

Build a chatbot that actually remembers what you said. Learn how chat history is passed to the LLM on every turn.

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("placeholder", "{history}"),
    ("human", "{user_input}")
])

chain.invoke({
    "history": st.session_state.history,
    "user_input": user_msg
})
```

---

### 🔜 Module 5 — RAG (Doc Q&A)
> **Concepts:** `FAISS`, embeddings, `RetrievalQA`

Upload a document and ask questions about it. Learn how to turn text into vectors and retrieve relevant chunks.

```python
# coming soon
retriever = vectorstore.as_retriever()
chain = retriever | prompt | llm | StrOutputParser()
```

---

### 🔜 Module 6 — Agent
> **Concepts:** `initialize_agent`, tools, calculator, search

Give the LLM tools it can use to take actions — search the web, run calculations, and more.

```python
# coming soon
agent = initialize_agent(tools=[search, calculator], llm=llm)
agent.invoke({"input": "What is 100th fibonacci number?"})
```

---

## 🔗 The LCEL Pipeline

As you progress through modules, your chain grows:

```
Module 1:  prompt | llm
Module 2:  prompt | llm                        (with system messages)
Module 3:  prompt | llm | parser
Module 4:  prompt | llm | parser               (with memory)
Module 5:  retriever | prompt | llm | parser
Module 6:  agent with tools
```

---

## 📋 Requirements

```txt
streamlit
langchain
langchain-core
langchain-groq
langchain-community
python-dotenv
```

---

## ⚠️ Notes

- Never commit your `.env` file — add it to `.gitignore`
- This project uses **LangChain v1.2+** — older tutorials may use deprecated APIs like `LLMChain`
- Use `llama-3.1-8b-instant` or `llama-3.3-70b-versatile` on Groq

---

## 🙌 Author

Built while learning LangChain from scratch — one module at a time.
