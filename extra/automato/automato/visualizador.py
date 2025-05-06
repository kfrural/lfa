import networkx as nx
import matplotlib.pyplot as plt

def desenhar_automato(automato, titulo: str = "Autômato Finito Determinístico"):
    """
    Cria uma visualização do autômato usando networkx e matplotlib.
    
    Args:
        automato: Instância da classe Automato
        titulo: Título do gráfico
    """
    G = nx.DiGraph()
    
    # Adicionar nós (estados)
    for i in range(len(automato.matriz_transicao)):
        G.add_node(i, final=i in automato.estados_finais)
    
    # Adicionar arestas (transições)
    for origem in range(len(automato.matriz_transicao)):
        for simbolo_idx, destino in enumerate(automato.matriz_transicao[origem]):
            if destino != 0:  # Ignora transições vazias
                G.add_edge(origem, destino, label=automato.alfabeto[simbolo_idx])
    
    # Configurar layout
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    
    # Desenhar nós
    cores_nos = ['lightblue' if not G.nodes[n]['final'] else 'lightcoral' 
                 for n in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=cores_nos, node_size=500)
    
    # Desenhar rótulos dos nós
    nx.draw_networkx_labels(G, pos)
    
    # Desenhar arestas
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
    
    # Desenhar rótulos das arestas
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    plt.title(titulo)
    plt.axis('off')
    plt.show()