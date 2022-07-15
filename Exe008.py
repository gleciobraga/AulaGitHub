''' Escreva um Programa que leia um valor em metros e
    Exiba convertido em centimetros e milimetros '''
    
nome = str(input(' Digite seu Nome:\n  '))
print(' Seja Muito Bem Vindo {}: '.format(nome))
print(' {} Esse Programa converte Valores de METROS para CENTIMETORS e para MILIMETROS'.format(nome))
metro = int(input(' Digite o Valor em METROS que Você quer saber:\n '))
cent = metro / 60
mili = cent / 60
print(' {} o valor de {} que você digitou equivale a:'.format(nome, metro))
print(' É igual a {} Centimetros é \n igual a {} Milimetros'.format( cent, mili))