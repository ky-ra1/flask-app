import database
import bcrypt

# DB functionality related to users

def insert_user(first_name, last_name, username, email, password1):
    password_hash = bcrypt.hashpw(password1.encode(), bcrypt.gensalt()).decode()
    database.sql_write("INSERT INTO users (first_name, last_name, username, email, passwords)"
        + " VALUES(%s, %s, %s, %s, %s)", [first_name, last_name, username, email, password_hash])

def get_user_by_id(id):
    results = database.sql_select('SELECT * FROM users WHERE id = %s', [id])
    return results[0]

def get_user_by_email(email):
    results = database.sql_select('SELECT * FROM users WHERE email = %s', [email])
    if len(results) > 0:
        return results[0]
    else:
        return None

def get_user_by_email_or_username(email, username):
    results = database.sql_select('SELECT * FROM users WHERE email = %s OR username = %s', [email, username])
    if len(results) > 0:
        return results[0]
    else:
        return None

# def get_all_users():
    results = database.sql_select("SELECT * USERS")

def update_user(id, first_name, last_name, email):
    pass

def delete_user(id):
    pass