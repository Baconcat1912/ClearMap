from flask import Flask, request, jsonify, render_template
from temporary_suck_api import get_ai_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    ai_response = get_ai_response(user_message)
    return jsonify({'reply': ai_response})

if __name__ == '__main__':
    app.run(debug=True)
