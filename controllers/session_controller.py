from flask import Blueprint, request, session, redirect, render_template
from models.user import get_user_by_email_or_username
import bcrypt

session_controller = Blueprint("session_controller", __name__, template_folder="../templates/session")

@session_controller.route('/login')
def loginpage():
    error = request.args.get('error', None)
    return render_template('login.html', error=error)

@session_controller.route('/sessions/create', methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # user = get_user_by_email(email)
    username = request.form.get('username')
    if username and email:
        return redirect('/login?error=Enter+username+or+email+only')
    user = get_user_by_email_or_username(email, username)
    valid = user and bcrypt.checkpw(password.encode(), user['passwords'].encode())
    if valid:
        session['user_id'] = user['id']
        session['username'] = user['username']
        return redirect('/')
    else:
        return redirect('/login?error=Incorrect+username+or+password')

@session_controller.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect('/')
