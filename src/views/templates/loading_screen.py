import customtkinter as ctk

class LoadingScreen(ctk.CTkFrame):
    def __init__(self, parent, on_complete):
        super().__init__(parent)

        # Configurações da tela
        self.configure(fg_color="#1D2530")  # Fundo escuro

        # Texto "Loading..."
        self.loading_label = ctk.CTkLabel(
            self,
            text="Loading...",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        self.loading_label.place(relx=0.5, rely=0.4, anchor="center")

        # Barra de progresso
        self.progress_bar = ctk.CTkProgressBar(
            self,
            orientation="horizontal",
            width=300,
            mode="indeterminate"  # Animação contínua
        )
        self.progress_bar.place(relx=0.5, rely=0.5, anchor="center")
        self.progress_bar.start()  # Inicia a animação da barra

        # Armazena a função que será chamada após o carregamento
        self.on_complete = on_complete

        # Simula um carregamento de 3 segundos antes de concluir
        self.after(3000, self.complete_loading)

    def complete_loading(self):
        self.progress_bar.stop()  # Para a barra de progresso
        self.on_complete()  # Chama a função de callback para a próxima tela
