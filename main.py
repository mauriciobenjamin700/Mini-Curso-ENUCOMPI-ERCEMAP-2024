import customtkinter as ctk
from src.views.templates.welcome_screen import WelcomeScreen
from src.views.templates.video_screen import VideoScreen
from src.views.templates.loading_screen import LoadingScreen
from src.views.templates.results_screen import ResultsScreen


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Minha Aplicação")
        self.geometry("800x600")

        # Inicializa as telas
        self.welcome_screen = WelcomeScreen(self, self.show_video_screen)  # Passa a função de transição
        self.video_screen = VideoScreen(self, self.show_loading_screen)  # Passa o callback para o VideoScreen
        self.loading_screen = None

        # Mostra inicialmente a tela de boas-vindas
        self.show_welcome_screen()

        # Alterna para a tela de vídeo automaticamente após 4 segundos
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

    def show_loading_screen(self):
        # Remove outras telas antes de exibir a de loading
        if self.video_screen:
            self.video_screen.pack_forget()
        self.loading_screen = LoadingScreen(self, self.show_results_screen)
        self.loading_screen.pack(fill="both", expand=True)

    def show_results_screen(self):
        if self.loading_screen:
            self.loading_screen.pack_forget()

        # Dados simulados (JSON)
        data = {
            "Cavalo": 20,
            "Bois": 10,
            "Zebras": 1,
            "Cabras": 2
        }
        self.results_screen = ResultsScreen(self, data, self.show_video_screen)
        self.results_screen.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
