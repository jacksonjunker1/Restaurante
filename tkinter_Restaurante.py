import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

class SistemaRestaurante:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão Gastronômica - SQL Server")
        self.root.geometry("1100x700")
        
        # --- CONEXÃO SQL SERVER ---
        try:
            dados_conexao = (
                "Driver={SQL Server};"
                "Server=JACKSON;" # Ex: DESKTOP-ABC ou localhost
                "Database=Restaurante;"     # Nome do banco de dados
                "Trusted_Connection=yes;"
            )
            self.conexao = pyodbc.connect(dados_conexao)
            self.cursor = self.conexao.cursor()
            print("Conectado ao SQL Server com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro de Conexão", f"Não foi possível conectar:\n{e}")

        # Estilo
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.create_widgets()
        self.atualizar_tabela()

    def create_widgets(self):
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(expand=True, fill="both", padx=10, pady=10)

        self.aba_cardapio = ttk.Frame(self.tabs)
        self.aba_pedido = ttk.Frame(self.tabs)
        self.aba_reserva = ttk.Frame(self.tabs)

        self.tabs.add(self.aba_cardapio, text=" 🍽️ Cardápio Completo ")
        self.tabs.add(self.aba_pedido, text=" 🛒 Fazer Pedido ")
        self.tabs.add(self.aba_reserva, text=" 📅 Agendar Reserva ")

        self.setup_cardapio()
        self.setup_pedido()
        self.setup_reserva()

    # --- ABA 1: CARDÁPIO ---
    def setup_cardapio(self):
        tk.Label(self.aba_cardapio, text="Nosso Cardápio", font=("Arial", 18, "bold"), pady=15).pack()
        
        frame_tabela = tk.Frame(self.aba_cardapio)
        frame_tabela.pack(expand=True, fill="both", padx=20, pady=5)

        colunas = ("id", "prato", "descricao", "preco")
        self.tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("prato", text="Prato")
        self.tree.heading("descricao", text="Descrição Detalhada")
        self.tree.heading("preco", text="Preço")

        self.tree.column("id", width=60, anchor="center")
        self.tree.column("prato", width=200)
        self.tree.column("descricao", width=500)
        self.tree.column("preco", width=100, anchor="center")

        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        
        frame_tabela.grid_columnconfigure(0, weight=1)
        frame_tabela.grid_rowconfigure(0, weight=1)

        ttk.Button(self.aba_cardapio, text="🔄 Recarregar Cardápio", command=self.atualizar_tabela).pack(pady=15)

    def atualizar_tabela(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        try:
            self.cursor.execute("SELECT ID_Cardapio, Prato, Descricao, Preco FROM Cardapio")
            for linha in self.cursor.fetchall():
                self.tree.insert("", tk.END, values=(linha[0], linha[1], linha[2], f"R$ {linha[3]:.2f}"))
        except Exception as e:
            print(f"Erro ao carregar cardápio: {e}")

    # --- ABA 2: PEDIDO (INTEGRADO COM SEU CÓDIGO) ---
    def setup_pedido(self):
        f = tk.Frame(self.aba_pedido)
        f.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(f, text="🛒 Finalizar Pedido", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(f, text="Qual prato deseja comer agora? (ID):").pack(anchor="w")
        self.ent_id_pedido = ttk.Entry(f, width=40)
        self.ent_id_pedido.pack(pady=5)

        tk.Label(f, text="Forma de pagamento (Cartão ou Dinheiro):").pack(anchor="w")
        self.combo_pag = ttk.Combobox(f, values=["Cartão", "Dinheiro", "Pix"], width=37, state="readonly")
        self.combo_pag.pack(pady=5)

        ttk.Button(f, text="Confirmar e Finalizar Compra", command=self.confirmar_pedido_sql).pack(pady=20)

    def confirmar_pedido_sql(self):
        id_p = self.ent_id_pedido.get()
        pag = self.combo_pag.get()
        
        if not id_p or not pag:
            messagebox.showwarning("Atenção", "Preencha o ID do prato e a forma de pagamento!")
            return

        try:
            # Busca o preço no banco igual ao seu código original fazia
            self.cursor.execute("SELECT Prato, Preco FROM Cardapio WHERE ID_Cardapio = ?", id_p)
            resultado = self.cursor.fetchone()
            
            if resultado:
                nome_prato = resultado[0]
                valor = resultado[1]
                messagebox.showinfo("Sucesso", f"Compra finalizada com sucesso!\n\nPrato: {nome_prato}\nValor: R$ {valor:.2f}\nPagamento: {pag}")
                self.ent_id_pedido.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "ID do prato não encontrado no sistema!")
        except Exception as e:
            messagebox.showerror("Erro SQL", f"Erro ao processar pedido: {e}")

    # --- ABA 3: RESERVA (INTEGRADO COM SEU CÓDIGO) ---
    def setup_reserva(self):
        f = tk.Frame(self.aba_reserva)
        f.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(f, text="📅 Agendar Nova Reserva", font=("Arial", 16, "bold")).grid(row=0, columnspan=2, pady=20)

        # Campos conforme seu código: Nome, Data, Hora, Pessoas
        tk.Label(f, text="Digite seu nome:").grid(row=1, column=0, sticky="e", pady=5)
        self.res_nome = ttk.Entry(f, width=30)
        self.res_nome.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(f, text="Digite a data (ex: 20/05):").grid(row=2, column=0, sticky="e", pady=5)
        self.res_data = ttk.Entry(f, width=30)
        self.res_data.grid(row=2, column=1, pady=5, padx=10)

        tk.Label(f, text="Digite a hora da reserva:").grid(row=3, column=0, sticky="e", pady=5)
        self.res_hora = ttk.Entry(f, width=30)
        self.res_hora.grid(row=3, column=1, pady=5, padx=10)

        tk.Label(f, text="Número de pessoas:").grid(row=4, column=0, sticky="e", pady=5)
        self.res_pessoas = ttk.Entry(f, width=30)
        self.res_pessoas.grid(row=4, column=1, pady=5, padx=10)

        ttk.Button(f, text="Salvar Reserva no Banco", command=self.gravar_reserva_sql).grid(row=5, columnspan=2, pady=25)

    def gravar_reserva_sql(self):
        # Captura os dados da tela
        nome = self.res_nome.get()
        data = self.res_data.get()
        hora = self.res_hora.get()
        pessoas = self.res_pessoas.get()

        if not all([nome, data, hora, pessoas]):
            messagebox.showwarning("Aviso", "Preencha todos os campos da reserva!")
            return

        try:
            # Supondo que sua tabela se chame 'Reserva' com colunas correspondentes
            query = "INSERT INTO Reserva (Nome, Data_Reserva, Hora_Reserva, Numero_Pessoas) VALUES (?, ?, ?, ?)"
            self.cursor.execute(query, (nome, data, hora, pessoas))
            self.conexao.commit() # Salva no SQL Server
            
            messagebox.showinfo("Reserva Confirmada", f"Olá {nome}, sua reserva para o dia {data} às {hora} foi salva!")
            
            # Limpa os campos
            self.res_nome.delete(0, tk.END)
            self.res_data.delete(0, tk.END)
            self.res_hora.delete(0, tk.END)
            self.res_pessoas.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Erro SQL", f"Erro ao salvar reserva: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaRestaurante(root)
    root.mainloop()