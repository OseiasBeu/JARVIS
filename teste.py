import tkinter as tk
import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import yfinance as yf
import openai
from get_env import print_env
import tkinter as tk
from PIL import Image, ImageTk


def change_background():
    # Carregar o gif desejado
    gif_path = r'C:\Users\beu.oseias_ifood\Documents\Projects\Jarvis\img\jarvis.jpg'  # Substitua pelo caminho do seu arquivo gif
    gif_image = Image.open(gif_path)
    gif_photo = ImageTk.PhotoImage(gif_image)

    # Definir a imagem como um Label para exibir no fundo da janela
    background_label = tk.Label(app, image=gif_photo)
    background_label.image = gif_photo  # Mantenha uma referência para a imagem para evitar que seja coletada pelo garbage collector
    background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Coloque no fundo da janela



env = print_env(['app_key'])

# Configura ambiente
openai.api_key = env['app_key']

# Model engine
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
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say(f'Tocando {musica} no youtube!')
        maquina.runAndWait()
    elif 'responda' in comando or 'fale sobre' in comando or 'crie' in comando or 'o que você acha sobre' in comando:
        prompt = comando.replace('responda', '')
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
        )
        reponse = completion.choices[0].text
        print(reponse)
        maquina.say(reponse)
        maquina.runAndWait()
    elif 'cotação' in comando or 'cote' in comando or 'qual o valor da ação' in comando:
        symbol = comando.replace('cotação', '').replace('cote', '').replace('qual o valor da ação', '').rstrip().strip().upper()
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

app = tk.Tk()
app.title("Assistente de Voz")
app.geometry("500x300")

start_button = tk.Button(app, text="Ativar Assistente de Voz", command=change_background)
start_button.pack(pady=20)

response = tk.Text(app, wrap="word", font=("Helvetica", 12), bg="lightgray")
response.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

app.mainloop()