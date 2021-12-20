num_1 = int(input('Infrome o primeiro número: '))
num_2 = int(input('Infrome o segundo número: '))

def multiplo(num_1, num_2):
    return num_1 % num_2 == 0

print('Múltiplo({},{}) == {}'.format(num_1, num_2, multiplo(num_1,num_2)))