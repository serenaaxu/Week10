from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._lista_fermate = []
        self._grafo = None

    def getAllFermate(self):
        fermate = DAO.readAllFermate()
        self._lista_fermate = fermate

    def creaGrafo(self):
        self._grafo = nx.Graph()
        print(len(self._lista_fermate))
        for fermata in self._lista_fermate:
            self._grafo.add_node(fermata)
        for u in self._grafo:
            for v in self._grafo[u]:
                print("Cerca connessione tra {u} e {v}")
                risultato = DAO.existsConnessioneTra(u, v)
                if(len(risultato)>0):
                    self._grafo_add_edge(u,v)
                    print(f"Aggiunto arco tra {u} e {v}")


        print(self._grafo)
