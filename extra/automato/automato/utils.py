import csv
from .core import Automato
from typing import List, Set
import networkx as nx
import matplotlib.pyplot as plt
# automato/utils.py
def ler_automato_de_arquivo(caminho_arquivo: str) -> Automato:
    matriz_transicao = []
    estados_finais = set()
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            
            # Ler número de estados
            try:
                linha = next(leitor)
                if not linha:
                    raise ValueError("Número de estados não pode estar vazio")
                num_estados = int(linha[0])
                if num_estados <= 0:
                    raise ValueError("Número de estados deve ser positivo")
            except (IndexError, ValueError) as e:
                raise IndexError(f"Erro na linha 1: {str(e)}")
            
            # Ler alfabeto
            try:
                linha = next(leitor)
                if not linha:
                    raise ValueError("Alfabeto não pode estar vazio")
                alfabeto = linha[0].strip()
                if not alfabeto:
                    raise ValueError("Alfabeto não pode estar vazio")
            except (IndexError, ValueError) as e:
                raise IndexError(f"Erro na linha 2: {str(e)}")
            
            # Ler estados finais
            try:
                linha = next(leitor)
                if not linha:
                    raise ValueError("Estados finais não podem estar vazios")
                estados_finais_str = linha[0].split(',')
                estados_finais = {int(estado.strip()) for estado in estados_finais_str}
                if not all(0 <= estado < num_estados for estado in estados_finais):
                    raise ValueError("Estados finais inválidos")
            except (IndexError, ValueError) as e:
                raise IndexError(f"Erro na linha 3: {str(e)}")
            
            # Criar matriz de transição vazia
            matriz_transicao = [[0] * len(alfabeto) for _ in range(num_estados)]
            
            # Ler transições com número da linha
            linha_num = 4  # Começa na linha 4 (já lemos 3 linhas)
            for linha in leitor:
                if not linha:
                    continue
                try:
                    origem, destino = map(int, linha[0].split(';'))
                    if not (0 <= origem < num_estados and 0 <= destino < num_estados):
                        raise ValueError(f"Estados de transição inválidos: origem={origem}, destino={destino}")
                    for i, simbolo in enumerate(alfabeto):
                        matriz_transicao[origem][i] = destino
                except (IndexError, ValueError) as e:
                    raise IndexError(f"Linha {linha_num}: {str(e)}")
                linha_num += 1
            
            return Automato(matriz_transicao, estados_finais, alfabeto)
            
    except Exception as e:
        raise Exception(f"Erro ao ler o arquivo: {str(e)}")