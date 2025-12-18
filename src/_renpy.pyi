from renpy.pygame.surface import Surface as Surface

def alpha_munge(pysrc: Surface, pydst: Surface, srcchan: int, dstchan: int, amap: bytes) -> None: ...
def bilinear(
    pysrc: Surface,
    pydst: Surface,
    source_xoff: float = 0.0,
    source_yoff: float = 0.0,
    source_width: float | None = None,
    source_height: float | None = None,
    dest_xoff: float = 0.0,
    dest_yoff: float = 0.0,
    dest_width: float | None = None,
    dest_height: float | None = None,
    precise: int = 0,
) -> None: ...
def blend(pysrc: Surfacea, pysrcb, pydst: Surface, alpha): ...
def blur(pysrc: Surface, pywrk: Surface, pydst: Surface, xrad: float, yrad: float | None = None) -> None: ...
def check(surf: Surface) -> None: ...
def colormatrix(
    pysrc: Surface,
    pydst: Surface,
    c00: float,
    c01: float,
    c02: float,
    c03: float,
    c04: float,
    c10: float,
    c11: float,
    c12: float,
    c13: float,
    c14: float,
    c20: float,
    c21: float,
    c22: float,
    c23: float,
    c24: float,
    c30: float,
    c31: float,
    c32: float,
    c33: float,
    c34: float,
) -> None: ...
def imageblend(pysrc: Surface, pysrcb, pydst: Surface, pyimg: Surface, aoff: int, amap: bytes) -> None: ...
def linblur(pysrc: Surface, pydst: Surface, radius: int, vertical: int = 0) -> None: ...
def linmap(pysrc: Surface, pydst: Surface, r: int, g: int, b: int, a: int) -> None: ...
def map(pysrc: Surface, pydst: Surface, r: bytes, g: bytes, b: bytes, a: bytes) -> None: ...
def pixellate(pysrc: Surface, pydst: Surface, avgwidth: int, avgheight: int, outwidth: int, outheight: int) -> None: ...
def premultiply_alpha(pysrc: Surface, pydst: Surface) -> None: ...
def save_png(surf: Surface, file: str, compress: int = -1) -> None: ...
def staticgray(
    pysrc: Surface, pydst: Surface, rmul: int, gmul: int, bmul: int, amul: int, shift: int, vmap: bytes
) -> None: ...
def subpixel(pysrc: Surface, pydst: Surface, xoffset: float, yoffset: float, shift: int) -> None: ...
def transform(
    pysrc: Surface,
    pydst: Surface,
    corner_x: float,
    corner_y: float,
    xdx: float,
    ydx: float,
    xdy: float,
    ydy: float,
    a: float = 1.0,
    precise: int = 0,
) -> None: ...
def version() -> tuple[int, int, int]: ...
