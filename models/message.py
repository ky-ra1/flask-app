import database

# DB funcionality related to messages

# INSERT message into db
def insert_message(message, user_id):
    database.sql_write("INSERT INTO messages (message, user_id) VALUES (%s, %s)", [
        message,
        user_id
    ])

# SELECT message from db (only if logged in)
def get_message(messages_user_id_fk):
    results = database.sql_select('SELECT id, message, user_id FROM message WHERE user_id = %s',[messages_user_id_fk])
    result = results[messages_user_id_fk]
    # result['loggedin'] = result[user_id]
    return result


# UPDATE message in db
def update_message(id, message, user_id):
    database.sql_write("UPDATE messages set message = %s, user_id = %s WHERE id = %s", [
        message,
        id,
        user_id
    ])


# DELETE message from db
def delete_message(user_id):
    database.sql_write("DELETE FROM messages WHERE user_id = %s", [user_id])