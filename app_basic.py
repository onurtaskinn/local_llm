import streamlit as st
import ollama
from typing import List, Dict

def generate_response(messages: List[Dict[str, str]], model: str = "llama3.2:latest") -> str:
    try:
        response = ollama.chat(
            model=model,
            messages=messages,
            stream=False
        )
        return response.message.content
    except ollama.ResponseError as e:
        return f"Error: {str(e)}"

def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def main():
    st.title("Local LLM Chat App")
    
    initialize_session_state()
    
    model = st.sidebar.selectbox(
        "Select Model",
        ["llama3.2:latest", "mistral", "codellama"]  
        
    )
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    if prompt := st.chat_input("What would you like to know?"):
    
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.write(prompt)
                
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(st.session_state.messages, model)
                st.write(response)
                    
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()