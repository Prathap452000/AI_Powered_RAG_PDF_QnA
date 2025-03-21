import streamlit as st
import google.generativeai as genai
import os
import tempfile
from PyPDF2 import PdfReader
import textwrap

# Configure Google API key directly in the code
# Replace this with your actual API key
GOOGLE_API_KEY = "Enter your Google API key here"
genai.configure(api_key=GOOGLE_API_KEY)

# Page configuration
st.set_page_config(page_title="PDF Q&A Assistant", layout="wide")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to split text into chunks
def split_text(text, chunk_size=10000):
    return textwrap.wrap(text, chunk_size)

# Function to get response from Gemini
def get_gemini_response(query, context):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""You are a helpful assistant that answers questions based on the provided document. 
    Use only the information in the document to answer the question.
    If the answer is not in the document, say "I don't have enough information to answer this question."
    
    Document: {context}
    
    Question: {query}
    
    Answer:"""
    
    response = model.generate_content(prompt)
    return response.text

# Main application
def main():
    st.title("📄 PDF Document Q&A System")
    
    # Information sidebar
    with st.sidebar:
        st.header("How to use")
        st.markdown("""
        1. Upload one or more PDF files
        2. Ask questions about the content
        3. Get answers from the AI-powered model
        """)
    
    # File upload
    uploaded_files = st.file_uploader("Upload PDF documents", type=["pdf"], accept_multiple_files=True)
    
    if uploaded_files:
        # Extract and store documents
        all_documents = {}
        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
                temp_path = temp_file.name
            
            document_text = extract_text_from_pdf(temp_path)
            all_documents[uploaded_file.name] = document_text
            os.unlink(temp_path)  # Remove temp file
        
        st.success(f"✅ Successfully processed {len(all_documents)} documents")
        
        # Combine all documents text
        full_text = " ".join(all_documents.values())
        
        # Process document text
        text_chunks = split_text(full_text)
        
        # Display document info
        with st.expander("Document Information"):
            st.write(f"Total character count: {len(full_text)}")
            st.write(f"Documents loaded:")
            for doc_name in all_documents.keys():
                st.write(f"- {doc_name}")
        
        # Query interface
        st.markdown("### Ask a question about your documents")
        query = st.text_input("Enter your question:")
        
        if query:
            with st.spinner("Generating response..."):
                response = get_gemini_response(query, full_text[:100000])  # Limiting context size
                
                st.markdown("### Answer")
                st.markdown(response)

if __name__ == "__main__":
    main()