import streamlit as st
import speech_recognition as sr  # Instale usando pip install SpeechRecognition
from modules import backbone, speak

def main():
    st.title('E.T.H.A.N : Entidade Tecnológica de Assistência Natural')

    comando = st.text_input('Fale um comando:')
    btn_execute = st.button('Executar Comando')

    if btn_execute or is_keyword_detected():  # Adiciona a condição para verificar a palavra-chave
        if not comando:
            st.warning('Por favor, insira um comando.')
        else:
            response = backbone.execute_command(comando)
            st.text(f'Resposta: {response}')
            speak.speak_function(response)

            if response == 'Desligando':
                st.text('Sequência de desligamento iniciada!')
                st.text('Até logo, Senhor!')

def is_keyword_detected():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga uma palavra-chave:")
        audio = recognizer.listen(source)

    try:
        # Use um modelo de linguagem ou lista de palavras-chave específicas
        # para verificar se a palavra-chave foi detectada.
        keyword = recognizer.recognize_google(audio)
        return "palavra_chave" in keyword.lower()
    except sr.UnknownValueError:
        return False
    except sr.RequestError as e:
        print(f"Erro na solicitação ao Google Speech Recognition service; {e}")
        return False

if __name__ == "__main__":
    main()
