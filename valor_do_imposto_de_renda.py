#Calcular o valor do imposto de renda de uma pessoa a partir do salário, valores segundo uma tabela

salario=float(input("digite o valor do seu salário: R$"))

if salario <= 1903.98:
    print("você está isento de imposto")
else:
    if salario <= 2826.65:
        irpf = salario * 0.075
    elif salario <= 3751.05:
        irpf = salario * 0.15
    elif salario <= 4664.68:
        irpf = salario * 0.225

print("o valor do imposto a recoler é: R$%.2f" % irpf)
