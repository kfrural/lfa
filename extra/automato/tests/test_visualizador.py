import unittest
from automato.visualizador import desenhar_automato
from .context import automato

class TestVisualizador(unittest.TestCase):
    def setUp(self):
        self.automato = automato.Automato(
            matriz_transicao=[[1, 2], [2, 3], [3, 3]],
            estados_finais={3},
            alfabeto="ab"
        )
    
    def test_desenhar_automato(self):
        # Verifica se o método executa sem erros
        desenhar_automato(self.automato)