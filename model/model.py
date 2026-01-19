import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.albums = []
        self.album_playlist_map = {}
        self.id_map = {}

    def load_albums(self, min_duration):
        """Carica album con durata totale > min_duration (in minuti)"""
        self.albums = DAO.get_album_by_min_duration(min_duration)
        self.id_map = {a.id: a for a in self.albums}

    def load_album_playlists(self):
        """Mappa album -> playlist"""
        self.album_playlist_map = DAO.get_album_playlist_map(self.albums)

    def build_graph(self):
        """Crea il grafo non orientato basato sulle playlist condivise"""
        self.G.clear()
        self.G.add_nodes_from(self.albums)

        for i, a1 in enumerate(self.albums):
            for a2 in self.albums[i+1:]:
                if self.album_playlist_map[a1] & self.album_playlist_map[a2]:
                    self.G.add_edge(a1, a2)

    def get_component(self, album):
        """Restituisce la componente connessa di un album"""
        if album not in self.G:
            return []
        return list(nx.node_connected_component(self.G, album))


