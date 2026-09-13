# Brian Lee — Engineering Portfolio

[Live portfolio](https://voostorm.github.io/brian-lee-portfolio/)

A static portfolio covering backend and web applications, systems and tools, games and graphics, and data and AI coursework. Twelve project pages separate the problem, Brian's contribution, implementation details, and source evidence.

## Edit and preview

Requires Python 3. No third-party build dependencies.

```sh
python3 scripts/build.py
python3 -m http.server 8000
```

Open `http://localhost:8000`. Edit project content in `scripts/content.py`, layout in `scripts/build.py`, styling in `assets/style.css`, and interactions in `assets/site.js`. Rebuild and commit generated HTML and SVG files with the sources. GitHub Pages serves the committed files using the existing publishing configuration.

## Behavior

- Content, navigation, case studies, and source links work without JavaScript.
- JavaScript adds combined category and technology filtering, result announcements, motion controls, and click-to-load YouTube players.
- The eight-second hero loop is muted, respects reduced-motion preferences, pauses out of view, and has a manual pause control. A still image remains available when playback fails.
- No frontend framework, external font, analytics, or backend service is required.

## Evidence and attribution

Descriptions are grounded in `voostorm/ttu-works`, `voostorm/usc-works`, `voostorm/mop-addons`, and the three public game repositories. Each case study links to evidence. Academic and personal work is not presented as professional employment. Original addon authors retain credit for their underlying projects.

The PrimeEngine entry links to a public milestone outline, rather than engine source. The RAG entry describes coursework demonstrations. Game entries identify team context. Zap's older sources disagree on its creation date, so the portfolio does not assert one. The capstone team count is omitted because source summaries conflict.

Education dates were checked against supplied transcripts: USC M.S., December 2025; Tennessee Tech B.S., December 2023, Cum Laude. Private transcripts are not included in this repository.

## Visual assets

`assets/systems-sculpture.webp` is the optimized artwork made with the built-in GPT Image tool. `assets/systems-loop.mp4` is an eight-second camera-motion loop rendered from that still with FFmpeg, not a generative-video output. The hero is decorative. Project SVG illustrations are labeled concept sketches; they are not application screenshots or measured results.

Generation prompt:

> Use case: stylized-concept. Asset type: right-side hero artwork for Brian Lee's software engineering portfolio, also source image for a subtle looping camera animation. Create a premium editorial 3D still life, square composition: one beautifully machined sculptural assembly of interlocking graphite-black rounded rectangular arches, a satin aluminum ring, and a single vivid burnt-orange sphere suspended within the assembly. Physical model of connected systems; abstract, elegant, precise, tactile surfaces with subtle brushed-metal texture. On a warm pale ivory seamless studio floor and backdrop (#efeee7), soft directional daylight from upper left, rich realistic contact shadows. Centered composition with generous empty margins around all objects, entire sculpture visible. Architectural product photography aesthetic, restrained and striking, no sci-fi glow. No text, no logos, no watermark, no people, no computers, no schematic or factual diagram. Output square high resolution.

Recreate the motion loop:

```sh
ffmpeg -loop 1 -i assets/systems-sculpture.webp -vf "scale=1600:1600,zoompan=z='1.02+0.02*(1-cos(2*PI*on/192))':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=192:s=720x720:fps=24" -frames:v 192 -c:v libx264 -crf 25 -pix_fmt yuv420p -movflags +faststart -an assets/systems-loop.mp4
```
