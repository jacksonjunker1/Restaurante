import pyodbc as sql
import pandas as pd 
import os

caminho_funcionarios = r"C:\Users\jacks\OneDrive\Documentos\restaurante\Banco_De_Dados_SQL\funcionarios.csv"

def DataFrame_Fncionarios():
    global arquivo_Funcionarios
    try:
        if os.path.exists(caminho_funcionarios):
            arquivo_Funcionarios = pd.read_csv(caminho_funcionarios)
            print('Arquivo, Carregado Com Sucesso...')
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")

    return arquivo_Funcionarios

if __name__ == '__main__' :
    DataFrame_Fncionarios()
    dados_funcionarios = list(map(tuple, arquivo_Funcionarios.values))

def gerar_conexao():
    global conexao 
    conexao = sql.connect(
        'DRIVER={SQL Server};'
        'SERVER=JACKSON;'
        'DATABASE=Restaurante;'
        'Trusted_Connection=yes;'
    )

    return conexao

if __name__ == '__main__':
    gerar_conexao()
    cursor = conexao.cursor()

def tabela_funcionarios():
    cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Funcionarios')
    CREATE TABLE Funcionarios(
        ID_Funcionarios int identity (100,1) primary key,
        Nome varchar(100) not null,
        Cargo char(35) not null,
        Departamento char(35) not null,
        Data_admissao date not null,
        Salario decimal(10,2) not null
        
        )
    ''')

    for funcionario in dados_funcionarios:
        cursor.execute('''
        Insert into Funcionarios(Nome,Cargo,Departamento,Data_admissao,Salario) values(?,?,?,?,?)''',
        funcionario
        )

if __name__ == "__main__":
    tabela_funcionarios()
    conexao.commit()
    print(f"Tabela criada com sucesso e {len(dados_funcionarios)} dados inseridos com sucesso...")
