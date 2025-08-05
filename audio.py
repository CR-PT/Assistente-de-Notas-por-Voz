import speech_recognition as sr

def gravar_audio():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("Fale agora...")
        audio = reconhecedor.listen(fonte)
        print("Áudio capturado com sucesso (ainda não transcrito).")