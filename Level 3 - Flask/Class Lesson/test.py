import pytest, requests

#CRUD

BASE_URL = 'http://127.0.0.1:5000/tasks'
tasks = []

def test_create_task():
    new_task_data = {
        "title": "New Task",
        "description": "New tasks description"
    }

    response = requests.post(f"{BASE_URL}", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_tasks():
    response = requests.get(f'{BASE_URL}')
    assert response.status_code == 200
    assert "tasks" and "total_tasks" in response.json()

def test_get_especific_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f'{BASE_URL}/{task_id}')
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
                    "completed": True,
                    "title": 'New title teste',
                    "description": 'New description test'
        }
        response = requests.put(f'{BASE_URL}/{task_id}', json=payload)
        assert response.status_code == 200
        assert "message" in response.json()

        #requisição get new informations

        response_get = requests.get(f'{BASE_URL}/{task_id}')
        assert payload["title"] == response_get.json()["title"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f'{BASE_URL}/{task_id}')
        assert response.status_code == 200

        #response_get = requests.get(f'{BASE_URL}/{task_id}')
        #assert response_get.status_code == 404
