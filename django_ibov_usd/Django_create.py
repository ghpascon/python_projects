import os
import subprocess

def criar_projeto(nome_projeto):
    # Cria um novo projeto Django com o nome especificado
    subprocess.run(['django-admin', 'startproject', nome_projeto])

def criar_app(nome_projeto, nome_app):
    # Navega até o diretório do projeto
    os.chdir(nome_projeto)
    
    # Cria um novo aplicativo dentro do projeto
    subprocess.run(['python', 'manage.py', 'startapp', nome_app])

if __name__ == "__main__":
    nome_projeto = input("Digite o nome do projeto: ")
    criar_projeto(nome_projeto)

    nome_app = input("Digite o nome do aplicativo: ")
    criar_app(nome_projeto, nome_app)

    print("Projeto e aplicativo criados com sucesso!")
