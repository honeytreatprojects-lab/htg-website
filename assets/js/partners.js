/* Honeytreat Group: partner logo marquee
   Renders into every element with [data-partners] on any page.
   Edit the PARTNERS list once and every page updates.
   Logos live in assets/img/partners/. Leave logo as "" to show a text placeholder. */
(function () {
  "use strict";

  var BASE = "assets/img/partners/";

  var PARTNERS = [
    { name: "LSETF", note: "Lagos State Employment Trust Fund", logo: "lsetf.png" },
    { name: "NBTE", note: "National Board for Technical Education", logo: "nbte.png" },
    { name: "NIOB", note: "Nigerian Institute of Building", logo: "niob.png" },
    { name: "Ojodu LCDA", note: "Ojodu Local Council Development Area", logo: "ojodu-lcda.png" },
    { name: "Bosch", note: "", logo: "bosch.png" },
    { name: "Coca-Cola", note: "", logo: "coca-cola.png" },
    { name: "7UP", note: "", logo: "7up.png" },
    { name: "AOSH", note: "", logo: "aosh.png" },
    { name: "IshK Tolaram Foundation", note: "", logo: "ishk.png" },
    { name: "Elizabeth Jack-Rich Foundation", note: "", logo: "elizabeth-foundation.png" },
    { name: "Mantrac", note: "CAT dealer", logo: "logo-mantrac.png" },
    { name: "Honeytreat Trade Academy", note: "Group company", logo: "hta.png" }
  ];

  var mounts = document.querySelectorAll("[data-partners]");
  if (!mounts.length) return;

  function placeholder(p) {
    var box = document.createElement("span");
    box.className = "pm-fallback";
    box.textContent = p.name;
    if (p.note) {
      var small = document.createElement("small");
      small.textContent = p.note;
      box.appendChild(small);
    }
    return box;
  }

  function item(p, decorative) {
    var li = document.createElement("li");
    li.className = "pm-item";
    li.title = p.note ? p.name + ", " + p.note : p.name;

    if (!p.logo) {
      li.classList.add("is-placeholder");
      li.appendChild(placeholder(p));
      return li;
    }

    var img = document.createElement("img");
    img.alt = decorative ? "" : p.name + " logo";
    img.width = 160;
    img.height = 64;
    img.decoding = "async";
    img.addEventListener("error", function () {
      li.classList.add("is-placeholder");
      li.replaceChildren(placeholder(p));
    }, { once: true });
    img.src = BASE + p.logo;
    li.appendChild(img);
    return li;
  }

  function group(list, hidden) {
    var ul = document.createElement("ul");
    ul.className = "pm-group";
    if (hidden) ul.setAttribute("aria-hidden", "true");
    list.forEach(function (p) { ul.appendChild(item(p, hidden)); });
    return ul;
  }

  function row(list, reverse, hiddenRow) {
    var r = document.createElement("div");
    r.className = "pm-row" + (reverse ? " is-reverse" : "");
    if (hiddenRow) r.setAttribute("aria-hidden", "true");

    var track = document.createElement("div");
    track.className = "pm-track";
    track.style.setProperty("--pm-duration", Math.max(30, list.length * 4) + "s");
    // Two identical groups make the loop seamless (track moves exactly -50%)
    track.appendChild(group(list, hiddenRow));
    track.appendChild(group(list, true));

    r.appendChild(track);
    return r;
  }

  function build(mount) {
    if (mount.dataset.built) return;
    mount.dataset.built = "1";
    var rows = parseInt(mount.getAttribute("data-rows"), 10) || 2;
    mount.classList.add("partner-marquee");
    mount.appendChild(row(PARTNERS, false, false));
    if (rows > 1) mount.appendChild(row(PARTNERS.slice().reverse(), true, true));
  }

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) build(entry.target);
        entry.target.classList.toggle("is-offscreen", !entry.isIntersecting);
      });
    }, { rootMargin: "300px 0px" });
    mounts.forEach(function (m) { io.observe(m); });
  } else {
    mounts.forEach(build);
  }
})();
