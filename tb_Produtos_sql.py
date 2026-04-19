import pyodbc as sql
import pandas as pd
import os
import random

pd.set_option('display.max_rows', None)
caminho_Cardapio = r"C:\Users\jacks\OneDrive\Documentos\restaurante\Banco_De_Dados_SQL\Produtos.csv"

def DataFrame_Cardapio():
    global arquivo_Cardapio
    if (os.path.exists(caminho_Cardapio)):
        arquivo_Cardapio = pd.read_csv(caminho_Cardapio)
        print("Arquivo Carregado Com Sucesso...")
    else:
        print("Erro ao carregar arquivo...")

    return arquivo_Cardapio

if __name__ == "__main__":
    DataFrame_Cardapio()
    dados_Cardapio = list(map(tuple, arquivo_Cardapio.values))

def Gerar_Conexao():
    global conexao
    conexao = sql.connect(
        'DRIVER={SQL Server};'
        'SERVER=JACKSON;'
        'DATABASE=Restaurante;'
        'Trusted_Connection=yes;'
    )
    return conexao

if __name__ == "__main__":
    Gerar_Conexao()
    cursor = conexao.cursor()

def Tabela_Cardapio():
    cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Cardapio')
        Create table Cardapio (
            ID_Cardapio int identity (1,1) primary key,
            Categoria char(25) not null,
            Prato varchar(100) not null,
            Descricao varchar(100) not null,
            Preco decimal(10,2) not null
        )

    ''')
    for prato in dados_Cardapio:
        cursor.execute('''
            INSERT INTO Cardapio (Categoria, Prato, Descricao, Preco) values (?,?,?,?)''',
            prato
            )
if __name__ == "__main__":
    Tabela_Cardapio()
    conexao.commit()
    print(f"Tabela Cardapio Criada e {len(dados_Cardapio)} Dados Inseridos com Sucesso...")
