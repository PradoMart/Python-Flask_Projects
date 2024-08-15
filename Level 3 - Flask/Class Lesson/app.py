from flask import Flask, request, jsonify
from models.task import ToDoTask
app = Flask(__name__)

tasks = []
task_id = 1

@app.route('/tasks', methods=['POST'])
def create_taks():
    global task_id
    data = request.get_json()
    new_task = ToDoTask(id=task_id, title=data['title'], description=data.get("description", ""))
    task_id += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "task created"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [ task.to_Dict() for task in tasks ]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }

    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_especific_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_Dict())
        else:
            return jsonify({"message": "Not Found"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task_update = None
    for t in tasks:
        if t.id == id:
            task_update = t
            break
    print(task_update)
    
    if task_update == None:
        return jsonify({"message": "Task not found."}), 404
    
    new_data = request.get_json()
    task_update.title = new_data['title']
    task_update.description = new_data['description']
    task_update.completed = new_data['completed']

    print(task_update)
    return jsonify({"message": "Task updated."})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task_delete = None
    for t in tasks:
        print(t)
        print(t.to_Dict())
        if t.id == id:
            task_delete = t
            break

    if not task_delete:
        return jsonify({'message': 'Task not found.'}), 404
    
    else:
        tasks.remove(task_delete)
        return jsonify({'message': 'Task deleted.'})

if __name__ == "__main__":
    app.run(debug=True)
