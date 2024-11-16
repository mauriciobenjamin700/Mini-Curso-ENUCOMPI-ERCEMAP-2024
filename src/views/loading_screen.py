import customtkinter as ctk

class LoadingScreen(ctk.CTkFrame):
    """
    Tela de carregamento com uma barra de progresso que simula um processo assíncrono.
    
    Args:
        parent: Referência ao widget pai onde esta tela será adicionada.
        on_complete: Função de callback que será chamada ao final do carregamento.
        data (dict, optional): Dados que serão passados para a função de callback.
    """
    def __init__(self, parent, on_complete, data=None):
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

        # Armazena a função que será chamada após o carregamento e os dados
        self.on_complete = on_complete
        self.data = data

        # Simula um carregamento de 3 segundos antes de concluir
        self.after(3000, self.complete_loading)

    #def complete_loading(self):
    #    self.progress_bar.stop()  # Para a barra de progresso
    #    if self.data:
    #        self.on_complete(self.data)  # Passa os dados para o callback
    #    else:
    #        print("Erro: Nenhum dado foi fornecido para a próxima tela.")
    #    self.destroy()  # Destroi a tela de loading
    def complete_loading(self):
        self.on_complete()  # Chama a função de callback após o carregamento
        self.destroy()  # Fecha a tela de carregamento