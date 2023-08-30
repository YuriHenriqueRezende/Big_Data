import pandas as pd

# Criando o primeiro DataFrame
data1 = {
    'Data': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Produto': ['Item A', 'Item B', 'Item A'],
    'Quantidade': [10, 5, 8],
    'Valor': [100.00, 50.00, 80.00]
}

df1 = pd.DataFrame(data1)

# Criando o segundo DataFrame
data2 = {
    'Data': ['2023-02-01', '2023-02-02', '2023-02-03'],
    'Produto': ['Item C', 'Item B', 'Item D'],
    'Quantidade': [12, 6, 3],
    'Valor': [120.00, 60.00, 30.00]
}

df2 = pd.DataFrame(data2)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)
