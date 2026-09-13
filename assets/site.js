const cards = [...document.querySelectorAll('.project-card')];
const search = document.querySelector('#project-search');
const filters = [...document.querySelectorAll('[data-filter]')];
let selected = 'all';
if (cards.length) {
  document.querySelector('#work-controls').hidden = false;
  function filterProjects() {
    const query = search.value.trim().toLowerCase();
    let count = 0;
    cards.forEach(card => {
      const match = (selected === 'all' || card.dataset.categories.split(' ').includes(selected)) && card.dataset.search.includes(query);
      card.hidden = !match;
      if (match) count++;
    });
    filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === selected)));
    document.querySelector('#project-count').textContent = `${count} ${count === 1 ? 'project' : 'projects'} · Academic, personal, and team work`;
    document.querySelector('#empty-state').hidden = count !== 0;
  }
  filters.forEach(button => button.addEventListener('click', () => { selected = button.dataset.filter; filterProjects(); }));
  search.addEventListener('input', filterProjects);
  document.querySelector('#reset-filters').addEventListener('click', () => { selected = 'all'; search.value = ''; filterProjects(); filters[0].focus(); });
}

const video = document.querySelector('#hero-video');
const toggle = document.querySelector('#motion-toggle');
if (video && toggle) {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let userPaused = false;
  toggle.hidden = false;
  const updateButton = () => { toggle.textContent = video.paused ? '▶ Play motion' : 'Ⅱ Pause motion'; };
  const play = async () => {
    if (!video.getAttribute('src')) video.src = video.dataset.src;
    try { await video.play(); } catch { /* The still image remains when playback is unavailable. */ }
    updateButton();
  };
  video.addEventListener('playing', () => { video.classList.add('is-playing'); updateButton(); });
  video.addEventListener('pause', updateButton);
  video.addEventListener('error', () => { video.classList.remove('is-playing'); toggle.hidden = true; });
  toggle.addEventListener('click', () => { userPaused = !video.paused; if (video.paused) play(); else video.pause(); });
  reduceMotion.addEventListener('change', () => { if (reduceMotion.matches) video.pause(); else if (!userPaused) play(); });
  const observer = new IntersectionObserver(entries => {
    if (!entries[0].isIntersecting) video.pause();
    else if (!reduceMotion.matches && !userPaused && !document.hidden) play();
  }, {threshold: 0.15});
  observer.observe(video);
  document.addEventListener('visibilitychange', () => { if (document.hidden) video.pause(); else if (!reduceMotion.matches && !userPaused && video.getBoundingClientRect().bottom > 0) play(); });
}

document.querySelectorAll('.video-load').forEach(button => {
  button.closest('.video-slot').hidden = false;
  button.addEventListener('click', () => {
  const slot = button.closest('.video-slot');
  const iframe = document.createElement('iframe');
  iframe.src = `https://www.youtube-nocookie.com/embed/${slot.dataset.video}`;
  iframe.title = slot.dataset.title;
  iframe.allow = 'encrypted-media; picture-in-picture; fullscreen';
  iframe.allowFullscreen = true;
  iframe.referrerPolicy = 'strict-origin-when-cross-origin';
  slot.replaceChildren(iframe);
  iframe.focus();
  });
});
