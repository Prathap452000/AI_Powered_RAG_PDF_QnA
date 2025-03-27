# 📄 PDF Q&A Assistant with Gemini AI

A Streamlit-based application that allows users to upload PDF documents and ask questions about their content using Google's Gemini AI.

## 🌟 Features

- Upload multiple PDF documents
- Extract and process text content
- Ask natural language questions about the documents
- Get AI-powered answers using Gemini 1.5 Flash
- Preserves document context for accurate responses
- Simple and intuitive UI

## 🛠️ Prerequisites

- Python 3.8+
- Google API key (for Gemini AI)
- Git (for cloning the repository)

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/ehtasham/PDF-QnA.git
cd PDF-QnA

### Set Up Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install Dependencies
pip install -r requirements.txt

### Configuration
1. Create a .env file in the project root:
touch .env

### Add your Google API key:
GOOGLE_API_KEY="your_api_key_here"

### Running the Application
streamlit run app.py
