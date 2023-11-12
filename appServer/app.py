from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
messagesList = []

@app.route('/')
def show_messages():
    return render_template('messages.html', messages = messagesList)

@app.route('/send_json', methods = ['POST'])
def make_json_message():
    data = request.get_json()

    title = data['message_title']
    author = data['message_author']
    body = data['message_body']

    message = (title, author, data)
    messagesList.append(message)

    return

@app.route('/read_json', methods = ['GET'])
def read_message():
    if len(messagesList) == 0:
        return{}
    
    message = messagesList.pop()

    (title, author, body) = message

    return {'message_title': title, 'message_author': author, 'message_body': body}

app.run()