/* Honeytreat Group — shared behaviour */
(function () {
  'use strict';

  /* ---------- Form delivery ----------
     Paste a form endpoint (e.g. a Formspree URL) below to receive
     enquiries directly. While it is empty, the form opens the visitor's
     email app with the message pre-filled, addressed to CONTACT_EMAIL. */
  var FORM_ENDPOINT = '';
  var CONTACT_EMAIL = 'contact@honeytreatgrp.com';

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Header shadow ---------- */
  var header = $('.site-header');
  var onScroll = function () { if (header) header.classList.toggle('is-scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile navigation ---------- */
  var toggle = $('.nav-toggle');
  var drawer = $('#mobile-nav');
  function setNav(open) {
    if (!toggle || !drawer) return;
    drawer.classList.toggle('is-open', open);
    document.body.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    $('.i-open', toggle).style.display = open ? 'none' : '';
    $('.i-close', toggle).style.display = open ? '' : 'none';
    if (open) { drawer.removeAttribute('inert'); } else { drawer.setAttribute('inert', ''); }
  }
  if (toggle && drawer) {
    setNav(false);
    toggle.addEventListener('click', function () { setNav(toggle.getAttribute('aria-expanded') !== 'true'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setNav(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 1080) setNav(false); });
  }

  /* ---------- Footer year ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Work gallery: filter + lightbox ---------- */
  var gallery = $('#gallery');
  if (gallery) {
    var cards = $$('.work-card', gallery);
    var chips = $$('#work-filters .chip');
    var empty = $('#gallery-empty');
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var f = chip.dataset.filter;
        chips.forEach(function (c) { c.setAttribute('aria-pressed', String(c === chip)); });
        var shown = 0;
        cards.forEach(function (card) {
          var match = f === 'all' || card.dataset.sector === f;
          card.hidden = !match;
          if (match) shown++;
        });
        if (empty) empty.classList.toggle('show', shown === 0);
      });
    });

    var lb = $('#lightbox');
    var lbImg = $('img', lb);
    var lbCap = $('figcaption', lb);
    var current = 0;
    var visible = function () { return cards.filter(function (c) { return !c.hidden; }); };
    var lastFocus = null;
    function show(i) {
      var list = visible();
      if (!list.length) return;
      current = (i + list.length) % list.length;
      var card = list[current];
      var img = $('img', card);
      lbImg.src = img.dataset.full || img.src;
      lbImg.alt = img.alt;
      lbCap.textContent = $('h3', card).textContent;
    }
    function open(card) {
      lastFocus = document.activeElement;
      show(visible().indexOf(card));
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
      $('.lb-close', lb).focus();
    }
    function close() {
      lb.classList.remove('open');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    }
    cards.forEach(function (card) {
      $('button', card).addEventListener('click', function () { open(card); });
    });
    $('.lb-close', lb).addEventListener('click', close);
    $('.lb-prev', lb).addEventListener('click', function () { show(current - 1); });
    $('.lb-next', lb).addEventListener('click', function () { show(current + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(current - 1);
      if (e.key === 'ArrowRight') show(current + 1);
    });
  }

  /* ---------- Careers filters ---------- */
  var jobs = $('#jobs');
  if (jobs) {
    var typeSel = $('#job-type');
    var coSel = $('#job-company');
    var count = $('#job-count');
    var noJobs = $('#jobs-empty');
    var apply = function () {
      var t = typeSel.value, c = coSel.value, n = 0;
      $$('.job', jobs).forEach(function (job) {
        var ok = (t === 'all' || job.dataset.type === t) && (c === 'all' || job.dataset.company === c);
        job.hidden = !ok;
        if (ok) n++;
      });
      count.textContent = n === 1 ? '1 open role' : n + ' open roles';
      noJobs.classList.toggle('show', n === 0);
    };
    typeSel.addEventListener('change', apply);
    coSel.addEventListener('change', apply);
    apply();
  }

  /* ---------- Contact form ---------- */
  var form = $('#contact-form');
  if (form) {
    var params = new URLSearchParams(window.location.search);
    var enquiry = params.get('enquiry');
    var role = params.get('role');
    if (enquiry) {
      var sel = form.elements.enquiry;
      $$('option', sel).forEach(function (o) { if (o.dataset.key === enquiry) sel.value = o.value; });
    }
    if (role) {
      form.elements.message.value = 'I would like to apply for the ' + role + ' role. A short summary of my experience:\n\n';
    }

    var status = $('#form-status');
    var messages = {
      name: 'Enter your full name.',
      email: 'Enter an email address like name@company.com.',
      phone: 'Enter a phone number with at least 10 digits.',
      enquiry: 'Choose what your enquiry is about.',
      message: 'Add a short message so we can route it to the right team.'
    };
    function validate(el) {
      var field = el.closest('.field');
      if (!field) return true;
      var v = el.value.trim();
      var ok = true;
      if (el.required && !v) ok = false;
      if (ok && el.type === 'email' && v) ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
      if (ok && el.type === 'tel' && v) ok = v.replace(/\D/g, '').length >= 10;
      field.classList.toggle('invalid', !ok);
      var err = $('.err', field);
      if (err && messages[el.name]) err.textContent = messages[el.name];
      return ok;
    }
    $$('input, select, textarea', form).forEach(function (el) {
      el.addEventListener('blur', function () { validate(el); });
      el.addEventListener('input', function () { if (el.closest('.field.invalid')) validate(el); });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.className = 'form-status';
      var fields = $$('input:not(.hp), select, textarea', form);
      var firstBad = null;
      fields.forEach(function (el) { if (!validate(el) && !firstBad) firstBad = el; });
      if (firstBad) { firstBad.focus(); return; }
      if (form.elements._gotcha && form.elements._gotcha.value) return;

      var data = new FormData(form);
      var btn = $('button[type="submit"]', form);

      if (!FORM_ENDPOINT) {
        var body = 'Name: ' + data.get('name') + '\nEmail: ' + data.get('email') + '\nPhone: ' + data.get('phone') +
          '\nCompany: ' + (data.get('company') || '-') + '\nEnquiry: ' + data.get('enquiry') + '\n\n' + data.get('message');
        window.location.href = 'mailto:' + CONTACT_EMAIL + '?subject=' +
          encodeURIComponent('Website enquiry: ' + data.get('enquiry')) + '&body=' + encodeURIComponent(body);
        status.textContent = 'Your email app has opened with the message ready. Press send there to reach us.';
        status.classList.add('ok');
        return;
      }

      btn.disabled = true;
      var label = btn.querySelector('span').textContent;
      btn.querySelector('span').textContent = 'Sending…';
      fetch(FORM_ENDPOINT, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error('bad status');
          form.reset();
          status.textContent = 'Message sent. Our team will be in touch shortly.';
          status.classList.add('ok');
        })
        .catch(function () {
          status.textContent = 'Message not sent. Check your connection and try again, or email ' + CONTACT_EMAIL + '.';
          status.classList.add('fail');
        })
        .then(function () {
          btn.disabled = false;
          btn.querySelector('span').textContent = label;
        });
    });
  }
})();
