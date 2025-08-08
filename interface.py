import tkinter as tk
from audio import gravar_audio
from consulta import listar_notas

def executar_interface():
    janela = tk.Tk()
    janela.title("Assistente de Notas por Voz")
    janela.geometry("300x200")

    label = tk.Label(janela, text="Menu Principal", font=("Arial", 14))
    label.pack(pady=10)

    btn_gravar = tk.Button(janela, text="Gravar Nova Nota", command=gravar_audio, width=25)
    btn_gravar.pack(pady=5)

    btn_consultar = tk.Button(janela, text="Consultar Notas", command=listar_notas, width=25)
    btn_consultar.pack(pady=5)

    btn_sair = tk.Button(janela, text="Sair", command=janela.destroy, width=25)
    btn_sair.pack(pady=5)

    janela.mainloop()
