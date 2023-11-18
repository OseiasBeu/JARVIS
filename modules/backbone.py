import wikipedia
import pywhatkit
import yfinance as yf
from modules import finance

def execute_command(comando):
    if 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)

        return resultado
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        resultado = f'Tocando {musica} no youtube!'
        print(resultado)
        return resultado
    
    # elif 'responda' in comando or 'fale sobre' in comando or 'crie' in comando or 'o que você acha sobre' in comando:
    #     prompt = comando.replace('responda','')
    #     completion = openai.Completion.create(
    #         engine = model_engine,
    #         prompt = prompt,
    #         max_tokens = 1024,
    #         temperature = 0.5,
    #     )
    #     reponse = completion.choices[0].text
    #     print(reponse)
    #     maquina.say(reponse)
    #     maquina.runAndWait()
    
    elif 'cotação' in comando or 'cote' in comando or 'qual o valor da ação' in comando:
        symbol = comando.replace('cotação','').replace('cote','').replace('qual o valor da ação','').rstrip().strip().upper()
        try:
            resultado = finance.obter_cotacao_acao(symbol)
            return resultado
            
        except Exception as e:
            print(f'Erro ao obter cotação da ação {symbol}:{e}')
            return f'Erro ao obter cotação da ação'