# query-pdf

# PDF Query App

This is a simple Python application that allows you to upload a PDF document and ask questions about its content. The application utilizes OpenAI's GPT-3 for question answering. It's built using Streamlit and various Python libraries.

## Getting Started

Before running the application, make sure you have the necessary dependencies installed and set up your environment.

### Prerequisites

You'll need the following Python libraries installed:

- `dotenv`: For loading environment variables.
- `openai`: The OpenAI API for question answering.
- `llama_index`: LlamaIndex is a data framework for LLM applications to ingest, structure, and access data.
- `PyPDF2`: For extracting text from PDF documents.
- `streamlit`: A Python web app framework for building user interfaces.

You can install these libraries using `pip`:

```bash
pip install python-dotenv openai llama_index PyPDF2 streamlit
```

### Environment Setup

To use the OpenAI API, you'll need to set your API key in a `.env` file in the same directory as your project. You can obtain an API key from the OpenAI website.

```dotenv
# .env

OPENAI_API_KEY=your_api_key_here
```

## Running the Application

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will start a local development server, and you can access the app in your web browser.

## How to Use

1. Upload a PDF: Use the file uploader to select a PDF document that you want to ask questions about.

2. Ask Questions: Enter your questions in the text input field and click the "Ask" button to get answers.

## Note

This is a basic example of a PDF question answering app. it can also be extended and customized.
