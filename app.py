from flask import Flask, render_template, session 
import os

from controllers.user_controller import user_controller
from controllers.session_controller import session_controller
from controllers.message_controller import message_controller
from models.message import get_all_messages

SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
@app.route('/')
def index():
  messages = get_all_messages(session.get('user_id'))
  return render_template('home.html', messages=messages)

@app.route('/about')
def about():
  return render_template('about.html')

app.register_blueprint(user_controller)
app.register_blueprint(session_controller)
app.register_blueprint(message_controller)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
