# Nullclass_DataScience_Internship

*📌 Streamlit AI Applications*

This repository contains three AI-powered Streamlit applications that utilize Google Gemini AI models to process text and images in different ways. Each application serves a unique purpose, leveraging natural language processing (NLP) and computer vision capabilities.

📜 Project Overview

Application	Description	Model Used
🗨️ Sentiment-Aware Chatbot	A chatbot that analyzes user sentiment and responds accordingly.	gemini-1.5-pro
📝 AI Article Generator	Compares responses from three different Gemini LLMs and lets users choose the best output.	gemini-1.5-pro, gemini-2.0-pro-exp, gemini-1.5-flash-latest
📷 Gemini Vision Bot	Analyzes images and text input to generate responses based on visual and textual context.	gemini-1.5-flash

🛠 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Ananyaa-Perumalsamy/Nullclass_DataScience_Internship

cd https://github.com/Ananyaa-Perumalsamy/Nullclass_DataScience_Internship

2️⃣ Create a Virtual Environment

python -m venv env

source env/bin/activate  # On macOS/Linux

env\Scripts\activate     # On Windows


3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Set Up API Key

Create a .env file in the project directory and add your Google API key:

GOOGLE_API_KEY=your_google_api_key


🚀 Running the Applications

Sentiment-Aware Chatbot

streamlit run sentiment_chatbot.py

Analyzes user input and responds based on sentiment (positive, negative, neutral).

Stores chat history and allows multiple conversations.


AI Article Generator

streamlit run article_generator.py

Compares responses from three Gemini models and allows users to select the best one.

Adjusts model preference based on user selection.

Image Recognition Bot

streamlit run image.py

Accepts text and image inputs.

Uses Gemini AI to analyze images and generate responses.

📦 File Structure

📁 Streamlit-AI-Apps/

│── sentiment_chatbot.py   # Sentiment analysis chatbot

│── article_generator.py   # AI article generator & model comparison

│── gemini_vision.py       # Text + Image processing bot

│── requirements.txt       # Required Python dependencies

│── .env                   # API Key (not included in repo)

│── README.md              # Project documentation


📌 Requirements.txt

streamlit

python-dotenv

google-generativeai

Pillow

💡 Future Enhancements

🔹 Improve UI with custom styling and animations.

🔹 Expand chatbot multi-turn memory for better conversations.

🔹 Add fine-tuning options for LLMs in article generation.

🔹 Implement real-time speech-to-text for vision bot.


🙌 Contributors
👤 Ananyaa P – AI/ML Developer

Feel free to contribute by opening a pull request or raising an issue! 🚀
