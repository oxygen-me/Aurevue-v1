# ================================================================
# AUREVUE GRID v3 — "MagMotion Base Geometry (10px Layout)"
# Deterministic, pixel-aligned, remainder-free adaptive grid system
# ================================================================

from dataclasses import dataclass
from typing import Tuple, Generator

# ----------------------------------------------------------------
# Temporary manual grid definition (replace later with settings)
# ----------------------------------------------------------------
USER_COLS = 14
USER_ROWS = 9
USER_BUFFER = 10

# ================================================================
# DATA CLASSES
# ================================================================

@dataclass(frozen=True)
class GridConfig:
    cols: int = USER_COLS
    rows: int = USER_ROWS
    t_buffer: int = USER_BUFFER
    margin_x: int = 10  # 10px margin on left/right
    margin_y: int = 10   # 10px margin on top/bottom


@dataclass(frozen=True)
class GridMetrics:
    win_w: int
    win_h: int

    cols: int
    rows: int

    tile_w: int
    tile_h: int

    t_buffer: int

    margin_x: int
    margin_y: int

    inner_w: int
    inner_h: int

    # 👇 Move it here — 4-space indent to be inside the class
    def to_pixels(self, grid_x, grid_y, grid_w=1, grid_h=1):
        """Convert grid coordinates to absolute pixel geometry."""
        x = self.margin_x + grid_x * self.tile_w
        y = self.margin_y + grid_y * self.tile_h
        w = grid_w * self.tile_w
        h = grid_h * self.tile_h
        return x, y, w, h


# ================================================================
# CORE GRID CALCULATION
# ================================================================

def calc_grid(win_w: int, win_h: int, cfg: GridConfig) -> GridMetrics:
    """
    Grid fits perfectly inside the frame — no part outside.
    """
    # Inner drawable area (10 px margins on all sides)
    inner_w = win_w - (cfg.margin_x * 2)
    inner_h = win_h - (cfg.margin_y * 2)

    # Tile size fits exactly within that space
    tile_w = inner_w / cfg.cols
    tile_h = inner_h / cfg.rows

    return GridMetrics(
        win_w=win_w,
        win_h=win_h,
        cols=cfg.cols,
        rows=cfg.rows,
        margin_x=cfg.margin_x,
        margin_y=cfg.margin_y,
        t_buffer=cfg.t_buffer,
        tile_w=tile_w,
        tile_h=tile_h,
        inner_w=inner_w,
        inner_h=inner_h,
    )

# ================================================================
# RECT + DEBUG UTILITIES
# ================================================================

def cell_rect(col: int, row: int, span_x: int, span_y: int, gm: GridMetrics) -> Tuple[int, int, int, int]:
    """Return pixel-space rect for a given grid coordinate and span."""
    col = max(0, min(col, gm.cols - 1))
    row = max(0, min(row, gm.rows - 1))
    span_x = max(1, min(span_x, gm.cols - col))
    span_y = max(1, min(span_y, gm.rows - row))

    x = gm.margin_x + col * (gm.tile_w + gm.t_buffer)
    y = gm.margin_y + row * (gm.tile_h + gm.t_buffer)
    w = gm.tile_w * span_x + gm.t_buffer * (span_x - 1)
    h = gm.tile_h * span_y + gm.t_buffer * (span_y - 1)
    return x, y, w, h


def grid_lines(gm: GridMetrics) -> Generator[Tuple[int, int, int, int], None, None]:
    """Yield all pixel line segments for a debug overlay."""
    # outer frame
    yield (gm.margin_x, gm.margin_y, gm.margin_x + gm.inner_w, gm.margin_y)  # top
    yield (gm.margin_x, gm.margin_y + gm.inner_h, gm.margin_x + gm.inner_w, gm.margin_y + gm.inner_h)  # bottom
    yield (gm.margin_x, gm.margin_y, gm.margin_x, gm.margin_y + gm.inner_h)  # left
    yield (gm.margin_x + gm.inner_w, gm.margin_y, gm.margin_x + gm.inner_w, gm.margin_y + gm.inner_h)  # right

    # verticals
    for c in range(1, gm.cols):
        x = gm.margin_x + c * (gm.tile_w + gm.t_buffer)
        yield (x, gm.margin_y, x, gm.margin_y + gm.inner_h)

    # horizontals
    for r in range(1, gm.rows):
        y = gm.margin_y + r * (gm.tile_h + gm.t_buffer)
        yield (gm.margin_x, y, gm.margin_x + gm.inner_w, y)

class TileMetrics:
    """
    Aurevue unified grid translator.
    Handles absolute geometry based on window, margins, and DPI scaling.
    Spacers are deprecated — tiles fill their full conceptual units.
    """

    def __init__(self, win_w, win_h, cols, rows,
                 margin_x=10, margin_y=10,
                 scale=1.0):
        # ----- Base window geometry -----
        self.win_w = win_w
        self.win_h = win_h
        self.cols = cols
        self.rows = rows
        self.margin_x = margin_x
        self.margin_y = margin_y
        self.scale = scale

        # ----- Derived grid area -----
        self.inner_w = (win_w - 2 * margin_x)
        self.inner_h = (win_h - 2 * margin_y)

        # ----- Derived tile size -----
        self.tile_w = (self.inner_w / cols)
        self.tile_h = (self.inner_h / rows)