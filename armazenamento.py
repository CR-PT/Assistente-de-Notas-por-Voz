import csv
from datetime import datetime
import os

def guardar_nota(texto, tema):
    data = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    nome_ficheiro = f"notas_{data}.csv"

    existe = os.path.exists(nome_ficheiro)
    
    with open(nome_ficheiro, mode='a', newline='', encoding='utf-8') as ficheiro:
        writer = csv.writer(ficheiro)
        if not existe:
            writer.writerow(["Data", "Hora", "Tema", "Nota"])
        writer.writerow([data, hora, tema, texto])
    
    print(f"\nNota guardada no ficheiro: {nome_ficheiro}")
