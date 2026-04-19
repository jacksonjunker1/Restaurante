import pyodbc as sql
import pandas as pd
import os 

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

def Tabela_Reservas():
    cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Reservas')
        CREATE TABLE Reserva (
            ID_Reserva INT PRIMARY KEY IDENTITY(1,1),
            Nome VARCHAR(100) NOT NULL,
            Data_Reserva VARCHAR(10) NOT NULL, 
            Hora_Reserva VARCHAR(10) NOT NULL,  
            Numero_Pessoas INT NOT NULL
    );
    ''')

if __name__ == "__main__":
    Tabela_Reservas()
    conexao.commit()
    print("Tabela Reservas Criada com Sucesso...")