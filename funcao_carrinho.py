from funcao_fazer_pedido import fazer_pedido
from tb_Produtos_sql import Gerar_Conexao
import pandas as pd
from tabulate import tabulate
import emoji as emj

def carrinho():
    
    conexao = Gerar_Conexao()
    df_carrinho = pd.read_sql('SELECT Prato, Nome_Prato, Quantidade, Preco FROM Carrinho', conexao)
    df_carrinho['Preco'] = 'R$' + df_carrinho['Preco'].astype(str)

    print(emj.emojize('='*20 + ':shopping_cart: CARRINHO ' + '='*20 + '\n'))
    print(tabulate(df_carrinho, headers=['Prato', 'Nome do Prato', 'Quantidade', 'Preço'] , tablefmt='fancy_grid', showindex=False))    


