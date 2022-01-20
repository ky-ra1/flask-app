from flask import Blueprint, request, session, redirect, render_template
from models.message import delete_message, insert_message, get_message, update_message

message_controller = Blueprint("message_controller", __name__, template_folder="../templates/messages")

@message_controller.route('/messages')
def create():
    if not session.get('user_id'):
        return redirect('/login')
    return render_template('create.html')
        
@message_controller.route('/messages', methods=["POST"])
def insert():
    if not session.get('user_id'):
        return redirect('/login')
    insert_message(
        request.form.get('message'),
        session.get('user_id')
    )
    return redirect('/')

@message_controller.route('/messages/<id>')
def show(id):
    message = get_message(id)
    return render_template('show.html', message=message)

@message_controller.route('/messages/<id>/edit')
def edit(id):
    if not session.get('user_id'):
        return redirect('/login')
    message = get_message(id)
    return render_template('edit.html', message=message)

@message_controller.route('/messages/<id>', methods=["POST"])
def update(id):
    if not session.get('user_id'):
        return redirect('/login')
    message = request.form.get("message")    
    update_message(id, message, session.get('user_id'))
    return redirect('/')

@message_controller.route('/messages/<id>/delete', methods=["POST"])
def delete(id):
    if not session.get('user_id'):
        return redirect('/login')
    delete_message(id)
    return redirect('/')