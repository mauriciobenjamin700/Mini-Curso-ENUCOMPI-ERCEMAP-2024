import customtkinter as ctk
from tkinter import filedialog
import os
from PIL import Image, ImageTk 

class VideoScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configuração da tela
        self.configure(fg_color="#1D2530")  # Cor de fundo escura

        image_path = "images/logo.png"  
        self.logo_image = Image.open(image_path)  # Carrega a imagem
        self.logo_image = self.logo_image.resize((240, 120), Image.Resampling.LANCZOS)  # Ajusta o tamanho
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        # Emblema no topo (substitua por uma imagem se necessário)
        self.logo_label = ctk.CTkLabel(
            self,
            image=self.logo_photo,  # Adicionamos a imagem carregada
            text=""  # Não exibimos texto
        )
        self.logo_label.place(relx=0.5, rely=0.1, anchor="center")

        # Caixa de vídeo (área central)
        self.video_frame = ctk.CTkFrame(
            self,
            width=700,
            height=290,
            fg_color="#D9D9D9",  # Cor do retângulo para vídeo
            corner_radius=10
        )
        self.video_frame.place(relx=0.5, rely=0.4, anchor="center")

        # Botão "Selecionar Vídeo"
        self.select_button = ctk.CTkButton(
            self,
            text="Selecionar Vídeo",
            font=("Arial", 16),
            command=self.select_video,
            fg_color="#FEFAE0", 
            text_color="black",
            hover_color="#d4ac0d", 
        )
        self.select_button.place(relx=0.5, rely=0.4, anchor="center")  # Centralizado no frame de vídeo

        # Label para exibir o nome do arquivo selecionado
        self.file_name_label = ctk.CTkLabel(
            self,
            text="Nenhum vídeo selecionado",  # Texto padrão inicial
            font=("Arial", 14),
            text_color="white",
            justify="center"
        )
        self.file_name_label.place(relx=0.5, rely=0.7, anchor="center")  # Posicionado abaixo do botão

        # Botão "Contar" no canto inferior direito
        self.count_button = ctk.CTkButton(
            self,
            text="📊 Contar",
            font=("Arial", 16),
            command=self.start_counting,
            fg_color="#f9e79f",  # Cor de fundo
            text_color="black",
            hover_color="#f4d03f",  # Cor ao passar o mouse
        )
        self.count_button.place(relx=0.9, rely=0.9, anchor="center")  # Canto inferior direito

    def select_video(self):
        # Abrir seletor de arquivos e permitir apenas vídeos
        file_path = filedialog.askopenfilename(
            title="Selecione um vídeo",
            filetypes=[
                ("Arquivos de vídeo", "*.mp4 *.avi *.mkv *.mov *.flv"),  # Tipos permitidos
                ("Todos os arquivos", "*.*")
            ]
        )

        if file_path:
            # Atualiza o texto do label com o nome do arquivo
            file_name = os.path.basename(file_path)  # Extrai apenas o nome do arquivo
            self.file_name_label.configure(text=f"Selecionado: {file_name}")
            print(f"Vídeo selecionado: {file_path}")  # Para debug
        else:
            self.file_name_label.configure(text="Nenhum vídeo selecionado")
            print("Nenhum vídeo foi selecionado.")

    def start_counting(self):
        print("Contagem iniciada!")
        # Aqui você pode implementar a lógica de contagem
