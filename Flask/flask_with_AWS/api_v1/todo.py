from flask import jsonify
from flask import request
from flask import Blueprint
from model import Todo,db
import requests

from . import api

@api.route('/todos',methods=['GET','POST'])
def todos():
    if request.method == 'POST':
        res = requests.post('https://hooks.slack.com/services/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', json={
            'text': 'Hello World'
        }, headers={'Content-Type': 'application/json'})
    elif request.method == 'GET':
        pass

    data = request.get_json()
    return jsonify(data)

@api.route('/slack/todos',methods=['POST'])
def slack_todos():
    res = request.form['text'].split(' ')
    cmd, *args = res

    ret_msg = ''
    if cmd == 'create':
        todo_name = args[0]
        todo = Todo()
        todo.title = todo_name

        db.session.add(todo)
        db.session.commit()
    
        ret_msg = 'todo created'
    elif cmd == 'list':
        pass

    return ret_msg