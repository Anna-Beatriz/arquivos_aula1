#Escreva uma função que receba como parâmetro um número N e 
# retorna True se esse número for primo, e False caso não seja primo.

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

primo = primos(num)
print(primo)