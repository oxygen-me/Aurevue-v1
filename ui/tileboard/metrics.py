from dataclasses import dataclass

@dataclass
class BoardMetrics:
    cols: int = 12
    rows: int = 10
    gap: int = 20
    outer: int = 20
    board_w: int = 1200
    board_h: int = 900

    def tile_size(self):
        tw = (self.board_w - (self.cols - 1) * self.gap - 2 * self.outer) / self.cols
        th = (self.board_h - (self.rows - 1) * self.gap - 2 * self.outer) / self.rows
        return tw, th

    def cell_rect(self, c, r):
        tw, th = self.tile_size()
        x = self.outer + c * (tw + self.gap)
        y = self.outer + r * (th + self.gap)
        return x, y, tw, th


class TilePreset:
    small  = (200, 120)
    medium = (300, 200)
    large  = (420, 280)

