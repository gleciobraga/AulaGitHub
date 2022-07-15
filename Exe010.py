''' crie um programa que leia quanto de dinheiro uma pessoa 
    tem na carteira e mostro quanto elapode comprar em dolares
    considerando a cotação de U$1,00= R$3,27'''
    
  
grana = float(input('Quanto vc tem na Carteira: \n'))
dolar = float(input('insira a cotação do dolar: \n' ))
calculo = grana * dolar

print(' O valor que você digitou de {}\n'.format(grana))
print(' Conforma a Cotação do Dolar que e de {}\n'.format(dolar))
print(' Seu Dinheiro vale exatamente {}\n'.format(calculo))