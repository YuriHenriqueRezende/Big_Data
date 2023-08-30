import pandas as pd

# Definindo os DataFrames
data1 = {
    'ID': [1, 2, 3, 4],
    'Nome': ['Ana', 'Pedro', 'Maria', 'João'],
    'Setores': ['Rh', 'Vendas', 'Administrativo', 'Produção']
}

data2 = {
    'ID': [1, 2, 3, 4],
    'Salários': [3000, 2800, 3200, 2500]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Unindo os DataFrames utilizando a função merge
df_final = pd.merge(df1, df2, on='ID')

print(df_final)
