# tests/test_core.py
import unittest
from automato.core import Automato
from .context import automato

class TestAutomato(unittest.TestCase):
    def setUp(self):
        # Criar um autômato de teste que aceita palavras que terminam com 'a'
        self.automato = Automato(
            matriz_transicao=[[1, 2], [2, 3], [3, 3]],
            estados_finais={3},
            alfabeto="ab"
        )
    
    def test_reconhecer(self):
        self.assertTrue(self.automato.reconhecer("aa"))  # Deve aceitar
        self.assertTrue(self.automato.reconhecer("ba"))  # Deve aceitar
        self.assertFalse(self.automato.reconhecer("ab")) # Não deve aceitar
        self.assertFalse(self.automato.reconhecer("bb")) # Não deve aceitar
    
    def test_alfabeto_invalido(self):
        self.assertFalse(self.automato.reconhecer("cx")) # Deve rejeitar símbolo inválido
    
    def test_palavra_vazia(self):
        self.assertFalse(self.automato.reconhecer("")) # Deve rejeitar palavra vazia