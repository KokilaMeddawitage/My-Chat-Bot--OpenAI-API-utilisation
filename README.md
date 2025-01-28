# My Chat Bot - OpenAI API Utilisation

This project is a chatbot application that uses **Flask** as the backend, **Streamlit** as the frontend, and **Google Generative AI (Gemini API)** for generating intelligent responses.

---

## Features

- **Flask Backend**: API server to handle requests and interact with the Gemini API.
- **Streamlit Frontend**: Interactive UI for chatbot interactions.
- **Virtual Environment**: Isolated environment for dependencies.
- **Postman Testing**: Test the backend API.
- **`.gitignore`**: Exclude unnecessary files like `venv/` and `.env`.

---

## Setup and Installation

- **Set up the virtual environement**: python3 -m venv venv
- **Activate the virtual environment**: source venv/bin/activate
- **Install the required Python packages**: pip install -r requirements.txt
- **Configure Environment Variables**: touch .env , GOOGLE_GENAI_API_KEY=your_api_key_here

### Run the Flask Backend

- python app.py
- streamlit run App.py

### Prerequisites

- Python 3.7+
- Git installed on your machine

### Steps

#### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```
