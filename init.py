import pandas as pd
print("Pandas funcionando! Versão:\n", pd.__version__)

df = pd.read_excel("Table.xlsx")

print("Tabela inicialmente implementada:\n")
print(df)
print("\n")



#Criando uma nova coluna com a porcentagem de peças boas
df["Boas (%)"] = df['Peças boas'] / df['Total Previsto'] * 100
print(df)
print("\n")

#Mudando o total previsto
df['Total Previsto'] = 200

#Criando uma nova coluna com a porcentagem de peças ruins
df["Ruins (%)"] = df['Com defeito'] / df['Total Previsto'] * 100
print(df)
print("\n")

#Imprimindo máquinas com melhor desempenho
maior_que_50 = df['Peças boas'] > 50

print("Maquinas com bom aproveitamento (mais de 50 peças boas)\n")
print(df[maior_que_50])
print("\n")

print("Descrição da tabela:\n")
print(df.describe())
print("\n")

print("Informações sobre a tabela:\n")
print(df.info())
print("\n")