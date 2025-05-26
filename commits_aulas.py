import subprocess
import os
# Caminho da pasta onde estão os arquivos das aulas
repo_path = r"C:\Users\geta0\Documents\vsc\Python\Python-Course\aulas"
os.chdir(repo_path)  # Entra na pasta certa

# Lista com os arquivos e suas mensagens de commit
commits = [
    ("aula40.py", "Aula 40 - [Aula sobre construção de calculadora com while, validação de números, operadores e laço de repetição com opção de saída / Lesson on building a calculator with while loop, number and operator validation, and exit condition with user input]"),
    ("aula41.py", "Aula 41 - [Aula sobre estrutura while/else e comportamento com break / Lesson on while/else structure and behavior with break]"),
    ("aula42.py", "Aula 42 - [Aula sobre contagem de caracteres e identificação da letra mais frequente em uma string / Lesson on character counting and identifying the most frequent letter in a string]"),
    ("aula43.py", "Aula 43 - [Aula sobre loops while com repetição condicional e concatenação de strings com for / Lesson on while loops with conditional repetition and string concatenation using for]"),
    ("aula44.py", "Aula 44 - [Aula sobre laços aninhados com while / Lesson on nested loops with while]"),
    ("aula45.py", "Aula 45 - [Aula sobre iteráveis, iteradores, iter() e next() em Python / Lesson on iterables, iterators, iter() and next() in Python"),
    ("aula46.py", "Aula 46 - [Aula sobre o uso de for com else, continue e break aninhado / Lesson on using for with else, nested continue and break]"),
    ("aula47.py", "Aula 47 - [Aula prática: jogo da palavra secreta com while, controle de fluxo e contagem de tentativas / Practical lesson: secret word game with while, flow control and attempt counter]"),
    ("aula48.py", "Aula 48 - [Introdução às listas em Python: mutabilidade, índices e tipos variados / Introduction to Python lists: mutability, indexing, and mixed types]"),
    ("aula49.py", "Aula 49 - [Operações CRUD com listas e métodos como append e pop / CRUD operations with lists and methods like append and pop]"),
    ("aula50.py", "Aula 50 - [Métodos de modificação em listas: append, pop, insert, del e clear / List modification methods: append, pop, insert, del, and clear]"),
]


for arquivo, mensagem in commits:
    caminho_completo = f"{repo_path}\\{arquivo}"
    subprocess.run(["git", "add", caminho_completo])
    subprocess.run(["git", "commit", "-m", mensagem])

print("✅ Todos os commits foram realizados com sucesso!")
