import speech_recognition as sr
from  modules import speak

def listen_function():
    try: 
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
        # speak.speak_function('Ethan> ')
            print('JARVIS> ')
            audio = r.listen(source)
            comando = r.recognize_google(audio,language='pt-br')
            comando = comando.lower()
            if 'jarvi' in comando or 'jarvis' in comando or 'jarwis' in comando:
                comando = comando.replace('jarvis', '').replace('jarvi','').replace('jarwis','')
                speak.speak_function(comando)
                return comando
                
    except Exception as e:
        # print(e)
        return 'Não entendi, poderia repetir?'
    
        
# listen_function()