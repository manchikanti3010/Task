"""
Test script to validate the AI Research Assistant setup
"""
import os
import sys
from dotenv import load_dotenv

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing imports...")
    
    try:
        import streamlit
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ Google Generative AI imported successfully")
    except ImportError as e:
        print(f"❌ Google Generative AI import failed: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ Pandas imported successfully")
    except ImportError as e:
        print(f"❌ Pandas import failed: {e}")
        return False
    
    try:
        import plotly.express as px
        print("✅ Plotly imported successfully")
    except ImportError as e:
        print(f"❌ Plotly import failed: {e}")
        return False
    
    try:
        from PyPDF2 import PdfReader
        print("✅ PyPDF2 imported successfully")
    except ImportError as e:
        print(f"❌ PyPDF2 import failed: {e}")
        return False
    
    return True

def test_config():
    """Test configuration loading"""
    print("\nTesting configuration...")
    
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    
    if google_api_key:
        print("✅ Google API key found")
        return True
    else:
        print("❌ Google API key not found. Please set GOOGLE_API_KEY in your .env file")
        return False

def test_gemini_api():
    """Test Gemini API connection"""
    print("\nTesting Gemini API...")
    
    try:
        import google.generativeai as genai
        from dotenv import load_dotenv
        
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            print("❌ No API key found")
            return False
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Test with a simple prompt
        response = model.generate_content("Hello, this is a test.")
        
        if response.text:
            print("✅ Gemini API connection successful")
            return True
        else:
            print("❌ Gemini API returned empty response")
            return False
            
    except Exception as e:
        print(f"❌ Gemini API test failed: {e}")
        return False

def test_utils():
    """Test utility functions"""
    print("\nTesting utility functions...")
    
    try:
        from utils import process_document, generate_summary, answer_question
        
        # Test with sample text
        sample_text = "This is a sample document for testing purposes. It contains some basic information."
        
        # Test summary generation
        summary = generate_summary(sample_text)
        if summary and "API not available" not in summary:
            print("✅ Summary generation working")
        else:
            print("⚠️ Summary generation returned API unavailable message")
        
        # Test question answering
        answer = answer_question(sample_text, "What is this document about?")
        if answer and "API not available" not in answer:
            print("✅ Question answering working")
        else:
            print("⚠️ Question answering returned API unavailable message")
        
        return True
        
    except Exception as e:
        print(f"❌ Utility functions test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧠 AI Research Assistant - Setup Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_config,
        test_gemini_api,
        test_utils
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nTo run the application:")
        print("streamlit run app.py")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
        
        if passed < 2:
            print("\n💡 Troubleshooting tips:")
            print("1. Install missing packages: pip install -r requirements.txt")
            print("2. Set up your .env file with GOOGLE_API_KEY")
            print("3. Get your API key from: https://makersuite.google.com/app/apikey")

if __name__ == "__main__":
    main() 