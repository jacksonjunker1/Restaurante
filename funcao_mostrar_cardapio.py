from tb_Produtos_sql import Gerar_Conexao
import pandas as pd
from tabulate import tabulate
import os 

def mostrar_cardapio(imprimir=True):
    global conexao, df_cardapio

    conexao = Gerar_Conexao()

    query = "SELECT ID_Cardapio,Prato, Descricao, Preco FROM Cardapio"
    df_cardapio = pd.read_sql(query, conexao)


    if imprimir:
        print("\n" + "="*20 + " CARDÁPIO " + "="*20)
        print(tabulate(df_cardapio, headers=['Numero','Prato', 'Descrição', 'Preço'] , tablefmt='fancy_grid', showindex=False))

    return df_cardapio