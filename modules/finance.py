import yfinance as yf
def obter_cotacao_acao(symbol):
    try:
        acao = yf.Ticker(symbol)
        dados_cotacao = acao.history(period='1d')
        cotacao_atual = dados_cotacao['Close'].iloc[-1]
        return f'Ação:{symbol} \n Cotação atual:{cotacao_atual}'
    except Exception as e:
        print(f'Erro ao obter cotação da ação {symbol}:{e}')
        return None 
    
# symbol = 'AAPL'
# cotacao = obter_cotacao_acao(symbol)
# if cotacao is not None:
#     print(f'Ação: {symbol}')
#     print(f'Cotação atual: {cotacao}')
    