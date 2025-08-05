import speech_recognition as sr
from voz_para_texto import converter_audio_para_texto

def gravar_audio():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("Fale agora...")
        audio = reconhecedor.listen(fonte)
        print("Áudio capturado com sucesso.")
    
    texto = converter_audio_para_texto(audio)
    print("\nTranscrição:")
    print(texto)
