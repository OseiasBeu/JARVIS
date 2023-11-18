import speech_recognition as sr
from  modules import speak

def listen_function():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        speak.speak_function('Estou te ouvindo')
        audio = r.listen(source)
    try:
        comando = r.recognize_google(audio,language='pt-br')
        comando = comando.lower()
        if 'ethan' in comando or 'jarvis' in comando or 'etham' in comando:
            comando = comando.replace('jarvis', '').replace('ethan','').replace('etham','')
            speak.speak_function(comando)
            
    except Exception as e:
        print(e)
        return 'Não entendi, poderia repetir?'
    return comando
        
# listen_function()