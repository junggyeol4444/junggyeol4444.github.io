
(function(){
  const input = document.getElementById('search-input');
  const box = document.getElementById('search-results');
  if(!input || !box) return;
  let index = null, docs = [];

  async function ensureIndex(){
    if(index) return index;
    try{
      const res = await fetch((window.__baseurl||'') + '/out/search-index.json', {cache:'no-store'});
      if(!res.ok) throw new Error('no index');
      docs = await res.json();
      index = window.SimpleSearch.build(docs);
      return index;
    }catch(e){
      console.warn('search index missing:', e);
      return null;
    }
  }
  function render(items){
    if(!items || items.length===0){ box.classList.remove('open'); box.innerHTML=''; return; }
    box.innerHTML = items.map(d => `<a href="${d.url}"><strong>${d.title||d.url}</strong><br><span>${(d.excerpt||'').slice(0,80)}</span></a>`).join('');
    box.classList.add('open');
  }
  input.addEventListener('input', async () => {
    const q = input.value.trim();
    const idx = await ensureIndex();
    if(!idx || !q){ render([]); return; }
    const items = idx.search(q);
    render(items);
  });
  document.addEventListener('click', (e)=>{
    if(!box.contains(e.target) && e.target!==input){ box.classList.remove('open'); }
  });
})();
