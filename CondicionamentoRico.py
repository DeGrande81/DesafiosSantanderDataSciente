# Entrada de dados
saldo_total = int(input("Digite Saldo:" ))
valor_saque = int(input("Digite Valor Saque:" ))

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
if saldo_total >= valor_saque:
    saldo = saldo_total-valor_saque
    print ("Saque realizadao com sucesso! Novo Saldo:", saldo)
#elif saldo_total<=valor_saque:
else:
    print ("Saldo insuficiente. Saque não realizado!")
