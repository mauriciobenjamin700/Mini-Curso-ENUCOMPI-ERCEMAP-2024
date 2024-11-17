import customtkinter as ctk
import json
import pandas as pd
from tkinter import filedialog


class ResultsScreen(ctk.CTkFrame):
    """
    Tela para exibição de resultados e exportação de dados em diferentes formatos.
    
    Args:
        parent: Referência ao widget pai onde esta tela será adicionada.
        data (dict): Dados a serem exibidos na tela e exportados.
        go_back_callback (function): Função de callback para retornar à tela anterior.
    """
    # Mapeamento de traduções
    ANIMAL_TRANSLATIONS = {
        "bird": "Pássaro",
        "cat": "Gato",
        "dog": "Cachorro",
        "horse": "Cavalo",
        "sheep": "Ovelha",
        "cow": "Vaca",
        "elephant": "Elefante",
        "bear": "Urso",
        "zebra": "Zebra",
        "giraffe": "Girafa",
    }

    def __init__(self, parent, data, go_back_callback):
        """
        Inicializa a tela com os elementos visuais necessários para exibição e exportação de resultados.

        Args:
            parent: Referência ao widget pai.
            data (dict): Dados a serem exibidos e exportados.
            go_back_callback (function): Função de callback para retornar à tela anterior.
        """
        super().__init__(parent)
        self.go_back_callback = go_back_callback  # Callback para voltar à tela anterior
        self.data = data  # Dados recebidos para exibição e exportação

        # Configuração da tela
        self.configure(fg_color="#1D2530")  # Cor de fundo escura

        # Botão de voltar no canto superior esquerdo
        self.back_button = ctk.CTkButton(
            self,
            text="⬅",
            command=self.go_back,  # Callback para voltar à tela anterior
            font=("Arial", 20, "bold"),
            width=50,
            height=40,
            fg_color="#FEFAE0",
            text_color="black",
            hover_color="#d4ac0d",
        )
        self.back_button.place(relx=0.05, rely=0.05, anchor="center")

        # Área de exibição dos resultados
        self.results_frame = ctk.CTkFrame(
            self,
            width=500,
            height=300,
            fg_color="#D9D9D9",  # Cor do retângulo de fundo
            corner_radius=10
        )
        self.results_frame.place(relx=0.4, rely=0.5, anchor="center")

        # Exibir o JSON formatado com alinhamento à esquerda
        self.results_label = ctk.CTkLabel(
            self.results_frame,
            text=self.format_data(data),  # Converte o JSON em texto formatado
            font=("Arial", 16),
            text_color="black",
            justify="left",
            anchor="w"  # Alinha o texto à esquerda
        )
        self.results_label.place(relx=0.05, rely=0.05, anchor="nw")  # Posiciona no canto superior esquerdo

        # Botão de exportação com opções
        self.export_button = ctk.CTkButton(
            self,
            text="⏬ Exportar",
            command=self.show_export_options,  # Mostra opções de exportação
            font=("Arial", 14),
            width=120,
            height=40,
            fg_color="#FEFAE0",
            text_color="black",
            hover_color="#d4ac0d"
        )
        self.export_button.place(relx=0.8, rely=0.2, anchor="center")

    def format_data(self, data):
        """
        Formata os dados para exibição em um formato legível e traduz os nomes para o português.

        Args:
            data (dict): Dados no formato de dicionário.

        Returns:
            str: Dados formatados em texto com linhas separadas.
        """
        formatted_lines = []
        for key, value in data.items():
            translated_key = self.ANIMAL_TRANSLATIONS.get(key, key)  # Tradução ou mantém o original
            formatted_lines.append(f"{translated_key} - {value}")
        return "\n".join(formatted_lines)

    def show_export_options(self):
        """
        Mostra opções para exportação dos dados em diferentes formatos.
        """
        options = [".csv", ".xlsx", ".json", ".txt"]
        for idx, ext in enumerate(options):
            ctk.CTkButton(
                self,
                text=ext,
                command=lambda e=ext: self.export_file(e),  # Exporta no formato escolhido
                font=("Arial", 12),
                width=80,
                height=30,
                fg_color="#D9D9D9",
                text_color="black",
                hover_color="#C0C0C0"
            ).place(relx=0.8, rely=0.3 + idx * 0.06, anchor="center")  # Espaçamento reduzido

    def export_file(self, file_type):
        """
        Exporta os dados para o formato especificado.

        Args:
            file_type (str): Extensão do arquivo ('.txt', '.json', '.csv', '.xlsx').
        """
        file_path = filedialog.asksaveasfilename(defaultextension=file_type, filetypes=[(file_type, f"*{file_type}")])   # Janela para salvar o arquivo

        if file_path:
            # Exporta nos diferentes formatos
            if file_type == ".csv":
                pd.DataFrame.from_dict(self.data, orient="index").to_csv(file_path, header=False)
            elif file_type == ".xlsx":
                pd.DataFrame.from_dict(self.data, orient="index").to_excel(file_path, header=False)
            elif file_type == ".json":
                with open(file_path, "w") as f:
                    json.dump(self.data, f, indent=4)
            elif file_type == ".txt":
                with open(file_path, "w") as f:
                    for key, value in self.data.items():
                        f.write(f"{key} - {value}\n")
            print(f"Arquivo exportado para {file_path}")

    def go_back(self):
        """
        Esconde a tela atual e chama a função de callback para voltar à tela anterior.
        """
        self.pack_forget()
        self.go_back_callback()
