#!/usr/bin/env python3
"""Render the 19 November 2026 world-news poster (1024x1024 PNG).

Draws at 2048x2048 and downscales with LANCZOS. All facts are the
verified stories of Thursday 19 November 2026, as reported that day.
No network, no copied artwork: every illustration is drawn here.
All coordinates and leading values are in 2048-pixel canvas units.
"""
import os
import random
from PIL import Image, ImageDraw, ImageFont

W = H = 2048
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "assets", "entry.png")

PAPER = (247, 242, 231)
INK = (20, 24, 31)
NAVY = (18, 38, 63)
NAVY2 = (28, 56, 88)
RED = (178, 38, 30)
GOLD = (201, 162, 39)
TEAL = (15, 107, 92)
CREAM = (250, 246, 236)
GREY = (90, 92, 96)
LINE = (200, 190, 168)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    # size is given in final 1024-pixel units; double for the 2048 canvas
    return ImageFont.truetype(path, int(size * 2))


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, color, max_w, leading):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def centre(draw, cx, y, text, fnt, color):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text,
              font=fnt, fill=color)


def flag_us(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(178, 38, 30), outline=(255, 255, 255), width=3)
    for i in range(1, 7, 2):
        d.rectangle([x, y + h * i / 13, x + w, y + h * (i + 1) / 13], fill=(255, 255, 255))
    d.rectangle([x, y, x + w * 0.42, y + h * 7 / 13], fill=(28, 56, 88))
    for r in range(3):
        for c in range(4):
            px = x + w * (0.05 + c * 0.09)
            py = y + h * (0.08 + r * 0.16)
            d.ellipse([px, py, px + 8, py + 8], fill=(255, 255, 255))


def flag_cn(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16), outline=(255, 255, 255), width=3)
    cx, cy = x + w * 0.18, y + h * 0.25
    d.regular_polygon((cx, cy, 13), 5, fill=(255, 222, 0))
    for fx, fy in [(0.42, 0.12), (0.52, 0.28), (0.52, 0.48), (0.42, 0.62)]:
        d.regular_polygon((x + w * fx, y + h * fy, 8), 5, fill=(255, 222, 0))


def flag_ru(d, x, y, w, h):
    for i, c in enumerate([(255, 255, 255), (0, 57, 166), (213, 0, 50)]):
        d.rectangle([x, y + h * i / 3, x + w, y + h * (i + 1) / 3], fill=c,
                    outline=(255, 255, 255), width=2)


def skyline(d, x0, y_base, w):
    """Low, windowless silhouette along the bottom of the hero panel."""
    rnd = random.Random(19)
    x = x0
    while x < x0 + w:
        bw = rnd.randint(70, 170)
        bh = rnd.randint(50, 130)
        d.rectangle([x, y_base - bh, x + bw, y_base], fill=(10, 22, 38))
        x += bw + 14


def icon_rocket(d, cx, cy, r):
    d.polygon([(cx, cy - r), (cx + r * 0.55, cy + r * 0.2), (cx, cy + r * 0.55),
               (cx - r * 0.55, cy + r * 0.2)], fill=RED)
    d.polygon([(cx - r * 0.25, cy + r * 0.55), (cx, cy + r * 1.05), (cx + r * 0.25, cy + r * 0.55)],
              fill=(255, 170, 40))
    d.ellipse([cx - r * 0.22, cy - r * 0.35, cx + r * 0.22, cy + r * 0.09], fill=CREAM)


def icon_tank(d, cx, cy, r):
    d.rectangle([cx - r, cy - r * 0.25, cx + r * 0.7, cy + r * 0.25], fill=NAVY2)
    d.rectangle([cx + r * 0.5, cy - r * 0.4, cx + r * 1.15, cy - r * 0.18], fill=NAVY2)
    d.rectangle([cx - r * 0.9, cy + r * 0.25, cx + r * 0.9, cy + r * 0.55], fill=INK)
    for i in range(5):
        d.ellipse([cx - r * 0.8 + i * r * 0.36, cy + r * 0.3,
                   cx - r * 0.5 + i * r * 0.36, cy + r * 0.6], fill=CREAM)


def icon_building(d, cx, cy, r):
    d.polygon([(cx - r, cy - r * 0.1), (cx, cy - r), (cx + r, cy - r * 0.1)], fill=TEAL)
    d.rectangle([cx - r * 0.85, cy - r * 0.1, cx + r * 0.85, cy + r * 0.8], fill=TEAL)
    for i in range(4):
        d.rectangle([cx - r * 0.65 + i * r * 0.36, cy + r * 0.1,
                     cx - r * 0.38 + i * r * 0.36, cy + r * 0.55], fill=CREAM)


def icon_flame(d, cx, cy, r):
    d.polygon([(cx, cy - r), (cx + r * 0.7, cy - r * 0.1), (cx + r * 0.45, cy + r * 0.6),
               (cx + r * 0.1, cy + r * 0.85), (cx - r * 0.5, cy + r * 0.6),
               (cx - r * 0.65, cy - r * 0.15)], fill=(230, 110, 20))
    d.polygon([(cx, cy - r * 0.35), (cx + r * 0.35, cy + r * 0.15), (cx, cy + r * 0.6),
               (cx - r * 0.35, cy + r * 0.15)], fill=(255, 200, 60))


def icon_globe(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(58, 130, 170), outline=NAVY, width=4)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], outline=CREAM, width=3)
    d.line([cx - r, cy, cx + r, cy], fill=CREAM, width=3)


def icon_factory(d, cx, cy, r):
    d.rectangle([cx - r, cy - r * 0.1, cx + r, cy + r * 0.7], fill=(110, 110, 118))
    d.polygon([(cx - r, cy - r * 0.1), (cx - r * 0.5, cy - r * 0.6), (cx, cy - r * 0.1),
               (cx + r * 0.5, cy - r * 0.6), (cx + r, cy - r * 0.1)], fill=(80, 80, 88))
    d.rectangle([cx + r * 0.55, cy - r, cx + r * 0.8, cy + r * 0.7], fill=(90, 90, 98))


def story_card(d, x, y, w, h, kicker, headline, body, icon):
    d.rectangle([x, y, x + w, y + h], fill=CREAM, outline=LINE, width=2)
    d.rectangle([x, y, x + w, y + 8], fill=RED)
    pad = 26
    tx = x + pad
    ty = y + 20
    d.text((tx, ty), kicker, font=font(SANS_B, 14), fill=RED)
    ty += 42
    ty = para(d, tx, ty, headline, font(SERIF, 21), INK, w - 2 * pad - 100, 50)
    para(d, tx, ty + 8, body, font(SANS, 15), (52, 56, 64), w - 2 * pad, 38)
    icon(d, x + w - 72, y + 58, 32)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 64

    # ---- masthead ----
    centre(d, W // 2, 24, "THE WORLD IN ONE IMAGE", font(SERIF, 58), INK)
    d.line([M, 146, W - M, 146], fill=INK, width=4)
    d.line([M, 156, W - M, 156], fill=INK, width=2)
    centre(d, W // 2, 170, "THURSDAY, 19 NOVEMBER 2026  •  THE DAY'S WORLD NEWS",
           font(SANS_B, 20), RED)

    # ---- hero: Shenzhen trilateral ----
    hx, hy, hw, hh = M, 226, W - 2 * M, 500
    d.rectangle([hx, hy, hx + hw, hy + hh], fill=NAVY)
    d.rectangle([hx, hy, hx + hw, hy + hh], outline=GOLD, width=4)
    fw, fh = 210, 130
    flag_us(d, hx + 70, hy + 32, fw, fh)
    flag_cn(d, hx + hw // 2 - fw // 2, hy + 32, fw, fh)
    flag_ru(d, hx + hw - 70 - fw, hy + 32, fw, fh)
    centre(d, W // 2, hy + 182, "TRUMP, XI AND PUTIN", font(SERIF, 52), (255, 255, 255))
    centre(d, W // 2, hy + 292, "MEET IN SHENZHEN", font(SERIF, 52), (255, 214, 120))
    centre(d, W // 2, hy + 408,
           "First-ever trilateral of the three leaders, on the APEC sidelines",
           font(SANS_B, 20), (235, 238, 242))
    centre(d, W // 2, hy + 448,
           "Ukraine, the Iran war, nuclear arms and AI on the agenda — Europe absent",
           font(SANS, 19), (200, 208, 220))

    # ---- story grid: 2 cols x 3 rows ----
    gx, gy = M, 748
    cw = (W - 2 * M - 28) // 2
    ch = 264
    stories = [
        ("MIDDLE EAST", "Houthi missile threat toward Riyadh",
         "The Saudi-led coalition said it dealt with a missile threat "
         "launched by Yemen's Houthis toward Riyadh; debris fell and "
         "material damage was reported.", icon_rocket),
        ("GAZA", "Israeli tanks cross Gaza's Yellow Line",
         "First ground operation beyond the ceasefire line since the "
         "October 2025 truce, near Nuseirat. 3 killed; 5,200+ people fled.",
         icon_tank),
        ("EUROPE", "Denmark set to ratify the Trump Greenland deal",
         "Danish parliament vote expected Thursday around 10:00. The deal "
         "expands the US military role in Greenland, home to 57,000 people.",
         icon_building),
        ("BANGLADESH", "Bangladesh in lockdown",
         "The Awami League called a nationwide lockdown for Thursday. The "
         "ancestral home of former leader Muhammad Yunus was set ablaze; "
         "two ruling-party members killed.", icon_flame),
        ("CLIMATE", "COP31 deadlock in Antalya",
         "21 issues remain unresolved at the climate summit, with new draft "
         "texts due early Thursday. The summit closes on Friday.",
         icon_globe),
        ("INDONESIA", "Refinery blast in Cepu, Central Java",
         "An explosion at a refinery in Cepu killed one worker. An "
         "investigation is under way.", icon_factory),
    ]
    for i, (kick, head, body, ic) in enumerate(stories):
        cx = gx + (i % 2) * (cw + 28)
        cy = gy + (i // 2) * (ch + 18)
        story_card(d, cx, cy, cw, ch, kick, head, body, ic)

    # ---- stat strip ----
    sy = 1594
    d.rectangle([M, sy, W - M, sy + 132], fill=INK)
    stats = [("€45bn", "EU loan to Ukraine"),
             ("97", "Border Guard platoons out"),
             ("21", "issues left at COP31"),
             ("5,200+", "people fled the Gaza operation")]
    sw = (W - 2 * M) // 4
    for i, (num, lab) in enumerate(stats):
        x0 = M + i * sw
        if i:
            d.line([x0, sy + 20, x0, sy + 112], fill=(90, 96, 104), width=2)
        centre(d, x0 + sw // 2, sy + 12, num, font(SERIF, 38), (255, 214, 120))
        centre(d, x0 + sw // 2, sy + 90, lab, font(SANS, 14), (225, 228, 232))

    # ---- in brief ----
    by = 1746
    d.text((M, by), "IN BRIEF", font=font(SANS_B, 18), fill=RED)
    briefs = [
        "Japan PM Takaichi held talks with Putin at APEC.",
        "Kim Jong Un inspected sites amid talk of a Trump meeting.",
        "Anthropic begins trading on the Nasdaq.",
        "Chancellor Merz hosts Macron and Burnham in Berlin for a Ukraine-guarantees summit.",
        "US and Venezuela announced anti-drug military cooperation.",
    ]
    yy = by + 42
    for b in briefs:
        d.ellipse([M + 4, yy + 8, M + 18, yy + 22], fill=RED)
        yy = para(d, M + 34, yy, b, font(SANS, 15), INK, W - 2 * M - 34, 36)
        yy += 2

    # ---- footer ----
    fy = 1986
    d.line([M, fy, W - M, fy], fill=INK, width=3)
    centre(d, W // 2, fy + 14,
           "THURSDAY, 19 NOVEMBER 2026  •  Reported by Reuters, BBC, Al Jazeera and UN News",
           font(SANS_B, 16), INK)

    out = img.resize((1024, 1024), Image.LANCZOS)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
