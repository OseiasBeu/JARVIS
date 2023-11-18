from modules import listen, backbone,speak
if __name__ == "__main__":
    print('Escutando...')
    while True:
        comando = listen.listen_function()
        response = backbone.execute_command(comando)
        speak.speak_function(response)
        
        saida = input('Deseja sair?')
        if saida == 'sim':
            break
        