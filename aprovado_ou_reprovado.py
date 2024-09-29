#Indique se o aluno foi aprovado ou reprovado a partir da média de 3 notas


nota1=float(input("digite o valor da primeira nota:"))
nota2=float(input("digite o valor da segunda nota"))
nota3=float(input("digite o valor da terceira nota:"))

media=(nota1+nota2+nota3)/3

if media >= 9.0:
    conceito="A"
elif media >= 7.5:
    conceito="B"
elif media >= 6.0:
    conceito="C"
elif media >=4.0:
    conceito="D"
else:
    conceito="E"

print("A média do aluno é: %.1f" % media)
print("O conceito do aluno é: %s" % conceito)

if media >= 6.0:
    print("aprovado")
else:
    print("reprovado")