parentese = input("Informe uma expressão com parênteses:")

pilha = []
x = 0

while x < len(parentese):
    if parentese[x] == "(":
        pilha.append("(")
    if parentese[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")
            break
    x = x + 1

if len(pilha) == 0:
    print("OK")
else:
    print("Erro")
