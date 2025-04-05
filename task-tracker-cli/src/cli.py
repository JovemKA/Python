import argparse


def main():
    parser = argparse.ArgumentParser(description='Gerenciador de tarefas CLI')
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis')


    args = parser.parse_args()

if __name__ == '__main__':
    main()