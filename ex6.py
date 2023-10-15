from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dados de entrada (características)
idade = [5, 10, 3, 8, 1, 15]
historico_manutencao = ['Bom', 'Ruim', 'Excelente', 'Regular', 'Excelente', 'Ruim']
num_falhas_anteriores = [0, 3, 0, 2, 0, 5]
nivel_automacao = ['Alto', 'Baixo', 'Médio', 'Alto', 'Médio', 'Baixo']

# Classificações
classificacao = ['Segura', 'Não Segura', 'Segura', 'Não Segura', 'Segura', 'Não Segura']

# Converta os dados categóricos em numéricos
le_historico_manutencao = LabelEncoder()
historico_manutencao_encoded = le_historico_manutencao.fit_transform(historico_manutencao)

le_nivel_automacao = LabelEncoder()
nivel_automacao_encoded = le_nivel_automacao.fit_transform(nivel_automacao)

# características em uma única lista
caracteristicas = list(zip(idade, historico_manutencao_encoded, num_falhas_anteriores, nivel_automacao_encoded))

# treina o modelo de árvore de decisão
modelo_arvore = DecisionTreeClassifier()
modelo_arvore.fit(caracteristicas, classificacao)


nova_maquina = [7, 'Regular', 1, 'Médio']
nova_maquina_encoded = [nova_maquina[0], le_historico_manutencao.transform([nova_maquina[1]])[0], nova_maquina[2], le_nivel_automacao.transform([nova_maquina[3]])[0]]
previsao = modelo_arvore.predict([nova_maquina_encoded])

print("Classificação da máquina:", previsao[0])
