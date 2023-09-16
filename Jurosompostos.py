valor_inicial = float(input("Valor Inicial: "))
taxa_juros = float(input("Taxa de Juros: "))
periodo = int(input("Digite o período em meses: "))


#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

valor_final = (valor_inicial*(1+(taxa_juros/100))**periodo)

print(f'Valor final do investimento: R$ {valor_final:.2f}')
