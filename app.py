import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
from utils import (
    process_document, generate_summary, answer_question, generate_questions,
    extract_key_points, generate_insights, save_session_data, load_session_data
)
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Research Assistant Pro",
    layout="wide",
    initial_sidebar_state="expanded"
)

def initialize_session_state():
    """Initialize session state variables"""
    if 'doc_text' not in st.session_state:
        st.session_state.doc_text = ""
    if 'summary' not in st.session_state:
        st.session_state.summary = ""
    if 'key_points' not in st.session_state:
        st.session_state.key_points = []
    if 'insights' not in st.session_state:
        st.session_state.insights = ""
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []
    if 'feedback' not in st.session_state:
        st.session_state.feedback = []
    if 'session_history' not in st.session_state:
        st.session_state.session_history = []
    if 'analytics' not in st.session_state:
        st.session_state.analytics = {
            'documents_processed': 0,
            'questions_asked': 0,
            'sessions_started': 0,
            'start_time': datetime.now()
        }

def sidebar_analytics():
    """Display analytics in sidebar"""
    st.sidebar.markdown("## Analytics")
    
    # Load analytics from file
    analytics = load_session_data("analytics.json")
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.metric("Documents", analytics.get('documents_processed', 0))
        st.metric("Questions", analytics.get('questions_asked', 0))
    
    with col2:
        st.metric("Sessions", analytics.get('sessions_started', 0))
        if 'start_time' in analytics:
            uptime = datetime.now() - datetime.fromisoformat(analytics['start_time'])
            st.metric("Uptime", f"{uptime.days}d {uptime.seconds//3600}h")

def export_data():
    """Export session data"""
    st.sidebar.markdown("## Export")
    
    if st.sidebar.button("Export Session Data"):
        export_data = {
            'timestamp': datetime.now().isoformat(),
            'document_text': st.session_state.doc_text[:1000] + "..." if len(st.session_state.doc_text) > 1000 else st.session_state.doc_text,
            'summary': st.session_state.summary,
            'key_points': st.session_state.key_points,
            'insights': st.session_state.insights,
            'questions': st.session_state.questions,
            'user_answers': st.session_state.user_answers,
            'feedback': st.session_state.feedback
        }
        
        # Save to JSON
        save_session_data(export_data, f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        # Create CSV for questions and answers
        if st.session_state.questions and st.session_state.user_answers:
            qa_data = []
            for i, (q, a, f) in enumerate(zip(st.session_state.questions, st.session_state.user_answers, st.session_state.feedback)):
                qa_data.append({
                    'Question': q,
                    'User_Answer': a,
                    'Feedback': f
                })
            
            df = pd.DataFrame(qa_data)
            csv = df.to_csv(index=False)
            st.sidebar.download_button(
                label="Download Q&A CSV",
                data=csv,
                file_name=f"qa_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )

def display_document_metrics():
    """Display document analysis metrics"""
    if st.session_state.doc_text:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Characters", len(st.session_state.doc_text))
        with col2:
            st.metric("Words", len(st.session_state.doc_text.split()))
        with col3:
            st.metric("Sentences", len(st.session_state.doc_text.split('.')))
        with col4:
            st.metric("Key Points", len(st.session_state.key_points))

def create_analytics_charts():
    """Create analytics charts"""
    if st.session_state.questions and st.session_state.user_answers:
        # Question complexity analysis
        word_counts = [len(q.split()) for q in st.session_state.questions]
        
        fig = px.bar(
            x=[f"Q{i+1}" for i in range(len(word_counts))],
            y=word_counts,
            title="Question Complexity (Word Count)",
            labels={'x': 'Questions', 'y': 'Word Count'}
        )
        st.plotly_chart(fig, use_container_width=True)

def main():
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header"> AI Research Assistant Pro</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("##  Features")
        feature_mode = st.selectbox(
            "Choose Analysis Mode:",
            ["Document Analysis", "Interactive Q&A", "Challenge Mode", "Analytics Dashboard"]
        )
        
        sidebar_analytics()
        export_data()
    
    # Main content area
    if feature_mode == "Document Analysis":
        document_analysis_page()
    elif feature_mode == "Interactive Q&A":
        interactive_qa_page()
    elif feature_mode == "Challenge Mode":
        challenge_mode_page()
    elif feature_mode == "Analytics Dashboard":
        analytics_dashboard_page()

def document_analysis_page():
    """Document analysis page"""
    st.markdown("## Document Analysis")
    
    uploaded_file = st.file_uploader(
        "Upload a PDF or TXT document",
        type=["pdf", "txt"],
        help="Upload your research document for AI-powered analysis"
    )
    
    if uploaded_file:
        with st.spinner("Processing document..."):
            doc_text = process_document(uploaded_file)
            st.session_state.doc_text = doc_text
            
            # Update analytics
            analytics = load_session_data("analytics.json")
            analytics['documents_processed'] = analytics.get('documents_processed', 0) + 1
            save_session_data(analytics, "analytics.json")
        
        # Display metrics
        display_document_metrics()
        
        # Generate analysis
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Summary")
            if st.button("Generate Summary"):
                with st.spinner("Generating summary..."):
                    summary = generate_summary(doc_text)
                    st.session_state.summary = summary
                st.markdown(f"<div class='feature-box'>{summary}</div>", unsafe_allow_html=True)
            elif st.session_state.summary:
                st.markdown(f"<div class='feature-box'>{st.session_state.summary}</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 🔍 Key Points")
            if st.button("Extract Key Points"):
                with st.spinner("Extracting key points..."):
                    key_points = extract_key_points(doc_text)
                    st.session_state.key_points = key_points
                for point in key_points:
                    st.markdown(f"• {point}")
            elif st.session_state.key_points:
                for point in st.session_state.key_points:
                    st.markdown(f"• {point}")
        
        # Insights section
        st.markdown("### AI Insights")
        if st.button("Generate Insights"):
            with st.spinner("Generating insights..."):
                insights = generate_insights(doc_text)
                st.session_state.insights = insights
            st.markdown(f"<div class='feature-box'>{insights}</div>", unsafe_allow_html=True)
        elif st.session_state.insights:
            st.markdown(f"<div class='feature-box'>{st.session_state.insights}</div>", unsafe_allow_html=True)

def interactive_qa_page():
    """Interactive Q&A page"""
    st.markdown("## Interactive Q&A")
    
    if not st.session_state.doc_text:
        st.warning("Please upload a document first in the Document Analysis section.")
        return
    
    st.markdown("Ask any question about your document:")
    
    # Question input
    question = st.text_input("Your question:", placeholder="e.g., What are the main findings?")
    
    if question:
        if st.button("Get Answer"):
            with st.spinner("Generating answer..."):
                answer = answer_question(st.session_state.doc_text, question)
                
                # Update analytics
                analytics = load_session_data("analytics.json")
                analytics['questions_asked'] = analytics.get('questions_asked', 0) + 1
                save_session_data(analytics, "analytics.json")
                
                # Save to history
                st.session_state.session_history.append({
                    'timestamp': datetime.now().isoformat(),
                    'question': question,
                    'answer': answer
                })
            
            st.markdown("### Answer:")
            st.markdown(f"<div class='feature-box'>{answer}</div>", unsafe_allow_html=True)
    
    # Session history
    if st.session_state.session_history:
        st.markdown("###  Session History")
        for i, entry in enumerate(reversed(st.session_state.session_history[-5:])):  # Show last 5
            with st.expander(f"Q: {entry['question'][:50]}..."):
                st.write(f"**Question:** {entry['question']}")
                st.write(f"**Answer:** {entry['answer']}")
                st.caption(f"Asked at: {entry['timestamp']}")

def challenge_mode_page():
    """Challenge mode page"""
    st.markdown("##  Challenge Mode")
    
    if not st.session_state.doc_text:
        st.warning("Please upload a document first in the Document Analysis section.")
        return
    
    # Generate questions if not already done
    if not st.session_state.questions:
        if st.button("Generate Challenge Questions"):
            with st.spinner("Generating questions..."):
                questions = generate_questions(st.session_state.doc_text, 5)
                st.session_state.questions = questions
                st.session_state.user_answers = [""] * len(questions)
                st.session_state.feedback = [""] * len(questions)
    
    # Display questions and answers
    if st.session_state.questions:
        st.markdown("### Test Your Understanding")
        
        for i, question in enumerate(st.session_state.questions):
            st.markdown(f"**Question {i+1}:** {question}")
            
            # Answer input
            st.session_state.user_answers[i] = st.text_area(
                f"Your answer {i+1}",
                value=st.session_state.user_answers[i],
                height=100
            )
            
            # Evaluate button
            if st.button(f"Evaluate Answer {i+1}"):
                if st.session_state.user_answers[i].strip():
                    with st.spinner("Evaluating..."):
                        eval_prompt = (
                            f"Evaluate this answer based on the document.\n\n"
                            f"Question: {question}\n"
                            f"User Answer: {st.session_state.user_answers[i]}\n\n"
                            f"Provide constructive feedback and a score out of 10."
                        )
                        feedback = answer_question(st.session_state.doc_text, eval_prompt)
                        st.session_state.feedback[i] = feedback
                
                if st.session_state.feedback[i]:
                    st.markdown("**Feedback:**")
                    st.markdown(f"<div class='feature-box'>{st.session_state.feedback[i]}</div>", unsafe_allow_html=True)

def analytics_dashboard_page():
    """Analytics dashboard page"""
    st.markdown("## Analytics Dashboard")
    
    # Load analytics
    analytics = load_session_data("analytics.json")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Documents", analytics.get('documents_processed', 0))
    with col2:
        st.metric("Questions Asked", analytics.get('questions_asked', 0))
    with col3:
        st.metric("Sessions Started", analytics.get('sessions_started', 0))
    with col4:
        if 'start_time' in analytics:
            uptime = datetime.now() - datetime.fromisoformat(analytics['start_time'])
            st.metric("Uptime", f"{uptime.days}d {uptime.seconds//3600}h")
    
    # Charts
    if st.session_state.questions:
        create_analytics_charts()
    
    # Session history table
    if st.session_state.session_history:
        st.markdown("### Recent Q&A Sessions")
        df = pd.DataFrame(st.session_state.session_history)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        st.dataframe(df[['timestamp', 'question']].tail(10))

if __name__ == "__main__":
    main()
