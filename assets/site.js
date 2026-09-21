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
