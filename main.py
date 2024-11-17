import customtkinter as ctk
from src.views.welcome_screen import WelcomeScreen
from src.views.video_screen import VideoScreen
from src.views.loading_screen import LoadingScreen
from src.views.results_screen import ResultsScreen
from src.models.detect_model import get_model, features
from src.controllers.apply import predict, track, count_unique_animals


class MainWindow(ctk.CTk):
    """
    Janela principal da aplicação, responsável por gerenciar e exibir as diferentes telas (boas-vindas, seleção de vídeo,
    carregamento e resultados) e realizar a lógica de transição entre elas.

    Args:
        ctk.CTk: Subclasse de CTk (CustomTkinter), que representa a janela principal.
    """
    def __init__(self):
        """
        Inicializa a janela principal e configura as telas e a lógica de transição entre elas.
        """
        super().__init__()

        # Configurações básicas da janela
        self.title("Minha Aplicação")  # Título da janela
        self.geometry("800x600")  # Define o tamanho da janela

        # Inicializa as telas
        self.welcome_screen = WelcomeScreen(self)  # Tela de boas-vindas
        self.video_screen = VideoScreen(self, self.show_loading_screen)  # Tela de seleção de vídeo
        self.loading_screen = None  # Inicialmente, a tela de carregamento é None
        self.results_screen = None  # Inicialmente, a tela de resultados é None

        # Exibe a tela inicial (boas-vindas)
        self.show_welcome_screen()

        # Configura a transição automática para a tela de vídeo após 10 segundos
        self.after(10000, self.show_video_screen)

    def show_welcome_screen(self):
        """
        Exibe a tela de boas-vindas, ocultando quaisquer outras telas que possam estar visíveis.
        """
        if self.video_screen:
            self.video_screen.pack_forget()  # Oculta a tela de vídeo, se estiver visível
        self.welcome_screen.pack(fill="both", expand=True)  # Exibe a tela de boas-vindas

    def show_video_screen(self):
        """
        Exibe a tela de seleção de vídeo, ocultando quaisquer outras telas que possam estar visíveis.
        """
        if self.welcome_screen:
            self.welcome_screen.pack_forget()  # Oculta a tela de boas-vindas, se estiver visível
        if self.loading_screen:
            self.loading_screen.pack_forget()  # Oculta a tela de carregamento, se estiver visível
        self.video_screen.pack(fill="both", expand=True)  # Exibe a tela de vídeo

    def show_loading_screen(self, video_path):
        """
        Exibe a tela de carregamento enquanto processa o vídeo selecionado.

        Args:
            video_path (str): Caminho do vídeo selecionado para processamento.
        """
        if self.video_screen:
            self.video_screen.pack_forget()  # Oculta a tela de vídeo, se estiver visível
        if self.results_screen:
            self.results_screen.pack_forget()  # Oculta a tela de resultados, se estiver visível

        # Cria e exibe a tela de carregamento
        self.loading_screen = LoadingScreen(self, lambda: self.process_video(video_path))
        self.loading_screen.pack(fill="both", expand=True)

    def process_video(self, video_path):
        """
        Processa o vídeo selecionado usando a função `predict` e exibe os resultados.

        Args:
            video_path (str): Caminho do vídeo selecionado.

        Exceptions:
            Em caso de erro no processamento, exibe uma mensagem de erro no console e retorna à tela de vídeo.
        """
        try:
            # Realiza a predição no vídeo
            results = predict(video_path)

            # Conta os animais únicos detectados
            counting_data = count_unique_animals(results)

            # Exibe a tela de resultados com os dados processados
            self.show_results_screen(counting_data)
        except Exception as e:
            print(f"Erro ao processar o vídeo: {e}")
            self.show_video_screen()  # Retorna à tela de vídeo em caso de erro

    def show_results_screen(self, data):
        """
        Exibe a tela de resultados com os dados processados.

        Args:
            data (dict): Dados resultantes do processamento, contendo a contagem de animais detectados.
        """
        if self.loading_screen:
            self.loading_screen.pack_forget()  # Oculta a tela de carregamento, se estiver visível

        # Inicializa a tela de resultados, se ainda não foi criada
        if not self.results_screen:
            self.results_screen = ResultsScreen(self, data, self.show_video_screen)
        else:
            # Atualiza os dados exibidos na tela de resultados
            self.results_screen.results_label.configure(text=self.results_screen.format_data(data))

        # Exibe a tela de resultados
        self.results_screen.pack(fill="both", expand=True)


if __name__ == "__main__":
    """
    Ponto de entrada da aplicação. Cria e executa a janela principal.
    """
    app = MainWindow()
    app.mainloop()
