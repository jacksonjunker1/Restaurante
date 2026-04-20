from tb_Produtos_sql import Gerar_Conexao
import pyodbc as sql
import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style, init
init(autoreset=True)


def mostrar_reservas():
    conexao = Gerar_Conexao()
    cursor = conexao.cursor()
    
    nome = input("Digite seu nome para ver suas reservas: ")
    cursor.execute('''
    SELECT Nome, Data_Reserva, Hora_Reserva, Numero_Pessoas 
    FROM Reserva WHERE Nome = ?''', (nome,)
    )
    headers = [
        f"{Fore.CYAN}Nome{Style.RESET_ALL}", 
        f"{Fore.BLACK}Data da Reserva{Style.RESET_ALL}", 
        f"{Fore.BLACK}Hora da Reserva{Style.RESET_ALL}", 
        f"{Fore.YELLOW}Número de Pessoas{Style.RESET_ALL}"
    ]

    print(Fore.YELLOW + " \nSuas reservas:\n " + Style.RESET_ALL)
    print(tabulate(cursor.fetchall(), headers=headers, tablefmt='psql'))