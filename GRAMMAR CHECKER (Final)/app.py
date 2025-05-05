from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import sqlite3
import os
import csv
import google.generativeai as genai
from datetime import datetime

app = Flask(__name__, template_folder='web', static_folder='web')
app.secret_key = 'your_secret_key' 

genai.configure(api_key='AIzaSyBlk-AzukxmjqorlZD-q18Jq-A-bfmeHqQ')
model = genai.GenerativeModel("gemini-2.0-flash")

def init_db():
    if not os.path.exists('users.db'):
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            conn.commit()
            print("✅ users.db created successfully.")

    

init_db()

# Signup 
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  

        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                flash("Signup successful! Please login.", "success")
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash("Username already exists", "error")
                return redirect(url_for('signup'))

    return render_template('signup.html')

# Login 
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  

        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = cursor.fetchone()

        if user:
            session['username'] = username
            return redirect(url_for('chat_page'))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

# Logout 
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Chat Page Route
@app.route('/chat')
def chat_page():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

# GRAMMAR CHECKING PROMPT (PREDEFINED)
@app.route('/check_grammar', methods=['POST'])
def check_grammar():
    if 'username' not in session:
        return jsonify({'response': 'Error: Not logged in'})

    try:
        data = request.json
        user_text = data.get('user_text')
        prompt = f"Correct the grammar, punctuation, and spelling of the following text. Return only the corrected version:\n\n{user_text}"

        response = model.generate_content(prompt).text if model.generate_content(prompt).text else "Error generating text."
        
        corrected_text = response.replace("**", "")

        return jsonify({'corrected_text': corrected_text})
    
    except Exception as e:
        return jsonify({'corrected_text': f"Error: {str(e)}"})



    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True, port=5001) 
 

