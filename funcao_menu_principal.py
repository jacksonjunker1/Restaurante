from tb_Produtos_sql import Gerar_Conexao
from funcao_mostrar_cardapio import mostrar_cardapio
from funcao_carregar_dados import carregar_dados
from funcao_fazer_pedido import fazer_pedido
from funcao_fazer_reserva import fazer_Reserva
from funcao_buscar_pratos import Busca_Pratos
from funcao_carrinho import carrinho
from funcao_minhas_reservas import mostrar_reservas
import pandas as pd
from tabulate import tabulate
import os 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    print('='*20 + 'Bem Vindo ao Restaurante' + '='*20)
    print('''
        1 → Ver Cardápio Completo
        2 → Fazer Pedido
        3 → Fazer Reserva
        4 → Ver Carrinho
        5 → Ver Minhas Reservas
        0 → Sair do Sistema
    ''')

    if __name__ == "__main__":
        # Tudo o que tiver 'input' ou 'print' do menu antigo deve ficar indentado aqui
        print("===========Bem Vindo ao Restaurante===========")
    
    while True:  # O programa ficará rodando aqui até você mandar parar
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_cardapio()
            input("\nPresione ENTER para continuar...") # Trava para você conseguir ler
        elif opcao == "0":
            print("Saindo do sistema...")
            break  # Única forma de sair do loop e fechar o programa
        
        if opcao == "1":
            limpar_tela()
            mostrar_cardapio()
        elif opcao == "2":
            limpar_tela()
            Busca_Pratos()
        elif opcao == "3":
            limpar_tela()
            fazer_Reserva()
        elif opcao == "4":
            limpar_tela()
            carrinho()
        elif opcao == "5":
            limpar_tela()
            mostrar_reservas()
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
