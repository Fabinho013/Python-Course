# Aula 46 - Aula sobre o uso de for com else, continue e break aninhado / Lesson on using for with else, nested continue and break
for i in range(20):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 16:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 4):
        print(i, j)
else:
    print('For completo com sucesso!')