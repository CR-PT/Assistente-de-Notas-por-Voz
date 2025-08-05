def extrair_palavras_chave(texto):
    palavras = texto.lower().split()
    return palavras

def classificar_tema(texto):
    palavras = extrair_palavras_chave(texto)

    temas = {
        "trabalho": ["reunião", "projeto", "email", "relatório", "cliente"],
        "pessoal": ["comprar", "chamar", "família", "amigo", "casa"],
        "lembrete": ["lembrar", "anotar", "hoje", "amanhã", "prazo"],
        "ideia": ["pensamento", "ideia", "criar", "inovar", "sugestão"]
    }

    for tema, keywords in temas.items():
        if any(palavra in palavras for palavra in keywords):
            return tema.capitalize()

    return "Geral"
