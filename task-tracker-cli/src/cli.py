#!/usr/bin/env python3

import argparse
import task_manager

def main():
    parser = argparse.ArgumentParser(description='Gerenciador de tarefas CLI')
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis')

    # Subcomando 'add'
    add_parser = subparsers.add_parser('add', help='Adiciona uma nova tarefa')
    add_parser.add_argument('description', type=str, help='Nova tarefa')

    # Subcomando 'list'
    list_parser = subparsers.add_parser('list', help='Lista as tarefas')
    list_parser.add_argument('status', nargs='?', type=str, help='Filta por status (todo, in-progress, done)', choices=['todo', 'in-progress', 'done'])

    # Subcomando 'update'
    update_parser = subparsers.add_parser('update', help='Atualiza uma tarefa existente')
    update_parser.add_argument('task_id', type=int, help='ID da tarefa a ser atualizada')
    update_parser.add_argument('description', type=str, help='Nova descrição da tarefa')

    # Subcomando 'delete'
    delete_parser = subparsers.add_parser('delete', help='Deleta uma tarefa existente')
    delete_parser.add_argument('task_id', type=int, help='ID da tarefa a ser deletada')

    # Subcomando 'mark-in-progress'
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Marca uma tarefa como em andamento')
    mark_in_progress_parser.add_argument('task_id', type=int, help='ID da tarefa a ser marcada como em andamento')

    # Subcomando 'mark-done'
    mark_done_parser = subparsers.add_parser('mark-done', help='Marca uma tarefa como concluída')
    mark_done_parser.add_argument('task_id', type=int, help='ID da tarefa a ser marcada como concluída')

    args = parser.parse_args()

    if args.command == 'add':
        task_manager.add_task(args.description)
    elif args.command == 'list':
        task_manager.list_tasks(args.status)
    elif args.command == 'update':
        task_manager.update_task(args.task_id, args.description)
    elif args.command == 'delete':
        task_manager.delete_task(args.task_id)
    elif args.command == 'mark-in-progress':
        task_manager.mark_in_progress(args.task_id)
    elif args.command == 'mark-done':
        task_manager.mark_done(args.task_id)
    else:
        print("Comando inválido")

if __name__ == '__main__':
    main()
