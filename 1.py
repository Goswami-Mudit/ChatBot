from langchain_openai import ChatOpenAI  
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import streamlit as st

st.title("YOUR PERSONAL CHATBOT🤖")


#openai key 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
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model_name="deepseek/deepseek-r1-0528:free",
    api_key="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",
    temperature=0.7
)

if 'conversation' not in st.session_state:
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory()
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask anything!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.spinner("Thinking..."):
        response = st.session_state.conversation.run(prompt)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
