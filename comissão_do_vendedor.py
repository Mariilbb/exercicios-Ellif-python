#calcular a comissão de um vendedor a partir de uma tabela pré estabelecida

valor_venda=float(input("digite o valor da venda:"))

if valor_venda <=100:
    comissao=valor_venda*0.05
elif valor_venda <=500:
    comissao=valor_venda*0.06
elif valor_venda <=1000:
    comissao=valor_venda*0.07
else:
    comissao=valor_venda*0.08

print(f"o valor da comissão é de R$ {comissao:.2f}")
