from funcao_menu_principal_Cliente import menu_principal_Cliente
from tb_Produtos_sql import Gerar_Conexao
import pandas as pd
from funcao_carrinho import carrinho
from tabulate import tabulate
import emoji
import os 
from colorama import Fore, Style, init
init(autoreset=True)

margem = '             '

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal_Administrador():
    conexao = Gerar_Conexao()
    cursor = conexao.cursor()

    
    print(Fore.YELLOW + '='*20 + 'Bem Vindo ao Restaurante' + '='*20+'\n')
    print(Fore.YELLOW + '='*20 + emoji.emojize(':hammer_and_wrench: Menu Administrativo :hammer_and_wrench:') + '='*20 + '\n')
    print(
        Fore.YELLOW + f'{margem}1 →' + Fore.WHITE + ' Ver Reservas\n' +
        Fore.YELLOW + f'{margem}2 →' + Fore.WHITE + ' Ver Pedidos\n' +
        Fore.YELLOW + f'{margem}3 →' + Fore.WHITE + ' Funcionarios\n' +
        Fore.RED + f'{margem}0 → Sair do Sistema'
        )
    
    opcao = int(input(Fore.CYAN + '\n Escolha Uma Opcão Acima: '))
    

    while True:

        query_reserva = 'SELECT Nome, Data_Reserva, Hora_Reserva, Numero_Pessoas FROM Reserva'
        query_funcionarios = 'SELECT * FROM Funcionarios'
        df_Reservas = pd.read_sql(query_reserva,conexao)
        df_funcionarios = pd.read_sql(query_funcionarios,conexao)
        
        headers_Reserva = [
            f"{Fore.WHITE}Nome{Style.RESET_ALL}", 
            F"{Fore.CYAN}Data_Reserva{Style.RESET_ALL}", 
            f"{Fore.LIGHTBLUE_EX}Hora_Reserva{Style.RESET_ALL}", 
            f"{Fore.GREEN}Numero_Pessoas{Style.RESET_ALL}"
            ]
        
        headers_funcionario = [
            f"{Fore.YELLOW}ID_Funcionario{Style.RESET_ALL}", 
            F"{Fore.YELLOW}Nome{Style.RESET_ALL}", 
            f"{Fore.YELLOW}Cargo{Style.RESET_ALL}", 
            f"{Fore.YELLOW}Departamento{Style.RESET_ALL}",
            f"{Fore.YELLOW}Data Admissao{Style.RESET_ALL}",
            f"{Fore.YELLOW}Salario{Style.RESET_ALL}"
            ]
        
        match opcao:

            case 1:
                limpar_tela()
                print(Fore.YELLOW + '='*20 + ' Reservas ' + '='*20 + '\n')
                print(tabulate(df_Reservas, headers = headers_Reserva, tablefmt = 'fancy_grid', showindex=False))
                break
            case 2:
                limpar_tela()
                carrinho()
                break
            case 3:
                limpar_tela()
                print(Fore.LIGHTBLACK_EX + '='*20 + Fore.MAGENTA + ' Funcionarios ' + Fore.LIGHTBLACK_EX + '='*20 + '\n')
                print(
                    f"{Fore.YELLOW} {margem} 1 → {Fore.WHITE} Ver Todos Os Funcionarios\n"
                    f"{Fore.YELLOW} {margem} 2 → {Fore.WHITE} Filtrar Por Nome\n"
                    f"{Fore.YELLOW} {margem} 3 → {Fore.WHITE} Filtrar Por Cargo\n"
                    f"{Fore.YELLOW} {margem} 4 → {Fore.WHITE} Filtrar Por Salario\n"
                    f"{Fore.YELLOW} {margem} 5 → {Fore.WHITE} Alterar Dados\n"
                    )
                opcao = int(input('Escolhe uma Opção Acima: '))

                if (opcao == 1):                
                    print(tabulate(df_funcionarios, headers= headers_funcionario, tablefmt='fancy_grid', showindex=False))
                elif(opcao == 2):
                    nome_funcionario = input('Digite o nome do funcionario que deseja buscar: ').capitalize()
                    query = f'''select ID_Funcionarios, Nome, Cargo,Departamento, Data_admissao, Salario 
                        from Funcionarios WHERE Nome like '%{nome_funcionario}%';
                        '''
                    df_funcionario = pd.read_sql(query,conexao)
                    print(tabulate(df_funcionario, headers= headers_funcionario, tablefmt='fancy_grid', showindex=False))
                elif(opcao == 3):
                    Cargo_funcionario = input('Digite o Cargo do funcionario que deseja buscar: ').capitalize()
                    query = f'''select ID_Funcionarios, Nome, Cargo,Departamento, Data_admissao, Salario 
                        from Funcionarios WHERE Cargo like '%{Cargo_funcionario}%';
                        '''
                    df_funcionario = pd.read_sql(query,conexao)
                    print(tabulate(df_funcionario, headers= headers_funcionario, tablefmt='fancy_grid', showindex=False))
                elif(opcao == 4):
                    Salario_funcionario = float(input('Digite o Salario que deseja buscar: '))
                    query = f'''select ID_Funcionarios, Nome, Cargo,Departamento, Data_admissao, Salario 
                        from Funcionarios WHERE Salario >= '{Salario_funcionario}';
                        '''
                    df_funcionario = pd.read_sql(query,conexao)

                    if (Salario_funcionario > df_funcionario['Salario'].values).all():
                        print('Não existe nenhum funcionario com esse salario')
                    else:
                        print(tabulate(df_funcionario, headers= headers_funcionario, tablefmt='fancy_grid', showindex=False)) 
                elif(opcao == 5):
                    print(Fore.YELLOW + '='*20 + " Alterar Dados Funcionarios " + '='*20 + '\n')
                    print(
                    f"{Fore.YELLOW} {margem} 1 → {Fore.WHITE} Alterar Salario\n"
                    f"{Fore.YELLOW} {margem} 2 → {Fore.WHITE} Alterar Cargo\n"
                    f"{Fore.YELLOW} {margem} 3 → {Fore.WHITE} Desligar Funcionario\n"
                    )
                    opcao = int(input(Fore.CYAN + 'Escolha uma Opção Acima: ' + Style.RESET_ALL))

                    if (opcao == 1):
                        nome_funcionario = input('Digite O Nome Do funcionario Que Deseja Alterar Salario: ').capitalize()
                        novo_salario = float(input(f'Digite O Novo Salario de {nome_funcionario}: '))

                        query = f'''UPDATE Funcionarios SET Salario = {novo_salario}
                            WHERE Nome like '%{nome_funcionario}%';'''
                        cursor.execute(query)
                        conexao.commit()
                        print('Dados Auterados com Sucesso...')
                    if (opcao == 2):
                        nome_funcionario = input('Digite O Nome Do funcionario Que Deseja Alterar Cargo: ').capitalize()
                        novo_cargo = input(f'Digite O Novo Cargo de {nome_funcionario}: ').capitalize()

                        df_funcionario = pd.read_sql("SELECT * FROM Funcionarios", conexao)
                        df_funcionario['Cargo'] = df_funcionario['Cargo'].str.strip()
                        filtro_salario = df_funcionario.loc[df_funcionario['Cargo'] == novo_cargo, 'Salario']

                        if not filtro_salario.empty:

                            novo_salario = filtro_salario.values[0]

                            query = f"""
                                    UPDATE Funcionarios 
                                    SET Cargo = '{novo_cargo}', Salario = {novo_salario} 
                                    WHERE Nome LIKE '%{nome_funcionario}%'
                                    """
                            cursor.execute(query)
                            conexao.commit()
        
                            print(f'\n{nome_funcionario} promovido a {novo_cargo}!')
                            print(f'Salário atualizado automaticamente para R$ {novo_salario:.2f}')
                        else:
                            print(f'\nErro: O cargo "{novo_cargo}" não existe na base de dados.')
                            print('Não foi possível definir o novo salário automaticamente.')
                    if(opcao == 3):
                        nome_funcionario = input('Digite O Nome Do funcionario Que Deseja Desligar: ').capitalize()

                        query = f'''DELETE FROM Funcionarios
                            WHERE Nome like '%{nome_funcionario}%';'''
                        cursor.execute(query)           
                        conexao.commit()
                        print('Funcionario Desligado com Sucesso...')
                break
            case 0:
                print('Fim do Programa...')
                break
            case _:
                print('Opção Invalida, Por Favor Escolha Uma Opção Válida.')
                return