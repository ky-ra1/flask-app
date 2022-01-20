from flask import Flask, render_template
import os

from controllers.user_controller import user_controller
from controllers.session_controller import session_controller
from controllers.message_controller import message_controller

SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
@app.route('/')
def index():
  return render_template('home.html')


# Don't forget to register controllers
app.register_blueprint(user_controller)
app.register_blueprint(session_controller)
app.register_blueprint(message_controller)


if __name__ == "__main__":
    app.run(debug=True)
