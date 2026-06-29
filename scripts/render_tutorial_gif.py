#!/usr/bin/env python3
"""Render a sanitized tutorial preview GIF for last30days API setup."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1280
HEIGHT = 720
OUT = Path("assets/tutorials/last30days-api-setup-preview.gif")


SCENES = [
    (
        "last30days + AEO/SEO",
        "Use real user language to supplement keyword clusters.",
        "No real API keys are shown in this tutorial.",
        "https://github.com/hanco1/han-aeo-v1",
    ),
    (
        "Step 1: ScrapeCreators",
        "Unlock TikTok, Instagram, Threads, and Reddit backup.",
        "Create a project key, then pause before the secret appears.",
        "https://scrapecreators.com",
    ),
    (
        "Step 2: xAI",
        "Optional: add X/Twitter-style recent conversation coverage.",
        "Use XAI_API_KEY only if X matters for your project.",
        "https://console.x.ai",
    ),
    (
        "Step 3: Brave Search API",
        "Optional: improve web context and auto-resolve.",
        "Useful when the agent cannot use WebSearch directly.",
        "https://api.search.brave.com",
    ),
    (
        "Step 4: OpenRouter",
        "Optional: enable deeper research routes.",
        "Not required for basic AEO/SEO keyword supplements.",
        "https://openrouter.ai/settings/keys",
    ),
    (
        "Step 5: Paste into .env",
        "Use fake-looking demo values in tutorials.",
        "Never record, share, or commit real keys.",
        "SCRAPECREATORS_API_KEY=sk_demo_replace_me",
    ),
    (
        "Step 6: Run diagnose",
        "Check which sources are available before researching.",
        "python .../last30days.py --diagnose",
        "\"available_sources\": [\"reddit\", \"youtube\", \"github\"]",
    ),
    (
        "Step 7: Research one real question",
        "Use concrete customer language, not generic keywords.",
        "/last30days bridal makeup booking concerns --agent",
        "Map results to FAQ, headings, and AEO content.",
    ),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/seguisb.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def rounded(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill: str, outline: str | None = None) -> None:
    draw.rounded_rectangle(xy, radius=18, fill=fill, outline=outline, width=2 if outline else 1)


def draw_scene(index: int, title: str, body: str, note: str, url: str) -> Image.Image:
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F7F8FB")
    d = ImageDraw.Draw(img)

    # Browser shell.
    rounded(d, (80, 70, 1200, 620), "#FFFFFF", "#D6DAE3")
    d.rectangle((80, 70, 1200, 132), fill="#EEF1F6")
    for i, color in enumerate(["#FF5F57", "#FFBD2E", "#28C840"]):
        d.ellipse((110 + i * 34, 92, 130 + i * 34, 112), fill=color)
    rounded(d, (250, 88, 1135, 116), "#FFFFFF", "#D6DAE3")
    d.text((270, 94), url, fill="#4F5B6B", font=font(15))

    # Side rail.
    d.rectangle((80, 132, 285, 620), fill="#172033")
    d.text((110, 165), "API setup", fill="#FFFFFF", font=font(26, True))
    d.text((110, 210), "for beginners", fill="#B8C2D6", font=font(18))
    d.text((110, 560), f"{index + 1}/{len(SCENES)}", fill="#B8C2D6", font=font(18))

    # Content panel.
    d.text((330, 185), title, fill="#172033", font=font(46, True))
    d.text((334, 260), body, fill="#293449", font=font(28))

    rounded(d, (335, 330, 1115, 440), "#F0F6FF", "#BED4FF")
    d.text((365, 365), note, fill="#183B73", font=font(25, True))

    # Safe key mask mock.
    if ".env" in title or "ScrapeCreators" in title or "xAI" in title or "Brave" in title or "OpenRouter" in title:
        rounded(d, (335, 480, 1115, 548), "#101828", "#101828")
        secret = url if "=" in url else "API_KEY=••••••••••••••••••••••••"
        d.text((365, 502), secret, fill="#D0F5A7", font=font(22))

    d.text((330, 585), "Tutorial preview uses fake values only.", fill="#697386", font=font(18))
    return img


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames = [draw_scene(i, *scene) for i, scene in enumerate(SCENES)]
    frames[0].save(
        OUT,
        save_all=True,
        append_images=frames[1:],
        duration=2200,
        loop=0,
        optimize=False,
    )
    print(OUT.resolve())


if __name__ == "__main__":
    main()
