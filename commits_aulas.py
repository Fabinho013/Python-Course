import subprocess
import os
# Caminho da pasta onde estão os arquivos das aulas
repo_path = r"C:\Users\geta0\Documents\vsc\Python\Python-Course\aulas"
os.chdir(repo_path)  # Entra na pasta certa

# Lista com os arquivos e suas mensagens de commit
commits = [
    ("aula51.py", "Aula 51 - [Aula sobre Cuidados com dados mutáveis e cópia de listas / Caution with mutable data and list copying]"),
    ("aula52.py", "Aula 52 - [Aula sobre Laço for com listas / Looping through lists with for]"),
    ("aula53.py", "Aula 53 - [Aula sobre Exibindo índices e elementos de uma lista com for e range / Displaying list indexes and elements with for and range]"),
    ("aula54.py", "Aula 54 - [Aula sobre Tipo tupla: uma lista imutável / Tuple type: an immutable list]"),
    ("aula55.py", "Aula 55 - [Aula sobre Enumerate: enumera iteráveis (índices) / Enumerate: enumerate iterables (indices)]"),
    ("aula56.py", "Aula 56 - [Aula sobre Lista de compras interativa com listas / Interactive shopping list with lists]"),
    ("aula57.py", "Aula 57 - [Aula sobre Imprecisão de ponto flutuante / Floating point imprecision]"),
    ("aula58.py", "Aula 58 - [Aula sobre Split e Join com list e str / Split and Join with list and str]"),
]


for arquivo, mensagem in commits:
    caminho_completo = f"{repo_path}\\{arquivo}"
    subprocess.run(["git", "add", caminho_completo])
    subprocess.run(["git", "commit", "-m", mensagem])

print("✅ Todos os commits foram realizados com sucesso!")
