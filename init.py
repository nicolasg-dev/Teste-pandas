import pandas as pd
print("Pandas funcionando! Versão:\n", pd.__version__)

df = pd.read_excel("Table.xlsx")

print("Tabela inicialmente implementada:\n")
print(df)
print("\n")


print("Peças > 50\n")
print(df[df['Peças boas'] > 50])
print("\n")

print("Descrição da tabela:\n")
print(df.describe())
print("\n")

print("Informações sobre a tabela:\n")
print(df.info())
print("\n")