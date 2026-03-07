import tkinter as tk
from tkinter import ttk 
from centraliza import center
import time
from plyer import notification
import threading
import os


# -- Def para iniciar os lembretes, aqui irá ativar a biblioteca e aparecer a notificação
# da atividade pegando os valores que o usuário inserir.

def iniciar_lembrete(titulo, mensagem, rep, horario_seg):
    for i in range(rep):
        notification.notify( title=titulo, message=mensagem, timeout=10)
        time.sleep(horario_seg)


# --
valor_entries = []


def submit_valor():
    try:
        titulo = valor_entries[0].get()
        mensagem = valor_entries[1].get()
        rep = int(valor_entries[2].get())
        horario = float(valor_entries[3].get())

        print(f"Lembrete agendado: {titulo} (Repete {rep}x a cada {horario}m)")

        horario_seg = horario * 60

        t = threading.Thread(target=iniciar_lembrete, args=(titulo, mensagem, rep, horario_seg))
        t.start()


        for entry in valor_entries:
            entry.delete(0, tk.END)
        

    except ValueError:
        print("Erro: 'Rep' e 'horario' devem ser números.")
    except IndexError:
        print("Erro: Campos não carregados.")


diretorio_atual = os.path.dirname(__file__)
caminho_tema = os.path.join( diretorio_atual, "Forest-ttk-theme-master", "forest-dark.tcl")


def main():
    global valor_entries
    valor_entries = []

    janela_principal = tk.Tk()

    janela_principal.title("Configurar Lembrete")
    janela_principal.geometry("380x350")

    center(janela_principal)

    janela_principal.tk.call("source", caminho_tema)

    style = ttk.Style(janela_principal)
    style.theme_use("forest-dark")

    fonte_personalizada = ("Times New Roman", 12)

    labels = ["Título:", "Mensagem:", "Repetições:", "Intervalo:"]

    for i, texto in enumerate(labels):
        ttk.Label(
            janela_principal,
            text=texto
        ).grid(row=i, column=0, padx=10, pady=10, sticky="w")

        txt_entry = ttk.Entry(
            janela_principal,
            font=fonte_personalizada, width=32
        )

        txt_entry.grid(row=i, column=1, padx=10, pady=10)

        valor_entries.append(txt_entry)
    janela_principal.columnconfigure(0, weight=1)
    janela_principal.columnconfigure(1, weight=1)
    btnSubmit = ttk.Button(
        janela_principal,
        text="Iniciar Lembrete",
        style="Accent.TButton",
        command=submit_valor
    )

    btnSubmit.grid(row=len(labels), column=0, columnspan=2, pady=20)

    janela_principal.mainloop()


if __name__ == "__main__":
    main()