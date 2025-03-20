from flask import Flask, jsonify

todo = Flask(__name__)  # Using 'todo' as the Flask instance

students = [
    {
        'id': 1,
        'name': 'tiger',
        'age': 10
    },
    {
        'id': 2,
        'name': 'jacob',
        'age': 11
    }
]

@todo.route('/students-list')
def get_students_list():
    return jsonify(students)

@todo.route('/students/get/<int:id>')
def get_students_by_id(id):
    print(id)
    for std in students:
        if std ['id'] == id:
            return jsonify(std)
        print(std)
    return jsonify('not found')

if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )
