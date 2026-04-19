from tb_Produtos_sql import Gerar_Conexao
from funcao_mostrar_cardapio import mostrar_cardapio
from funcao_carregar_dados import carregar_dados
import pandas as pd
from tabulate import tabulate
import os 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def Busca_Pratos():

    carregar_dados()
    from funcao_fazer_pedido import fazer_pedido

    conexao = Gerar_Conexao()

    while True:
        limpar_tela()
        print("="*20 + " MENU DE BUSCA " + "="*20)
        
        print('''
            1 → Entradas
            2 → Carne
            3 → Peixe
            4 → Vegano
            5 → Massas
            6 → Sushi
            7 → Bebidas
            8 → Sobremesas
            ''')
        
        opcao = input("Escolha uma das opções acima: ").capitalize()
        
        query = f'''SELECT ID_Cardapio, Prato, Descricao, Preco 
        FROM Cardapio
        WHERE Categoria = '{opcao}';'''
        df_cardapio = pd.read_sql(query, conexao)
        df_cardapio['Preco'] = 'R$' + df_cardapio['Preco'].astype(str)

        match opcao:

            case 'Entradas':
                limpar_tela()
                print("\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(tabulate(df_cardapio, headers=['Numero','Prato', 'Descrição', 'Preço'] , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Carne':
                limpar_tela()
                print("\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(tabulate(df_cardapio, headers=['Numero','Prato', 'Descrição', 'Preço'] , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Peixe':
                limpar_tela()
                print("\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(tabulate(df_cardapio, headers=['Numero','Prato', 'Descrição', 'Preço'] , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Vegano':
                limpar_tela()
                print("\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(tabulate(df_cardapio, headers=['Numero','Prato', 'Descrição', 'Preço'] , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Massas':
                limpar_tela()
                print("\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(tabulate(df_cardapio, headers=['Numero','Prato', 'Descrição', 'Preço'] , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Sushi':
                limpar_tela()
                print("\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(tabulate(df_cardapio, headers=['Numero','Prato', 'Descrição', 'Preço'] , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Bebidas':
                limpar_tela()
                print("\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(tabulate(df_cardapio, headers=['Numero','Prato', 'Descrição', 'Preço'] , tablefmt='fancy_grid', showindex=False))
                fazer_pedido()
                break
            case 'Sobremesas':
                limpar_tela()
                print("\n" + "="*20 + " CARDÁPIO " + "="*20 + "\n")
                print(tabulate(df_cardapio, headers=['Numero','Prato', 'Descrição', 'Preço'] , tablefmt='fancy_grid', showindex=False)) 
                fazer_pedido()
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")