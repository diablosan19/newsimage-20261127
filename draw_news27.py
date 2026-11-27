#!/usr/bin/env python3
"""Draw the Friday 27 November 2026 world front page (1024x1024 PNG).

All copy was researched fresh from wire/primary sources on 27 Nov 2026
(see ../research-news27-notes.md). Scenes are drawn with PIL primitives
only: flat shapes, no photographs, no external assets, no network.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

FB = "/usr/share/fonts/truetype/liberation/"
SERIF_B = FB + "LiberationSerif-Bold.ttf"
SANS = FB + "LiberationSans-Regular.ttf"
SANS_B = FB + "LiberationSans-Bold.ttf"
SANS_I = FB + "LiberationSans-Italic.ttf"

PAPER = (246, 241, 229)
INK = (22, 21, 19)
RED = (166, 30, 34)
NAVY = (23, 58, 94)
TEAL = (15, 92, 77)
GOLD = (185, 138, 29)
GREY = (90, 86, 78)
CARD = (255, 255, 255)
LINE = (180, 172, 156)
LIGHT = (238, 232, 216)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, width, max_lines):
    """Word-wrap text to fit width; never splits a word. Raises if it cannot fit."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if not cur:
                raise ValueError("single word too wide: %r" % w)
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        raise ValueError("needs %d lines, max %d: %r" % (len(lines), max_lines, text))
    return lines


def draw_scene(d, box, kind):
    """Flat drawn scene inside box (x0, y0, x1, y1). All coordinates relative."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0

    def X(f):
        return x0 + f * w

    def Y(f):
        return y0 + f * h

    def rect(fx0, fy0, fx1, fy1, fill):
        d.rectangle([X(fx0), Y(fy0), X(fx1), Y(fy1)], fill=fill)

    def ell(fx0, fy0, fx1, fy1, fill):
        d.ellipse([X(fx0), Y(fy0), X(fx1), Y(fy1)], fill=fill)

    def poly(pts, fill):
        d.polygon([(X(a), Y(b)) for a, b in pts], fill=fill)

    def line(pts, fill, width=2):
        d.line([(X(a), Y(b)) for a, b in pts], fill=fill, width=width)

    if kind == "drone":
        rect(0, 0, 1, 0.62, (43, 63, 92))
        ell(0.62, 0.08, 0.88, 0.34, (232, 214, 160))
        rect(0, 0.62, 1, 1, (58, 52, 44))
        rect(0.08, 0.72, 0.22, 1, (90, 82, 66))
        rect(0.30, 0.66, 0.44, 1, (90, 82, 66))
        poly([(0.42, 0.30), (0.58, 0.42), (0.42, 0.54)], (40, 40, 40))
        line([(0.42, 0.42), (0.30, 0.42)], (40, 40, 40), 3)
        line([(0.30, 0.36), (0.30, 0.48)], (40, 40, 40), 3)
        line([(0.54, 0.42), (0.66, 0.42)], (40, 40, 40), 3)
        poly([(0.60, 0.55), (0.72, 0.72), (0.52, 0.72)], (166, 30, 34))
        ell(0.58, 0.68, 0.74, 0.84, (232, 120, 40))
    elif kind == "gaza":
        rect(0, 0, 1, 0.55, (214, 178, 132))
        rect(0, 0.55, 1, 1, (74, 66, 58))
        rect(0.06, 0.30, 0.26, 0.72, (120, 108, 92))
        rect(0.32, 0.22, 0.52, 0.72, (140, 126, 106))
        rect(0.58, 0.34, 0.78, 0.72, (120, 108, 92))
        rect(0.84, 0.44, 0.96, 0.72, (140, 126, 106))
        for bx in (0.10, 0.36, 0.62, 0.87):
            rect(bx, 0.40, bx + 0.05, 0.48, (40, 36, 30))
            rect(bx, 0.56, bx + 0.05, 0.64, (40, 36, 30))
        poly([(0.38, 0.22), (0.46, 0.02), (0.54, 0.22)], (150, 150, 148))
        ell(0.40, 0.00, 0.56, 0.16, (170, 170, 168))
        poly([(0.66, 0.30), (0.74, 0.10), (0.82, 0.30)], (232, 120, 40))
        ell(0.68, 0.26, 0.80, 0.38, (232, 120, 40))
    elif kind == "storm":
        rect(0, 0, 1, 0.58, (52, 68, 88))
        rect(0, 0.58, 1, 1, (38, 44, 56))
        ell(0.06, 0.10, 0.34, 0.38, (226, 226, 222))
        ell(0.24, 0.04, 0.52, 0.32, (226, 226, 222))
        ell(0.44, 0.12, 0.68, 0.38, (210, 210, 206))
        for i in range(6):
            fx = 0.10 + i * 0.15
            line([(fx, 0.44), (fx - 0.05, 0.62)], (140, 180, 220), 3)
        poly([(0.62, 0.44), (0.94, 0.44), (0.90, 0.54), (0.66, 0.54)], (240, 240, 238))
        rect(0.70, 0.52, 0.74, 0.60, (240, 240, 238))
        poly([(0.60, 0.62), (0.78, 0.62), (0.72, 0.72), (0.66, 0.72)], (166, 30, 34))
        line([(0.60, 0.62), (0.96, 0.62)], (200, 200, 196), 2)
    elif kind == "tanker":
        rect(0, 0, 1, 0.60, (120, 160, 190))
        rect(0, 0.60, 1, 1, (24, 68, 110))
        poly([(0.10, 0.55), (0.88, 0.55), (0.80, 0.72), (0.18, 0.72)], (90, 30, 26))
        rect(0.14, 0.38, 0.84, 0.55, (140, 44, 36))
        rect(0.62, 0.22, 0.78, 0.38, (230, 230, 226))
        line([(0.70, 0.08), (0.70, 0.22)], (230, 230, 226), 3)
        poly([(0.70, 0.08), (0.82, 0.13), (0.70, 0.18)], (166, 30, 34))
        line([(0.06, 0.80), (0.94, 0.80)], (200, 220, 235), 3)
        line([(0.14, 0.90), (0.86, 0.90)], (200, 220, 235), 3)
        poly([(0.40, 0.28), (0.48, 0.44), (0.34, 0.44)], (232, 120, 40))
    elif kind == "migration":
        rect(0, 0, 1, 1, (232, 226, 208))
        line([(0.08, 0.70), (0.88, 0.70)], (60, 60, 58), 3)
        for fx, fy, col in [(0.16, 0.62, NAVY), (0.34, 0.62, RED), (0.52, 0.62, TEAL),
                            (0.70, 0.62, GOLD), (0.84, 0.62, (90, 60, 110))]:
            ell(fx - 0.045, fy - 0.10, fx + 0.045, fy - 0.01, col)
            poly([(fx - 0.05, fy), (fx + 0.05, fy), (fx + 0.03, fy + 0.16),
                  (fx - 0.03, fy + 0.16)], col)
        poly([(0.12, 0.30), (0.80, 0.30), (0.80, 0.22), (0.94, 0.34),
              (0.80, 0.46), (0.80, 0.38), (0.12, 0.38)], (166, 30, 34))
    elif kind == "ballot":
        rect(0, 0, 1, 1, (222, 228, 222))
        rect(0.30, 0.42, 0.70, 0.88, (250, 250, 248))
        d.rectangle([X(0.30), Y(0.42), X(0.70), Y(0.88)], outline=(40, 40, 40), width=3)
        rect(0.26, 0.34, 0.74, 0.44, (23, 58, 94))
        poly([(0.38, 0.66), (0.48, 0.78), (0.64, 0.52)], (15, 92, 77))
        line([(0.38, 0.66), (0.48, 0.78), (0.64, 0.52)], (15, 92, 77), 5)
        rect(0.10, 0.12, 0.24, 0.26, (166, 30, 34))
        rect(0.76, 0.12, 0.90, 0.26, (185, 138, 29))
    elif kind == "football":
        rect(0, 0, 1, 0.55, (36, 84, 52))
        rect(0, 0.55, 1, 1, (86, 122, 62))
        line([(0.08, 0.55), (0.92, 0.55)], (255, 255, 255), 2)
        line([(0.10, 0.12), (0.10, 0.42)], (232, 200, 60), 4)
        line([(0.90, 0.12), (0.90, 0.42)], (232, 200, 60), 4)
        line([(0.10, 0.12), (0.90, 0.12)], (232, 200, 60), 4)
        ell(0.40, 0.60, 0.60, 0.92, (122, 72, 40))
        d.ellipse([X(0.40), Y(0.60), X(0.60), Y(0.92)], outline=(255, 255, 255), width=2)
        line([(0.42, 0.76), (0.58, 0.76)], (255, 255, 255), 2)
        line([(0.50, 0.62), (0.50, 0.90)], (255, 255, 255), 2)
    elif kind == "helmet":
        rect(0, 0, 1, 1, (238, 238, 240))
        poly([(0.18, 0.72), (0.18, 0.40), (0.38, 0.16), (0.66, 0.16), (0.82, 0.40),
              (0.82, 0.60), (0.68, 0.60), (0.68, 0.72)], (20, 20, 24))
        rect(0.18, 0.56, 0.82, 0.64, (200, 170, 30))
        rect(0.30, 0.30, 0.58, 0.44, (240, 240, 238))
        d.rectangle([X(0.30), Y(0.30), X(0.58), Y(0.44)], outline=(200, 170, 30), width=3)
        poly([(0.68, 0.60), (0.86, 0.60), (0.86, 0.66), (0.68, 0.66)], (200, 170, 30))
        line([(0.24, 0.78), (0.76, 0.78)], (90, 90, 90), 3)
    elif kind == "refinery":
        rect(0, 0, 1, 0.55, (200, 170, 120))
        rect(0, 0.55, 1, 1, (70, 64, 58))
        rect(0.10, 0.34, 0.26, 0.80, (110, 104, 96))
        rect(0.32, 0.44, 0.48, 0.80, (110, 104, 96))
        poly([(0.58, 0.80), (0.66, 0.20), (0.74, 0.80)], (130, 122, 112))
        ell(0.62, 0.30, 0.78, 0.50, (240, 240, 236))
        poly([(0.66, 0.06), (0.74, 0.22), (0.70, 0.22), (0.76, 0.34), (0.66, 0.34),
              (0.68, 0.24), (0.62, 0.24)], (232, 120, 40))
        line([(0.14, 0.50), (0.22, 0.50)], (232, 120, 40), 3)
        line([(0.36, 0.58), (0.44, 0.58)], (232, 120, 40), 3)
    elif kind == "truck":
        rect(0, 0, 1, 0.55, (220, 200, 170))
        rect(0, 0.55, 1, 1, (60, 56, 52))
        poly([(0.10, 0.68), (0.52, 0.68), (0.52, 0.40), (0.10, 0.40)], (200, 90, 40))
        poly([(0.54, 0.68), (0.74, 0.68), (0.74, 0.48), (0.64, 0.48)], (40, 90, 140))
        rect(0.58, 0.52, 0.70, 0.62, (200, 220, 235))
        ell(0.20, 0.66, 0.32, 0.82, (20, 20, 20))
        ell(0.60, 0.66, 0.72, 0.82, (20, 20, 20))
        poly([(0.78, 0.30), (0.86, 0.44), (0.82, 0.44), (0.88, 0.54), (0.78, 0.54),
              (0.80, 0.44), (0.74, 0.44)], (232, 120, 40))
    elif kind == "chart":
        rect(0, 0, 1, 1, (228, 236, 228))
        line([(0.10, 0.88), (0.92, 0.88)], (60, 60, 58), 3)
        line([(0.10, 0.88), (0.10, 0.10)], (60, 60, 58), 3)
        for i, fh in enumerate((0.30, 0.44, 0.36, 0.58, 0.72)):
            fx = 0.18 + i * 0.15
            rect(fx, 0.88 - fh, fx + 0.09, 0.88, TEAL if i < 4 else RED)
        poly([(0.16, 0.62), (0.30, 0.46), (0.44, 0.52), (0.60, 0.34), (0.86, 0.16)],
             (166, 30, 34))
        line([(0.16, 0.62), (0.30, 0.46), (0.44, 0.52), (0.60, 0.34), (0.86, 0.16)],
             (166, 30, 34), 3)
    elif kind == "market":
        rect(0, 0, 1, 1, (226, 232, 240))
        line([(0.08, 0.50), (0.92, 0.50)], (120, 120, 116), 2)
        for i, (fy0, fy1, col) in enumerate(((0.30, 0.44, TEAL), (0.36, 0.56, RED),
                                             (0.28, 0.40, TEAL), (0.44, 0.62, RED),
                                             (0.34, 0.46, TEAL))):
            fx = 0.16 + i * 0.16
            line([(fx + 0.04, fy0 - 0.08), (fx + 0.04, fy1 + 0.08)], col, 2)
            rect(fx, fy0, fx + 0.08, fy1, col)
        poly([(0.84, 0.30), (0.90, 0.40), (0.78, 0.40)], TEAL)
    elif kind == "chess":
        for r in range(4):
            for c in range(4):
                rect(c * 0.25, r * 0.25, (c + 1) * 0.25, (r + 1) * 0.25,
                     (240, 235, 220) if (r + c) % 2 == 0 else (60, 50, 40))
        ell(0.10, 0.08, 0.22, 0.22, (250, 250, 248))
        rect(0.13, 0.20, 0.19, 0.30, (250, 250, 248))
        ell(0.58, 0.58, 0.74, 0.76, (20, 20, 22))
        rect(0.62, 0.74, 0.70, 0.86, (20, 20, 22))
        ell(0.30, 0.60, 0.40, 0.72, (250, 250, 248))
        line([(0.76, 0.10), (0.90, 0.24)], (166, 30, 34), 4)
        line([(0.90, 0.10), (0.76, 0.24)], (166, 30, 34), 4)


LEADS = [
    dict(n=1, kind="drone", region="KUWAIT", field="MIDDLE EAST", label="REPORTED",
         src="REUTERS / BBC", time="06:03 UTC",
         head="Two Italians killed in Kuwait drone strike",
         deck="Italy and Kuwait blame Iran; Tehran denies it. Two technicians dead at an air-defence post."),
    dict(n=2, kind="gaza", region="GAZA", field="MIDDLE EAST", label="REPORTED",
         src="REUTERS / BBC", time="07:26 UTC",
         head="Hamas weighs reply as Gaza strikes kill 10",
         deck="A deputy education minister is among the dead in Deir al-Balah; Hamas weighs its response."),
    dict(n=3, kind="storm", region="USA", field="NORTH AMERICA", label="CONFIRMED",
         src="BBC / AP", time="01:15 UTC",
         head="Thanksgiving storms cut power to 800,000",
         deck="Floods and torn roofs; more than 1,000 flights cancelled or delayed."),
]

PANELS = [
    dict(n=4, kind="tanker", region="SPAIN", label="CONFIRMED", src="REUTERS",
         head="Tanker capsizes off Ibiza; one dead"),
    dict(n=5, kind="migration", region="UK", label="OFFICIAL", src="NYT",
         head="UK migration lowest since 1997"),
    dict(n=6, kind="ballot", region="NEW ZEALAND", label="OFFICIAL", src="REUTERS",
         head="Final NZ vote count confirms parliament"),
    dict(n=7, kind="football", region="USA", label="CONFIRMED", src="AP",
         head="Bears stun Lions 39-35 in last seconds"),
    dict(n=8, kind="helmet", region="USA", label="CONFIRMED", src="AP",
         head="Steelers cut Aaron Rodgers"),
    dict(n=9, kind="refinery", region="THAILAND", label="CONFIRMED", src="AP",
         head="Bangkok refinery blast injures nine"),
    dict(n=10, kind="truck", region="EGYPT", label="CONFIRMED", src="BBC",
         head="Driver held over Cairo crash that killed 31"),
    dict(n=11, kind="chart", region="AUSTRALIA", label="OFFICIAL", src="ABS",
         head="Australia spending jumps 12.2% on data centres"),
    dict(n=12, kind="market", region="ASIA", label="REPORTED", src="REUTERS",
         head="Asia stocks extend rebound; BoK call due"),
    dict(n=13, kind="chess", region="CHESS", label="CONFIRMED", src="INDIA TODAY",
         head="Gukesh, Sindarov draw marathon Game 3"),
]

LIST = [
    (14, "Musk: every US child gets two SpaceX shares", "REUTERS"),
    (15, "Trump demands probe of 'fake' GDP figures", "AP"),
    (16, "Depardieu to stand trial over alleged 2018 rape", "REUTERS"),
    (17, "UK train knifeman guilty of trying to murder 14", "BBC"),
    (18, "German boat dealer 'supplied Channel smuggling gangs'", "BBC"),
    (19, "UK-EU treaties published; 10-year exit clause", "BBC"),
    (20, "Kyiv hit by Russian ballistic missiles; mall struck", "REUTERS"),
    (21, "Davis Cup: Spain beat Austria 2-0 in Bologna", "REUTERS"),
    (22, "Eldridge in $10bn deal for Lukoil foreign assets", "REUTERS"),
    (23, "Senate Democrats probe Vance over Vitol oil licence", "REUTERS"),
    (24, "MLB sues players' union ahead of lockout", "AP"),
    (25, "Army: Iowa explosives blast 'a success'", "AP"),
    (26, "Judge blocks FCC early review of ABC licence", "AP"),
    (27, "Black Friday: essentials join gifts in carts", "AP"),
    (28, "Ebola in Congo passes 12,000 cases", "AP"),
    (29, "Cheaper HIV jab reaches Africa; Zambia first", "BBC"),
    (30, "Myanmar will not fully comply with ICJ orders", "REUTERS"),
    (31, "Strobe Talbott, ex-deputy secretary of state, dies at 80", "AP"),
    (32, "FedEx plane overruns Miami runway", "AP"),
    (33, "Kenya cult leader convicted of new charges", "REUTERS"),
    (34, "Iranian activist Mahmoudian arrested in Tehran", "AP"),
    (35, "India top court: judicial member must sit on PMLA bench", "TOI"),
    (36, "Embraer warns US jet tariff will lift fares", "REUTERS"),
]

TIMELINE = [
    ("19:37", "BEARS WIN"), ("22:16", "GUKESH DRAW"), ("00:45", "ASIA OPEN"),
    ("03:31", "IBIZA"), ("04:04", "NZ COUNT"), ("05:22", "UK MIGRATION"),
    ("06:03", "KUWAIT"), ("07:26", "GAZA"),
]

# World pin map: rough equirectangular continent outlines (lon, lat) and
# pin positions for stories 1-13, with per-pin label offsets (dx, dy in px).
CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 80),
     (-80, 73), (-75, 72), (-65, 60), (-55, 52), (-60, 46), (-70, 42),
     (-75, 35), (-80, 32), (-81, 25), (-84, 30), (-90, 29), (-97, 26),
     (-105, 22), (-110, 24), (-115, 30), (-125, 40), (-125, 48), (-135, 58),
     (-155, 58), (-165, 60)],
    [(-58, 64), (-45, 60), (-30, 68), (-22, 70), (-35, 76), (-55, 76)],
    [(-78, 8), (-72, 12), (-62, 10), (-52, 5), (-50, 0), (-44, -3), (-35, -8),
     (-40, -20), (-48, -28), (-58, -38), (-68, -52), (-72, -54), (-73, -40),
     (-72, -20), (-78, -5)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53), (8, 57), (10, 59),
     (18, 56), (21, 55), (24, 58), (28, 60), (30, 62), (32, 68), (40, 68),
     (45, 66), (40, 60), (35, 55), (30, 50), (28, 45), (23, 40), (19, 42),
     (12, 44), (8, 44), (3, 42), (-2, 37), (-6, 36)],
    [(-17, 15), (-16, 20), (-10, 30), (0, 35), (10, 37), (20, 32), (32, 31),
     (35, 28), (37, 22), (43, 12), (51, 11), (48, 2), (40, -10), (35, -18),
     (32, -28), (26, -34), (18, -35), (14, -22), (12, -6), (9, 4), (-8, 5),
     (-13, 8)],
    [(32, 68), (45, 68), (55, 70), (70, 72), (90, 75), (110, 76), (130, 72),
     (150, 70), (170, 66), (178, 65), (162, 60), (158, 52), (142, 50),
     (140, 40), (132, 35), (127, 35), (122, 30), (120, 22), (110, 20),
     (105, 10), (100, 8), (97, 16), (92, 21), (88, 22), (80, 15), (76, 8),
     (72, 20), (66, 25), (60, 25), (55, 26), (52, 28), (48, 30), (44, 29),
     (40, 32), (36, 36), (32, 42), (30, 46), (28, 50), (30, 55), (32, 62)],
    [(95, 5), (100, 0), (105, -5), (110, -7), (115, -8), (120, -10),
     (125, -8), (130, -2), (135, 0), (140, -4), (138, -8)],
    [(113, -22), (114, -30), (115, -35), (120, -34), (124, -33), (129, -32),
     (132, -32), (135, -35), (138, -35), (140, -38), (145, -38), (150, -37),
     (153, -32), (153, -27), (150, -22), (146, -19), (142, -15), (142, -11),
     (137, -12), (135, -15), (132, -12), (130, -13), (126, -14), (122, -17),
     (118, -20), (113, -22)],
    [(167, -45), (170, -42), (174, -39), (176, -38), (174, -42), (170, -46)],
]
# (story, lon, lat, label dx, label dy)
PINS = [
    (1, 47, 29, 8, -8), (2, 34, 31, -16, -8), (3, -95, 38, 0, -10),
    (4, 2, 39, -4, -11), (5, -1, 52, 9, -4), (6, 172, -41, -14, 0),
    (7, -87, 42, 0, 9), (8, -80, 40, 10, 8), (9, 100, 14, 8, -4),
    (10, 31, 30, 10, 9), (11, 149, -35, -4, 9), (12, 139, 36, 8, -8),
    (13, 78, 18, -4, 10),
]


def draw_pinmap(d, box):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    d.rectangle([x0, y0, x1, y1], fill=(214, 228, 238))
    for poly in CONTINENTS:
        pts = [(x0 + (lon + 170) / 360.0 * w, y0 + (75 - lat) / 130.0 * h)
               for lon, lat in poly]
        d.polygon(pts, fill=(168, 186, 158))
    f_pin = font(SANS_B, 8)
    for n, lon, lat, dx, dy in PINS:
        px = x0 + (lon + 170) / 360.0 * w
        py = y0 + (75 - lat) / 130.0 * h
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED,
                  outline=(255, 255, 255), width=1)
        tx, ty = px + dx, py + dy
        tw = d.textlength(str(n), font=f_pin) + 4
        d.rectangle([tx - tw / 2, ty - 5, tx + tw / 2, ty + 5], fill=RED)
        d.text((tx, ty - 5), str(n), font=f_pin, fill=(255, 255, 255),
               anchor="ma")

DATECHECK = [
    ("COP31 talks collapse, Antalya", "Sun 22 Nov"),
    ("Macy's Thanksgiving parade postponed", "25 Nov"),
    ("US tariff package unveiled (Greer)", "25 Nov"),
    ("Huawei guilty of stealing trade secrets", "25 Nov"),
    ("Duran Duran guitarist Andy Taylor dies, 65", "25 Nov"),
    ("Guinea orders Conakry clean-up", "25 Nov"),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    f_name = font(SERIF_B, 40)
    f_date = font(SANS_B, 17)
    f_sub = font(SANS, 13)
    d.text((W // 2, 8), "THE WORLD FRONT PAGE", font=f_name, fill=INK, anchor="ma")
    d.text((W // 2, 52), "FRIDAY 27 NOVEMBER 2026", font=f_date, fill=RED, anchor="ma")
    d.text((W // 2, 72), "36 STORIES  •  10 REGIONS  •  15 FIELDS  •  ALL FIRST REPORTED OVERNIGHT",
           font=f_sub, fill=INK, anchor="ma")
    d.rectangle([8, 90, W - 8, 94], fill=INK)

    # ---- 3 leads ----
    col_w, gap = 328, 8
    y0 = 100
    scene_h = 92
    for i, L in enumerate(LEADS):
        x = 8 + i * (col_w + gap)
        d.rectangle([x, y0, x + col_w, y0 + 212], fill=CARD, outline=LINE, width=1)
        d.rectangle([x, y0, x + col_w, y0 + 22], fill=NAVY)
        d.text((x + 8, y0 + 3), "%d  %s" % (L["n"], L["region"]), font=font(SANS_B, 13),
               fill=(255, 255, 255))
        d.text((x + col_w - 8, y0 + 4), L["label"], font=font(SANS_B, 11),
               fill=(255, 210, 90), anchor="ra")
        draw_scene(d, (x + 1, y0 + 23, x + col_w - 1, y0 + 23 + scene_h), L["kind"])
        d.text((x + 1, y0 + 23 + scene_h), " ", font=font(SANS, 1))
        hy = y0 + 23 + scene_h + 6
        lines = wrap(d, L["head"], font(SANS_B, 18), col_w - 16, 3)
        for ln in lines:
            d.text((x + 8, hy), ln, font=font(SANS_B, 18), fill=INK)
            hy += 22
        deck_lines = wrap(d, L["deck"], font(SANS, 11), col_w - 16, 2)
        for ln in deck_lines:
            d.text((x + 8, hy), ln, font=font(SANS, 11), fill=(52, 50, 46))
            hy += 14
        d.text((x + 8, y0 + 212 - 15), "%s  •  %s" % (L["src"], L["time"]),
               font=font(SANS_B, 10), fill=GREY)

    # ---- Section bar: panels 4-13 ----
    d.rectangle([8, 322, W - 8, 342], fill=NAVY)
    d.text((16, 326), "THE DAY IN PICTURES  —  STORIES 4–13", font=font(SANS_B, 13),
           fill=(255, 255, 255))

    # ---- Panels 4-13: 2 rows x 5 ----
    pw, ph, pgap = 198, 100, 7
    for idx, P in enumerate(PANELS):
        r, c = divmod(idx, 5)
        x = 8 + c * (pw + pgap)
        y = 348 + r * (ph + 6)
        d.rectangle([x, y, x + pw, y + ph], fill=CARD, outline=LINE, width=1)
        d.rectangle([x, y, x + 24, y + 18], fill=RED)
        d.text((x + 12, y + 2), str(P["n"]), font=font(SANS_B, 12),
               fill=(255, 255, 255), anchor="ma")
        d.text((x + 30, y + 3), P["region"], font=font(SANS_B, 10), fill=NAVY)
        draw_scene(d, (x + 6, y + 22, x + 64, y + 80), P["kind"])
        d.rectangle([x + 6, y + 22, x + 64, y + 80], outline=LINE, width=1)
        tx = x + 70
        lines = wrap(d, P["head"], font(SANS_B, 11), pw - 76, 4)
        ty = y + 22
        for ln in lines:
            d.text((tx, ty), ln, font=font(SANS_B, 11), fill=INK)
            ty += 13
        d.text((tx, y + ph - 15), "%s · %s" % (P["label"], P["src"]),
               font=font(SANS_B, 9), fill=GREY)

    # ---- Timeline strip ----
    ty0 = 556
    d.rectangle([8, ty0, W - 8, ty0 + 32], fill=LIGHT, outline=LINE, width=1)
    d.text((16, ty0 + 10), "FIRST WIRE — UTC", font=font(SANS_B, 11), fill=NAVY)
    x_start, x_end = 160, W - 16
    step = (x_end - x_start) / (len(TIMELINE) - 1)
    d.line([(x_start, ty0 + 17), (x_end, ty0 + 17)], fill=(200, 192, 172), width=2)
    for i, (t, lab) in enumerate(TIMELINE):
        cx = x_start + i * step
        d.line([(cx, ty0 + 12), (cx, ty0 + 22)], fill=RED, width=2)
        d.text((cx, ty0 + 2), t, font=font(SANS_B, 9), fill=INK, anchor="ma")
        d.text((cx, ty0 + 22), lab, font=font(SANS, 8), fill=GREY, anchor="ma")

    # ---- Section bar: list 14-36 + region bar ----
    d.rectangle([8, 594, W - 8, 614], fill=NAVY)
    d.text((16, 598), "THE REST OF THE DAY  —  STORIES 14–36", font=font(SANS_B, 13),
           fill=(255, 255, 255))
    d.text((W - 16, 599), "36 STORIES, 10 REGIONS", font=font(SANS_B, 11),
           fill=(255, 210, 90), anchor="ra")
    d.text((8, 618), "MID EAST 3  •  W EUROPE 7  •  E EUROPE 2  •  N AMERICA 12  •  S AMERICA 1  •  "
           "AFRICA 4  •  S ASIA 2  •  E ASIA 1  •  SE ASIA 2  •  OCEANIA 2",
           font=font(SANS_B, 10), fill=NAVY)

    # ---- Numbered list 14-36 ----
    f_num = font(SANS_B, 12)
    f_head = font(SANS_B, 12)
    f_src = font(SANS, 11)
    row_h = 23
    col_x = [8, 516]
    col_w = 500
    left = LIST[:12]
    right = LIST[12:]
    for ci, items in enumerate((left, right)):
        x = col_x[ci]
        for ri, (n, head, src) in enumerate(items):
            y = 636 + ri * row_h
            d.text((x, y), "%d." % n, font=f_num, fill=RED)
            num_w = d.textlength("%d. " % n, font=f_num)
            full = head + "  —  " + src
            if d.textlength(full, font=f_head) > col_w - num_w - 4:
                raise ValueError("list line too wide: %r" % full)
            d.text((x + num_w, y), head, font=f_head, fill=INK)
            hw = d.textlength(head, font=f_head)
            d.text((x + num_w + hw, y), "  —  " + src, font=f_src, fill=GREY)

    # ---- Bottom band: DATE CHECK | pin map | markets ----
    by0 = 918
    # DATE CHECK box
    d.rectangle([8, by0, 430, 1016], outline=RED, width=2)
    d.rectangle([8, by0, 430, by0 + 20], fill=RED)
    d.text((16, by0 + 3), "DATE CHECK  —  NOT TODAY'S NEWS", font=font(SANS_B, 12),
           fill=(255, 255, 255))
    dy = by0 + 23
    for name, day in DATECHECK:
        d.text((16, dy), "%s  —  first reported %s  —  EXCLUDED" % (name, day),
               font=font(SANS, 10), fill=INK)
        dy += 11.5
    # Pin map
    d.rectangle([438, by0, 690, 1016], fill=CARD, outline=LINE, width=1)
    d.text((446, by0 + 4), "WORLD PIN MAP — STORIES 1–13", font=font(SANS_B, 10),
           fill=NAVY)
    draw_pinmap(d, (442, by0 + 20, 686, 1012))
    # Markets + sources
    mx = 698
    d.rectangle([mx, by0, W - 8, 1016], fill=CARD, outline=LINE, width=1)
    d.text((mx + 10, by0 + 6), "MARKETS — ASIA EARLY, FRI 27 NOV",
           font=font(SANS_B, 11), fill=NAVY)
    d.text((mx + 10, by0 + 24), "NIKKEI +1.2%  KOSPI +0.9%  HANG SENG +1.9%",
           font=font(SANS_B, 11), fill=INK)
    d.text((mx + 10, by0 + 42), "ASX +0.2%  USD/JPY 159.1  US SHUT THU",
           font=font(SANS_B, 11), fill=INK)
    d.text((mx + 10, by0 + 62),
           "SOURCES: REUTERS · AP · BBC · NYT · AFP · INDIA TODAY ·",
           font=font(SANS, 9), fill=GREY)
    d.text((mx + 10, by0 + 74),
           "TOI · THE HINDU · ABS · ONS · GLOBAL FUND · SALESFORCE",
           font=font(SANS, 9), fill=GREY)
    d.text((mx + 10, by0 + 88), "Drawn scenes only — no photographs.",
           font=font(SANS_I, 9), fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    print("saved", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
