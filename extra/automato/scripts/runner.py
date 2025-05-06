from automato.core import Automato
from automato.utils import ler_automato_de_arquivo
from automato.visualizador import desenhar_automato

def main():
    try:
        print("Lendo arquivo CSV...")
        automato = ler_automato_de_arquivo("data/automato.csv")
        print("Autômato carregado com sucesso!")
        
        print("Criando visualização...")
        desenhar_automato(automato)
        print("Visualização criada com sucesso!")
        
        print("\nDigite palavras para testar (ou 'sair' para encerrar):")
        while True:
            palavra = input().strip()
            if palavra.lower() == 'sair':
                break
            resultado = automato.reconhecer(palavra)
            print(f"Resultado: {resultado}")
            
    except FileNotFoundError:
        print("Erro: Arquivo 'automato.csv' não encontrado.")
    except ImportError as e:
        print(f"Erro: Falta de biblioteca necessária. Instale com 'pip install -r requirements.txt'")
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()
