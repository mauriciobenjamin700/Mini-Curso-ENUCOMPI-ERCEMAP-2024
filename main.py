import customtkinter as ctk
from src.views.welcome_screen import WelcomeScreen
from src.views.video_screen import VideoScreen
from src.views.loading_screen import LoadingScreen
from src.views.results_screen import ResultsScreen
from src.models.detect_model import get_model, features
from src.controllers.apply import predict, track


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Minha Aplicação")
        self.geometry("800x600")

        # Inicializa as telas
        self.welcome_screen = WelcomeScreen(self, self.show_video_screen)  # Passa a função de transição
        self.video_screen = VideoScreen(self, self.show_loading_screen)  # Passa o callback para o VideoScreen
        self.loading_screen = None
        self.results_screen = None  # Inicializa como None

        # Mostra inicialmente a tela de boas-vindas
        self.show_welcome_screen()

        # Alterna para a tela de vídeo automaticamente após 10 segundos
        self.after(10000, self.show_video_screen)

    def show_welcome_screen(self):
        # Remove outras telas antes de exibir esta
        if self.video_screen:
            self.video_screen.pack_forget()
        self.welcome_screen.pack(fill="both", expand=True)

    def show_video_screen(self):
        # Remove outras telas antes de exibir esta
        if self.welcome_screen:
            self.welcome_screen.pack_forget()
        if self.loading_screen:
            self.loading_screen.pack_forget()
        self.video_screen.pack(fill="both", expand=True)

    def show_loading_screen(self, video_path):
    # Remove outras telas antes de exibir a de loading
        if self.video_screen:
            self.video_screen.pack_forget()
        if self.results_screen:
            self.results_screen.pack_forget()

        # Exibe a tela de loading
        self.loading_screen = LoadingScreen(self, lambda: self.process_video(video_path))
        self.loading_screen.pack(fill="both", expand=True)

    def process_video(self, video_path):
        # Processa o vídeo usando a função `predict`
        try:
            results = predict(video_path)
            counting_data = {class_name: count for class_name, count in results[0]['counting_class'].items()}

            # Exibe a tela de resultados com os dados processados
            self.show_results_screen(counting_data)
        except Exception as e:
            print(f"Erro ao processar o vídeo: {e}")
            self.show_video_screen()  # Volta para a tela de vídeo em caso de erro




    def show_results_screen(self, data):
        # Remove a tela de loading
        if self.loading_screen:
            self.loading_screen.pack_forget()

        # Inicializa a tela de resultados, se necessário
        if not self.results_screen:
            self.results_screen = ResultsScreen(self, data, self.show_video_screen)
        else:
            # Atualiza os dados da tela de resultados
            self.results_screen.results_label.configure(text=self.results_screen.format_data(data))

        # Exibe a tela de resultados
        self.results_screen.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
