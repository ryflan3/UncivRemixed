#!/usr/bin/env python3
"""Pixel-art map sprites for the mod's tile improvements.

Each sprite is drawn on a 64x64 canvas whose bottom 56 rows are the hex (centre 32,36), in the HexaRealm
proportions. A ground layer (fields, water, earthworks) is drawn flat; an object layer (buildings, boats,
trees) gets a dark one-pixel outline. FantasyHex versions are the same sprites reduced 2:1.
"""
import os, sys, math, collections
from PIL import Image, ImageDraw

STONE, STONE_D, STONE_L = (150, 146, 140), (108, 104, 102), (186, 182, 174)
SAND, SAND_D = (222, 196, 140), (184, 154, 100)
WHITE, WHITE_D = (242, 238, 226), (204, 198, 182)
RED, RED_D = (190, 76, 48), (146, 52, 34)
THATCH, THATCH_D = (206, 170, 88), (160, 124, 56)
WOOD, WOOD_D, WOOD_L = (132, 86, 46), (90, 56, 30), (170, 120, 70)
WATER, WATER_L = (84, 166, 212), (156, 212, 238)
GREEN, GREEN_D = (92, 150, 64), (58, 108, 46)
DARK = (44, 32, 26)
SLATE, SLATE_D = (88, 98, 118), (60, 68, 86)

def dk(c, f=0.74): return tuple(int(v * f) for v in c[:3])
def lt(c, f=1.18): return tuple(min(255, int(v * f)) for v in c[:3])

class Sp:
    def __init__(self):
        self.g = Image.new('RGBA', (64, 64), (0, 0, 0, 0)); self.o = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
        self.G = ImageDraw.Draw(self.g); self.O = ImageDraw.Draw(self.o)
    def finish(self, outline=DARK, half=False):
        g, o = (halve(self.g), halve(self.o)) if half else (self.g, self.o.copy())
        n = o.size[0]; px = o.load(); edge = []
        for y in range(n):
            for x in range(n):
                if px[x, y][3]: continue
                if any(0 <= x + dx < n and 0 <= y + dy < n and px[x + dx, y + dy][3] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    edge.append((x, y))
        for x, y in edge: px[x, y] = outline + (255,)
        im = Image.alpha_composite(g, o)
        if im.crop((0, 0, n, n // 8)).getbbox() is None: im = im.crop((0, n // 8, n, n))
        return im

# ----------------------------------------------------------------------------- building blocks (object layer)
def box(d, x, y, w, h, c, shade=True):
    """Wall with its bottom-left corner at (x, y)."""
    d.rectangle((x, y - h + 1, x + w - 1, y), fill=c)
    if shade and w >= 4: d.rectangle((x + w - max(1, w // 3), y - h + 1, x + w - 1, y), fill=dk(c, 0.84))
def gable(d, x, y, w, rh, c, over=1):
    """Gable roof sitting on a wall whose top-left is (x, y)."""
    mid = x + (w - 1) / 2
    d.polygon([(x - over, y), (x + w - 1 + over, y), (math.ceil(mid), y - rh), (math.floor(mid), y - rh)], fill=c)
    d.polygon([(math.ceil(mid), y - rh), (x + w - 1 + over, y), (math.ceil(mid), y)], fill=dk(c, 0.8))
def hip(d, x, y, w, rh, c, inset=3, over=1):
    d.polygon([(x - over, y), (x + w - 1 + over, y), (x + w - 1 - inset, y - rh), (x + inset, y - rh)], fill=c)
    d.polygon([(x + w // 2, y - rh), (x + w - 1 - inset, y - rh), (x + w - 1 + over, y), (x + w // 2, y)], fill=dk(c, 0.8))
def house(d, x, y, w, h, wall, roof, rh=None, door=True, kind='gable'):
    box(d, x, y, w, h, wall)
    (gable if kind == 'gable' else hip)(d, x, y - h, w, rh or max(3, w // 2), roof)
    if door: d.rectangle((x + w // 2 - 1, y - min(3, h - 1), x + w // 2, y), fill=DARK)
def tower(d, x, y, w, h, c, roof=None, rh=5, window=True):
    box(d, x, y, w, h, c)
    if roof: d.polygon([(x - 1, y - h), (x + w, y - h), (x + w // 2, y - h - rh), (x + (w - 1) // 2, y - h - rh)], fill=roof)
    else:
        for i in range(0, w, 2): d.point((x + i, y - h), fill=c)
    if window: d.rectangle((x + w // 2 - 1, y - h + 3, x + w // 2 - 1, y - h + 4), fill=DARK)
def flag(d, x, y, h, c1, c2=None, w=6):
    d.line((x, y, x, y - h), fill=(70, 64, 60))
    d.rectangle((x + 1, y - h, x + w, y - h + 3), fill=c1)
    if c2: d.rectangle((x + 1 + w // 2, y - h, x + w, y - h + 3), fill=c2)
def tree(d, x, y, c=GREEN, r=3):
    d.line((x, y, x, y - 2), fill=WOOD_D)
    d.ellipse((x - r, y - 2 - 2 * r + 1, x + r, y - 2), fill=c); d.ellipse((x - r + 1, y - 2 - 2 * r + 1, x + 1, y - r - 1), fill=lt(c))
def palm(d, x, y, h=9):
    d.line((x, y, x + 1, y - h), fill=WOOD, width=1); d.point((x, y - h // 2), fill=WOOD_D)
    for dx, dy in ((-5, 1), (-4, -2), (0, -4), (4, -2), (5, 1)):
        d.line((x + 1, y - h, x + 1 + dx, y - h + dy), fill=GREEN_D)
        d.point((x + 1 + dx // 2, y - h + dy // 2 - 1), fill=GREEN)
def dome(d, x, y, w, h, c):
    d.pieslice((x, y - h, x + w - 1, y + h - 1), 180, 360, fill=c); d.pieslice((x + w // 2, y - h, x + w - 1, y + h - 1), 270, 360, fill=dk(c, 0.82))
def barrel(d, x, y):
    d.rectangle((x, y - 3, x + 2, y), fill=WOOD); d.point((x, y - 2), fill=WOOD_L); d.line((x, y - 1, x + 2, y - 1), fill=WOOD_D)
def crate(d, x, y, s=3):
    d.rectangle((x, y - s, x + s, y), fill=WOOD_L); d.line((x, y - s, x + s, y), fill=WOOD_D)
def cow(d, x, y, c=WHITE, patch=WOOD_D):
    d.rectangle((x, y - 2, x + 4, y - 1), fill=c); d.point((x + 5, y - 3), fill=c); d.point((x + 1, y - 2), fill=patch); d.point((x + 3, y - 1), fill=patch)
    d.point((x, y), fill=dk(c)); d.point((x + 4, y), fill=dk(c))
def fence(d, pts, c=WOOD_D):
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]; n = max(abs(x1 - x0), abs(y1 - y0))
        for s in range(0, n + 1):
            x = round(x0 + (x1 - x0) * s / n); y = round(y0 + (y1 - y0) * s / n)
            d.point((x, y), fill=c)
            if s % 3 == 0: d.point((x, y - 1), fill=c)
def ring(d, box_, c, step=2.2, r=0, top=None):
    """Dots (posts, thorn bushes) around an ellipse."""
    x0, y0, x1, y1 = box_; cx, cy, rx, ry = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2, (y1 - y0) / 2
    n = int(2 * math.pi * max(rx, ry) / step)
    for i in range(n):
        a = 2 * math.pi * i / n; x = round(cx + rx * math.cos(a)); y = round(cy + ry * math.sin(a))
        d.rectangle((x - r, y - r - 1, x + r, y), fill=c)
        if top: d.point((x, y - r - 1), fill=top)
def boat(d, x, y, w=12, hull=WOOD, sail=WHITE, sh=9, stripes=None):
    d.polygon([(x, y - 2), (x + w, y - 2), (x + w - 2, y + 1), (x + 2, y + 1)], fill=hull); d.line((x + 1, y - 2, x + w - 1, y - 2), fill=WOOD_L)
    mx = x + w // 2
    d.line((mx, y - 3, mx, y - 3 - sh), fill=WOOD_D)
    if sail:
        d.polygon([(mx + 1, y - 3 - sh), (mx + 1, y - 4), (mx + w // 2 - 1, y - 4)], fill=sail) if stripes is None else None
        if stripes:
            for i in range(sh - 2):
                d.line((mx - w // 2 + 2, y - 3 - sh + 1 + i, mx + w // 2 - 2, y - 3 - sh + 1 + i), fill=stripes[(i // 2) % 2])

# ----------------------------------------------------------------------------- the sprites
def arctic_research_station():
    s = Sp(); G, O = s.G, s.O
    G.ellipse((12, 40, 52, 50), fill=(228, 236, 244)); G.ellipse((16, 42, 44, 48), fill=(246, 250, 253))
    for x in (19, 26, 33, 38): O.line((x, 40, x, 43), fill=STONE_D)
    box(O, 17, 40, 24, 8, (228, 112, 44)); O.rectangle((17, 32, 40, 33), fill=(246, 150, 70))
    for x in (20, 25, 30): O.rectangle((x, 35, x + 2, 37), fill=(60, 96, 140))
    O.rectangle((35, 36, 37, 40), fill=DARK)
    dome(O, 41, 42, 12, 8, WHITE); O.line((41, 42, 52, 42), fill=WHITE_D)
    O.line((14, 43, 14, 20), fill=STONE_D); O.line((11, 26, 17, 26), fill=STONE_D); O.line((12, 30, 16, 30), fill=STONE_D); O.point((14, 19), fill=(230, 40, 40))
    flag(O, 46, 33, 9, (230, 60, 50), w=5)
    return s

def rice_paddy():
    s = Sp(); G = s.G
    bund = (124, 100, 62); water = (110, 178, 196); shoot = (150, 206, 96); shoot_d = (92, 160, 70)
    for poly in ([(13, 34), (27, 27), (33, 35), (19, 43)], [(30, 26), (45, 27), (50, 35), (36, 34)],
                 [(22, 45), (35, 37), (49, 38), (44, 49), (29, 52)], [(11, 37), (17, 45), (15, 40)]):
        G.polygon(poly, fill=water, outline=bund)
        xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
        m = Image.new('L', (64, 64), 0); ImageDraw.Draw(m).polygon(poly, fill=255); mp = m.load(); gp = s.g.load()
        for y in range(min(ys) + 1, max(ys)):
            for x in range(min(xs) + 1, max(xs)):
                if mp[x, y] and gp[x, y][:3] == water and y % 2 == 0 and (x + y // 2) % 2 == 0:
                    gp[x, y] = (shoot if (x + y) % 4 else shoot_d) + (255,)
    return s

def mountain_citadel():
    s = Sp(); G, O = s.G, s.O
    O.polygon([(15, 54), (21, 40), (27, 33), (37, 32), (45, 41), (50, 54)], fill=(118, 112, 110))
    O.polygon([(33, 32), (37, 32), (45, 41), (50, 54), (36, 54)], fill=(88, 84, 86))
    O.line((21, 44, 26, 50), fill=(96, 92, 92)); O.line((30, 40, 33, 47), fill=(140, 134, 130))
    tower(O, 20, 37, 6, 12, (92, 90, 96)); tower(O, 39, 39, 6, 11, (80, 78, 86))
    box(O, 25, 34, 14, 10, (100, 98, 104)); tower(O, 28, 33, 8, 20, (112, 110, 116))
    O.rectangle((31, 30, 32, 34), fill=DARK); O.point((30, 20), fill=(250, 220, 90)); O.point((33, 24), fill=(250, 220, 90))
    flag(O, 32, 13, 8, (20, 120, 50), w=6)
    return s

def fortress():
    s = Sp(); G, O = s.G, s.O
    G.polygon([(14, 30), (50, 30), (52, 46), (12, 46)], fill=(134, 112, 78))
    box(O, 15, 31, 34, 5, STONE_L); tower(O, 13, 32, 5, 9, STONE_L, window=False); tower(O, 46, 32, 5, 9, STONE, window=False)
    box(O, 27, 40, 10, 10, (128, 124, 122)); hip(O, 27, 30, 10, 4, (60, 110, 70), inset=2)
    box(O, 13, 48, 38, 7, STONE)
    for x in range(13, 51, 2): O.point((x, 41), fill=STONE)
    tower(O, 11, 49, 6, 12, STONE, window=False); tower(O, 47, 49, 6, 12, STONE_D, window=False)
    O.rectangle((30, 44, 33, 48), fill=DARK); O.point((30, 44), fill=STONE); O.point((33, 44), fill=STONE)
    flag(O, 32, 26, 8, (20, 120, 50), w=6)
    return s

def hillfort():
    s = Sp(); G, O = s.G, s.O
    G.ellipse((8, 22, 56, 54), fill=(126, 132, 70)); G.ellipse((11, 24, 53, 51), fill=(150, 152, 84))
    G.ellipse((14, 26, 50, 48), fill=(112, 120, 62)); G.ellipse((16, 27, 48, 46), fill=(160, 146, 96))
    G.polygon([(29, 46), (35, 46), (37, 54), (27, 54)], fill=(160, 146, 96))
    ring(O, (16, 28, 48, 46), WOOD_D, step=2.0, top=WOOD_L)
    O.rectangle((29, 44, 35, 48), fill=(0, 0, 0, 0))
    for x, y in ((24, 38), (34, 35), (38, 42)):
        O.rectangle((x, y - 2, x + 5, y), fill=(190, 170, 130)); O.polygon([(x - 1, y - 3), (x + 6, y - 3), (x + 3, y - 8), (x + 2, y - 8)], fill=THATCH)
        O.polygon([(x + 3, y - 8), (x + 6, y - 3), (x + 3, y - 3)], fill=THATCH_D); O.point((x + 2, y), fill=DARK)
    return s

def dry_dock():
    s = Sp(); G, O = s.G, s.O
    G.rectangle((20, 26, 43, 50), fill=(60, 132, 180)); G.rectangle((22, 28, 41, 50), fill=(96, 170, 208))
    for x in (15, 44): box(O, x, 51, 5, 26, WOOD)
    for y in range(28, 51, 4): O.line((15, y, 19, y), fill=WOOD_D); O.line((44, y, 48, y), fill=WOOD_D)
    box(O, 15, 27, 34, 3, WOOD_L)
    O.polygon([(26, 31), (37, 31), (39, 40), (36, 49), (27, 49), (24, 40)], fill=(176, 130, 78))
    O.line((31, 31, 31, 49), fill=WOOD_D); O.line((32, 31, 32, 49), fill=WOOD)
    for y in (34, 38, 42, 46): O.line((26, y, 37, y), fill=WOOD_D)
    O.line((50, 46, 50, 22), fill=WOOD_D); O.line((50, 22, 40, 26), fill=WOOD_D); O.line((40, 26, 40, 30), fill=(60, 60, 64))
    O.rectangle((51, 44, 54, 47), fill=WOOD_L)
    return s

def caravanserai():
    s = Sp(); G, O = s.G, s.O
    G.polygon([(16, 27), (48, 27), (50, 44), (14, 44)], fill=(238, 216, 164))
    box(O, 16, 29, 32, 5, lt(SAND, 1.06))
    for x in range(19, 46, 5): O.rectangle((x, 26, x + 1, 28), fill=SAND_D)
    box(O, 14, 43, 4, 13, SAND, shade=False); box(O, 46, 43, 4, 13, SAND_D, shade=False)
    box(O, 14, 48, 36, 8, SAND)
    for x in (18, 23, 39, 44): O.rectangle((x, 44, x + 1, 46), fill=SAND_D)
    O.rectangle((29, 42, 34, 48), fill=DARK); O.rectangle((30, 41, 33, 41), fill=DARK)
    dome(O, 13, 40, 7, 4, (64, 158, 164)); dome(O, 44, 40, 7, 4, (64, 158, 164)); dome(O, 28, 24, 8, 4, (64, 158, 164))
    G.rectangle((30, 34, 33, 36), fill=WATER); G.rectangle((29, 33, 34, 33), fill=STONE)
    palm(O, 54, 44, 10)
    O.rectangle((6, 46, 10, 48), fill=(196, 152, 96)); O.point((11, 45), fill=(196, 152, 96)); O.point((8, 45), fill=(196, 152, 96)); O.line((6, 49, 6, 50), fill=(150, 110, 66)); O.line((10, 49, 10, 50), fill=(150, 110, 66))
    return s

def longphort():
    s = Sp(); G, O = s.G, s.O
    G.ellipse((12, 22, 52, 46), fill=(150, 140, 96))
    G.polygon([(14, 44), (50, 44), (52, 54), (12, 54)], fill=(96, 170, 208)); G.line((16, 49, 26, 49), fill=WATER_L); G.line((38, 52, 48, 52), fill=WATER_L)
    x0, y0, x1, y1 = 12, 22, 52, 48; cx, cy, rx, ry = 32, 35, 20, 13
    for i in range(0, 46):
        a = math.pi + math.pi * i / 45; x = round(cx + rx * math.cos(a)); y = round(cy + ry * math.sin(a))
        O.rectangle((x, y - 3, x, y), fill=WOOD if i % 2 else WOOD_D); O.point((x, y - 4), fill=WOOD_L)
    house(O, 17, 39, 12, 4, WOOD_D, THATCH, rh=5, kind='hip'); house(O, 34, 36, 12, 4, WOOD_D, THATCH, rh=5, kind='hip')
    O.polygon([(18, 47), (46, 47), (43, 51), (21, 51)], fill=WOOD); O.line((19, 47, 45, 47), fill=WOOD_L)
    O.line((18, 47, 16, 43), fill=WOOD); O.point((15, 42), fill=WOOD_L); O.line((46, 47, 48, 44), fill=WOOD)
    for x in range(22, 44, 3): O.point((x, 49), fill=(214, 60, 44) if (x // 3) % 2 else (240, 210, 80))
    O.line((32, 46, 32, 34), fill=WOOD_D)
    for i in range(8):
        O.line((26, 35 + i, 38, 35 + i), fill=(200, 50, 44) if (i // 2) % 2 == 0 else WHITE)
    return s

def hidden_cove():
    s = Sp(); G, O = s.G, s.O
    G.polygon([(14, 40), (50, 40), (52, 53), (12, 53)], fill=(96, 170, 208)); G.ellipse((20, 36, 44, 48), fill=(70, 140, 190))
    O.polygon([(10, 44), (13, 30), (20, 22), (30, 19), (42, 21), (50, 28), (54, 44), (46, 44), (43, 36), (36, 31), (28, 31), (22, 36), (19, 44)], fill=(112, 106, 104))
    O.polygon([(30, 19), (42, 21), (50, 28), (54, 44), (46, 44), (43, 36), (36, 31), (32, 31)], fill=(84, 80, 82))
    O.polygon([(13, 30), (20, 22), (30, 19), (26, 24), (18, 29)], fill=(146, 140, 134))
    O.pieslice((25, 28, 39, 46), 180, 360, fill=(26, 22, 28)); O.rectangle((25, 37, 39, 39), fill=(26, 22, 28))
    for x, y in ((16, 26), (24, 20), (38, 20), (47, 26)): O.ellipse((x - 3, y - 4, x + 3, y), fill=GREEN_D); O.point((x - 1, y - 3), fill=GREEN)
    boat(O, 26, 46, 12, hull=WOOD_D, sail=None, sh=8)
    O.polygon([(33, 35), (33, 42), (38, 42)], fill=(30, 28, 32)); O.point((34, 40), fill=WHITE)
    O.rectangle((44, 48, 48, 50), fill=(150, 96, 40)); O.line((44, 48, 48, 48), fill=(246, 208, 70)); O.point((46, 49), fill=(246, 208, 70))
    return s

def onsen():
    s = Sp(); G, O = s.G, s.O
    G.ellipse((22, 36, 52, 52), fill=(120, 116, 112)); G.ellipse((24, 37, 50, 50), fill=(150, 222, 224)); G.ellipse((28, 39, 42, 45), fill=(196, 240, 240))
    for x, y in ((22, 42), (26, 37), (36, 36), (46, 38), (50, 44), (44, 50), (32, 51), (25, 48)):
        O.ellipse((x - 2, y - 2, x + 2, y + 1), fill=(128, 124, 122)); O.point((x - 1, y - 2), fill=(170, 166, 160))
    for x, y in ((31, 34), (38, 30), (43, 34), (34, 27)):
        G.point((x, y), fill=(255, 255, 255, 230)); G.point((x + 1, y - 1), fill=(255, 255, 255, 200)); G.point((x, y - 2), fill=(255, 255, 255, 170)); G.point((x + 1, y - 3), fill=(255, 255, 255, 120))
    box(O, 10, 36, 14, 6, WHITE)
    O.polygon([(7, 30), (26, 30), (22, 25), (11, 25)], fill=(176, 52, 44)); O.polygon([(17, 25), (22, 25), (26, 30), (17, 30)], fill=(134, 38, 34))
    O.point((6, 29), fill=(176, 52, 44)); O.point((27, 29), fill=(134, 38, 34)); O.line((11, 24, 22, 24), fill=(90, 30, 28))
    O.rectangle((15, 33, 18, 36), fill=(96, 60, 36)); O.line((10, 33, 13, 33), fill=WHITE_D)
    O.rectangle((14, 44, 16, 46), fill=STONE); O.rectangle((13, 43, 17, 43), fill=STONE_D); O.point((15, 45), fill=(250, 220, 90)); O.line((15, 47, 15, 49), fill=STONE_D)
    return s

def isibaya():
    s = Sp(); G, O = s.G, s.O
    G.ellipse((9, 22, 55, 52), fill=(176, 150, 96)); G.ellipse((22, 31, 42, 45), fill=(150, 122, 78))
    ring(O, (9, 22, 55, 52), (110, 84, 44), step=2.0, top=(150, 120, 60))
    ring(O, (22, 31, 42, 45), WOOD_D, step=2.2)
    for x, y in ((15, 34), (22, 27), (32, 25), (42, 28), (48, 35), (44, 46), (18, 45)):
        dome(O, x - 3, y, 7, 5, THATCH); O.point((x, y), fill=DARK)
    cow(O, 26, 37); cow(O, 33, 41, c=(110, 70, 40), patch=WHITE); cow(O, 31, 35, c=(60, 44, 36), patch=WHITE)
    O.rectangle((30, 50, 34, 53), fill=(0, 0, 0, 0))
    return s

def olive_grove():
    s = Sp(); G, O = s.G, s.O
    for y in (30, 37, 44): G.line((13, y + 2, 50, y + 2), fill=(170, 150, 104))
    leaf = (130, 150, 100)
    for row, (y, xs) in enumerate(((30, (20, 30, 40)), (37, (15, 25, 35, 45)), (44, (20, 30)))):
        for x in xs:
            O.line((x, y, x, y - 2), fill=(96, 72, 48)); O.point((x - 1, y - 1), fill=(96, 72, 48))
            O.ellipse((x - 4, y - 8, x + 4, y - 2), fill=leaf); O.ellipse((x - 3, y - 8, x + 1, y - 5), fill=lt(leaf, 1.14))
            O.point((x + 2, y - 4), fill=(60, 50, 70)); O.point((x - 2, y - 3), fill=(60, 50, 70))
    house(O, 38, 49, 9, 5, STONE_L, RED, rh=4)
    O.ellipse((49, 45, 53, 49), fill=STONE); O.point((51, 47), fill=STONE_D)
    return s

def distillery():
    s = Sp(); G, O = s.G, s.O
    G.ellipse((10, 40, 54, 52), fill=(140, 130, 96))
    house(O, 12, 47, 22, 9, STONE, SLATE, rh=6, kind='hip')
    for x in (15, 20, 28): O.rectangle((x, 41, x + 1, 43), fill=(250, 214, 110))
    box(O, 33, 47, 11, 14, STONE_L)
    O.polygon([(31, 33), (45, 33), (41, 27), (35, 27)], fill=SLATE); O.polygon([(38, 27), (41, 27), (45, 33), (38, 33)], fill=SLATE_D)
    O.polygon([(34, 27), (42, 27), (39, 22), (37, 22)], fill=SLATE); O.rectangle((37, 19, 38, 21), fill=SLATE_D); O.line((35, 18, 40, 18), fill=SLATE)
    O.rectangle((37, 41, 39, 47), fill=DARK)
    for x, y in ((47, 47), (51, 47), (49, 43)): barrel(O, x, y)
    dome(O, 6, 47, 6, 5, (206, 120, 60)); O.line((9, 41, 9, 38), fill=(206, 120, 60)); O.line((9, 38, 12, 38), fill=(170, 92, 44))
    for x, y in ((38, 15), (39, 12), (41, 10)): G.point((x, y), fill=(240, 240, 240, 200)); G.point((x + 1, y), fill=(240, 240, 240, 150))
    return s

def council_mound():
    s = Sp(); G, O = s.G, s.O
    G.polygon([(9, 52), (17, 40), (47, 40), (55, 52)], fill=(118, 138, 70)); G.polygon([(34, 40), (47, 40), (55, 52), (38, 52)], fill=(96, 116, 60))
    G.polygon([(15, 42), (20, 35), (44, 35), (49, 42)], fill=(140, 156, 82)); G.polygon([(20, 35), (44, 35), (46, 38), (18, 38)], fill=(170, 160, 110))
    for i, y in enumerate(range(41, 53, 2)): G.line((29 - i // 2, y, 35 + i // 2, y), fill=(196, 176, 128)); G.line((29 - i // 2, y + 1, 35 + i // 2, y + 1), fill=(160, 140, 100))
    box(O, 24, 37, 16, 6, (190, 160, 116))
    O.polygon([(21, 31), (42, 31), (33, 18), (30, 18)], fill=THATCH); O.polygon([(32, 18), (33, 18), (42, 31), (32, 31)], fill=THATCH_D)
    O.rectangle((31, 33, 33, 37), fill=DARK); O.line((31, 17, 32, 15), fill=WOOD_D)
    for x in (17, 46): O.line((x, 38, x, 29), fill=WOOD_D); O.rectangle((x - 1, 28, x + 1, 29), fill=(214, 70, 50))
    return s

def preceptory():
    s = Sp(); G, O = s.G, s.O
    G.polygon([(12, 36), (52, 36), (54, 50), (10, 50)], fill=(160, 150, 110))
    fence(O, [(11, 50), (26, 50)], STONE); fence(O, [(38, 50), (53, 50)], STONE); fence(O, [(11, 50), (13, 37)], STONE); fence(O, [(53, 50), (51, 37)], STONE_D)
    house(O, 22, 46, 20, 9, WHITE, RED, rh=6, kind='hip', door=False)
    for x in (25, 30, 35): O.rectangle((x, 40, x, 43), fill=(60, 70, 96))
    box(O, 12, 46, 10, 13, WHITE); O.polygon([(10, 33), (23, 33), (17, 23), (16, 23)], fill=RED); O.polygon([(17, 23), (23, 33), (17, 33)], fill=RED_D)
    O.line((16, 22, 16, 17), fill=(90, 80, 70)); O.line((14, 19, 18, 19), fill=(90, 80, 70))
    O.rectangle((16, 42, 17, 46), fill=DARK); O.rectangle((16, 36, 17, 38), fill=(60, 70, 96))
    O.line((46, 46, 46, 30), fill=(90, 80, 70)); O.rectangle((47, 30, 53, 36), fill=WHITE)
    O.line((50, 31, 50, 35), fill=(200, 30, 30)); O.line((48, 33, 52, 33), fill=(200, 30, 30))
    return s

def kampung():
    s = Sp(); G, O = s.G, s.O
    G.polygon([(10, 44), (54, 44), (52, 53), (12, 53)], fill=(232, 214, 160))
    def stilt_house(x, y, w=11):
        for sx in (x + 1, x + w - 2): O.line((sx, y, sx, y - 4), fill=WOOD_D)
        box(O, x, y - 4, w, 5, (206, 170, 110))
        O.polygon([(x - 3, y - 9), (x + w + 2, y - 9), (x + w - 1, y - 16), (x + w // 2, y - 12), (x, y - 16)], fill=(120, 76, 44))
        O.polygon([(x + w // 2, y - 12), (x + w - 1, y - 16), (x + w + 2, y - 9), (x + w // 2, y - 9)], fill=(88, 54, 32))
        O.rectangle((x + w // 2 - 1, y - 7, x + w // 2, y - 4), fill=DARK); O.line((x + w // 2 - 2, y - 3, x + w // 2 - 3, y), fill=WOOD_L)
    stilt_house(13, 44); stilt_house(29, 40, 12); stilt_house(40, 49, 10)
    palm(O, 26, 50, 10); palm(O, 52, 40, 9)
    O.polygon([(14, 50), (22, 50), (20, 52), (16, 52)], fill=WOOD); O.line((14, 50, 22, 50), fill=WOOD_L)
    return s

def inuksuk():
    s = Sp(); G, O = s.G, s.O
    G.ellipse((16, 44, 50, 52), fill=(222, 230, 240))
    st, sd, sl = (138, 140, 150), (100, 102, 114), (176, 178, 186)
    def slab(x, y, w, h, c=st): O.rectangle((x, y - h + 1, x + w - 1, y), fill=c); O.line((x, y - h + 1, x + w - 2, y - h + 1), fill=sl); O.line((x + w - 1, y - h + 1, x + w - 1, y), fill=sd)
    slab(24, 48, 5, 8); slab(34, 48, 5, 8); slab(22, 40, 19, 4, sd); slab(26, 36, 11, 6); slab(17, 30, 29, 3); slab(27, 27, 9, 4, sd); slab(29, 23, 6, 4)
    slab(45, 49, 5, 3, sd); slab(46, 46, 4, 3); slab(47, 43, 2, 2, sl)
    slab(13, 50, 4, 2); slab(14, 48, 2, 2, sd)
    return s

def alpine_pasture():
    s = Sp(); G, O = s.G, s.O
    G.ellipse((10, 34, 54, 53), fill=(126, 176, 80)); G.ellipse((14, 36, 44, 50), fill=(150, 196, 96))
    for x, y in ((18, 46), (40, 49), (30, 51), (47, 40)): G.point((x, y), fill=(250, 240, 120)); G.point((x + 2, y - 1), fill=(240, 240, 250))
    box(O, 15, 42, 16, 4, WHITE); box(O, 15, 38, 16, 5, (120, 78, 44))
    O.polygon([(11, 34), (34, 34), (24, 25), (21, 25)], fill=(110, 100, 96)); O.polygon([(23, 25), (24, 25), (34, 34), (23, 34)], fill=(82, 74, 72))
    for x in (15, 20, 28): O.point((x, 32), fill=STONE_L)
    O.rectangle((22, 39, 24, 42), fill=DARK); O.rectangle((17, 36, 18, 37), fill=(250, 214, 110)); O.rectangle((27, 36, 28, 37), fill=(250, 214, 110))
    fence(G, [(34, 44), (52, 42)], WOOD); fence(G, [(36, 52), (53, 49)], WOOD); fence(G, [(52, 42), (53, 49)], WOOD)
    cow(O, 38, 47); cow(O, 44, 45, c=(150, 96, 56), patch=WHITE); cow(O, 12, 50)
    dome(O, 33, 40, 5, 4, THATCH)
    return s

def feitoria(port=False):
    s = Sp(); G, O = s.G, s.O
    dx = -5 if port else 0
    G.polygon([(12 + dx, 36), (46 + dx, 36), (50 + dx, 50), (10 + dx, 50)], fill=(196, 176, 128))
    box(O, 16 + dx, 38, 26, 4, WHITE_D)
    house(O, 24 + dx, 43, 14, 6, WHITE, RED, rh=5, kind='hip', door=False)
    box(O, 13 + dx, 49, 32, 7, WHITE)
    for x in range(13 + dx, 45 + dx, 2): O.point((x, 42), fill=WHITE)
    O.rectangle((27 + dx, 45, 30 + dx, 49), fill=DARK); O.rectangle((28 + dx, 44, 29 + dx, 44), fill=DARK)
    tower(O, 11 + dx, 49, 7, 17, WHITE, roof=RED, rh=6)
    flag(O, 14 + dx, 26, 8, (20, 130, 70), (210, 40, 40), w=7)
    tower(O, 41 + dx, 49, 5, 10, WHITE_D, window=False)
    if not port:
        crate(O, 49, 50); barrel(O, 54, 50); crate(O, 50, 45, 2)
    else:
        G.polygon([(40, 42), (56, 38), (60, 52), (42, 54)], fill=(96, 170, 208)); G.line((46, 50, 52, 49), fill=WATER_L)
        O.polygon([(40, 46), (54, 43), (55, 45), (41, 48)], fill=WOOD_L)
        for x, y in ((43, 49), (48, 48), (53, 47)): O.line((x, y, x, y + 2), fill=WOOD_D)
        O.line((43, 46, 43, 33), fill=WOOD_D); O.line((43, 33, 50, 35), fill=WOOD_D); O.line((50, 35, 50, 39), fill=(60, 60, 64)); crate(O, 49, 42, 2)
        boat(O, 45, 53, 11, hull=WOOD_D, sail=WHITE, sh=8)
    return s

def canal():
    s = Sp(); G, O = s.G, s.O
    top = [(4, 34), (16, 32), (30, 35), (46, 33), (60, 36)]; bot = [(4, 41), (16, 39), (30, 42), (46, 40), (60, 43)]
    G.polygon(top + bot[::-1], fill=(84, 160, 206))
    for (x0, y0), (x1, y1) in zip(top, top[1:]): G.line((x0, y0, x1, y1), fill=STONE_L); G.line((x0, y0 + 1, x1, y1 + 1), fill=STONE)
    for (x0, y0), (x1, y1) in zip(bot, bot[1:]): G.line((x0, y0, x1, y1), fill=STONE); G.line((x0, y0 + 1, x1, y1 + 1), fill=STONE_D)
    for x, y in ((9, 37), (22, 37), (38, 38), (52, 38)): G.line((x, y, x + 4, y), fill=WATER_L)
    O.polygon([(26, 31), (36, 31), (38, 44), (24, 44)], fill=STONE_L); O.polygon([(31, 31), (36, 31), (38, 44), (31, 44)], fill=STONE)
    O.pieslice((27, 35, 35, 47), 180, 360, fill=(50, 96, 140)); O.rectangle((27, 41, 35, 43), fill=(50, 96, 140))
    O.line((25, 31, 37, 31), fill=WHITE_D)
    box(O, 44, 31, 6, 4, WOOD_L); gable(O, 44, 27, 6, 3, RED)
    barge = (150, 104, 60)
    O.polygon([(10, 38), (19, 37), (18, 40), (11, 40)], fill=barge); O.rectangle((13, 36, 16, 37), fill=(210, 190, 140))
    return s

SPRITES = collections.OrderedDict([
    ('Arctic Research Station', (arctic_research_station, 'Snow')), ('Rice Paddy', (rice_paddy, 'Marsh')),
    ('Mountain Citadel', (mountain_citadel, 'Grassland')), ('Fortress', (fortress, 'Plains')), ('Hillfort', (hillfort, 'Grassland')),
    ('Dry Dock', (dry_dock, 'Coast')), ('Caravanserai', (caravanserai, 'Desert')), ('Longphort', (longphort, 'Grassland')),
    ('Hidden Cove', (hidden_cove, 'Beach')), ('Onsen', (onsen, 'Grassland')), ('Isibaya', (isibaya, 'Plains')),
    ('Olive Grove', (olive_grove, 'Plains')), ('Distillery', (distillery, 'Grassland')), ('Council Mound', (council_mound, 'Grassland')),
    ('Preceptory', (preceptory, 'Plains')), ('Kampung', (kampung, 'Beach')), ('Inuksuk', (inuksuk, 'Snow')),
    ('Alpine Pasture', (alpine_pasture, 'Grassland')), ('Feitoria', (feitoria, 'Plains')),
    ('Feitoria Port', (lambda: feitoria(True), 'Plains')), ('Canal', (canal, 'Grassland'))])

def halve(im):
    """2:1 reduction that keeps hard pixel edges: each 2x2 block takes its most common opaque colour."""
    w, h = im.size; out = Image.new('RGBA', (w // 2, h // 2), (0, 0, 0, 0)); sp = im.load(); op = out.load()
    for y in range(h // 2):
        for x in range(w // 2):
            px = [sp[2 * x + i, 2 * y + j] for j in (0, 1) for i in (0, 1)]
            solid = [p for p in px if p[3] > 127]
            if len(solid) >= 2:
                cnt = collections.Counter(solid); best = max(cnt.values())
                op[x, y] = max((p for p in cnt if cnt[p] == best), key=lambda p: -sum(p[:3]))
    return out

if __name__ == '__main__':
    out = sys.argv[1]
    for sub in ('HexaRealm', 'FantasyHex'): os.makedirs(os.path.join(out, sub), exist_ok=True)
    for name, (fn, _) in SPRITES.items():
        sp = fn(); sp.finish().save(os.path.join(out, 'HexaRealm', name + '.png'))
        sp.finish(half=True).save(os.path.join(out, 'FantasyHex', name + '.png'))
    print(len(SPRITES), 'sprites')
