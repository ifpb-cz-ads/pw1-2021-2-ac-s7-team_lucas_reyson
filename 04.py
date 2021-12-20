num_1 = float(input('Infrome a base do triângulo: '))
num_2 = float(input('Infrome a altura do triângulo: '))

def area(num_1, num_2):
    return (num_1 * num_2) / 2

print('Área do triangulo({}, {}) == {}'.format(num_1, num_2, area(num_1, num_2)))
