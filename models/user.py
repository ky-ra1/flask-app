import database
import bcrypt

def insert_user(first_name, last_name, email, password):
    # Decode the generated hash to convert it to a string to insert into DB

    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    database.sql_write("INSERT INTO users (first_name, last_name, email, password)"
        + " VALUES(%s, %s, %s)", [first_name, last_name, email, password_hash])

def get_user_by_id(id):
    results = database.sql_select('SELECT * FROM users WHERE id = %s', [id])
    return results[0]

def get_user_by_email(email):
    results = database.sql_select("SELECT * FROM users WHERE email = %s", [email])
    if len(results) > 0:
        return results[0]
    else:
        return None

def get_all_users():
    results = database.sql_select("SELECT * USERS")

def update_user(id, first_name, last_name, email):
    pass

def delete_user(id):
    pass