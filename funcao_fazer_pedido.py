from tb_Produtos_sql import Gerar_Conexao
from funcao_mostrar_cardapio import mostrar_cardapio
from funcao_carregar_dados import carregar_dados
from funcao_buscar_pratos import Busca_Pratos
import pandas as pd
from tabulate import tabulate
import sys


def fazer_pedido():
    conexao = Gerar_Conexao()
    cursor = conexao.cursor()

    df_cardapio = mostrar_cardapio(imprimir=False)
    quantidade = 0
    valor_compra = 0
    
    while True:
        print('='*20 + 'Fazer Pedidos' + '='*20 + '\n')
        
        nome_cliente = input('Digite seu nome: ')
        Prato = int(input('\nQual Prato Deseja (peça pelo numero): '))
        Endereco = input('\nDigite o endereço para entrega: ')
        forma_pagamento = input('\nDigite a forma de pagamento (Cartão ou Dinheiro): ').capitalize()
        quantidade += 1
        valor_compra = df_cardapio.loc[df_cardapio['ID_Cardapio'] == Prato, 'Preco'].values[0]
        ID_Cardapio = df_cardapio.loc[df_cardapio['ID_Cardapio'] == Prato, 'ID_Cardapio'].values[0]
        nome_prato = df_cardapio.loc[df_cardapio['ID_Cardapio'] == Prato, 'Prato'].values[0]

# CONVERSÃO: Transformamos o valor do pandas em um inteiro comum do Python
        # Isso resolve o erro 'numpy.int64' que travou o seu terminal agora
        ID_Cardapio_SQL = int(ID_Cardapio)
        valor_compra_sql = float(valor_compra)
        # 1. LÓGICA DO CARRINHO
        cursor.execute('SELECT Quantidade FROM Carrinho WHERE Nome_Cliente = ? AND ID_Prato = ?', (nome_cliente, ID_Cardapio_SQL))
        item_existe = cursor.fetchone()

        if item_existe:
            # Se ja existe, atualiza a quantidade e o preco
            cursor.execute('''
                UPDATE Carrinho 
                SET Quantidade = Quantidade + 1, Preco = Preco + ? 
                WHERE Nome_Cliente = ? AND ID_Prato = ?
            ''', (valor_compra_sql, nome_cliente, ID_Cardapio_SQL))
        else:
            # Se não existe, cria a linha
            cursor.execute('''
                INSERT INTO Carrinho (Nome_Cliente, ID_Prato,Prato, Nome_Prato, Quantidade, Preco) 
                VALUES (?, ?, ?, ?, 1, ?)
            ''', (nome_cliente, ID_Cardapio_SQL, Prato, nome_prato, valor_compra_sql))

        conexao.commit()

        # 2. BUSCA O ID DO CARRINHO GERADO
        cursor.execute('SELECT MAX(ID_Carrinho) FROM Carrinho WHERE Nome_Cliente = ?', (nome_cliente,))
        resultado_id = cursor.fetchone()
        
        if resultado_id and resultado_id[0] is not None:
            ID_Carrinho_Gerado = resultado_id[0]
        else:
            ID_Carrinho_Gerado = 0 

        # 3. LÓGICA DA TABELA PEDIDOS
        cursor.execute('''
            INSERT INTO Pedidos (Nome_Cliente, ID_Carrinho, Prato, ID_Prato, Endereco, Forma_Pagamento)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome_cliente, ID_Carrinho_Gerado, Prato, ID_Cardapio_SQL, Endereco, forma_pagamento))

        conexao.commit()

        if Prato in df_cardapio['ID_Cardapio'].values:
            
            print(f'\nCompra Finalizada com sucesso! Valor: R$ {valor_compra:.2f}')
            print(f'\nEndereço de entrega: {Endereco}')
            print(f'\nForma de pagamento: {forma_pagamento}')

            opcao = input('\nDeseja fazer outro pedido? (S/N): ').capitalize()

        if opcao == 'S':
            Busca_Pratos()
            continue
        else:
            print('Obrigado por comprar conosco!')
            sys.exit()
            break     # Sai do while e encerra o programa AGORA

    return valor_compra, Endereco, forma_pagamento
