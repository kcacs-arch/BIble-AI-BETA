Code
templates
index.html
.gitignore
app.py
replit.md
Packager files
.pythonlibs
requirements.txt
Config files
.replit
Biblical AI Counselor
Overview
A web-based AI counselor application that provides biblical guidance and wisdom using Google's Gemini AI. The application is designed to offer counsel rooted in Scripture and biblical principles.

Project Information
Created by: Three students at Grace Christian Academy (GCA)
Kristians Cacs (AI Architect)
Leo Lopez (Presentation & Validation Specialist)
Nolan Andre (User Experience & Quality Control)
Purpose: Advanced science project for high school biology class
Technology: AI-powered biblical counseling interface
Tech Stack
Python 3.11: Main programming language
Gradio: Web interface framework for the chatbot
Google Gemini AI: AI model (gemini-2.5-flash) for generating responses
google-genai: Python SDK for Google's Gemini API
Project Structure
.
├── app.py              # Main application file
├── templates/          # Flask HTML templates (currently unused after Gradio refactor)
│   └── index.html
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── replit.md          # This documentation file
Environment Variables
GEMINI_API_KEY: Required API key for Google Gemini AI service
Key Features
Biblical counseling based on Scripture
Chat interface powered by Gradio
Integration with Google's Gemini AI
System instruction ensures responses are rooted in the Holy Bible
Running the Application
The application runs on port 5000 and is accessible via the Replit webview.

Command: python app.py

Deployment
Configured for Replit Autoscale deployment with the following settings:

Deployment target: autoscale (stateless web application)
Run command: python app.py
Recent Changes (Oct 17, 2025)
Migrated from Flask+Gradio hybrid to pure Gradio ChatInterface
Fixed port configuration to use port 5000 for Replit compatibility
Renamed template directory to templates for Flask convention (now unused after Gradio migration)
Added .gitignore for Python projects
Configured deployment settings for Replit Autoscale
Added project documentation
Implemented proper conversation history handling using Gradio's messages format
Updated chatbot to use OpenAI-style message dictionaries for better history management
Removed Flask dependency from requirements.txt
User Preferences
None specified yet
