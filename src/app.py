import os

from flask import Flask, render_template, request, jsonify
import requests
from flask.cli import load_dotenv

app = Flask(__name__, static_folder='static', template_folder='templates')
load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL")

@app.route('/')
def index():
    return render_template('index.html', backend_url=BACKEND_URL)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('input')
    try:
        response = requests.post(f"{BACKEND_URL}/chatbot", json={"input": question})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)