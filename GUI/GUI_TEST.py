import streamlit as st
from modules import listen, backbone, speak

def main():
    st.title('E.T.H.A.N : Entidade Tecnológica de Assistência Natural')
    i = 0
    while True:
        # for i in range(5):
        i+=1
        comando = st.text_input(f'Fale um comando {i}:', key=f'input_{i}')
        
        if st.button('Executar Comando',key=f'btn{i}'):
            if not comando:
                st.warning('Por favor, insira um comando.')
            else:
                response = backbone.execute_command(comando)
                st.text(f'Resposta: {response}')
                speak.speak_function(response)

                if response == 'Desligando':
                    st.text('Sequência de desligamento iniciada!')
                    st.text('Até logo, Senhor!')
                    break

if __name__ == "__main__":
    main()
