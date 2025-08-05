from audio import gravar_audio
from consulta import listar_notas

def menu():
    while True:
        print("\n=== Assistente de Notas por Voz ===")
        print("1. Gravar nova nota")
        print("2. Consultar notas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gravar_audio()
        elif opcao == "2":
            listar_notas()
        elif opcao == "3":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
