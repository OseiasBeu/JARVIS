import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QMovie
import pyttsx3

class GifViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Visualizador de GIF')

        # Carrega os arquivos GIF
        self.gif_paths = ['../utils/img/2_Ethan.gif', r'../utils/img/1_Ethan.gif']  # Substitua pelos caminhos dos seus arquivos GIF
        self.current_gif_index = 0

        # Inicializa o QMovie com o primeiro GIF
        self.movie = QMovie(self.gif_paths[self.current_gif_index])

        # Cria um rótulo para exibir o GIF
        self.gif_label = QLabel(self)
        self.gif_label.setMovie(self.movie)
        self.movie.start()

        # Configura o layout
        layout = QVBoxLayout()
        layout.addWidget(self.gif_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def change_gif(self):
        # Troca para o próximo GIF
        self.current_gif_index = (self.current_gif_index + 1) % len(self.gif_paths)

        # Atualiza o QMovie
        self.movie.setFileName(self.gif_paths[self.current_gif_index])
        self.movie.start()

        # Anuncia a mudança usando fala
        self.speak(f"GIF alterado para {self.gif_paths[self.current_gif_index]}")

    def speak(self, text):
        # Função para sintetizar a fala
        self.engine.say(text)
        self.engine.runAndWait()

def main():
    app = QApplication(sys.argv)
    gif_viewer_app = GifViewerApp()
    gif_viewer_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
