import pandas as pd
teste = pd.read_csv("Custos.csv", encoding='latin-1')
teste['margem'] = 1 - (teste['Preço Custo']/teste['Valor de Venda'])
teste[['margem']].sort_values('margem')