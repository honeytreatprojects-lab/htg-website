/* Honeytreat Group: careers in-page application form
   Intercepts "Apply" and "Send an open application" in #open-roles and opens #apply-dialog.
   If the browser lacks <dialog> support, the links still go to contact.html as before. */
(function () {
  "use strict";

  var dialog = document.getElementById("apply-dialog");
  if (!dialog || typeof dialog.showModal !== "function") return;

  var LINKEDIN_REQUIRED = true;          // set to false to make LinkedIn optional
  var MAX_BYTES = 5 * 1024 * 1024;       // 5 MB
  var ALLOWED_EXT = ["pdf", "doc", "docx"];
  var FALLBACK_EMAIL = "contact@honeytreatgrp.com";
  var COMPANIES = {
    htg: "Honeytreat Group",
    htl: "Honeytreat Limited",
    hgsl: "Honeytreat Global Services",
    hta: "Honeytreat Trade Academy"
  };

  function $(id) { return document.getElementById(id); }

  var form = $("apply-form");
  var success = $("apply-success");
  var statusEl = $("apply-status");
  var titleEl = $("apply-title");
  var roleLabel = $("apply-role-label");
  var fileInput = $("a-cv");
  var dropzone = fileInput.closest(".dropzone");
  var fileNameEl = dropzone.querySelector(".dz-file");
  var submitBtn = form.querySelector('button[type="submit"]');
  var submitText = submitBtn.querySelector("span");
  var lastTrigger = null;

  /* ---------- open / close ---------- */

  function openFor(trigger) {
    var role = new URL(trigger.href, location.href).searchParams.get("role") || "";
    var job = trigger.closest(".job");
    var company = job ? (COMPANIES[job.getAttribute("data-company")] || "") : "";

    resetForm();
    $("a-role").value = role || "Open application";
    $("a-company").value = company;
    $("a-subject").value = role ? "Job application: " + role : "Open application";
    titleEl.textContent = role ? "Apply for this role" : "Send an open application";
    roleLabel.textContent = role
      ? role + (company ? ", " + company : "")
      : "We keep strong profiles on file for future openings.";

    lastTrigger = trigger;
    dialog.showModal();
    document.documentElement.classList.add("apply-lock");
    $("a-name").focus();
  }

  document.addEventListener("click", function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var trigger = e.target.closest('#open-roles a[href*="enquiry=career"]');
    if (!trigger) return;
    e.preventDefault();
    openFor(trigger);
  });

  dialog.querySelectorAll("[data-apply-close]").forEach(function (btn) {
    btn.addEventListener("click", function () { dialog.close(); });
  });

  // Close on backdrop click (only when the press started on the backdrop)
  var pressedBackdrop = false;
  dialog.addEventListener("pointerdown", function (e) { pressedBackdrop = e.target === dialog; });
  dialog.addEventListener("click", function (e) {
    if (pressedBackdrop && e.target === dialog) dialog.close();
  });

  dialog.addEventListener("close", function () {
    document.documentElement.classList.remove("apply-lock");
    if (lastTrigger) lastTrigger.focus();
  });

  /* ---------- helpers ---------- */

  function setError(input, msg) {
    var field = input.closest(".field");
    var err = field && field.querySelector(".err");
    if (err) err.textContent = msg;
    if (msg) input.setAttribute("aria-invalid", "true");
    else input.removeAttribute("aria-invalid");
    if (input === fileInput) dropzone.classList.toggle("is-invalid", !!msg);
    return !msg;
  }

  function setStatus(msg, type) {
    statusEl.textContent = msg;
    statusEl.classList.remove("is-error", "is-success");
    if (type) statusEl.classList.add(type);
  }

  function setBusy(busy) {
    submitBtn.disabled = busy;
    form.setAttribute("aria-busy", busy ? "true" : "false");
    submitText.textContent = busy ? "Sending application…" : "Submit application";
  }

  function normaliseUrl(value) {
    var v = value.trim();
    if (!v) return "";
    if (!/^https?:\/\//i.test(v)) v = "https://" + v;
    return v.replace(/^http:\/\//i, "https://");
  }

  function formatSize(bytes) {
    return bytes < 1048576
      ? Math.max(1, Math.round(bytes / 1024)) + " KB"
      : (bytes / 1048576).toFixed(1) + " MB";
  }

  function fileError(file) {
    if (!file) return "Upload your CV to continue.";
    var ext = (file.name.split(".").pop() || "").toLowerCase();
    if (ALLOWED_EXT.indexOf(ext) === -1) return "Upload your CV as a PDF, DOC or DOCX file.";
    if (file.size > MAX_BYTES) return "This file is " + formatSize(file.size) + ". Upload a CV of 5 MB or less.";
    return "";
  }

  function resetForm() {
    form.reset();
    form.hidden = false;
    success.hidden = true;
    form.querySelectorAll("[aria-invalid]").forEach(function (el) { setError(el, ""); });
    fileNameEl.hidden = true;
    fileNameEl.textContent = "";
    dropzone.classList.remove("has-file", "is-drag", "is-invalid");
    setStatus("");
    setBusy(false);
  }

  /* ---------- CV upload ---------- */

  fileInput.addEventListener("change", function () {
    var file = fileInput.files[0];
    if (file) {
      fileNameEl.textContent = file.name + " (" + formatSize(file.size) + ")";
      fileNameEl.hidden = false;
      dropzone.classList.add("has-file");
      setError(fileInput, fileError(file));
    } else {
      fileNameEl.hidden = true;
      dropzone.classList.remove("has-file");
    }
  });

  ["dragenter", "dragover"].forEach(function (t) {
    fileInput.addEventListener(t, function () { dropzone.classList.add("is-drag"); });
  });
  ["dragleave", "drop"].forEach(function (t) {
    fileInput.addEventListener(t, function () { dropzone.classList.remove("is-drag"); });
  });

  // Clear a field's error as soon as the person edits it
  form.addEventListener("input", function (e) {
    if (e.target !== fileInput && e.target.getAttribute("aria-invalid")) setError(e.target, "");
  });

  /* ---------- validation ---------- */

  function validate() {
    var firstBad = null;
    function check(input, msg) {
      if (!setError(input, msg) && !firstBad) firstBad = input;
    }

    var name = $("a-name"), email = $("a-email"), phone = $("a-phone"),
        loc = $("a-location"), li = $("a-linkedin"), portfolio = $("a-portfolio"),
        consent = $("a-consent");

    check(name, name.value.trim().length < 2 ? "Enter your full name." : "");
    check(email, /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.value.trim()) ? "" : "Enter a valid email address, e.g. name@example.com.");
    check(phone, phone.value.replace(/\D/g, "").length >= 10 ? "" : "Enter a phone number with at least 10 digits.");
    check(loc, loc.value.trim() ? "" : "Enter the city or area you live in.");

    li.value = normaliseUrl(li.value);
    if (li.value || LINKEDIN_REQUIRED) {
      check(li, /^https:\/\/([a-z]{2,3}\.)?linkedin\.com\/(in|pub)\/[^\s/?#]+/i.test(li.value)
        ? "" : "Enter your LinkedIn profile link, e.g. https://www.linkedin.com/in/your-name");
    }

    portfolio.value = normaliseUrl(portfolio.value);
    check(fileInput, fileError(fileInput.files[0]));
    check(consent, consent.checked ? "" : "Tick this box to submit your application.");

    if (firstBad) firstBad.focus();
    return !firstBad;
  }

  /* ---------- submit ---------- */

  function showSuccess() {
    var first = $("a-name").value.trim().split(/\s+/)[0] || "";
    var role = $("a-role").value;
    $("apply-success-text").textContent =
      "Thank you" + (first ? ", " + first : "") + ". We've received your application" +
      (role && role !== "Open application" ? " for " + role : "") +
      ". Our team will review it and contact you by email if your profile is a match.";
    form.hidden = true;
    success.hidden = false;
    $("apply-success-title").focus();
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    setStatus("");

    if (!validate()) {
      setStatus("Some details need attention. Check the highlighted fields.", "is-error");
      return;
    }
    if ($("a-hp").value) { showSuccess(); return; } // bot trap

    if (/YOUR_FORM_ID/.test(form.getAttribute("action"))) {
      setStatus("Online applications are not connected yet. Email your CV to " + FALLBACK_EMAIL + ".", "is-error");
      return;
    }

    setBusy(true);
    fetch(form.getAttribute("action"), {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" }
    })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        showSuccess();
      })
      .catch(function () {
        setStatus("Your application was not sent. Check your connection and try again, or email your CV to " + FALLBACK_EMAIL + ".", "is-error");
      })
      .then(function () { setBusy(false); });
  });
})();
