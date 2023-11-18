import pyttsx3

def speak_function(text):
    print(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    volume = engine.getProperty('volume')
    rate = engine.getProperty('rate')

    # for voice in voices:
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('volume', volume-0.10)
    engine.setProperty('rate', rate-10)
    engine.say(text)
    engine.runAndWait()
    
# speak_function('Olá Mundo!')