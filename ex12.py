from sklearn.tree import DecisionTreeClassifier

# Dados de entrada (características)
vibracao = [3.2, 4.0, 3.7, 5.5, 6.2, 2.1, 2.8, 1.9, 7.3, 6.8, 2.4, 5.9, 4.5, 2.6, 4.8, 3.4, 6.1, 2.0, 5.0, 7.0]
corrente = [12.5, 14.2, 11.8, 15.6, 17.0, 10.2, 9.5, 8.8, 18.4, 17.8, 10.8, 16.2, 13.4, 9.9, 13.9, 11.5, 16.7, 8.6, 14.8, 18.0]
temperatura = [50.0, 51.2, 48.5, 53.1, 56.8, 45.7, 43.2, 41.6, 59.3, 57.9, 46.9, 54.7, 49.7, 44.5, 50.8, 47.3, 55.4, 41.0, 52.3, 58.7]

# Classificações
classificacao = ['Não Defeituosa', 'Não Defeituosa', 'Não Defeituosa', 'Não Defeituosa', 'Não Defeituosa', 'Defeituosa', 'Defeituosa', 'Defeituosa', 'Não Defeituosa', 'Não Defeituosa', 'Defeituosa', 'Não Defeituosa', 'Não Defeituosa', 'Não Defeituosa', 'Defeituosa', 'Não Defeituosa', 'Não Defeituosa', 'Não Defeituosa', 'Não Defeituosa', 'Não Defeituosa']

caracteristicas = list(zip(vibracao, corrente, temperatura))

# Crie e treine o modelo de árvore de decisão
modelo_arvore = DecisionTreeClassifier()
modelo_arvore.fit(caracteristicas, classificacao)


nova_medicao = [5.2, 16.9, 52.8]
previsao = modelo_arvore.predict([nova_medicao])

print("Classificação da máquina:", previsao[0])
