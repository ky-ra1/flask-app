from flask import Blueprint, request, redirect, render_template
from models.user import insert_user

user_controller = Blueprint("user_controller", __name__, template_folder="../templates/users")

@user_controller.route('/signup')
def signup():
    return render_template('signup.html')

@user_controller.route('/users', methods=["POST"])
def create_user():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    # password2 == password1

    insert_user(first_name, last_name, username, email, password1, password2)
    return redirect('/')