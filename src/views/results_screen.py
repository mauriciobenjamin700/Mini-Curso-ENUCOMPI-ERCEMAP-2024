import customtkinter as ctk
import json
import pandas as pd
from tkinter import filedialog


class ResultsScreen(ctk.CTkFrame):
    def __init__(self, parent, data, go_back_callback):
        super().__init__(parent)
        self.go_back_callback = go_back_callback  # Callback para voltar à tela anterior

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
        # Converte o JSON em um texto legível
        formatted_text = "\n".join([f"{key} - {value}" for key, value in data.items()])
        return formatted_text

    def show_export_options(self):
        # Janela para exportar o JSON em diferentes formatos
        options = [".csv", ".xlsx", ".json", ".txt", ".pdf"]
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
        # Janela para salvar o arquivo
        file_path = filedialog.asksaveasfilename(defaultextension=file_type, filetypes=[(file_type, f"*{file_type}")])

        if file_path:
            data_dict = {
                "Cavalo": 20,
                "Bois": 10,
                "Zebras": 1,
                "Cabras": 2,
            }
            # Exporta nos diferentes formatos
            if file_type == ".csv":
                pd.DataFrame.from_dict(data_dict, orient="index").to_csv(file_path, header=False)
            elif file_type == ".xlsx":
                pd.DataFrame.from_dict(data_dict, orient="index").to_excel(file_path, header=False)
            elif file_type == ".json":
                with open(file_path, "w") as f:
                    json.dump(data_dict, f, indent=4)
            elif file_type == ".txt":
                with open(file_path, "w") as f:
                    for key, value in data_dict.items():
                        f.write(f"{key} - {value}\n")
            elif file_type == ".pdf":
                # Aqui seria necessário usar uma biblioteca como ReportLab para exportar PDF
                with open(file_path, "w") as f:
                    f.write("PDF exportado (exemplo)\n")
                    for key, value in data_dict.items():
                        f.write(f"{key} - {value}\n")
            print(f"Arquivo exportado para {file_path}")

    def go_back(self):
        # Esconde a tela atual
        self.pack_forget()
        # Chama o callback para exibir a tela anterior
        self.go_back_callback()
