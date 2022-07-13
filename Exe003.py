# Pequeno programa( usuario digita o nome, depois digita um numero depois outro numero e o programa faz a soma dos
# dois numeros

nome = str(input('Digite Seu nome: '))
print('Seja Muito Bem Vindo {}'.format(nome))
n1 = int(input('Digite um Numero:  '))
n2 = int(input('Digite um Segundo Numero: '))
soma = n1 + n2
print('{} a soma de {} e de {} e Igual a {}'.format(nome,n1, n2, soma))
