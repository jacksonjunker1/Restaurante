from funcao_fazer_pedido import fazer_pedido
from tb_Produtos_sql import Gerar_Conexao
import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style, init
init(autoreset=True)
import emoji as emj

def carrinho():
    
    conexao = Gerar_Conexao()
    df_carrinho = pd.read_sql('SELECT Prato, Nome_Prato, Quantidade, Preco FROM Carrinho', conexao)
    df_carrinho['Preco'] = 'R$' + df_carrinho['Preco'].astype(str)
    headers = [
        f"{Fore.LIGHTBLACK_EX}Prato{Style.RESET_ALL}", 
        f"{Fore.WHITE}Nome do Prato{Style.RESET_ALL}", 
        f"{Fore.CYAN}Quantidade{Style.RESET_ALL}", 
        f"{Fore.YELLOW}Preço{Style.RESET_ALL}"
    ]

    print(emj.emojize(Fore.YELLOW + '='*20 + ' :shopping_cart: CARRINHO ' + '='*20 + '\n'))
    print(tabulate(df_carrinho, headers=headers , tablefmt='fancy_grid', showindex=False))    

