from tb_Produtos_sql import Gerar_Conexao
from funcao_mostrar_cardapio import mostrar_cardapio
from funcao_carregar_dados import carregar_dados
import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style, init
init(autoreset=True)
import os 
margem = '                '
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def Busca_Pratos():

    carregar_dados()
    from funcao_fazer_pedido import fazer_pedido

    conexao = Gerar_Conexao()

    while True:
        limpar_tela()
        print(Fore.YELLOW + "="*20 + " MENU DE BUSCA " + "="*20)
        
        print(
            Fore.YELLOW + f'{margem}1 →' + Fore.WHITE + ' Entradas\n' +
            Fore.YELLOW + f'{margem}2 →' + Fore.WHITE + ' Carne\n' +
            Fore.YELLOW + f'{margem}3 →' + Fore.WHITE + ' Peixe\n' +
            Fore.YELLOW + f'{margem}4 →' + Fore.WHITE + ' Vegano\n' +
            Fore.YELLOW + f'{margem}5 →' + Fore.WHITE + ' Massas\n' +
            Fore.YELLOW + f'{margem}6 →' + Fore.WHITE + ' Sushi \n' +
            Fore.YELLOW + f'{margem}7 →' + Fore.WHITE + ' Bebidas\n' +
            Fore.YELLOW + f'{margem}8 →' + Fore.WHITE + ' Sobremesas\n'
            )
        
        opcao = input(Fore.BLUE + "Escolha uma das opções acima: ").capitalize()
        
        query = f'''SELECT ID_Cardapio, Prato, Descricao, Preco 
        FROM Cardapio
        WHERE Categoria = '{opcao}';'''
        df_cardapio = pd.read_sql(query, conexao)
        df_cardapio['Preco'] = 'R$' + df_cardapio['Preco'].astype(str)

        headers = [
            f"{Fore.CYAN}Numero{Style.RESET_ALL}", 
            f"{Fore.BLACK}Prato{Style.RESET_ALL}", 
            f"{Fore.BLACK}Descrição{Style.RESET_ALL}", 
            f"{Fore.YELLOW}Preço{Style.RESET_ALL}"
        ]


        match opcao:

            case 'Entradas':
                limpar_tela()
                print(Fore.YELLOW + "\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(Fore.CYAN + tabulate(df_cardapio, headers=headers , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Carne':
                limpar_tela()
                print(Fore.YELLOW + "\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(Fore.CYAN + tabulate(df_cardapio, headers=headers , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Peixe':
                limpar_tela()
                print(Fore.YELLOW + "\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(Fore.CYAN + tabulate(df_cardapio, headers=headers , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Vegano':
                limpar_tela()
                print(Fore.YELLOW + "\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(Fore.CYAN + tabulate(df_cardapio, headers=headers , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Massas':
                limpar_tela()
                print(Fore.YELLOW + "\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(Fore.CYAN + tabulate(df_cardapio, headers=headers , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Sushi':
                limpar_tela()
                print(Fore.YELLOW + "\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(Fore.CYAN + tabulate(df_cardapio, headers=headers , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Bebidas':
                limpar_tela()
                print(Fore.YELLOW + "\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(Fore.CYAN + tabulate(df_cardapio, headers=headers , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Sobremesas':
                limpar_tela()
                print(Fore.YELLOW + "\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(Fore.CYAN + tabulate(df_cardapio, headers=headers , tablefmt='fancy_grid', showindex=False)) 
                fazer_pedido()
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")