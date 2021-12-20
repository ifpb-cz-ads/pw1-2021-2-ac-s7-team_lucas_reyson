s = str(input('Infome uma string: '))

def acha(s, lista):
    return s in lista

Lista = ['MA',  'ME', 'MI', 'MO', 'MU']

print('{}'.format(s), acha(s, Lista))

