
(function() {
  // Activate current nav link
  var here = window.location.pathname.replace(/\/$/, '');
  document.querySelectorAll('.tgd-nav a[href^="/"]').forEach(function(a) {
    var href = a.getAttribute('href');
    if (!href) return;
    var u = href.replace(/\/$/, '');
    if (u && (here === u || here.startsWith(u))) a.classList.add('active');
  });

  // Mobile sidebar toggle (optional)
  var btn = document.querySelector('[data-toggle="sidebar"]');
  var sidebar = document.querySelector('.tgd-sidebar');
  if (btn && sidebar) btn.addEventListener('click', function() {
    sidebar.style.display = (getComputedStyle(sidebar).display === 'none') ? 'block' : 'none';
  });

  // Simple tab switcher for creator pages
  document.querySelectorAll('[data-tab-target]').forEach(function(btn){
    btn.addEventListener('click', function(e){
      var target = btn.getAttribute('data-tab-target');
      if (!target) return;
      // toggle button styles
      document.querySelectorAll('[data-tab-target]').forEach(function(b){ b.classList.remove('primary'); });
      btn.classList.add('primary');
      // toggle panes
      document.querySelectorAll('.tab-pane').forEach(function(p){ p.hidden = true; });
      var pane = document.getElementById(target);
      if (pane) pane.hidden = false;
    });
  });
})();
