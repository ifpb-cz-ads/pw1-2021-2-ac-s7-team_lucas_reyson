T = [-10, -8, 0, 1, 2, 5, -2, -4]

menor_t = T[0]
maior_t = T[0]
soma = 0

for z in T:
    if z < minima:
        minima = z
    if z > maxima:
        maxima = z
    soma = soma + z
     
print("A menor temperatura é: {}".format(minima))
print("A maior temperatura é: {}".format(maxima))
print("A temperatura média é: {}".format(soma))