/* Honeytreat Group: motion
   1. Photos fade in once loaded (with a soft shimmer while loading)
   2. Sections and cards rise into view as you scroll
   3. Key numbers count up when they appear
   Content that is already on screen is never hidden, and everything stays
   still for visitors who have "reduce motion" switched on. */
(function () {
  "use strict";

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasIO = "IntersectionObserver" in window;

  /* ---------- 1. Image fade-in ---------- */
  document.querySelectorAll(".media img, .hex-img img, .work-card img").forEach(function (img) {
    if (img.complete && img.naturalWidth) return;
    img.classList.add("img-fade");
    img.addEventListener("load", function () {
      if (img.naturalWidth) img.classList.add("is-loaded");
    });
  });

  if (reduce || !hasIO) return;

  /* ---------- 2. Scroll reveal ---------- */
  var fold = window.innerHeight * 0.92;

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      io.unobserve(el);
      el.classList.add("is-in");
      var delay = parseInt(el.style.getPropertyValue("--reveal-delay"), 10) || 0;
      // Hand control back to the site's own hover transitions afterwards
      setTimeout(function () {
        el.classList.remove("reveal", "is-in");
        el.style.removeProperty("--reveal-delay");
      }, 900 + delay);
    });
  }, { rootMargin: "0px 0px -6% 0px", threshold: 0.06 });

  function prep(el, delay) {
    if (el.getBoundingClientRect().top < fold) return; // already visible: leave it alone
    el.classList.add("reveal");
    if (delay) el.style.setProperty("--reveal-delay", delay + "ms");
    io.observe(el);
  }

  document.querySelectorAll(
    ".section-head, .split > *, .form-card, .open-app, .cta-inner > *, .legal, .jobs-toolbar, .filters"
  ).forEach(function (el) { prep(el, 0); });

  document.querySelectorAll(
    ".sectors, .companies, .values, .gallery, .paths, .programs, .mv, .org-children, " +
    ".directory, .culture, .process, .timeline, .ways, .channels, .facts-grid"
  ).forEach(function (list) {
    Array.prototype.forEach.call(list.children, function (child, i) {
      prep(child, Math.min(i, 6) * 80);
    });
  });

  /* ---------- 3. Count-up numbers ---------- */
  function countUp(el) {
    var m = el.textContent.trim().match(/^([\d,]+)(\D*)$/);
    if (!m) return;
    var target = parseInt(m[1].replace(/,/g, ""), 10);
    var suffix = m[2];
    var isYear = !suffix && target >= 1900 && target <= 2100;
    if (isYear || target < 5) return;
    var final = el.textContent;
    var start = null;
    var duration = 1400;
    el.style.fontVariantNumeric = "tabular-nums";
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString("en-US") + suffix;
      if (p < 1) requestAnimationFrame(step);
      else el.textContent = final;
    }
    requestAnimationFrame(step);
  }

  var countIO = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      countIO.unobserve(entry.target);
      countUp(entry.target);
    });
  }, { threshold: 0.6 });

  document.querySelectorAll(".fact strong, .hex-badge strong").forEach(function (el) {
    countIO.observe(el);
  });
})();
