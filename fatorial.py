#Escreva uma função que recebe como parâmetro de entrada um número N positivo, 
#e retorna o fatorial de n.
num = int(input('Digite um número: '))

def fatorial(num):
    resultado = 1
    c = 1

    while c <= num:
        resultado = resultado * c
        c = c + 1
    
    return resultado

funFat = fatorial(num)
print(funFat)