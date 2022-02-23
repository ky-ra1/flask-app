from flask import Blueprint, request, session, redirect, render_template
from models.message import delete_message, get_all_messages, insert_message, get_message, update_message

message_controller = Blueprint("message_controller", __name__, template_folder="../templates/messages")


@message_controller.route('/messages')
def message():
    message_items = get_all_messages()
    return render_template('message.html', message_items=message_items)


@message_controller.route('/messages/<id>/create')
def create():
    if not session.get('user_id'):
        return redirect('/login')
    return render_template('create.html')
        
@message_controller.route('/messages', methods=["POST"])
def insert():
    if not session.get('user_id'):
        return redirect('/login')
    message = request.form.get('message')
    if len(message) < 5:
        return redirect('/?error=Please+enter+a+message+at+least+5+characters+long')
    insert_message(
        message,
        session.get('user_id')
    )
    return redirect('/')

@message_controller.route('/messages/<id>/show')
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
    update_message(message, id)
    return redirect('/')

@message_controller.route('/messages/<id>/delete', methods=["POST"])
def delete(id):
    if not session.get('user_id'):
        return redirect('/login')
    delete_message(id)
    return redirect('/')