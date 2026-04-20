from funcao_menu_principal_Cliente import menu_principal_Cliente
from funcao_menu_principal_Adim import menu_principal_Administrador
from colorama import Fore, Style, init
init(autoreset=True)
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

Margem = '                '

print(Fore.YELLOW + '=' * 20 + 'Bem Vindo ao Restaurante' + '=' * 20 + '\n')
print(Fore.YELLOW + '=' * 20 + 'Selecione o Tipo de Usuário' + '=' * 20 + '\n')
print( 
    Fore.YELLOW + f'{Margem}1 → ' + Fore.WHITE + 'Cliente\n' + 
    Fore.YELLOW + f'{Margem}2 → ' + Fore.WHITE + 'Administrador\n' + 
    Fore.YELLOW + f'{Margem}0 → ' + Fore.WHITE + 'Sair do Sistema'
    )

opcao = int(input(Fore.CYAN + '\nEscolha uma opção: '))

if opcao == 1:
    limpar_tela()
    menu_principal_Cliente()
elif opcao == 2:
    limpar_tela()
    menu_principal_Administrador()
else:
    print('Opção inválida. Por favor, escolha uma opção válida.')   