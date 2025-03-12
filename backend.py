from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder='.')

# Database settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://your_mysql_user:your_mysql_password@db/chat_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define DB
class Chat(db.Model):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Serve the static HTML
@app.route('/', methods=['GET'])
def serve_root_html():
    return render_template('index.html')

@app.route('/<room>', methods=['GET'])
def serve_html(room):
    return render_template('index.html')

# POST API to add a message
@app.route('/api/chat/<room>', methods=['POST'])
def post_message(room):
    username = request.form.get('username')
    message = request.form.get('msg')

    if not username or not message:
        return "Username and message are required!", 400

    # Create a new chat entry
    new_chat = Chat(room=room, username=username, message=message)
    db.session.add(new_chat)
    db.session.commit()

    return "Message received", 200

# GET API to fetch messages
@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    # Query messages for the given room
    chats = Chat.query.filter_by(room=room).order_by(Chat.timestamp).all()
    messages = [f"[{chat.timestamp}] {chat.username}: {chat.message}" for chat in chats]
    return "\n".join(messages), 200

if __name__ == '__main__':
    # Ensure the database tables are created
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')