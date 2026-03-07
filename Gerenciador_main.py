# ---------------------------------------------------------
# Sistema: Gerenciador de Lembretes
# Autor: Luiz Augusto Pereira
# Linguagem: Python
# Bibliotecas: Tkinter, Plyer, Threading
#
# Descrição:
# Sistema que permite criar lembretes com notificações
# programadas. O usuário define título, mensagem,
# quantidade de repetições e intervalo entre notificações.
# As tarefas ativas são exibidas em uma tabela onde
# podem ser editadas ou removidas.
# ---------------------------------------------------------

import tkinter as tk
from tkinter import ttk 
from centraliza import center
import time
from plyer import notification
import threading
import os
from tkinter import messagebox

# -- Def para iniciar os lembretes, aqui irá ativar a biblioteca e aparecer a notificação
# da atividade pegando os valores que o usuário inserir.
# Vai coletar o id da tarefa para que possa aparecer na tabela

def iniciar_lembrete(titulo, mensagem, rep, horario_seg, item_id, tree):

# -- Aqui o i vai verificar quantas repetições serão necessárias  
# ele vai puxar o .sleep para começar o timer e após isso enviar a mensagem
# após a mensagem ser notificada pela ultima vez o def remover vai excluir a mensagem pelo id dela

    for i in range(rep):
        time.sleep(horario_seg)
        notification.notify(
            title=titulo,
            message=mensagem,
            timeout=10
        )


    def remover():
        if tree.exists(item_id):
            tree.delete(item_id)

    tree.after(0, lambda: tree.delete(item_id))


# -- Definindo o valor entries para começar como uma lista vazia 
valor_entries = []


# -- O def dubmit valor vai pegar os valores que o usuario coletar 
# A função submit_valor coleta os valores digitados pelo usuário

def submit_valor():

    try:
        titulo = valor_entries[0].get()
        mensagem = valor_entries[1].get()
        rep = int(valor_entries[2].get())
        horario = float(valor_entries[3].get())
# Aqui os minutos serão transformados em segundos para funcionar no .sleep 

        if not titulo or not mensagem:
            messagebox.showwarning("Erro!", "Faltou inserir o Titulo e a descrição da tarefa que vai ser notificada.")
            return

        horario_seg = horario * 60

        values_table = [titulo, mensagem, rep, horario]
        item_id = tree.insert("", "end", values=values_table)

# O threading ele vai pegar a execução da tarefa e colocar em segundo plano, assim é possivel criar varias tarefas dessa maneira
# caso o usuario fechar o sistema o daemon vai fazer com que não seja mais enviado nenhum notificação 

        t = threading.Thread(
            target=iniciar_lembrete,
            args=(titulo, mensagem, rep, horario_seg, item_id, tree),
            daemon=True
        )
        t.start()

        for entry in valor_entries:
            entry.delete(0, tk.END)

    except ValueError:
        messagebox.showwarning("Erro!", "Faltou inserir quantas vezes e em quando tempo a tarefa vai ser notificada.")
    except IndexError:
        messagebox.showwarning("Erro!", "Campos não carregados.")




# Declarando o diretorio do tema para a aplicação

diretorio_atual = os.path.dirname(__file__)
caminho_tema = os.path.join(
    diretorio_atual,
    "Forest-ttk-theme-master",
    "forest-dark.tcl"
)

tree = None


# Def excluir linha vai pegar a linha que o usuario clicou dentro da tabela e excluir ela

def excluir_linha():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Erro!", "Linha não foi selecionada. Para selecionar o item a ser deletado, clique em um dos itens da tabela.")

        return
    for item in selected_item:
        tree.delete(item)


# Def editar linha vai pegar a linha que o usuario clicou dentro da tabela e enviar os valores novamente para os campos de entrada

def editar_linha():
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showwarning("Erro!", "Linha não foi selecionada. Para selecionar o item a ser editado, clique em um dos itens da tabela.")

        return

    item = selected_item[0]

    valores = tree.item(item, "values")

    for i, entry in enumerate(valor_entries):
        entry.delete(0, tk.END)
        entry.insert(0, valores[i])

    tree.delete(item)


def main():
    global valor_entries
    valor_entries = []

    janela_principal = tk.Tk()

    janela_principal.title("Gerenciador de Lembretes")
    janela_principal.geometry("650x716")

    center(janela_principal)

    janela_principal.tk.call("source", caminho_tema)

    style = ttk.Style(janela_principal)
    style.theme_use("forest-dark")

    fonte_personalizada = ("Times New Roman", 12)

    labels = ["Título:", "Mensagem:", "Repeticoes:", "Intervalo:"]

    ttk.Label(
        janela_principal,
        text="Gerenciador de Lembretes",
        font=("Times New Roman", 24)
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        pady=20
    )

    for i, texto in enumerate(labels, start=1):

        ttk.Label(
            janela_principal,
            text=texto
        ).grid(
            row=i,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        txt_entry = ttk.Entry(
            janela_principal,
            font=fonte_personalizada,
            width=60
        )

        txt_entry.grid(
            row=i,
            column=1,
            padx=10,
            pady=10,
            sticky="w"
        )

        valor_entries.append(txt_entry)

    btnSubmit = ttk.Button(
        janela_principal,
        text="Adicionar Lembrete",
        style="Accent.TButton",
        command=submit_valor
    )
    ttk.Label(
    janela_principal,
    text="Tarefas Ativas:",
    font=("Times New Roman", 18)
    ).grid(row=6, column=0, columnspan=2, pady=18)

    global tree

    tree = ttk.Treeview(
        janela_principal,
        selectmode="browse",
        columns=("col1", "col2", "col3", "col4"),
        show="headings"
    )

    tree.column("col1", width=150, minwidth=50)
    tree.heading("col1", text="Título da mensagem:")

    tree.column("col2", width=280, minwidth=50)
    tree.heading("col2", text="Descrição:")

    tree.column("col3", width=50, minwidth=50)
    tree.heading("col3", text="Repetir: ")

    tree.column("col4", width=100, minwidth=50)
    tree.heading("col4", text="A cada (min):")

    tree.grid(
        row=7,
        column=0,
        columnspan=2,
        padx=10,
        pady=0,
        sticky="nsew"
    )

    btnSubmit.grid(
        row=len(labels) + 1,
        column=0,
        columnspan=2,
        pady=0
    )

    btnSubmit2 = ttk.Button(
        janela_principal,
        text="Editar Lembrete",
        style="Accent.TButton",
        command=editar_linha
    )

    btnSubmit2.grid(
        row=8,
        column=0,
        columnspan=1,
        padx= 10,
        pady=20
        
        
    )
    btnSubmit3 = ttk.Button(
        janela_principal,
        text="Excluir lembrete",
        style="Accent.TButton",
        command=excluir_linha
    )

    btnSubmit3.grid(
        row=8,
        column=0,
        columnspan=2,
        pady=20
    )

    janela_principal.mainloop()


if __name__ == "__main__":
    main()