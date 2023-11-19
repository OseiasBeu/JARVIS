from modules import listen, backbone,speak
if __name__ == "__main__":
    print('Eu sou: E.T.H.A.N > Entidade Tecnológica de Assistência Natural')
    while True:
        comando = listen.listen_function()
        response = backbone.execute_command(comando)
        speak.speak_function(response)
        
        if response == 'Desligando':
            speak.speak_function('Sequência de desligamento iniciada!')
            speak.speak_function('Até logo, Senhor!')
            break