import database

# DB funcionality related to messages

# INSERT message into db
def insert_message(message, user_id):
    database.sql_write("INSERT INTO messages (message, user_id) VALUES (%s, %s)", [
        message,
        user_id
    ])

# SELECT message from db (only if logged in)
def get_message(id):
    results = database.sql_select('SELECT id, message, user_id FROM message WHERE id = %s',[id])
    result = results[0]
    # result['loggedin'] = result[user_id]
    return result


# UPDATE message in db
def update_message(id, message, user_id):
    database.sql_write("UPDATE messages set message = %s, user_id = %s WHERE id = %s", [
        id,
        message,
        user_id
    ])


# DELETE message from db
def delete_message(id):
    database.sql_write("DELETE FROM messages WHERE id = %s", [id])
