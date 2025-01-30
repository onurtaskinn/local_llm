import streamlit as st
import ollama

def get_streaming_response(messages, model, temperature):
    try:
        return ollama.chat(
            model=model,
            messages=messages,
            stream=True,
            options={"temperature": temperature}
        )
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def main():
    st.title("Local LLM Chat App")
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    model = st.sidebar.selectbox("Select Model", ["llama3.2:latest", "mistral", "codellama"])
    temperature = st.sidebar.slider("Temperature", 0.0, 2.0, 0.7, 0.1)
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    if prompt := st.chat_input("What would you like to know?"):

        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            response_text = ""
            
            stream = get_streaming_response(st.session_state.messages, model, temperature)
            if stream:
                for chunk in stream:
                    if chunk.message:
                        response_text += chunk.message.content
                        response_placeholder.markdown(response_text)
                
                st.session_state.messages.append({"role": "assistant", "content": response_text})

if __name__ == "__main__":
    main()