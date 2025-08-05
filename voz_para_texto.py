import speech_recognition as sr

def converter_audio_para_texto(audio):
    reconhecedor = sr.Recognizer()
    try:
        texto = reconhecedor.recognize_google(audio, language='pt-PT')
        return texto
    except sr.UnknownValueError:
        return "[Erro] Não foi possível entender o áudio."
    except sr.RequestError:
        return "[Erro] Falha na ligação ao serviço de reconhecimento de fala."
