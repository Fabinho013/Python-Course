import subprocess
import os
# Caminho da pasta onde estão os arquivos das aulas
repo_path = r"C:\Users\geta0\Documents\vsc\Python\Python-Course\aulas"
os.chdir(repo_path)  # Entra na pasta certa

# Lista com os arquivos e suas mensagens de commit
commits = [
    ("aula1.py", "Aula 1 - [Hello, world!]"),
    ("aula2.py", "Aula 2 - [Aula sobre argumentos em funções, argumentos nomeados e não nomeados, e uso de sep e end no print / Lesson on function arguments, named and unnamed arguments, and usage of sep and end in print]"),
    ("aula3.py", "Aula 3 - [Aula sobre strings, tipagem dinâmica e forte, uso de aspas simples e duplas, e escape de caracteres / Lesson on strings, dynamic and strong typing, use of single and double quotes, and character escaping]"),
    ("aula4.py", "Aula 4 - [Aula sobre os tipos int e float, números positivos e negativos, casas decimais e uso da função type / Lesson on int and float types, positive and negative numbers, decimal points, and use of the type function]"),
    ("aula5.py", "Aula 5 - [Aula sobre o tipo de dado booleano (bool), valores True e False, e o uso do operador lógico de igualdade == / Lesson on boolean data type (bool), True and False values, and use of the logical equality operator ==]"),
    ("aula6.py", "Aula 6 - [Aula sobre conversão de tipos (coerção), tipos primitivos imutáveis e uso das funções int, float, bool e str / Lesson on type conversion (coercion), primitive immutable types, and use of int, float, bool, and str functions]"),
    ("aula7.py", "Aula 7 - [Aula sobre variáveis, atribuição de valores, boas práticas com PEP8 e operadores lógicos em expressões / Lesson on variables, value assignment, PEP8 best practices, and logical operators in expressions]"),
    ("aula8.py", "Aula 8 - [Aula sobre declaração de múltiplas variáveis, cálculo de ano de nascimento, verificação de maioridade e conversão para float / Lesson on declaring multiple variables, calculating year of birth, checking age of majority, and float conversion]"),
    ("aula9.py", "Aula 9 - [Aula sobre operadores aritméticos: adição, subtração, multiplicação, divisão, divisão inteira, exponenciação e módulo / Lesson on arithmetic operators: addition, subtraction, multiplication, division, floor division, exponentiation, and modulo]"),
    ("aula10.py", "Aula 10 - [Aula sobre concatenação de strings e repetição de caracteres / Lesson on string concatenation and character repetition.]"),
    ("aula11.py", "Aula 11 - [Aula sobre precedência de operadores matemáticos / Lesson on operator precedence in mathematical expressions]"),
    ("aula12.py", "Aula 12 - [Aula sobre cálculo do IMC e interpolação de variáveis em strings / Lesson on BMI calculation and string interpolation]"),
    ("aula13.py", "Aula 13 - [Aula sobre f-strings e formatação de strings com valores numéricos / Lesson on f-strings and formatting strings with numeric values]"),
    ("aula14.py", "Aula 14 - [Aula sobre formatação de strings com .format() / Lesson on string formatting with .format()]"),
    ("aula15.py", "Aula 15 - [Aula sobre entrada de dados com input() e conversão de tipos / Lesson on data input with input() and type conversion]"),
    ("aula16.py", "Aula 16 - [Aula sobre estruturas condicionais if, elif e else / Lesson on conditional structures if, elif, and else]"),
    ("aula17.py", "Aula 17 - [Aula sobre múltiplas condições com elif e blocos if independentes / Lesson on multiple conditions with elif and independent if blocks]"),
    ("aula18.py", "Aula 18 - [Aula sobre operadores de comparação (relacionais) / Lesson on comparison (relational) operators]"),
    ("aula19.py", "Aula 19 - [Aula prática com entrada de dados, operações matemáticas e comparação / Practical lesson with data input, math operations, and comparison]"),
    ("aula20.py", "Aula 20 - [Aula sobre operadores lógicos e avaliação de curto-circuito / Lesson on logical operators and short-circuit evaluation]"),
    ("aula21.py", "Aula 21 - [Aula sobre o operador lógico or e validações condicionais / Lesson on the logical operator or and conditional validations]"),
    ("aula22.py", "Aula 22 - [Aula sobre o operador lógico not e verificação de valores vazios / Lesson on the logical operator not and empty value checking]"),
    ("aula23.py", "Aula 23 - [Aula sobre os operadores in e not in com strings / Lesson on in and not in operators with strings]"),
    ("aula24.py", "Aula 24 - [Aula sobre interpolação de strings com % e formatação de tipos / Lesson on string interpolation with % and type formatting]"),
    ("aula25.py", "Aula 25 - [Aula sobre formatação avançada com f-strings e alinhamento de valores / Lesson on advanced formatting with f-strings and value alignment]"),
    ("aula26.py", "Aula 26 - [Aula sobre fatiamento de strings e a função len() / Lesson on string slicing and the len() function]"),
    ("aula27.py", "Aula 27 - [Aula Exercício prático com validação de entrada e manipulação de strings / Practical exercise with input validation and string manipulation]"),
    ("aula28.py", "Aula 28 - [Aula Introdução ao tratamento de erros com try e except / Introduction to error handling with try and except]"),
    ("aula29.py", "Aula 29 - [Aula Variáveis, Constantes e Complexidade de Código / Variables, Constants, and Code Complexity]"),
    ("aula30.py", "Aula 30 - [Aula id, is, None e o Controle de Fluxo com Flags / id, is, None and Flow Control with Flags]"),
    ("aula31.py", "Aula 31 - [Aula Controle de Fluxo com Flags, None, is e is not / Flow Control with Flags, None, is and is not]"),
    ("aula32.py", "Aula 32 - [Aula Exercícios práticos: par ou ímpar, saudação por hora, e classificação de nome / Practical exercises: even or odd, greeting by hour, and name classification]"),
    ("aula33.py", "Aula 33 - [Aula Tipos built-in, imutabilidade e métodos de string / Built-in types, immutability, and string methods]")
]


for arquivo, mensagem in commits:
    caminho_completo = f"{repo_path}\\{arquivo}"
    subprocess.run(["git", "add", caminho_completo])
    subprocess.run(["git", "commit", "-m", mensagem])

print("✅ Todos os commits foram realizados com sucesso!")
