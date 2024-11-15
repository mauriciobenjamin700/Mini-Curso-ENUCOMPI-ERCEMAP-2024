import customtkinter as ctk
from PIL import Image, ImageTk

class WelcomeScreen(ctk.CTkFrame):
    def __init__(self, parent, on_start):
        super().__init__(parent)

        # Configurações da tela
        self.configure(fg_color="#cfd4d6")  # Fundo da tela

        # Carregar a imagem de fundo
        self.bg_image = Image.open("images/background.png")  # Substitua pelo caminho da sua imagem
        self.bg_image = self.bg_image.resize((1000, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Label para a imagem de fundo
        self.bg_label = ctk.CTkLabel(self, image=self.bg_photo, text="")
        self.bg_label.place(relwidth=1, relheight=1)  # Expande a imagem para ocupar a tela inteira

        # Texto sobreposto sem fundo
        self.title_label = ctk.CTkLabel(
            self, 
            text="Olá, seja bem-vindo à\nContagem de Animais\npor Meio da YOLO!",
            font=("Arial", 24, "bold"),
            text_color="black",
            justify="left",  # Alinhar o texto à esquerda
            anchor="w"       # Alinhar à esquerda dentro do widget
        )
        self.title_label.place(relx=0.02, rely=0.2, anchor="w")  # Posiciona à esquerda com padding

        # Botão de navegação ou próximo passo
        """self.next_button = ctk.CTkButton(
            self,
            text="Iniciar",
            command=on_start,  # Chama a função para carregar a próxima tela
            font=("Arial", 18, "bold"),
            width=150,
            height=40,
            fg_color="#c0c3bd",
            text_color="black" 
        )
        self.next_button.place(relx=0.5, rely=0.8, anchor="center")"""
