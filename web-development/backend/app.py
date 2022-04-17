from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

SUBJECTS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Arquitetura de Computadores e Sistemas Operacionais',
        'teacher': 'Felipe Fink Grael',
        'inprogress': True
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Fundamentos do Desenvolvimento Python',
        'teacher': 'Jonh Carvalho',
        'inprogress': True
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Projeto em Arquitetura de Computadores, Sistemas Operacionais e Redes',
        'teacher': 'Alcione Dolavale',
        'inprogress': True
    },
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/subjects', methods=['GET', 'POST'])
def all_subjects():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        SUBJECTS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'teacher': post_data.get('teacher'),
            'inprogress': post_data.get('inprogress')
        })
        response_object['message'] = 'Disciplina Adicionada!'
    else:
        response_object['subjects'] = SUBJECTS
    return jsonify(response_object)

def remove_subject(subject_id):
    for subject in SUBJECTS:
        if subject['id'] == subject_id:
            SUBJECTS.remove(subject)
            return True
    return False

@app.route('/subjects/<subject_id>', methods=['PUT', 'DELETE'])
def single_subject(subject_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_subject(subject_id)
        SUBJECTS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'teacher': post_data.get('teacher'),
            'inprogress': post_data.get('inprogress')
        })
        response_object['message'] = 'Disciplina Atualizada!'
    if request.method == 'DELETE':
        remove_subject(subject_id)
        response_object['message'] = 'Disciplina Removida!'
    return jsonify(response_object)
    
if __name__ == '__main__':
    app.run()