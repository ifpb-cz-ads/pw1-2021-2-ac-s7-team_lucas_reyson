L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
x =0
while x <len(L):
        if p in L:
            posisao = L.index(p)
            print("{} foi encontrado na Lista".format(p))
            x=+1
            break
        else:
            print("valor nao encontrado!")