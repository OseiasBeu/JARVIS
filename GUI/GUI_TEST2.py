import streamlit as st
from modules import listen, backbone, speak

def main():
    st.title('E.T.H.A.N : Entidade Tecnológica de Assistência Natural')

    comando = st.text_input('Fale um comando:')
    btn_execute = st.button('Executar Comando')

    if btn_execute:
        if not comando:
            st.warning('Por favor, insira um comando.')
        else:
            response = backbone.execute_command(comando)
            st.text(f'Resposta: {response}')
            speak.speak_function(response)

            if response == 'Desligando':
                st.text('Sequência de desligamento iniciada!')
                st.text('Até logo, Senhor!')

if __name__ == "__main__":
    main()
