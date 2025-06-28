# 🧠 AI Research Assistant Pro

A professional-grade research assistant powered by Google's Gemini AI that helps you analyze documents, generate summaries, answer questions, and test your understanding with interactive features.

## ✨ Features

### 📄 Document Analysis
- **Smart Summarization**: AI-powered document summaries with customizable length
- **Key Points Extraction**: Automatically identify and extract main points from documents
- **AI Insights**: Generate analytical insights about themes, patterns, and implications
- **Document Metrics**: Character count, word count, sentence analysis

### 💬 Interactive Q&A
- **Natural Language Questions**: Ask any question about your uploaded documents
- **Context-Aware Answers**: AI provides accurate answers based on document content
- **Session History**: Track your Q&A sessions with timestamps
- **Export Capabilities**: Save your conversations for later reference

### 🎯 Challenge Mode
- **AI-Generated Questions**: Test your understanding with intelligent questions
- **Real-time Feedback**: Get detailed feedback and scoring on your answers
- **Learning Analytics**: Track your performance and progress
- **Interactive Evaluation**: Receive constructive feedback with scores

### 📊 Analytics Dashboard
- **Usage Analytics**: Track documents processed, questions asked, and session data
- **Performance Metrics**: Monitor application uptime and usage patterns
- **Data Visualization**: Interactive charts and graphs
- **Export Options**: Download analytics data in multiple formats

### 🔧 Professional Features
- **Session Management**: Persistent session data across browser sessions
- **Data Export**: Export results in JSON and CSV formats
- **Error Handling**: Robust error handling with graceful fallbacks
- **Responsive Design**: Modern, professional UI with custom styling
- **Configuration Management**: Centralized settings and configuration

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.7 or higher
- Google Generative AI API key (free tier available)

### 2. Installation

```bash
# Clone or download the project
cd research-assistant

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your Google API key
```

### 3. Get Google API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

### 4. Configure Environment

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Test Setup

```bash
python test_setup.py
```

### 6. Run Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 📖 Usage Guide

### Document Analysis
1. Navigate to "📄 Document Analysis" in the sidebar
2. Upload a PDF or TXT document
3. Click "Generate Summary" to get an AI summary
4. Use "Extract Key Points" to identify main concepts
5. Generate "AI Insights" for deeper analysis

### Interactive Q&A
1. Upload a document first in Document Analysis
2. Switch to "💬 Interactive Q&A" mode
3. Type your question in the text input
4. Click "Get Answer" to receive AI-generated responses
5. View your session history in the expandable sections

### Challenge Mode
1. Upload a document and switch to "🎯 Challenge Mode"
2. Click "Generate Challenge Questions" to create test questions
3. Answer each question in the provided text areas
4. Click "Evaluate Answer" to get feedback and scoring
5. Review your performance and learn from feedback

### Analytics Dashboard
1. Use "📊 Analytics Dashboard" to view usage statistics
2. Monitor your activity with interactive charts
3. Export your data using the sidebar export options
4. Track your learning progress over time

## 🛠️ Technical Details

### Architecture
- **Frontend**: Streamlit with custom CSS styling
- **AI Backend**: Google Gemini 1.5 Flash API
- **Data Processing**: Pandas for data manipulation
- **Visualization**: Plotly for interactive charts
- **Document Processing**: PyPDF2 for PDF parsing

### API Usage
- Uses Google's Gemini 1.5 Flash model
- Free tier includes generous usage limits
- Automatic text chunking for large documents
- Error handling with graceful fallbacks

### File Structure
```
research-assistant/
├── app.py              # Main Streamlit application
├── utils.py            # Core utility functions
├── config.py           # Configuration settings
├── test_setup.py       # Setup validation script
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .env               # Environment variables (create this)
```

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google Generative AI API key

### Customization
Edit `config.py` to modify:
- API model selection
- Text processing limits
- UI settings
- Error messages
- Prompt templates

## 📊 Performance

### API Limits
- Gemini 1.5 Flash: Up to 1M tokens context window
- Free tier: 15 requests per minute
- Automatic rate limiting and retry logic

### Optimization
- Text chunking for large documents
- Caching of generated content
- Efficient session state management
- Minimal API calls through smart prompting

## 🐛 Troubleshooting

### Common Issues

**API Key Not Found**
```
❌ Google API key not found. Please set GOOGLE_API_KEY in your .env file
```
Solution: Ensure your `.env` file exists and contains the correct API key.

**Import Errors**
```
❌ Google Generative AI import failed
```
Solution: Run `pip install -r requirements.txt` to install all dependencies.

**API Connection Failed**
```
❌ Gemini API test failed
```
Solution: Check your internet connection and API key validity.

### Testing Your Setup
Run the test script to validate your installation:
```bash
python test_setup.py
```

## 📈 Future Enhancements

- [ ] Multi-language support
- [ ] Document comparison features
- [ ] Advanced analytics and reporting
- [ ] Integration with cloud storage
- [ ] Collaborative features
- [ ] Mobile-responsive design
- [ ] API rate limiting dashboard
- [ ] Custom model fine-tuning

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Google for providing the Gemini AI API
- Streamlit for the excellent web framework
- The open-source community for various dependencies

---

**Need Help?** Check the troubleshooting section or run `python test_setup.py` to diagnose issues.
