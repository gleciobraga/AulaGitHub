''' faça um programa que leia algo pelo teclado e mostre na tela
    seu tipo primitivo e todas as informações possiveis sobre ela'''
6
a = input('Digite algo:  ')
print('O tipo primitivo desse valor e ', type(a))
print('Só tem espaços?',a.isspace())
print('É um numero?',a.isnumeric())
print('É Alfabetico?',a.isalpha())
print('É alfa alfaumérico?',a.isalnum())
print('Esta em maiúscula?',a.isupper())
print('Esta em Minúscula?',a.islower())
print('esta capitalizada?',a.istitle())