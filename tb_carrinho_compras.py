import pyodbc as sql
from tb_Produtos_sql import Gerar_Conexao

def tabela_carrinho():
    conexao = Gerar_Conexao()
    cursor = conexao.cursor()

    cursor.execute('''
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Carrinho')
        CREATE TABLE Carrinho (
            ID_Carrinho INT IDENTITY (1,1) PRIMARY KEY,
            Nome_Cliente VARCHAR(100) NOT NULL,
                ID_Prato int
                    references Cardapio(ID_Cardapio) not null,
            Prato VARCHAR(100) NOT NULL,
            Nome_Prato VARCHAR(100) NOT NULL,
            Quantidade INT NOT NULL,
            Preco DECIMAL(10, 2) NOT NULL
        );
    ''')
    conexao.commit()

if __name__ == "__main__":
    tabela_carrinho()
    print("Tabela 'Carrinho' criada com sucesso!")