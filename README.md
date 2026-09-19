# Cutelemon6 Typora Themes

[简体中文](README.zh-CN.md) · [Design principles](docs/DESIGN.md) · [Font credits & licenses](THIRD_PARTY_NOTICES.md)

Three Typora themes for everyday writing and longer reading: a clean light theme, a balanced dark theme, and a serif editorial theme with restrained red headings.

All three start with **16 px body text**, a **680 px text column**, and a **28 / 22 / 18 px heading scale**. Their character comes from type, spacing, and a small number of deliberate color choices.

| Day | Night | Editorial |
| --- | --- | --- |
| [![Day preview](assets/previews/day.png)](assets/previews/day.png) | [![Night preview](assets/previews/night.png)](assets/previews/night.png) | [![Editorial preview](assets/previews/editorial.png)](assets/previews/editorial.png) |
| White, sans serif, teal links | Charcoal, sans serif, pale blue links | White, serif, dark red headings, teal links |

*Browser-rendered previews using the CSS and fonts shipped in this repository. Open an image to inspect it at full size.*

## Choose a theme

| Theme menu entry | Body type | Line height | Links |
| --- | --- | --- | --- |
| **Cutelemon6 Day** | Open Sans + Source Han Sans CN Regular | 1.65 | Teal `#0F6B68` |
| **Cutelemon6 Night** | Open Sans + Source Han Sans CN Regular | 1.65 | Pale graphite blue `#91BDE4` |
| **Cutelemon6 Editorial** | Source Serif 4 Regular + Source Han Serif CN Medium | 1.70 | Teal `#0F6B68` |

Day and Night are a working pair. Editorial offers a more bookish rhythm while keeping the same compact heading scale and text column. Its chapter headings use dark red `#963D36`.

The Chinese fonts use the mainland Simplified Chinese glyph convention. Fonts are bundled and loaded locally; installation does not require adding them to the operating system's font library. Code uses the available system monospace font, such as Menlo or Consolas.

## Install

1. [Download the repository ZIP](https://github.com/Cutelemon6/cutelemon6-typora-themes/archive/refs/heads/main.zip) and extract it.
2. In Typora, open **Preferences / Settings → Appearance → Open Theme Folder**.
3. Copy **everything inside `themes/`** into that folder. The three CSS files and the `cutelemon6` resource folder must remain side by side.
4. Save your documents and restart Typora. Choose a theme from the **Themes** menu.

```text
Typora theme folder/
├── cutelemon6-day.css
├── cutelemon6-night.css
├── cutelemon6-editorial.css
└── cutelemon6/
    ├── base.css
    ├── fonts-sans.css
    ├── fonts-serif.css
    ├── fonts/
    └── licenses/
```

For the intended size, leave Typora's font size on **Auto** and zoom at **100%**. A custom font size can override the default. Open [the Markdown specimen](examples/showcase.md) to check headings, links, lists, tables, code, formulas, and footnotes.

## Switch with the system

On a supported Typora installation, set **Cutelemon6 Day** as the light theme and **Cutelemon6 Night** as the dark theme, then enable the separate dark-theme setting. Typora can follow the operating system's appearance using those two choices. See [Typora's dark mode guide](https://support.typora.io/Dark-Mode/).

Select **Cutelemon6 Editorial** manually when you want the serif treatment. A manual selection may update the theme assigned to the current system appearance; select Day or Night again to restore the pair.

Three fixed choices keep the theme menu small. All share one layout file, so a spacing fix reaches the whole family.

## Layout details

- **Headings:** left aligned; a thin divider under H2; 32 px above and 10 px below H2.
- **Paragraphs:** 12 px after each paragraph; 4 px between list items.
- **Links:** a visible 1 px underline, strengthened on hover; visited links keep the same color.
- **Quotes:** a quiet tinted surface and a left border, with normal upright text.
- **Code:** 13.5 px monospace text, 1.6 line height, a modest border, and CodeMirror token colors.
- **Tables:** 15 px text, light borders, and subtle alternating rows.
- **Print:** white paper in all three themes, 10.5 pt body text by default. Editorial retains its red chapter headings. Paper size and margins remain under Typora's export controls.

## Customize

Each theme entry defines its palette and typography through CSS variables. Change `--cutelemon6-link` in a theme entry to adjust its link color. Shared spacing and element styles live in [`themes/cutelemon6/base.css`](themes/cutelemon6/base.css).

For personal overrides that survive updates, use Typora's [theme-specific user CSS](https://support.typora.io/Add-Custom-CSS/), for example `cutelemon6-day.user.css`:

```css
:root {
  --cutelemon6-link: #0f6b68;
}

#write {
  max-width: 744px; /* includes 32 px of padding on each side */
}
```

The [design principles](docs/DESIGN.md) explain the tradeoffs behind these defaults and provide a guide for extending the themes.

## Preview and validation

For a local browser preview, run this from the repository root, then open the printed address with `/preview/` appended:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
# Open http://127.0.0.1:8000/preview/
```

The browser preview covers basic Markdown layout. Formulas, footnotes, editor interactions, and CodeMirror syntax highlighting should be checked in Typora using the full specimen.

The shipped CSS, local font loading, 16 px body size, three palettes, and basic Markdown layout have been checked in a macOS browser. **Native Typora editing and PDF pagination still need verification; Windows and Linux have not been tested.** Platform monospace fonts and font rasterization can change the appearance slightly.

To check package references and font file integrity:

```bash
python3 scripts/check.py
```

## License and credits

The original theme CSS, documentation, specimen, preview page, and scripts are licensed under [MIT](LICENSE).

**Bundled fonts keep their own licenses and are not covered by MIT.** Source Han Sans, Source Han Serif, and Source Serif 4 are distributed under SIL OFL 1.1; the bundled Open Sans version uses Apache 2.0. The repository ships upstream font binaries unchanged, with their notices and licenses. See [third-party notices](THIRD_PARTY_NOTICES.md) and the [font manifest](font-manifest.json) for sources and SHA-256 values.

This is an independent theme project. Typora and the font authors do not sponsor or endorse it.
