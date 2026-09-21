# Brian Lee — Engineering Portfolio

[Live portfolio](https://voostorm.github.io/brian-lee-portfolio/)

A static portfolio covering backend and web applications, systems and tools, games and graphics, and data and AI coursework. Twelve project pages separate the problem, Brian's contribution, implementation details, and source evidence.

## Edit and preview

Requires Python 3. No third-party build dependencies.

```sh
python3 scripts/build.py
python3 -m http.server 8000
```

Open `http://localhost:8000`. Edit project content in `scripts/content.py`, layout in `scripts/build.py`, styling in `assets/style.css`, and interactions in `assets/site.js`. Rebuild and commit generated HTML files with the sources. GitHub Pages serves the committed files using the existing publishing configuration.

## Behavior

- Content, navigation, case studies, and source links work without JavaScript.
- JavaScript adds combined category and technology filtering, result announcements and click-to-load YouTube players.
- The opening feature shows Fish Fish from its running WebGL build, with direct links to the case study and playable game.
- No frontend framework, external font, analytics, or backend service is required.

## Evidence and attribution

Descriptions are grounded in `voostorm/ttu-works`, `voostorm/usc-works`, `voostorm/mop-addons`, and the three public game repositories. Each case study links to evidence. Academic and personal work is not presented as professional employment. Original addon authors retain credit for their underlying projects.

The PrimeEngine entry links to a public milestone outline, rather than engine source. The RAG entry describes coursework demonstrations. Game entries identify team context. Zap's older sources disagree on its creation date, so the portfolio does not assert one. The capstone team count is omitted because source summaries conflict.

Education dates were checked against supplied transcripts: USC M.S., December 2025; Tennessee Tech B.S., December 2023, Cum Laude. Private transcripts are not included in this repository.

## Visual evidence

The hero and game cards use captures from the actual Fish Fish and Magnet Bomber WebGL builds and the running Zap Python game. The AI workflow image is the original submitted `Q2-graph.png` from `usc-works`. No game screen or interface has been invented or painted over.

Projects without application captures display excerpts from their public source files. The PrimeEngine card quotes its public milestone outline, because engine source and screenshots are not available in that repository. Code excerpts are text, not screenshots of a fabricated application.

`assets/evidence/manifest.json` records each visual's caption, original source URL, and excerpt line numbers where relevant. Source excerpts retain their original content with common indentation removed; compact cards show only the first seven lines. Case studies show the longer excerpt and link to the original. Game capture URLs identify the exact build commit. The image files are local, so viewing the portfolio does not require third-party image requests.

To update a visual, replace its file in `assets/evidence/`, update the manifest attribution, run `python3 scripts/build.py`, and commit the source and generated pages together. The former sculpture, motion loop, and project concept SVGs have been removed.
