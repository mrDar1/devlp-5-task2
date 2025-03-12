from flask import Flask, render_template, request
from datetime import datetime
import json

app = Flask(__name__, template_folder='.')

# JSON file to store chat
chats_file = 'chats.json'

# Load JSON file or initialize empty JSON
def load_chats():
    try:
        with open(chats_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_chats(chats):
    with open(chats_file, 'w') as file:
        json.dump(chats, file)

# Initialize chats variable from file
chats = load_chats()

# Implemented by Dor
@app.route('/', methods=['GET'])
def serve_html():
    # Serve the HTML file
    return render_template('index.html')

# Implemented by Dor
@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    # Return chat for the room or an empty string if no messages exist
    return "\n".join(chats.get(room, []))



# Implemented by Dar
@app.route('/<room>', methods=['GET'])
def get_room(room):
    # Serve the HTML file
    return render_template('index.html')

# Implemented by Dar
@app.route('/api/chat/<room>', methods=['POST'])
def post_chat(room):
    username = request.form.get('username')
    msg = request.form.get('msg')

    if not username or not msg:
        return "miss username or message", 200

    if room not in chats:
        chats[room] = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    chats[room].append(f"[{timestamp}] {username}: {msg}")
    save_chats(chats)  # Save to JSON file

    return "success", 200  # Returning plain string

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)