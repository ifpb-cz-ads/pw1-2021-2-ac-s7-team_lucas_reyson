L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
v=int(input("Digite outro valor a procurar:"))
x =0
posicao = False
posicao2 = False
while x <len(L):
    print("Primeiro valor")
    if p in L:
        posicao = L.index(p)
        print(f"{p} foi encontrado na Lista")
        x=+1
        posicao = True
        break
    else:
        print("valor nao encontrado!")
        break
while x <len(L):
    print("Segundo valor:")
    if v in L:
        posicao2 = L.index(v)
        print(f"{v} foi encontrado na Lista")
        x=+1
        posicao2 = True
        break
    else:
        print("valor não encontrado!")
        break

if posicao and posicao2:
    print("O valor {} foi encontrado primeiro" .format(p))
    
else:
    print("Um dos valores não esta na lista")