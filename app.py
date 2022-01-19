from flask import Flask, redirect
import psycopg2
import os

from controllers.user_controller import user_controller
from controllers.session_controller import session_controller


DB_URL = os.environ.get("DATABASE_URL", "dbname=Project2")
SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
@app.route('/')
def index():
  conn = psycopg2.connect(DB_URL)
  cur = conn.cursor()
  cur.execute('SELECT 1', [])  # Query to check that the DB connected
  conn.close()
  return 'Hiiii'


# Don't forget to register controllers
app.register_blueprint(user_controller)
app.register_blueprint(session_controller)



if __name__ == "__main__":
    app.run(debug=True)
