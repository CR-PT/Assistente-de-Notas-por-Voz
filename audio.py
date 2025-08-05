import speech_recognition as sr
from voz_para_texto import converter_audio_para_texto
from analise import classificar_tema
from armazenamento import guardar_nota

def gravar_audio():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("Fale agora...")
        audio = reconhecedor.listen(fonte)
        print("Áudio capturado com sucesso.")
    
    texto = converter_audio_para_texto(audio)
    print("\nTranscrição:")
    print(texto)
    tema = classificar_tema(texto)
    print(f"\nTema identificado: {tema}")
    
    guardar_nota(texto, tema)



