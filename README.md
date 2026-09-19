# Honeytreat Group website

Static multi-page site: index, about, services, work, csr, careers, contact.

## Editing
All page content, contact details, images and icons live in `build.py`.
Edit it, then run `python3 build.py` to regenerate the seven .html files, sitemap.xml and robots.txt.
Styles: `assets/css/styles.css`. Behaviour: `assets/js/main.js`.

## Before launch
1. `assets/js/main.js` → set `FORM_ENDPOINT` (e.g. a Formspree form URL). Until then the contact form opens the visitor's email app.
2. `build.py` → set `SOCIAL` profile URLs and confirm `SITE_URL`.
3. `build.py` → replace the Unsplash placeholder photos in `IMG` with real HTG project photos (or point the entries to files in `assets/img/`).
4. Confirm the job listings in `JOBS` are current.
