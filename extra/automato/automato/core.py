from typing import List, Set, Dict
import networkx as nx
import matplotlib.pyplot as plt

class Automato:
    def __init__(self, matriz_transicao: List[List[int]], estados_finais: Set[int], alfabeto: str):
        """
        Inicializa o autômato finito determinístico.
        
        Args:
            matriz_transicao: Matriz de transições onde matriz[i][j] é o estado destino
                             ao ler o símbolo j do alfabeto no estado i
            estados_finais: Conjunto de estados finais
            alfabeto: String contendo todos os símbolos do alfabeto
        """
        self.matriz_transicao = matriz_transicao
        self.estados_finais = estados_finais
        self.alfabeto = alfabeto
    
    def reconhecer(self, palavra: str) -> bool:
        """
        Verifica se uma palavra é aceita pelo autômato.
        
        Args:
            palavra: String a ser verificada
            
        Returns:
            bool: True se a palavra é aceita, False caso contrário
        """
        estado_atual = 0
        
        for c in palavra:
            indice_simbolo = self.alfabeto.find(c)
            
            if indice_simbolo == -1:
                return False
                
            estado_atual = self.matriz_transicao[estado_atual][indice_simbolo]
        
        return estado_atual in self.estados_finais