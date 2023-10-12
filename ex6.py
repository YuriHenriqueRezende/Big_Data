from sklearn import tree

# Dados de entrada (características)
idade = [5, 10, 3, 8, 1, 15]
historico_manutencao = ['Bom', 'Ruim', 'Excelente', 'Regular', 'Excelente', 'Ruim']
num_falhas_anteriores = [0, 3, 0, 2, 0, 5]
nivel_automacao = ['Alto', 'Baixo', 'Médio', 'Alto', 'Médio', 'Baixo']

# Classificações
classificacao = ['Segura', 'Não Segura', 'Segura', 'Não Segura', 'Segura', 'Não Segura']

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
historico_manutencao_encoded = label_encoder.fit_transform(historico_manutencao)
nivel_automacao_encoded = label_encoder.fit_transform(nivel_automacao)

caracteristicas = list(zip(idade, historico_manutencao_encoded, num_falhas_anteriores, nivel_automacao_encoded))

modelo_arvore_decisao = tree.DecisionTreeClassifier()
modelo_arvore_decisao.fit(caracteristicas, classificacao)

nova_maquina = [[6, label_encoder.transform(["Regular"])[0], 1, label_encoder.transform(["Alto"])[0]]]
previsao = modelo_arvore_decisao.predict(nova_maquina)
print("A classificação da nova máquina é:", previsao[0])
