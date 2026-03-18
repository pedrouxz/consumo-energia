## Esse código calculara o consumo mensal em kWh de eletrodomésticos.
## Autor do código: Pedro Henrique (pedrouxz)

# Entrada de dados.
nome_aparelho = str(input("Digite o nome do aparelho. "))
potencia_aparelho = float(input("Digite a potência do aparelho em watts (W). "))
tempo_medio = float(input("Digite o tempo médio de uso diário em horas. "))

# Processamento
consumo_Mensal = (potencia_aparelho * tempo_medio * 30) / 1000
custo_Estimado = consumo_Mensal * 0.5

# Saída de dados.
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_Mensal} kWh/ mês.")
print(f"Custo estímado: R${custo_Estimado:.2f} por kWh.")
