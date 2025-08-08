import os
import csv

def listar_notas():
    print("\n=== Notas Disponíveis ===")
    ficheiros = [f for f in os.listdir() if f.startswith("notas_") and f.endswith(".csv")]

    if not ficheiros:
        print("Nenhuma nota encontrada.")
        return

    for ficheiro in ficheiros:
        print(f"- {ficheiro}")

    nome = input("\nInsira o nome do ficheiro a consultar (ex: notas_2025-08-01.csv): ")

    if not os.path.exists(nome):
        print("[Erro] Ficheiro não encontrado.")
        return

    tema_filtro = input("Deseja filtrar por tema? (Deixe vazio para mostrar tudo): ").capitalize()

    print("\n=== Conteúdo ===")
    with open(nome, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        encontrou = False
        for linha in reader:
            if tema_filtro == "" or linha["Tema"] == tema_filtro:
                print(f"[{linha['Data']} {linha['Hora']}] ({linha['Tema']}) {linha['Nota']}")
                encontrou = True
        if not encontrou:
            print("Nenhuma nota encontrada com esse filtro.")
