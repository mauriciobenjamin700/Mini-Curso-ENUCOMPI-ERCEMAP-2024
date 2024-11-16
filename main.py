import customtkinter as ctk
from src.views.templates.welcome_screen import WelcomeScreen
from src.views.templates.video_screen import VideoScreen

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Minha Aplicação")
        self.geometry("800x600")

        # Inicializa as telas
        self.welcome_screen = WelcomeScreen(self, self.show_video_screen)  # Passa a função de transição
        self.video_screen = VideoScreen(self)

        # Mostra inicialmente a tela de boas-vindas
        self.show_welcome_screen()

        # Alterna para a tela de vídeo automaticamente após 4 segundos
        self.after(4000, self.show_video_screen)

    def show_welcome_screen(self):
        # Remove outras telas antes de exibir esta
        self.video_screen.pack_forget()
        self.welcome_screen.pack(fill="both", expand=True)

    def show_video_screen(self):
        # Remove outras telas antes de exibir esta
        self.welcome_screen.pack_forget()
        self.video_screen.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
