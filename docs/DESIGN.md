# Design principles

[简体中文](DESIGN.zh-CN.md) · [Back to README](../README.md)

Cutelemon6 aims to give a document in progress the order of a finished page. Body text sets a steady density. Headings explain the structure. Color signals a purpose. The character of the page comes from how precisely these relationships work together.

Our preference is for clear, restrained typography with a slight bookish quality. It should support a long passage without images and accommodate commands, tables, and unfinished drafts. A pleasing first impression matters, alongside the experience of editing for a while and returning to the same text later.

## 1. Establish the scale with ordinary paragraphs

Set several consecutive paragraphs before designing headings and decoration. All three themes begin at 16 px, with a text column of about 680 px at its maximum width. This accommodates a useful amount of information while leaving room for Chinese and Latin text on the same line.

A line height of 1.65 gives the sans-serif themes an editing-oriented density. The serif theme uses 1.70 to allow slightly more space for its finer details. A 12 px paragraph gap and 4 px list-item gap keep boundaries visible while maintaining a continuous reading rhythm.

These are starting values, not universal optima for every reader and display. Evaluate changes with ordinary paragraphs at the size used for actual editing, as well as with enlarged headings.

## 2. Express hierarchy through relationships

H1, H2, and H3 use 28, 22, and 18 px. All headings align with the body text, giving the eye a consistent edge along which to find the document's structure.

H2 receives 32 px above and 10 px below, placing it visibly closer to the text it introduces. A thin rule at this level gives each chapter a steady pause. H3 continues the hierarchy through size, weight, and spacing.

Decoration can stop once the hierarchy is clear. Larger titles, heavier rules, and a separate color for every heading level can make several elements compete for attention at once.

## 3. Give Chinese and Latin text a shared rhythm

Day and Night pair Open Sans with Source Han Sans. Distinct Latin letterforms sit alongside an orderly Chinese paragraph texture. Names, numbers, and punctuation can enter the same line without requiring a separate treatment.

Editorial pairs Source Serif 4 Regular with Source Han Serif Medium. The slightly stronger Chinese weight keeps its strokes present at everyday screen sizes, while the Latin text remains Regular to avoid an overly heavy paragraph. Headings then increase in weight to establish a useful distinction.

Judge a pairing by its visual weight, apparent size, and rhythm in mixed text. The same numeric weight does not imply the same darkness across different typefaces. This project keeps the family names, chosen weights, and real specimens available for inspection.

## 4. Concentrate color in a few places

Day uses dark gray for body text and headings, reserving teal for links and related interactions. Editorial concentrates dark red in chapter headings and keeps teal for links, giving structural markers and navigation distinct signals.

Night redistributes light and dark: charcoal behind the page, gray-white body text, and pale graphite-blue links. Colors on a dark page need enough luminance and must sit comfortably within a large neutral field. This requires its own palette rather than a mechanical inversion of the light version.

Links always retain a fine underline. Their purpose remains visible even when a reader does not distinguish the hue. The palette can have a character of its own while the means of recognizing information stays consistent.

## 5. Integrate technical material with the prose

Code uses 13.5 px monospace text, a tinted surface, and a light border. Token colors distinguish comments, strings, keywords, and numbers; the block as a whole stays close to the surrounding page's tonal range. Inline code receives enough background and edge definition to remain recognizable without turning a sentence into a sequence of prominent boxes.

Tables use 15 px text, a light grid, and very subtle alternating rows. They should support comparisons across columns while retaining a visual weight close to the paragraphs around them.

Quotes use a left border, a quiet surface, and an inset to establish another voice. Chinese text stays upright. The treatment identifies the material's source or role while preserving the prominence of the main prose.

## 6. Give three moods a common structure

Day serves everyday light-mode writing. Night offers the same type and structure on a dark surface. Editorial adds serif text and red chapters for longer pieces. The differences remain concentrated in typography and color; the text column and heading scale stay consistent.

Three fixed entries give each choice a purpose. Typora can pair the light and dark themes through its native appearance settings, with Editorial selected manually when desired. Switching themes can then preserve the reader's familiarity with a document's structure.

A shared `base.css` also protects visual consistency. A correction to quote spacing or table borders should reach the whole family.

## 7. Stay honest about real use

Screen editing and paper output use different scales. Printing returns to a white background with 10.5 pt body text by default. Editorial retains its red chapters. Paper size and margins remain under the export settings.

A browser preview, native editing, and PDF pagination are different levels of verification. Documentation should state which have actually been checked. Preview images should use the shipped styles and fonts; font origins and licenses should be easy to find; untested platforms should be named.

Good defaults deserve maintenance and should remain adjustable. Restraint here means making bounded choices: each emphasis has a purpose, and each addition should improve something specific.

## Questions for future changes

- Do weight and spacing still work through a full page of ordinary text?
- If color is temporarily removed, are chapters and links still recognizable?
- Does the prose remain the main content after the new element is added?
- Does the change work across the light, dark, and serif themes?
- Does it solve a concrete problem, or only add another visible effect?

These questions are more useful to this project than labels such as “premium,” “eye-friendly,” or “minimal.”
