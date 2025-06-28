"""
Configuration settings for the AI Research Assistant
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = "gemini-1.5-flash"

# Application Settings
APP_TITLE = "AI Research Assistant Pro"
APP_ICON = "🧠"
PAGE_LAYOUT = "wide"

# Document Processing
MAX_TEXT_LENGTH = 30000  # Maximum text length for Gemini API
MAX_SUMMARY_WORDS = 150
DEFAULT_NUM_QUESTIONS = 5

# File Types
SUPPORTED_FILE_TYPES = ["pdf", "txt"]

# Analytics
ANALYTICS_FILE = "analytics.json"
SESSION_HISTORY_LIMIT = 5

# Export Settings
EXPORT_FORMATS = ["json", "csv"]

# UI Settings
SIDEBAR_STATE = "expanded"
CHART_HEIGHT = 400

# Error Messages
API_ERROR_MESSAGE = "API not available. Please check your Google API key."
DOCUMENT_ERROR_MESSAGE = "Failed to read document: {}"
SUMMARY_ERROR_MESSAGE = "Summary error: {}"
ANSWER_ERROR_MESSAGE = "Answer error: {}"

# Prompts
SUMMARY_PROMPT = "Summarize the following text in approximately {} words:\n\n{}"
QUESTION_PROMPT = "Based on the following document, generate {} thoughtful questions that would help someone understand the key concepts and main points.\n\nDocument:\n{}\n\nGenerate {} questions:"
ANSWER_PROMPT = "You are a helpful research assistant. Use the following document to answer the question.\n\nDocument:\n{}\n\nQuestion: {}\n\nPlease provide a clear and accurate answer based on the document content."
EVALUATION_PROMPT = "Evaluate this answer based on the document.\n\nQuestion: {}\nUser Answer: {}\n\nProvide constructive feedback and a score out of 10."
KEY_POINTS_PROMPT = "Extract 5-7 key points from the following document. Format as a bulleted list:\n\n{}"
INSIGHTS_PROMPT = "Analyze the following document and provide 3-4 insights about:\n1. Main themes and patterns\n2. Potential implications\n3. Areas for further research\n\nDocument:\n{}" 