# automato/interface.py
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from automato.core import Automato
from automato.utils import ler_automato_de_arquivo
from automato.visualizador import desenhar_automato

class InterfaceAutomato:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Autômatos Finitos")
        self.root.geometry("800x600")
        
        # Criar frames
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(fill=tk.X, padx=10, pady=5)
        
        self.frame_visualizacao = ttk.Frame(root)
        self.frame_visualizacao.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Criar campos de entrada
        self.label_arquivo = ttk.Label(self.frame_entrada, text="Arquivo CSV:")
        self.label_arquivo.pack(side=tk.LEFT)
        
        self.entrada_arquivo = ttk.Entry(self.frame_entrada, width=50)
        self.entrada_arquivo.pack(side=tk.LEFT, padx=5)
        
        self.botao_carregar = ttk.Button(self.frame_entrada, text="Carregar", command=self.carregar_automato)
        self.botao_carregar.pack(side=tk.LEFT)
        
        # Criar área de visualização
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_visualizacao)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Criar campo para teste de palavras
        self.frame_teste = ttk.Frame(root)
        self.frame_teste.pack(fill=tk.X, padx=10, pady=5)
        
        self.entrada_palavra = ttk.Entry(self.frame_teste, width=40)
        self.entrada_palavra.pack(side=tk.LEFT, padx=5)
        
        self.botao_testar = ttk.Button(self.frame_teste, text="Testar", command=self.testar_palavra)
        self.botao_testar.pack(side=tk.LEFT)
        
        self.label_resultado = ttk.Label(self.frame_teste, text="")
        self.label_resultado.pack(side=tk.LEFT, padx=5)
        
        self.automato = None
        
    def carregar_automato(self):
        try:
            caminho = self.entrada_arquivo.get()
            self.automato = ler_automato_de_arquivo(caminho)
            self.atualizar_visualizacao()
            self.label_resultado.config(text="Autômato carregado com sucesso!")
        except Exception as e:
            self.label_resultado.config(text=f"Erro: {str(e)}")
            
    def atualizar_visualizacao(self):
        self.ax.clear()
        desenhar_automato(self.automato, self.ax)
        self.canvas.draw()
        
    def testar_palavra(self):
        if self.automato is None:
            self.label_resultado.config(text="Carregue um autômato primeiro!")
            return
            
        palavra = self.entrada_palavra.get()
        resultado = self.automato.reconhecer(palavra)
        self.label_resultado.config(text=f"Resultado: {resultado}")

def main():
    root = tk.Tk()
    app = InterfaceAutomato(root)
    root.mainloop()

if __name__ == "__main__":
    main()