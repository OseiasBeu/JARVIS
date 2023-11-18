from hugchat import hugchat
from hugchat.login import Login
from modules import get_env 

# from get_env import print_env
def create(comando):
    senha = get_env.print_env(['pass'])['pass']
    email = get_env.print_env(['email'])['email']

    sign = Login(email, senha)
    cookies = sign.login()

    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)

    # Create a chatbot connection
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    id = chatbot.new_conversation()
    chatbot.change_conversation(id)

    return chatbot.chat(comando)