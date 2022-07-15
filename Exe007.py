''' Desenvolva um Programa que leia as duas notas do 
aluno, Calcule e mostre a sua média. Dica ordem de precedemcia  '''

nome = input(' Digite seu Nome\n ')
print(' Olá Seja Muito Bem Vindo{}!\n Vamos calcular sua nota?! '.format(nome))
n1 = int(input(' Digite sua Primeira nota:\n '))
n2 = int(input(' Agora digeote a sua Segunda nota:\n '))
ntotal = n1 + n2
media = ntotal / 2
print(' {} a Sua media e de \n {}:'.format(nome, media ))