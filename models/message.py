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
    results = database.sql_select('SELECT id, message, user_id FROM messages WHERE id = %s',[id])
    result = results[0]
    # result['loggedin'] = result[user_id]
    return result

# select all messages 
def get_all_messages(messages_user_id_fk):
    results = database.sql_select('SELECT id, message, user_id FROM messages WHERE user_id = %s',[messages_user_id_fk])
    # result['loggedin'] = result[user_id]
    return results


# UPDATE message in db
def update_message(message, id):
    database.sql_write("UPDATE messages set message = %s WHERE id = %s", [
        message,
        id,
        ])
    
   

# DELETE one message from db
def delete_message(id):
    database.sql_write("DELETE FROM messages WHERE id = %s", [id])

# # delete all messages
# def delete_all_message(messages_user_id_fk):
#     database.sql_write("DELETE FROM messages WHERE id = %s", [id])
