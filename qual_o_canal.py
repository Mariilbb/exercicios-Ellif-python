#informe o numero do canal que a pessoa está assistindo e ele te dará o nome

canal=int(input("digite o numero do canal que você está assistindo:"))

if canal==2:
    print("você está assistindo o canal bandeirantes")
elif canal==4:
    print("você está assistindo ao canal sbt")
elif canal==6:
    print("você está assistindo ao canal cnt")
elif canal==7:
    print("você está assistindo ao canal record")
elif canal==9:
    print("você está assistindo ao canal cultura")
elif canal==12:
    print("você está assistindo ao canal globo")
else:
    print("você digitou um numero invalido")