from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dados de entrada (características)
consumo_energia = [1000, 3000, 1500, 2500, 1200, 3500]
tempo_operacao = [200, 500, 300, 400, 250, 600]
tipo_energia = ['Eletrica', 'Gas', 'Eletrica', 'Gas', 'Eletrica', 'Gas']

# Classificações
classificacao = ['Eficiente', 'Ineficiente', 'Eficiente', 'Eficiente', 'Ineficiente', 'Ineficiente']

# Converta os dados categóricos em numéricos
le_tipo_energia = LabelEncoder()
tipo_energia_encoded = le_tipo_energia.fit_transform(tipo_energia)

# Combine todas as características em uma única lista
caracteristicas = list(zip(consumo_energia, tempo_operacao, tipo_energia_encoded))

# treina o modelo de árvore de decisão
modelo_arvore = DecisionTreeClassifier()
modelo_arvore.fit(caracteristicas, classificacao)

nova_maquina = [2200, 350, 'Gas']
nova_maquina_encoded = [nova_maquina[0], nova_maquina[1], le_tipo_energia.transform([nova_maquina[2]])[0]]
previsao = modelo_arvore.predict([nova_maquina_encoded])

print("Classificação da máquina:", previsao[0])
