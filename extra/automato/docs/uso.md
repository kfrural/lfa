# Guia de Uso do Autômato Finito Determinístico

## Formato do Arquivo CSV
O arquivo CSV deve ter o seguinte formato:

1. Primeira linha: número de estados
2. Segunda linha: alfabeto (sem espaços)
3. Terceira linha: estados finais (separados por vírgula)
4. Linhas subsequentes: transições no formato "estado_origem;estado_destino"

Exemplo:
```
3
ab
1,3
1;2
3;2
1;3
3;3
```

## Exemplo de Uso
```python
from automato.core import Automato
from automato.utils import ler_automato_de_arquivo
from automato.visualizador import desenhar_automato

# Ler o autômato de um arquivo
automato = ler_automato_de_arquivo("automato.csv")

# Visualizar o autômato
desenhar_automato(automato)

# Testar palavras
palavra = "aa"
resultado = automato.reconhecer(palavra)
print(f"A palavra '{palavra}' é aceita? {resultado}")