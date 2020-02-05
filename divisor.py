#Escreva uma função que recebe como parâmetro um número N 
# e exibe todos os divisores desse número.

num = int(input('Digite um número: '))

def divisores(num):
    c = 1

    while c <= num:
        if num % c == 0:
            print(c)
        c = c + 1


divisores(num)
