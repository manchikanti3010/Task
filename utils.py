from PyPDF2 import PdfReader
import google.generativeai as genai
import os
import re
import json
from datetime import datetime
from dotenv import load_dotenv
import streamlit as st

# Load Google API key from multiple sources
load_dotenv()

# Try to get API key from Streamlit secrets first (for deployment)
try:
    google_api_key = st.secrets.get("GOOGLE_API_KEY", None)
except:
    google_api_key = None

# Fall back to environment variable if not in secrets
if not google_api_key:
    google_api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API with error handling
try:
    if google_api_key:
        genai.configure(api_key=google_api_key)
        # Initialize Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        # Test the connection
        test_response = model.generate_content("Hello")
        API_AVAILABLE = True
    else:
        API_AVAILABLE = False
        model = None
except Exception as e:
    print(f"Warning: Gemini API not available: {e}")
    API_AVAILABLE = False
    model = None

def process_document(uploaded_file):
    """Extract text from uploaded PDF or TXT file"""
    try:
        text = ""
        if uploaded_file.type == "application/pdf":
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text() or ""
        else:
            text = str(uploaded_file.read(), "utf-8", errors="replace")
        return text
    except Exception as e:
        return f"Failed to read document: {str(e)}"

def generate_summary(text, max_words=150):
    """Summarize the document using Gemini"""
    if not API_AVAILABLE:
        return "API not available. Please check your Google API key configuration in Streamlit Cloud secrets."
    
    try:
        text = re.sub(r"\s+", " ", text).strip()
        
        # Split text into chunks if it's too long
        if len(text) > 30000:  # Gemini has a context limit
            chunks = [text[i:i+30000] for i in range(0, len(text), 30000)]
            summaries = []
            
            for chunk in chunks[:3]:  # Limit to first 3 chunks
                prompt = f"Summarize the following text in approximately {max_words} words:\n\n{chunk}"
                response = model.generate_content(prompt)
                summaries.append(response.text)
            
            return "\n\n".join(summaries)
        else:
            prompt = f"Summarize the following text in approximately {max_words} words:\n\n{text}"
            response = model.generate_content(prompt)
            return response.text
    except Exception as e:
        return f"Summary error: {str(e)}"

def answer_question(text, question):
    """Use Gemini to answer a question or evaluate an answer"""
    if not API_AVAILABLE:
        return "API not available. Please check your Google API key configuration in Streamlit Cloud secrets."
    
    try:
        context = re.sub(r"\s+", " ", text).strip()
        
        # Limit context length to avoid token limits
        if len(context) > 30000:
            context = context[:30000]
        
        prompt = (
            f"You are a helpful research assistant. Use the following document to answer the question.\n\n"
            f"Document:\n{context}\n\n"
            f"Question: {question}\n\n"
            f"Please provide a clear and accurate answer based on the document content."
        )

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Answer error: {str(e)}"

def generate_questions(text, num_questions=3):
    """Generate questions using Gemini"""
    if not API_AVAILABLE:
        return [
            "What is the primary goal of the document?",
            "What technologies or methods are discussed?",
            "What are the main findings or recommendations?"
        ]
    
    try:
        context = re.sub(r"\s+", " ", text).strip()
        
        if len(context) > 30000:
            context = context[:30000]
        
        prompt = (
            f"Based on the following document, generate {num_questions} thoughtful questions that would help someone understand the key concepts and main points.\n\n"
            f"Document:\n{context}\n\n"
            f"Generate {num_questions} questions:"
        )
        
        response = model.generate_content(prompt)
        questions_text = response.text
        
        # Extract questions from the response
        questions = []
        lines = questions_text.split('\n')
        for line in lines:
            line = line.strip()
            if line and (line.startswith(str(num_questions)) or line.startswith('•') or line.startswith('-') or line.startswith('1.') or line.startswith('2.') or line.startswith('3.')):
                # Clean up the question
                question = re.sub(r'^\d+\.\s*', '', line)
                question = re.sub(r'^[•\-]\s*', '', question)
                if question and len(question) > 10:
                    questions.append(question)
        
        # If we couldn't parse questions properly, return default ones
        if len(questions) < num_questions:
            return [
                "What is the primary goal or main topic of this document?",
                "What are the key findings or conclusions presented?",
                "What methodologies or approaches are discussed in the document?"
            ]
        
        return questions[:num_questions]
    except Exception as e:
        # Fallback to static questions if Gemini fails
        return [
            "What is the primary goal of the document?",
            "What technologies or methods are discussed?",
            "What are the main findings or recommendations?"
        ]

def extract_key_points(text):
    """Extract key points and insights from the document"""
    if not API_AVAILABLE:
        return ["API not available. Please check your Google API key configuration in Streamlit Cloud secrets."]
    
    try:
        context = re.sub(r"\s+", " ", text).strip()
        if len(context) > 30000:
            context = context[:30000]
        
        prompt = (
            f"Extract 5-7 key points from the following document. Format as a bulleted list:\n\n{context}"
        )
        
        response = model.generate_content(prompt)
        return response.text.split('\n')
    except Exception as e:
        return [f"Error extracting key points: {str(e)}"]

def generate_insights(text):
    """Generate insights and analysis from the document"""
    if not API_AVAILABLE:
        return "API not available. Please check your Google API key configuration in Streamlit Cloud secrets."
    
    try:
        context = re.sub(r"\s+", " ", text).strip()
        if len(context) > 30000:
            context = context[:30000]
        
        prompt = (
            f"Analyze the following document and provide 3-4 insights about:\n"
            f"1. Main themes and patterns\n"
            f"2. Potential implications\n"
            f"3. Areas for further research\n\n"
            f"Document:\n{context}"
        )
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating insights: {str(e)}"

def save_session_data(session_data, filename="session_data.json"):
    """Save session data to a JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(session_data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving session data: {e}")
        return False

def load_session_data(filename="session_data.json"):
    """Load session data from a JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error loading session data: {e}")
        return {}