# AI-Grammar-Punctuation-Checker
A sleek, smart grammar and punctuation correction tool powered by Gemini API, with login/signup features, elegant UI, and a history feature (under development). Just input incorrect sentences—get polished corrections instantly! ✅🔤

---

# 📝 AI Grammar & Punctuation Checker – Flask + Gemini API

This project is a **smart grammar and punctuation correction app** built using **Python Flask**, styled with a **modern HTML/CSS interface**, and powered by **Google's Gemini API**. The user only needs to enter incorrect text—corrections are instantly displayed!

---

## 🚀 Features

- ✨ **Flask-powered Web App**
- 🎨 **Aesthetic HTML/CSS UI**
- 🤖 **Gemini API** used with a **predefined grammar-correction prompt**
- 🔐 **Signup & Login** functionality (stored using SQLite)
- 📜 **User credential history** stored in the backend
- ⏳ **Chat history feature under development**

---

## 🔧 Installation & Setup

### 1. Clone the Repository
bash
git clone https://github.com/your-username/grammar-checker.git
cd grammar-checker


### 2. Install Required Packages
pip install flask
pip install google-generativeai


### 3. Setup Gemini API
Visit Gemini API (Google AI) to get your API key.
Ensure you check the version of the API you're using.
In your main Python file, configure it like this:
import google.generativeai as genai  
genai.configure(api_key="YOUR_API_KEY")

---

## 💻 Usage
Run the Flask app: python app.py
Open your browser at http://localhost:5000
Sign up or log in.
Enter your grammatically incorrect sentence.
The corrected sentence will appear in the output box!

---

## ✅ Coming Soon
🔄 Per-user correction history logs
📥 Downloadable history reports
🎙️ (Optional) Voice input
