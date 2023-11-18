import speech_recognition as sr
import pyttsx3

import yfinance as yf
import openai 
from get_env import print_env

env = print_env(['app_key'])

#configura ambeinte
openai.api_key = env['app_key']

# model_engine 
model_engine = 'text-davinci-003'

audio = sr.Recognizer()
maquina = pyttsx3.init()

def listen_command():
    try:
        with sr.Microphone() as source:
            print('Escutando..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'jarvis' in comando:
                comando = comando.replace('jarvis', '')
                maquina.say(comando)
                maquina.runAndWait()

    except Exception as e:
        print(f'Microfone não está ok {e}')
    # print(f'o comando é: {comando}')
    return comando
    
    
            
def execute_command():
    comando = listen_command()
    if 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say(f'Tocando {musica} no youtube!')
        maquina.runAndWait()
    
    elif 'responda' in comando or 'fale sobre' in comando or 'crie' in comando or 'o que você acha sobre' in comando:
        prompt = comando.replace('responda','')
        completion = openai.Completion.create(
            engine = model_engine,
            prompt = prompt,
            max_tokens = 1024,
            temperature = 0.5,
        )
        reponse = completion.choices[0].text
        print(reponse)
        maquina.say(reponse)
        maquina.runAndWait()
    elif 'cotação' in comando or 'cote' in comando or 'qual o valor da ação' in comando:
        symbol = comando.replace('cotação','').replace('cote','').replace('qual o valor da ação','').rstrip().strip().upper()
        try:
            acao = yf.Ticker(symbol)
            dados_cotacao = acao.history(period='1d')
            cotacao_atual = dados_cotacao['Close'].iloc[-1]
            print(f'Ação:{symbol}')
            print(f'Cotação atual:{cotacao_atual}')
            
            maquina.say(f'Ação:{symbol}')
            maquina.say(f'Cotação atual:{cotacao_atual}')
            
            maquina.runAndWait()
            
        except Exception as e:
            print(f'Erro ao obter cotação da ação {symbol}:{e}')
            return None
        
while True:
    execute_command()
    saida = input('Deseja sair?')
    if saida == 'sim':
        break