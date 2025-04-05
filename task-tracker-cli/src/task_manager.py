import json
import os
from asyncio import tasks
from datetime import datetime

TASK_FILE = '../data/tasks.json'

def load_tasks():
    """Carrega as tarefas do arquivo JSON."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.decoder.JSONDecodeError:
            return []

def save_tasks(tasks):
    """Salva as tarefas no arquivo JSON."""
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    """adiciona uma nova tarefa."""
    task = load_tasks()
    task_id= 1 if not tasks else max(task['id'] for task in tasks) + 1
    new_task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat(),
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Tarefa adicionada com sucesso (ID: {task_id})')

def update_task(task_id, description):
    """Atualiza a descrição de uma tarefa."""
    tasks = load_tasks()
    for taks in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Tarefa {task_id} atualizada com sucesso}')
            return
        print(f'Tarefa com ID {task_id} não encontrada.')
