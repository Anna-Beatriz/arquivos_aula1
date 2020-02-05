#Escreva uma função que recebe como parâmetro um número N e 
#retorna a soma de todos os divisores desse número.

num = int(input('Digite um número: '))

def somaDivisores(num):
    c = 1
    a = 0
    while c <= num:
        if num % c == 0:
            print(c)
            a = a + c
        c = c + 1
    return a

soma = somaDivisores(num)
print('A soma de todos os números é: ', soma)