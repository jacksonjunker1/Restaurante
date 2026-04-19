from tb_Produtos_sql import Gerar_Conexao
from funcao_carregar_dados import carregar_dados
from tb_Reservas_sql import Tabela_Reservas 

def fazer_Reserva():
    cursor = Gerar_Conexao()
    print('='*20 + 'Fazer Reserva' + '='*20)
    nome = input('Digite seu nome: ')
    data = input('Digite a data da reserva (DD/MM/AAAA): ')
    hora = input('Digite a hora da reserva (HH:MM): ')
    numero_pessoas = input('Digite o número de pessoas: ')

    cursor.execute('''
        INSERT INTO Reserva (Nome, Data_Reserva, Hora_Reserva, Numero_Pessoas)
        VALUES (?, ?, ?, ?)
    ''', (nome, data, hora, numero_pessoas))
    cursor.commit()


    print(f'Reserva feita com sucesso! Nome: {nome}, Data: {data}, Hora: {hora}, Número de Pessoas: {numero_pessoas}')

    return nome, data, hora, numero_pessoas