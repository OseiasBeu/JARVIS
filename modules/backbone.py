import wikipedia
import pywhatkit

from modules import finance
from modules import createSomething
from modules import listen
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
    
    elif 'responda' in comando or 'fale sobre' in comando or 'crie' in comando or 'o que você acha sobre' in comando:
        resultado = createSomething.create(comando)
        return resultado
    elif 'cotação' in comando or 'cote' in comando or 'qual o valor da ação' in comando:
        symbol = comando.replace('cotação','').replace('cote','').replace('qual o valor da ação','').rstrip().strip().upper()
        try:
            resultado = finance.obter_cotacao_acao(symbol)
            return resultado
            
        except Exception as e:
            print(f'Erro ao obter cotação da ação {symbol}:{e}')
            return f'Erro ao obter cotação da ação'
    elif comando == 'sair' or comando == 'fechar programa':
        return 'Desligando'
    else:
        listen.listen_function()