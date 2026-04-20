from funcao_mostrar_cardapio import mostrar_cardapio
from funcao_fazer_reserva import fazer_Reserva
from funcao_buscar_pratos import Busca_Pratos
from funcao_carrinho import carrinho
from funcao_minhas_reservas import mostrar_reservas
import pandas as pd
import emoji
import os 
from colorama import Fore, Style, init
init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal_Cliente():
    margem = '                '
    print(Fore.YELLOW + ('=')*20 + 'Bem Vindo ao Restaurante ' + emoji.emojize('=')*20+'\n')
    print(Fore.YELLOW + '='*20 + emoji.emojize(':bust_in_silhouette: Menu Cliente :bust_in_silhouette:') + '='*20 + '\n')
    print(
            Fore.YELLOW + f'{margem}1 →' + Fore.WHITE + ' Ver Cardápio Completo\n' +
            Fore.YELLOW + f'{margem}2 →' + Fore.WHITE + ' Fazer Pedido\n' +
            Fore.YELLOW + f'{margem}3 →' + Fore.WHITE + ' Fazer Reserva\n' +
            Fore.YELLOW + f'{margem}4 →' + Fore.WHITE + ' Ver Carrinho\n' +
            Fore.YELLOW + f'{margem}5 →' + Fore.WHITE + ' Ver Minhas Reservas\n'
            + Fore.RED + f'{margem}0 → Sair do Sistema'
        )
    if __name__ == "__main__":
        # Tudo o que tiver 'input' ou 'print' do menu antigo deve ficar indentado aqui
        print(Fore.YELLOW + "=========== Bem Vindo ao Restaurante ===========")
    
    while True:  # O programa ficará rodando aqui até você mandar parar
        opcao = input(Fore.CYAN + "\nEscolha uma opção: ")

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
