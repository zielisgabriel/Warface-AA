import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear') #Esse comando vai apagar o que tinha no terminal (apenas estético)

#Carregar o dataset
tabela = pd.read_csv("netflix_titles.csv")

#1 Quais colunas estão presentes no dataset?
colunas = tabela.columns
print('1. Colunas existentes:', colunas)

#2 Quantos filmes estão disponíveis na Netflix?
lista_filmes = tabela[tabela['type'] == 'Movie'].shape[0]
print('\n2. Quantidade de filmes disponíveis:', lista_filmes)

#3 Quem são os 5 diretores com mais filmes e séries na plataforma?
lista_diretores = tabela['director'].value_counts().head(5)
print('\n3. Os 5 diretores com mais filmes e séries na plataforma:')
print(lista_diretores)

#4 Quais diretores também atuaram como atores em suas próprias produções?
diretores_atores = tabela[tabela.apply(lambda row: isinstance(row['director'], str) and isinstance(row['cast'], str) and row['director'] in row['cast'], axis=1)]
diretores_atores_unicos = diretores_atores['director'].unique()
print('\n4. Diretores que atuaram em suas próprias produções:', diretores_atores_unicos)

#Explore o dataset e compartilhe um insight ou número que você considere interessante
#Ex: Filmes com mais de 3 horas de duração
filmes = tabela[tabela['type'] == 'Movie'] #Filtrar apenas os filmes
filmes = filmes.copy() #Copiar o DataFrame para evitar o aviso de SettingWithCopyWarning
filmes['duration_min'] = pd.to_numeric(filmes['duration'].str.replace(' min', ''), errors='coerce') #Converter a coluna 'duration' para minutos (removendo 'min' e convertendo para int)
filmes_longos = filmes[filmes['duration_min'] > 180] #Filtrar filmes com duração maior que 120 minutos (2 horas)
print("\n5. Filmes com mais de 3 horas de duração:\n")
print(filmes_longos[['title', 'duration']])