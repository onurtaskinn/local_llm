# Local LLM Chat App

A simple chat application that lets you interact with local LLM models using Streamlit and Ollama.

## Features

- Chat interface built with Streamlit
- Support for multiple models (llama3.2, mistral, codellama)
- Two versions available:
  - Basic version with standard responses
  - Streaming version with real-time response generation
- Adjustable temperature settings (in streaming version)
- Message history tracking

## Prerequisites

- Python 3.x
- Ollama installed on your system

## Installation

1. Clone the repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the App

Choose which version you want to run:

For basic version:
```bash
streamlit run app_basic.py
```

For streaming version:
```bash
streamlit run app_streaming.py
```

## Usage

1. Select your preferred model from the sidebar
2. Adjust temperature (streaming version only)
3. Type your message in the chat input
4. View the AI's response in real-time

## Project Structure

- `app_basic.py`: Standard chat implementation
- `app_streaming.py`: Real-time streaming implementation
- `requirements.txt`: Required Python packages

## Dependencies

- streamlit
- ollama
- requests