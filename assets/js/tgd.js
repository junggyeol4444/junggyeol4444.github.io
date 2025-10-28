
(function() {
  // Activate current nav link
  var here = window.location.pathname.replace(/\/$/, '');
  document.querySelectorAll('.tgd-nav a').forEach(function(a) {
    var href = a.getAttribute('href');
    if (!href) return;
    var u = href.replace(/\/$/, '');
    if (u && (here === u || here.startsWith(u))) {
      a.classList.add('active');
    }
  });

  // Mobile: simple sidebar toggle (opt-in if button exists)
  var btn = document.querySelector('[data-toggle="sidebar"]');
  var sidebar = document.querySelector('.tgd-sidebar');
  if (btn && sidebar) {
    btn.addEventListener('click', function() {
      sidebar.style.display = (getComputedStyle(sidebar).display === 'none') ? 'block' : 'none';
    });
  }
})();
