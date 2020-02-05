#Escreva uma função que receba como parâmetro um número N e 
# exibe todos os número primos menores que N.

num = int(input('Digite um número: '))

def primos(num):
    c = 1
    a = 0
    while c <= num:
        if num % c == 0:
            a = a + 1
        c = c + 1
    
    if a == 2:
        return True
    else:
        return False

def primosMenores(num):
    for i in range(num):
        if primos(i) == True:
            print(i)

primosMenores(num)

