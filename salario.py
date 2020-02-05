#Escreva um programa que leia o salário de um funcionário  e 
# exiba na tela o valor do salário com um reajuste de aumento, sendo que:
#Caso o salário atual seja maior que R$ 2.000,00 receberá 7% de aumento.
#Caso contrário, receberá 15% de aumento.

salario = float(input('Informe o salário: '))

if salario > 2000:
     aumento = salario * 7 / 100
else:
    aumento = salario * 15 / 100

novoSalario = salario + aumento
print(aumento)
print(novoSalario)


