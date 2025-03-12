from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

# Dictionary to store chat
chats = {}

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

