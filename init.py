import pandas as pd
print("Pandas funcionando! Versão:\n", pd.__version__)
print("\n")

df = pd.read_excel("Table.xlsx")

def atualiza(df):
    #Atualizando uma nova coluna com a porcentagem de peças ruins
    df["Ruins (%)"] = df['Com defeito'] / df['Total Previsto'] * 100
    #Atualizando uma nova coluna com a porcentagem de peças boas
    df["Boas (%)"] = df['Peças boas'] / df['Total Previsto'] * 100

#Imprime a tabela
print("Tabela inicialmente implementada:\n")
print(df)
print("\n")

#Criando uma nova coluna com a porcentagem de peças boas
print("Criando uma nova coluna com a porcentagem de peças BOAS\n")
df["Boas (%)"] = df['Com defeito'] / df['Total Previsto'] * 100
print(df)
print("\n")

#Mudando o total previsto
df['Total Previsto'] = 200

atualiza(df)# chama atualiza

#Criando uma nova coluna com a porcentagem de peças ruins
print("Criando uma nova coluna com a porcentagem de peças RUINS\n")
df["Ruins (%)"] = df['Com defeito'] / df['Total Previsto'] * 100
print(df)
print("\n")

#Imprimindo máquinas com melhor desempenho
maior_que_50 = df['Peças boas'] > 50

#Imprime as maquinas que fizeram mais de 50 peças boas
print("Maquinas com bom aproveitamento (mais de 50 peças boas)\n")
print(df[maior_que_50])
print("\n")

#Descrição da tabela
print("Descrição da tabela:\n")
print(df.describe())
print("\n")

#Informações sobre a tabela
print("Informações sobre a tabela:\n")
print(df.info())
print("\n")
