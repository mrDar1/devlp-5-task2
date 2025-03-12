from flask import Flask, render_template
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


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)