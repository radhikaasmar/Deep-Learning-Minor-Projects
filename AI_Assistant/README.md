# AI Personal Assistant

A simple web application built with Flask that serves as an AI-powered personal assistant. It uses OpenAI's API to answer questions and summarize emails.

## Features

- **Ask Anything**: Get answers to your questions from an AI assistant
- **Email Summarization**: Paste an email and get a concise 2-3 sentence summary

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  
   # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install flask python-dotenv openai
   ```
4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
2. Run the application:
   ```bash
   python main.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000/`

## Requirements

- Python 3.7+
- OpenAI API key
- Flask
- python-dotenv
- openai

## Project Structure

```
AIAssistant/
├── main.py              # Flask application
├── static/
│   └── style.css        # CSS styles
├── templates/
│   └── index.html       # Main HTML template
├── .env                 # Environment variables (not in repo)
└── README.md           # This file
```