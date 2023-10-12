# Importar as bibliotecas necessárias
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn import tree
import matplotlib.pyplot as plt


# Criar um dataframe com os dados das máquinas
dados = {'precisao_na_montagem': ['Alta', 'Media', 'Alta', 'Media', 'Baixa', 'Baixa'],
         'velocidade_de_producao': ['Media', 'Baixa', 'Alta', 'Alta', 'Baixa', 'Media'],
         'taxa_de_retrabalho': ['Baixa', 'Alta', 'Baixa', 'Baixa', 'Alta', 'Alta'],
         'classificacao': ['Alta Qualidade', 'Baixa Qualidade', 'Alta Qualidade', 'Alta Qualidade', 'Baixa Qualidade', 'Baixa Qualidade']}
df = pd.DataFrame(dados)

# Codificar as variáveis categóricas em números
df['precisao_na_montagem'] = df['precisao_na_montagem'].map({'Baixa': 0, 'Media': 1, 'Alta': 2})
df['velocidade_de_producao'] = df['velocidade_de_producao'].map({'Baixa': 0, 'Media': 1, 'Alta': 2})
df['taxa_de_retrabalho'] = df['taxa_de_retrabalho'].map({'Alta': 0, 'Baixa': 1})
df['classificacao'] = df['classificacao'].map({'Baixa Qualidade': 0, 'Alta Qualidade': 1})

# Separar as variáveis de entrada e saída
X = df.drop('classificacao', axis=1)
y = df['classificacao']

# Criar e treinar o modelo de árvore de decisão
modelo = DecisionTreeClassifier(criterion='gini')
modelo.fit(X,y)

fig = plt.figure(figsize=(10,8))
tree.plot_tree(modelo)

