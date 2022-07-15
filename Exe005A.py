''' Trinando com Operadores'''
    
nome = input('Olá quale eo seu nome? ')
print('seja bem vindo {}'.format(nome))
n1 = int(input('Um Valor:'))
n2 = int(input('Outro Valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
ex = n1**n2
raz1 = n1**(1/2)
raz2 = n2**(1/2)
print(' A soma e {}\n o produto e {}\n a divisão é {}.'.format(s, m, d))
print(' Divisão Inteira e {}\n e a Potência é {}'.format(di, ex))
print(' A Raiz do priemiro numero e{}\n A Raiz do Segundo numero e {}'.format(raz1, raz2 ))