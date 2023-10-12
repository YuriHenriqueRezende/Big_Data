from sklearn import tree
from sklearn.preprocessing import LabelEncoder

# Dados de entrada (características)
velocidade_operacao = [10, 5, 8, 6, 12, 4]
complexidade_tarefa = ['Baixa', 'Alta', 'Media', 'Alta', 'Baixa', 'Alta']
manutencao_necessaria = ['Baixa', 'Alta', 'Media', 'Alta', 'Baixa', 'Media']

# Classificações
classificacao = ['Montagem', 'Teste', 'Montagem', 'Teste', 'Montagem', 'Teste']

label_encoder = LabelEncoder()
complexidade_tarefa_encoded = label_encoder.fit_transform(complexidade_tarefa)
manutencao_necessaria_encoded = label_encoder.fit_transform(manutencao_necessaria)

caracteristicas = list(zip(velocidade_operacao, complexidade_tarefa_encoded, manutencao_necessaria_encoded))

modelo_arvore_decisao = tree.DecisionTreeClassifier()
modelo_arvore_decisao.fit(caracteristicas, classificacao)

nova_maquina = [[7, label_encoder.transform(["Media"])[0], label_encoder.transform(["Baixa"])[0]]]
previsao = modelo_arvore_decisao.predict(nova_maquina)
print("A classificação da nova máquina é:", previsao)
