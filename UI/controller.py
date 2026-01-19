import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        try:
            min_durata = float(self._view.txt_durata.value)
        except ValueError:
            self._view.show_alert("Inserire una durata valida")
            return

        self._model.load_albums(min_durata)
        self._model.load_album_playlists()
        self._model.build_graph()

        # aggiorna dropdown album
        self._view.dd_album.options = [ft.dropdown.Option(a.title) for a in self._model.albums]
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Grafo creato: {len(self._model.G.nodes)} album, {len(self._model.G.edges)} archi")
        )
        self._view.update()

    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        title = e.control.value
        self._selected_album = next((a for a in self._model.albums if a.title == title), None) #next serve a estrarre il primo elemento che soddisfa la condizione del ciclo for

    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        if not self._selected_album:
            self._view.show_alert("Selezionare un album")
            return

        component = self._model.get_component(self._selected_album)
        total_duration = sum(a.duration for a in component)

        self._view.lista_visualizzazione_2.controls.clear()
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Dimensione componente: {len(component)}"))
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Durata totale: {total_duration:.2f} minuti"))
        self._view.update()

