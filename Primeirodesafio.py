saldo_atual = float(input ("Saldo Atual:"))
valor_deposito = float(input("Valor Depósito:"))
valor_retirada = float(input("Valor Retirada:"))

print("Saldo Atual:", saldo_atual)
print("Valor depositado:", valor_deposito)
print("Saque Realizado:", valor_retirada)

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.

#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).

saldo = (saldo_atual+valor_deposito)-(valor_retirada)
print("Saldo atualizado na conta:", saldo)
