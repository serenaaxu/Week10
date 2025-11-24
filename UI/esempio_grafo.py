import networkx as nx

g = nx.Graph() # grafo semplice

g.add_node(1)   # aggiunge un nodo al grafo
# g.add_node("abc")
# f.add_node(ft.Text())
g.add_node(2)

g.add_edge(1,2, attributo = "pippo")
g.add_edge(1,2) # per creare un arco si usa add_edge
g.add_edge(2,3)
g.add_edge(2,3) # non ha effetto su un grafo semplice ripeterlo


print(f"Arco tra 1 e 2: {g[1][2]}")


altri_nodi = [4,5,6,7,8]
g.add_nodes_from(altri_nodi) # ogni arco è una tupla

altri_archi = [ (2,4), (4,5), (6,7), (6,8),(1,4)]
g.add_nodes_from(altri_archi)


print(g.edges)

primo_nodo = g[1] # dizionario
print(primo_nodo)

if 12 in g:
    print("Nodo presente")
else:
    print("Nodo assente")

# stampo nodi
for nodo in g:
    print(nodo)


print("Stampo i vicini del nodo 1")
for nodo in g[1]:
    print(nodo) # printa i nodi collegati al nodo 1

densita = nx.density(g)
print(f"Densita: {densita}")

dg = nx.DiGraph() # grafo diretto
dg.add_nodes_from(altri_nodi)
dg.add_edges_from(altri_archi)
print(dg.edges)
print(dg[4]) # mi dice che esiste un arco verso 5
print(dg[5]) # mi dice che non esistono archi

mg = nx.MultiDiGraph()
mg.add_edge(1,2, weight = 5) # arco 0
mg.add_edge(1,2) # arco 1
mg.add_edge(1,2) # arco 2
# dizionario di dizionari di dizionari
print(mg[1])
print(f"Arco tra 1 e 2 0-mo: {mg[1],[2],[0]}")