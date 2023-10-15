from sklearn.tree import DecisionTreeClassifier

# Dados de entrada (características)
precisao_montagem = ['Alta', 'Media', 'Alta']
velocidade_producao = ['Media', 'Baixa', 'Alta']
taxa_retrabalho = ['Baixa', 'Alta', 'Baixa']

# Classificações correspondentes
classificacao = ['Alta Qualidade', 'Baixa Qualidade', 'Alta Qualidade']

# Combine todas as características em uma única lista
caracteristicas = list(zip(precisao_montagem, velocidade_producao, taxa_retrabalho))

# Cria um mapeamento de rótulos únicos
label_encoder_mapping = {}
for feature in caracteristicas:
    for label in feature:
        if label not in label_encoder_mapping:
            label_encoder_mapping[label] = len(label_encoder_mapping)

# Converta dados categóricos em numéricos
caracteristicas_encoded = [
    [label_encoder_mapping[valor] for valor in feature]
    for feature in caracteristicas
]

# treina o modelo de árvore de decisão
modelo_arvore = DecisionTreeClassifier()
modelo_arvore.fit(caracteristicas_encoded, classificacao)

nova_maquina = ['Media', 'Alta', 'Baixa']
nova_maquina_encoded = [label_encoder_mapping[valor] for valor in nova_maquina]
previsao = modelo_arvore.predict([nova_maquina_encoded])

print("Classificação da máquina:", previsao[0])
