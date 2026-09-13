"""Build a dependency-free, progressively enhanced GitHub Pages portfolio."""
from pathlib import Path
from html import escape as e
from content import PROJECTS

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://voostorm.github.io/brian-lee-portfolio/'

def link(url, label, cls='text-link'):
    return f'<a class="{cls}" href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(label)} <span aria-hidden="true">↗</span></a>'

def head(title, description, prefix='', path=''):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | Brian Lee</title><meta name="description" content="{e(description)}">
<meta name="theme-color" content="#f5f4ef"><link rel="canonical" href="{BASE}{path}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)} | Brian Lee">
<meta property="og:description" content="{e(description)}"><meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{BASE}assets/systems-sculpture.webp">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}assets/style.css"><script src="{prefix}assets/site.js" defer></script></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header wrap"><a class="brand" href="{prefix}index.html" aria-label="Brian Lee home"><span class="brand-mark" aria-hidden="true">b.</span> Brian Lee<span class="brand-sub"> / Software engineer</span></a>
<nav aria-label="Main navigation"><a href="{prefix}index.html#work">Work</a><a href="{prefix}index.html#about">About</a><a class="nav-contact" href="{prefix}index.html#contact">Let’s talk <span aria-hidden="true">↗</span></a></nav></header>'''

def footer(prefix=''):
    return f'''<footer class="wrap footer"><a class="brand" href="{prefix}index.html">Brian (Won S.) Lee</a><span>Los Angeles, CA · English & Korean</span><a href="#top">Back to top ↑</a></footer></body></html>'''

def tags(p):
    return '<ul class="tags" aria-label="Technologies">'+''.join(f'<li>{e(t)}</li>' for t in p['stack'])+'</ul>'

def sketch(p):
    # These are explanatory illustrations, never claimed to be application screenshots.
    v=p['visual']; out=[]
    def rect(x,y,w,h,label='',fill='#fff',stroke='#babdb4'):
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}"/>')
        if label: txt(x+w/2,y+h/2+4,label)
    def txt(x,y,s,color='#363a35',size=12):
        out.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="monospace" font-size="{size}" fill="{color}">{e(s)}</text>')
    def line(x,y,a,b,color='#92988e'):
        out.append(f'<path d="M{x} {y}L{a} {b}" stroke="{color}" fill="none" stroke-width="1.5"/>')
    def circle(x,y,r,fill,stroke='none'):
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}"/>')
    if v=='portal':
        rect(44,31,272,146,fill='#fff');rect(44,31,272,26,fill='#e5e8df');txt(117,48,'DEMAND RESPONSE',size=10)
        for i,h in enumerate([25,38,29,52,43,62,48,75,60]):rect(128+i*17,151-h,10,h,fill='#627961',stroke='none')
        for i,s in enumerate(['Meters','Members','Organizations']):txt(80,86+i*25,s,size=8)
        line(117,66,117,162);txt(221,169,'Energy usage · concept',size=8)
    elif v=='crawler':
        rect(27,78,67,42,'Queue',fill='#f8f2df')
        for i in range(7):
            y=28+i*25;line(94,99,156,y+6);circle(163,y+6,6,'#ba6037');line(170,y+6,240,99)
        rect(240,78,91,42,'CSV output');txt(174,218,'7 WORKERS / SHARED QUEUE',size=10)
    elif v=='dashboard':
        rect(36,38,288,143,fill='#fff');rect(36,38,288,26,fill='#e7e3f0');txt(180,55,'SCHEDULE SERVICE',size=10)
        for i,s in enumerate(['GET /allcourses','GET /coursesbyfaculty','GET /schbydeptandterms']):txt(180,92+i*26,s,size=12)
        txt(180,209,'13 GET MAPPINGS · JAVA + SPRING',size=10)
    elif v=='addons':
        txt(180,45,'SAVED COOLDOWN ORDER',size=11)
        for i,s in enumerate(['01','02','03','04']):
            rect(49+i*69,82,55,55,fill=['#39483e','#6c7a53','#a26749','#7a697d'][i],stroke='none')
            txt(76+i*69,115,s,'#fff',16)
        out.append('<path d="M75 158 Q180 208 284 157" stroke="#9d512f" fill="none" stroke-dasharray="4 4"/>')
        txt(180,213,'PREPARE → SAVE → PLAY',size=10)
    elif v=='engine':
        for x,y in [(135,70),(250,105)]:
            out.append(f'<path d="M{x} {y}l40 -18 36 22v55l-39 19 -37 -22z M{x} {y}l37 22 39 -18 M{x+37} {y+22}v74" stroke="#5b6768" fill="none" stroke-width="1.5"/>')
        out.append('<path d="M32 119L224 32V204Z" stroke="#b46743" fill="#b46743" fill-opacity=".06" stroke-dasharray="5 5"/>')
        circle(32,119,5,'#b46743');txt(180,225,'FRUSTUM / BOUNDING VOLUMES',size=10)
    elif v=='rag':
        for x,y,w,s in [(22,44,95,'Documents'),(21,140,97,'Question'),(141,88,99,'Retrieval'),(265,88,73,'Model')]:rect(x,y,w,39,s)
        line(117,63,141,108);line(118,159,141,108);line(240,108,265,108);txt(180,211,'CONTEXT → GENERATION',size=10)
    elif v=='terminal':
        rect(37,28,286,174,fill='#252e29',stroke='none')
        for i in range(3):circle(53+i*14,42,3,['#d98257','#bfb896','#779679'][i])
        for i,s in enumerate(['$ ./nethelper.sh hosts.txt','[P] ping    [N] nslookup','[S] ssh     [H] hostname','[I] interfaces','> Select a host _']):txt(180,75+i*24,s,'#cee0cb',11)
    elif v=='database':
        for x,y,s in [(35,45,'BOOK'),(223,45,'COPY'),(35,145,'MEMBER'),(223,145,'LOAN')]:rect(x,y,103,41,s)
        line(138,65,223,65);line(274,86,274,145);line(138,165,223,165);txt(179,213,'RELATIONAL DATA / JDBC',size=10)
    elif v=='go':
        for i in range(5):line(99+i*40,34,99+i*40,194);line(99,34+i*40,259,34+i*40)
        for x,y,c in [(179,114,'#282c26'),(139,114,'#fff'),(219,114,'#fff'),(179,74,'#282c26'),(179,154,'#282c26'),(219,154,'#fff')]:circle(x,y,14,c,'#85887b')
        circle(139,74,6,'#b46743');txt(180,223,'EVALUATE → SEARCH → MOVE',size=10)
    else:
        # A visual motif for the game mechanic, explicitly captioned as a concept sketch.
        if v=='fish':
            for y in [65,120,180]:out.append(f'<path d="M20 {y}q40 -20 80 0t80 0t80 0t80 0" stroke="#9cbab0" fill="none"/>')
            out.append('<path d="M55 170Q180 -25 242 106v27q0 20 -17 20t-17 -20" stroke="#385f52" fill="none" stroke-width="3"/>')
            out.append('<path d="M250 151q38 -32 68 0q-30 32 -68 0l-16 14v-28z" fill="#769f8b"/>')
            circle(301,146,3,'#fff');txt(180,222,'CAST / HOOK / REEL',size=10)
        elif v=='magnet':
            for r in [36,65,97]:circle(180,116,r,'none','#a3abbc')
            circle(180,116,23,'#526580');rect(86,52,20,20,fill='#b77454',stroke='none');rect(261,145,20,20,fill='#b77454',stroke='none');txt(180,224,'PULL / LAUNCH / DETONATE',size=10)
        else:
            circle(180,111,16,'#dc6b99')
            for x,y in [(70,54),(285,60),(81,175),(270,163)]:rect(x,y,17,17,fill='#e6dcc7',stroke='#827a83')
            for a,b in [(180,55),(180,170),(120,111),(240,111)]:line(180,111,a,b,'#dc6b99')
            txt(180,222,'DODGE / FIRE / SURVIVE',size=10)
    return f'<svg viewBox="0 0 360 240" xmlns="http://www.w3.org/2000/svg">'+''.join(out)+'</svg>'

(ROOT/'projects').mkdir(exist_ok=True)
for p in PROJECTS:
    (ROOT/'assets'/f"{p['id']}.svg").write_text(sketch(p))
    media=''
    if p.get('video'):
        media=f'''<section class="demo" aria-labelledby="demo-heading"><p class="eyebrow">See it in action</p><h2 id="demo-heading">Gameplay demo</h2>
        <div class="video-slot" hidden data-video="{p['video']}" data-title="{e(p['title'])} gameplay"><button class="button video-load" type="button">▶ Load gameplay video</button><p>Loads the YouTube player when selected.</p></div>
        <div class="demo-links">{link('https://www.youtube.com/watch?v='+p['video'],'Watch on YouTube')}{link(p['play'],'Play the WebGL build') if p.get('play') else ''}</div></section>'''
    page=head(p['title'],p['summary'],'../',f"projects/{p['id']}.html")
    page+=f'''<main class="wrap case" id="main"><div id="top"></div><a class="back" href="../index.html#work">← All projects</a>
    <div class="case-intro"><div><p class="eyebrow">{e(p['category'])} / {e(p['year'])}</p><h1>{e(p['title'])}</h1><p class="lead">{e(p['summary'])}</p>{tags(p)}<p class="project-context">{e(p['context'])}</p></div><figure class="case-art art-{p['visual']}"><img src="../assets/{p['id']}.svg" alt=""><figcaption>Concept sketch · {e(p['title'])}</figcaption></figure></div>
    <div class="case-layout"><div class="case-copy"><section><p class="eyebrow">01 / The problem</p><h2>What this project explores</h2><p>{e(p['problem'])}</p></section><section><p class="eyebrow">02 / My contribution</p><h2>The work I took on</h2><p>{e(p['contribution'])}</p><ul class="implementation">{''.join('<li>'+e(x)+'</li>' for x in p['details'])}</ul></section><section><p class="eyebrow">03 / The result</p><h2>What it demonstrates</h2><p>{e(p['outcome'])}</p></section>{media}</div>
    <aside class="evidence"><p class="eyebrow">Explore the evidence</p><h2>Go one level deeper.</h2>{''.join(link(s['url'],s['label']) for s in p['proof'])}<hr><p>Interested in this work?</p><a class="text-link" href="mailto:wlee.techjob@gmail.com">Get in touch ↗</a></aside></div>
    <a class="button outline" href="../index.html#work">← Explore more projects</a></main>'''+footer('../')
    (ROOT/'projects'/f"{p['id']}.html").write_text(page)

cards=[]
for n,p in enumerate(PROJECTS,1):
    search=' '.join([p['title'],p['category'],p['summary'],*p['stack']]).lower()
    cards.append(f'''<article class="project-card" data-categories="{p['filters']}" data-search="{e(search)}"><a class="card-visual art-{p['visual']}" href="projects/{p['id']}.html" tabindex="-1" aria-hidden="true"><span class="card-number">{n:02d}</span><img src="assets/{p['id']}.svg" alt="" loading="lazy" width="360" height="240"><span class="art-caption">Concept sketch</span><span class="card-arrow">↗</span></a><div class="card-body"><p class="eyebrow">{e(p['category'])}</p><h3><a href="projects/{p['id']}.html">{e(p['title'])}</a></h3><p class="summary">{e(p['summary'])}</p>{tags(p)}<p class="card-meta">{e(p['year'])} <span aria-hidden="true">/</span> {'Team project' if 'team' in p['context'].lower() else 'Personal project' if p['id'] in ['zap','addon-engineering'] else 'Coursework'}</p></div></article>''')

index=head('Software, systems & interactive experiences','Brian Lee’s software engineering portfolio: backend APIs, data and AI workflows, C++ engine systems, Unity games, and Lua tools.')
index+='''<main id="main"><div id="top"></div><section class="hero wrap" aria-labelledby="hero-title"><div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span> Open to early-career engineering roles</p><h1 id="hero-title">Built to solve.<br>Made to <em>explore.</em></h1><p class="hero-description">I’m Brian, a software engineer in Los Angeles.<br>From backend services to game systems, I turn complex problems into software you can use.</p><div class="hero-actions"><a class="button" href="#work">Explore my work <span aria-hidden="true">↓</span></a><a class="text-link" href="https://github.com/voostorm" target="_blank" rel="noopener noreferrer">GitHub ↗</a></div><div class="hero-credentials"><span>M.S. Computer Science <strong>USC ’25</strong></span><span>Backend · Systems · Games · AI</span></div></div><figure class="hero-art"><img src="assets/systems-sculpture.webp" width="1000" height="1000" alt="An abstract sculpture of interlocking graphite arches, a silver ring, and an orange sphere" fetchpriority="high"><video id="hero-video" muted loop playsinline preload="none" aria-hidden="true" poster="assets/systems-sculpture.webp" data-src="assets/systems-loop.mp4"></video><figcaption><span>CONNECTED SYSTEMS / 001</span><button id="motion-toggle" type="button" hidden>Play motion</button></figcaption></figure></section>
<div class="discipline-strip"><div class="wrap"><span>Ideas into implementations</span><span>Backend & web</span><span>Systems & tools</span><span>Games & graphics</span><span>Data & AI</span></div></div>
<section class="wrap work-section" id="work" aria-labelledby="work-heading"><div class="section-heading"><div><p class="eyebrow">01 / Project collection</p><h2 id="work-heading">Selected work<span class="accent">.</span></h2></div><p>Different domains. The same curiosity.<br>Explore the problem, my contribution, and the code.</p></div>
<div class="work-controls" id="work-controls" hidden><div class="filters" role="group" aria-label="Filter projects"><button data-filter="all" aria-pressed="true">All work <span>12</span></button><button data-filter="web" aria-pressed="false">Backend & web</button><button data-filter="systems" aria-pressed="false">Systems & tools</button><button data-filter="games" aria-pressed="false">Games & graphics</button><button data-filter="ai" aria-pressed="false">Data & AI</button></div><label class="search"><span class="sr-only">Search projects or technologies</span><span aria-hidden="true">⌕</span><input type="search" id="project-search" placeholder="Find a technology…" autocomplete="off"></label></div><p id="project-count" class="result-count" role="status" aria-live="polite">12 projects · Academic, personal, and team work</p><div class="project-grid">'''+''.join(cards)+'''</div><div class="empty-state" id="empty-state" hidden><h3>No matching projects</h3><p>Try a broader search or another category.</p><button class="button outline" id="reset-filters">Show all work</button></div><noscript><p>All projects are shown. Follow any project title to explore it.</p></noscript></section>
<section class="about-section" id="about"><div class="wrap about-grid"><div class="about-heading"><p class="eyebrow">02 / A little about me</p><h2>Curiosity is<br>the common thread<span class="accent">.</span></h2><div class="portrait"><img src="brian_face.jpeg" alt="Brian Lee" width="80" height="80" loading="lazy"><div><strong>Brian (Won S.) Lee</strong><span>Software engineer · Los Angeles</span></div></div></div><div class="about-copy"><p class="lead">I like understanding how things work—and making them work better.</p><p>My projects span academic backend services, search and AI experiments, game development, and modifications to the tools I use. I enjoy the point where a user-facing problem becomes a concrete question about code, data, or system behavior.</p><p>I’m looking for an early-career engineering role where I can contribute, learn from thoughtful teammates, and keep building. I’m open to opportunities across the United States.</p><div class="education"><div><span class="edu-year">2025</span><div><h3>University of Southern California</h3><p>M.S. in Computer Science · December 2025</p></div></div><div><span class="edu-year">2023</span><div><h3>Tennessee Technological University</h3><p>B.S. in Computer Science · Cum Laude · December 2023</p></div></div></div><div class="archive-links">'''+link('https://github.com/voostorm/ttu-works','Undergraduate work')+link('https://github.com/voostorm/usc-works','Graduate work')+'''</div></div></div></section>
<section class="wrap contact-section" id="contact"><div><p class="eyebrow">03 / What’s next</p><h2>Let’s build<br>something useful<span class="accent">.</span></h2><p>Have an engineering opportunity or a question about a project?</p></div><div class="contact-links"><a class="contact-email" href="mailto:wlee.techjob@gmail.com">wlee.techjob@gmail.com <span aria-hidden="true">↗</span></a><div>'''+link('https://www.linkedin.com/in/brianwslee/','LinkedIn')+link('https://github.com/voostorm/','GitHub')+'''</div><p class="contact-note">For game-related inquiries: <a href="mailto:voostorm.gaming@gmail.com">voostorm.gaming@gmail.com</a></p></div></section></main>'''+footer()
(ROOT/'index.html').write_text(index)
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}{p}</loc></url>' for p in ['']+[f"projects/{x['id']}.html" for x in PROJECTS])+'</urlset>')
print(f'Built index and {len(PROJECTS)} case studies.')
