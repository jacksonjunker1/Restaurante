from tb_Produtos_sql import Gerar_Conexao
import pyodbc as sql
import pandas as pd
from tabulate import tabulate


def mostrar_reservas():
    conexao = Gerar_Conexao()
    cursor = conexao.cursor()
    
    nome = input("Digite seu nome para ver suas reservas: ")
    cursor.execute('''
    SELECT Nome, Data_Reserva, Hora_Reserva, Numero_Pessoas 
    FROM Reserva WHERE Nome = ?''', (nome,)
    )
    print(tabulate(cursor.fetchall(), headers=['Nome', 'Data da Reserva', 'Hora da Reserva', 'Número de Pessoas'], tablefmt='psql'))