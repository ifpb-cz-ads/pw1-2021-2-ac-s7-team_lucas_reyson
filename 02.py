lista_01 = []
lista_02 = []
lista_03 = []

while True:
    nums = int(input("Infome um numero para a primeira lista (0 encerra):"))
    if nums == 0:
        break
    lista_01.append(nums)
while True:
    nums = int(input("Infome um numero para a segunda lista (0 encerra):"))
    if nums == 0:
        break
    lista_02.append(nums)

juncao = lista_01[:]
juncao.extend(lista_02)

x = 0
while x < len(juncao):
    y = 0
    while y < len(lista_03):
        if juncao[x] == lista_03[y]:
            break
        y = y + 1
    if y == len(lista_03):
        lista_03.append(juncao[x])
    x = x + 1
x = 0
while x < len(lista_03):
    print("{}".format(lista_03[x]))
    x = x + 1