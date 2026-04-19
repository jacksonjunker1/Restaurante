from tb_Produtos_sql import Gerar_Conexao
import pandas as pd
from tabulate import tabulate
import os 

def carregar_dados():
    global df_cardapio,conexao
    conexao = Gerar_Conexao()
    query = "SELECT ID_Cardapio, Categoria, Prato, Descricao, Preco FROM Cardapio"
    df_cardapio = pd.read_sql(query, conexao)
    return df_cardapio