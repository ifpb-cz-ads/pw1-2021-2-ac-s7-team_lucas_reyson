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

for i in lista_01:
    if i not in lista_03:
        lista_03.append(i)
for i in lista_02:
    if i not in lista_03:
        lista_03.append(i)

print("{}".format(lista_03))

