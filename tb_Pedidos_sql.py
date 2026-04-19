from tb_Produtos_sql import Gerar_Conexao
import pyodbc as sql
import os 

def tabela_pedidos():
    conexao = Gerar_Conexao()
    cursor = conexao.cursor()

    cursor.execute('''
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Pedidos')
        CREATE TABLE Pedidos (
            ID_Pedido INT IDENTITY (1,1) PRIMARY KEY,
            Nome_Cliente VARCHAR(100) NOT NULL,
                ID_Carrinho int
                    references Carrinho(ID_Carrinho) not null,
            Prato VARCHAR(100) NOT NULL,
                ID_Prato int
                    references Cardapio(ID_Cardapio) not null,
            Endereco VARCHAR(255) NOT NULL,
            Forma_Pagamento CHAR(25) NOT NULL
        );
    ''')
    conexao.commit()

if __name__ == "__main__":
    tabela_pedidos()
    print("Tabela 'Pedidos' criada com sucesso!")