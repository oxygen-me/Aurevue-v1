from ui.sidebar.sidebar import SideBar
from ui.tiles.presets.weather_tile import WeatherTile
from ui.tiles.presets.notes_tile import NotesTile
from ui.tiles.presets.music_tile import MusicTile
from ui.topbar.topbar import TopBar


class TileManager:
    """Controls creation, rendering, and lifetime of all MicroTiles on a board."""

    def __init__(self, board, metrics):
        self.board = board
        self.metrics = metrics
        print("TileManager init metrics =", self.metrics)
        self.tiles = []

    # -----------------------------
    # Public API
    # -----------------------------
    def add_tile(self, tile):
        """Attach an existing tile instance to the board."""
        tile.setParent(self.board)
        tile.show()
        self.tiles.append(tile)

    def create_tile(self, tile_cls, **kwargs):
        """Spawn a tile from its class (ex: WeatherTile, NotesTile, etc)."""
        tile = tile_cls(self.board, metrics=self.metrics, **kwargs)
        tile.show()
        self.tiles.append(tile)
        return tile

    def clear_tiles(self):
        """Destroy all tiles."""
        for tile in self.tiles:
            tile.setParent(None)
            tile.deleteLater()
        self.tiles.clear()

    def render_default_set(self):
        self.clear_tiles()

        topbar = TopBar(self.board, metrics=self.metrics, grid_x=0, grid_y=0, grid_w=14, grid_h=1)
        sidebar = SideBar(self.board, metrics=self.metrics, grid_x=0, grid_y=1, grid_w=3, grid_h=8)

        note = NotesTile(self.board, metrics=self.metrics, grid_x=3, grid_y=1, grid_w=3, grid_h=2)
        weather = WeatherTile(self.board, metrics=self.metrics, grid_x=6, grid_y=1, grid_w=3, grid_h=2)
        music = MusicTile(self.board, metrics=self.metrics, grid_x=9, grid_y=1, grid_w=5, grid_h=2)

        self.add_tile(topbar)
        self.add_tile(sidebar)

        self.add_tile(note)
        self.add_tile(weather)
        self.add_tile(music)