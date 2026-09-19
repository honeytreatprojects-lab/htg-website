"""
Honeytreat Group website — static page builder.
Edit content here, run `python3 build.py`, and the seven .html pages are regenerated
with the same header, footer, icons and metadata.
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE_NAME = "Honeytreat Group"
SITE_URL = "https://honeytreatgrp.com"  # update if the live domain differs

PHONES = ["0805 186 6667", "0807 937 8912", "0805 873 4429"]
EMAILS = ["contact@honeytreatgrp.com", "honeytreatgroup@gmail.com"]
ADDRESS = "9A Bankole Street, Magodo Phase I, Lagos, Nigeria"

# Replace '#' with the real profile URLs before launch
SOCIAL = {"facebook": "#", "instagram": "#", "linkedin": "#"}

# Photography. These are stock placeholders — swap for real HTG project photos.
U = "https://images.unsplash.com/photo-{}?auto=format&fit=crop&w={}&q=80"
IMG = {
    "welding": "1504328345606-18bbc8c9d7d1",
    "site_team": "1504307651254-35680f356dfd",
    "industrial": "1581094794329-c8112a89af12",
    "building": "1486325212027-8081e485255e",
    "team": "1521737711867-e3b97375f902",
    "classroom": "1523240795612-9a054b0db644",
    "equipment": "1572120360610-d971b9d7767c",
    "training": "1524178232363-1fb2b075b655",
    "workshop": "1522202176988-66273c2fd55f",
}


def img(key, w=900):
    return U.format(IMG[key], w)


# ---------------------------------------------------------------- icons
ICONS = {
    "construction": ['<path d="M10 10V5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5"/>', '<path d="M14 6a6 6 0 0 1 6 6v3"/>', '<path d="M4 15v-3a6 6 0 0 1 6-6"/>', '<rect x="2" y="15" width="20" height="4" rx="1"/>'],
    "training": ['<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/>', '<path d="M22 10v6"/>', '<path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>'],
    "equipment": ['<path d="M12 12H5a2 2 0 0 0-2 2v5"/>', '<circle cx="13" cy="19" r="2"/>', '<circle cx="5" cy="19" r="2"/>', '<path d="M8 19h3m5-17v17h6M6 12V7c0-1.1.9-2 2-2h3l5 5"/>'],
    "realestate": ['<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/>', '<path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/>', '<path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/>', '<path d="M10 6h4"/>', '<path d="M10 10h4"/>', '<path d="M10 14h4"/>', '<path d="M10 18h4"/>'],
    "mining": ['<path d="M14.531 12.469 6.619 20.38a1 1 0 1 1-3-3l7.912-7.912"/>', '<path d="M15.686 4.314A12.5 12.5 0 0 0 5.461 2.958 1 1 0 0 0 5.58 4.71a22 22 0 0 1 6.318 3.393"/>', '<path d="M17.7 3.7a1 1 0 0 0-1.4 0l-4.6 4.6a1 1 0 0 0 0 1.4l2.6 2.6a1 1 0 0 0 1.4 0l4.6-4.6a1 1 0 0 0 0-1.4z"/>', '<path d="M19.686 8.314a12.501 12.501 0 0 1 1.356 10.225 1 1 0 0 1-1.751-.119 22 22 0 0 0-3.393-6.319"/>'],
    "energy": ['<path d="M3 22h12"/>', '<path d="M4 9h10"/>', '<path d="M14 22V4a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v18"/>', '<path d="M14 13h2a2 2 0 0 1 2 2v2a2 2 0 0 0 2 2a2 2 0 0 0 2-2V9.83a2 2 0 0 0-.59-1.42L18 5"/>'],
    "check": ['<path d="M20 6 9 17l-5-5"/>'],
    "check-circle": ['<circle cx="12" cy="12" r="10"/>', '<path d="m9 12 2 2 4-4"/>'],
    "arrow": ['<path d="M5 12h14"/>', '<path d="m12 5 7 7-7 7"/>'],
    "external": ['<path d="M15 3h6v6"/>', '<path d="M10 14 21 3"/>', '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>'],
    "phone": ['<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>'],
    "mail": ['<rect x="2" y="4" width="20" height="16" rx="2"/>', '<path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>'],
    "pin": ['<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/>', '<circle cx="12" cy="10" r="3"/>'],
    "clock": ['<circle cx="12" cy="12" r="10"/>', '<path d="M12 6v6l4 2"/>'],
    "target": ['<circle cx="12" cy="12" r="10"/>', '<circle cx="12" cy="12" r="6"/>', '<circle cx="12" cy="12" r="2"/>'],
    "eye": ['<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/>', '<circle cx="12" cy="12" r="3"/>'],
    "users": ['<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>', '<circle cx="9" cy="7" r="4"/>', '<path d="M22 21v-2a4 4 0 0 0-3-3.87"/>', '<path d="M16 3.13a4 4 0 0 1 0 7.75"/>'],
    "shield": ['<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>', '<path d="m9 12 2 2 4-4"/>'],
    "sun": ['<circle cx="12" cy="12" r="4"/>', '<path d="M12 2v2"/>', '<path d="M12 20v2"/>', '<path d="m4.93 4.93 1.41 1.41"/>', '<path d="m17.66 17.66 1.41 1.41"/>', '<path d="M2 12h2"/>', '<path d="M20 12h2"/>', '<path d="m6.34 17.66-1.41 1.41"/>', '<path d="m19.07 4.93-1.41 1.41"/>'],
    "heart": ['<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>'],
    "gem": ['<path d="M6 3h12l4 6-10 13L2 9Z"/>', '<path d="M11 3 8 9l4 13 4-13-3-6"/>', '<path d="M2 9h20"/>'],
    "briefcase": ['<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>', '<rect x="2" y="6" width="20" height="14" rx="2"/>'],
    "trending": ['<path d="M22 7 13.5 15.5 8.5 10.5 2 17"/>', '<path d="M16 7h6v6"/>'],
    "award": ['<path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"/>', '<circle cx="12" cy="8" r="6"/>'],
    "laptop": ['<path d="M20 16V7a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9m16 0H4m16 0 1.28 2.55a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45L4 16"/>'],
    "wrench": ['<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>'],
    "bulb": ['<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/>', '<path d="M9 18h6"/>', '<path d="M10 22h4"/>'],
    "leaf": ['<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/>', '<path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>'],
    "utensils": ['<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/>', '<path d="M7 2v20"/>', '<path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/>'],
    "book": ['<path d="M12 7v14"/>', '<path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>'],
    "home": ['<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/>', '<path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>'],
    "layers": ['<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/>', '<path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/>', '<path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>'],
    "globe": ['<circle cx="12" cy="12" r="10"/>', '<path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/>', '<path d="M2 12h20"/>'],
    "send": ['<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/>', '<path d="m21.854 2.147-10.94 10.939"/>'],
    "calendar": ['<rect x="3" y="4" width="18" height="18" rx="2"/>', '<path d="M16 2v4"/>', '<path d="M8 2v4"/>', '<path d="M3 10h18"/>'],
    "chevron": ['<path d="m6 9 6 6 6-6"/>'],
    "menu": ['<path d="M4 6h16"/>', '<path d="M4 12h16"/>', '<path d="M4 18h16"/>'],
    "close": ['<path d="M18 6 6 18"/>', '<path d="m6 6 12 12"/>'],
    "handcoins": ['<circle cx="8" cy="8" r="6"/>', '<path d="M18.09 10.37A6 6 0 1 1 10.34 18"/>', '<path d="M7 6h1v4"/>', '<path d="m16.71 13.88.7.71-2.82 2.82"/>'],
    "facebook": ['<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>'],
    "instagram": ['<rect x="2" y="2" width="20" height="20" rx="5"/>', '<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/>', '<path d="M17.5 6.5h.01"/>'],
    "linkedin": ['<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>', '<rect x="2" y="9" width="4" height="12"/>', '<circle cx="4" cy="4" r="2"/>'],
}


def icon(name, cls="icon", extra=""):
    return (f'<svg class="{cls}" {extra} viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
            + "".join(ICONS[name]) + "</svg>")


def hexi(name, variant=""):
    return f'<span class="hex-icon {variant}">{icon(name)}</span>'


ARROW = icon("arrow")

# ---------------------------------------------------------------- shared data
NAV = [
    ("index.html", "Home"),
    ("about.html", "About us"),
    ("services.html", "Services"),
    ("work.html", "Our work"),
    ("csr.html", "CSR"),
    ("careers.html", "Careers"),
]

SERVICES = [
    {"id": "construction", "icon": "construction", "title": "Construction & engineering", "by": "Honeytreat Limited",
     "short": "Residential, commercial and industrial structures built to specification, on schedule and to safety standard.",
     "long": ["We build strong, reliable structures for homes, businesses and industry. Every project is planned around quality, site safety and long-term performance, from groundwork to handover.",
              "Our engineers and site teams manage design coordination, procurement and supervision, so clients deal with one accountable team from start to finish."],
     "offer": ["Residential and commercial builds", "Industrial facilities", "Civil and structural works", "Project management and supervision", "Renovation and fit-out", "HSE-compliant site operations"],
     "img": "site_team"},
    {"id": "training", "icon": "training", "title": "Vocational training", "by": "Honeytreat Trade Academy",
     "short": "Hands-on trade programmes that prepare people for real jobs in construction and industry.",
     "long": ["Through Honeytreat Trade Academy, we train people in practical skills they can use from day one. Programmes combine workshop practice with site exposure, taught by working tradespeople.",
              "More than 7,000 professionals have trained with us, with certifications that employers across Nigeria recognise."],
     "offer": ["Welding and fabrication", "Tiling and finishing", "Electrical installation", "Plumbing and pipe fitting", "Equipment operation", "Corporate workforce upskilling"],
     "img": "training"},
    {"id": "leasing", "icon": "equipment", "title": "Equipment leasing", "by": "Honeytreat Global Services",
     "short": "Well-maintained heavy machinery for construction and industrial work, with operators available.",
     "long": ["We lease heavy-duty machines for construction, mining and industrial projects. Each unit is serviced on a fixed schedule and inspected before it leaves our yard.",
              "Flexible short- and long-term terms let contractors access the right equipment without the cost of ownership."],
     "offer": ["Earthmoving equipment", "Lifting and material handling", "Short- and long-term hire", "Certified operators on request", "Scheduled maintenance", "Delivery to site"],
     "img": "equipment"},
    {"id": "real-estate", "icon": "realestate", "title": "Real estate investment", "by": "Honeytreat Global Services",
     "short": "Property development and management that creates lasting value for investors and communities.",
     "long": ["We develop and manage residential and commercial property built to last. Our in-house construction capability gives investors tighter control of cost, quality and delivery time.",
              "From land acquisition to leasing and facility management, we look after the full life of each asset."],
     "offer": ["Residential developments", "Commercial property", "Land acquisition and titling support", "Property and facility management", "Investment advisory", "Joint-venture developments"],
     "img": "building"},
    {"id": "mining", "icon": "mining", "title": "Mining", "by": "Honeytreat Global Services",
     "short": "Resource exploration and extraction using modern equipment and responsible site practice.",
     "long": ["We carry out exploration and extraction with modern tools and trained crews. Operations follow strict safety procedures and environmental controls at every stage.",
              "Our equipment fleet and construction experience allow us to set up and run sites efficiently."],
     "offer": ["Exploration support", "Extraction operations", "Haulage and logistics", "Site preparation", "Safety and environmental compliance", "Equipment supply for mining"],
     "img": "industrial"},
    {"id": "cng", "icon": "energy", "title": "CNG energy", "by": "Honeytreat Global Services",
     "short": "Compressed natural gas supply that lowers fuel costs and cuts emissions for fleets and industry.",
     "long": ["We supply compressed natural gas as a cleaner, more affordable alternative to petrol and diesel. Businesses reduce running costs while lowering their environmental impact.",
              "We support fleet operators and industrial users with supply planning and conversion guidance."],
     "offer": ["CNG supply and distribution", "Fleet fuel programmes", "Industrial gas supply", "Conversion guidance", "Safety training", "Supply planning"],
     "img": "welding"},
]

COMPANIES = [
    {"abbr": "HTL", "name": "Honeytreat Limited", "desc": "The group's founding company, delivering construction and engineering projects since 2009.",
     "tags": ["Construction", "Engineering"], "href": "services.html#construction", "label": "View construction services", "ext": False},
    {"abbr": "HGSL", "name": "Honeytreat Global Services", "desc": "Equipment leasing, real estate, mining and CNG energy for industry and investors.",
     "tags": ["Equipment", "Real estate", "Mining", "CNG"], "href": "https://honeytreatglobal.com", "label": "Visit honeytreatglobal.com", "ext": True},
    {"abbr": "HTA", "name": "Honeytreat Trade Academy", "desc": "Vocational training that turns practical skills into careers in construction and industry.",
     "tags": ["Vocational training", "Certification"], "href": "https://honeytreatacademy.com", "label": "Visit honeytreatacademy.com", "ext": True},
]

PARTNERS = [("LSETF", "Lagos State Employment Trust Fund"), ("Mantrac", "CAT dealer"), ("Bosch", ""), ("NIOB", "Nigerian Institute of Building"),
            ("AOSH", ""), ("IshK Skills Hub", ""), ("Hybrid Edge", ""), ("OLAN", ""), ("GHTA", ""), ("Honeytreat Trade Academy", "Group company")]


# ---------------------------------------------------------------- layout
def head(title, desc, path):
    full = f"{title} | {SITE_NAME}" if path != "index.html" else f"{SITE_NAME} | Construction, training, real estate and energy in Nigeria"
    canonical = SITE_URL + "/" + ("" if path == "index.html" else path)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1E1A45">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/img/htg-logo-color.png">
<link rel="icon" type="image/png" href="assets/img/favicon-64.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def header(active):
    def cur(p):
        return ' aria-current="page"' if p == active else ""
    links = "".join(f'<a href="{p}"{cur(p)}>{t}</a>' for p, t in NAV)
    mlinks = "".join(f'<a class="m-link" href="{p}"{cur(p)}><span>{t}</span>{icon("arrow", "icon icon-sm")}</a>' for p, t in NAV)
    return f"""<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html" aria-label="Honeytreat Group home">
      <img src="assets/img/htg-logo-color.png" alt="Honeytreat Group" width="177" height="58">
    </a>
    <nav class="main-nav" aria-label="Main">{links}</nav>
    <a class="btn btn-primary header-cta" href="contact.html"{cur("contact.html")}>Contact us</a>
    <button class="nav-toggle" type="button" aria-controls="mobile-nav" aria-expanded="false" aria-label="Open menu">
      {icon("menu", "icon i-open")}{icon("close", "icon i-close", 'style="display:none"')}
    </button>
  </div>
</header>
<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
  {mlinks}
  <a class="m-link" href="contact.html"{cur("contact.html")}><span>Contact us</span>{icon("arrow", "icon icon-sm")}</a>
  <a class="btn btn-primary btn-block" href="tel:{PHONES[0].replace(' ', '')}">{icon("phone")}<span>Call {PHONES[0]}</span></a>
  <div class="m-contact"><a href="mailto:{EMAILS[0]}">{EMAILS[0]}</a><span>{ADDRESS}</span></div>
</nav>
"""


def footer():
    quick = "".join(f'<li><a href="{p}">{t}</a></li>' for p, t in NAV[1:]) + '<li><a href="contact.html">Contact us</a></li>'
    socials = "".join(f'<a href="{u}" aria-label="Honeytreat Group on {n.title()}" rel="noopener">{icon(n)}</a>' for n, u in SOCIAL.items())
    phones = "".join(f'<a href="tel:{p.replace(" ", "")}">{p}</a><br>' for p in PHONES)
    emails = "".join(f'<a href="mailto:{e}">{e}</a><br>' for e in EMAILS)
    return f"""<footer class="site-footer">
  <div class="container footer-top">
    <div class="footer-brand">
      <img src="assets/img/htg-logo-white.png" alt="Honeytreat Group" width="171" height="56">
      <p>A Lagos-based group delivering construction, training, equipment leasing, real estate, mining and CNG energy since 2009.</p>
      <div class="socials">{socials}</div>
    </div>
    <div class="footer-col">
      <h2>Company</h2>
      <ul>{quick}</ul>
    </div>
    <div class="footer-col">
      <h2>Group companies</h2>
      <ul>
        <li><a href="services.html#construction">Honeytreat Limited</a></li>
        <li><a href="https://honeytreatglobal.com" rel="noopener" target="_blank">Honeytreat Global Services</a></li>
        <li><a href="https://honeytreatacademy.com" rel="noopener" target="_blank">Honeytreat Trade Academy</a></li>
        <li><a href="csr.html">Samson Soyebi Foundation</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h2>Get in touch</h2>
      <ul class="footer-contact">
        <li>{icon("phone")}<span>{phones}</span></li>
        <li>{icon("mail")}<span>{emails}</span></li>
        <li>{icon("pin")}<span>{ADDRESS}</span></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <span>&copy; <span data-year>2026</span> Honeytreat Group. All rights reserved.</span>
      <span>Parent company of Honeytreat Limited, Honeytreat Global Services and Honeytreat Trade Academy.</span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def page_hero(title, lead, image_key, actions=""):
    return f"""<section class="page-hero">
  <div class="container page-hero-grid">
    <div class="hero-seq">
      <h1>{title}</h1>
      <p class="lead">{lead}</p>
      {f'<div class="btn-row">{actions}</div>' if actions else ''}
    </div>
    <div class="hex-media" aria-hidden="true">
      <div class="hex-outline"></div>
      <div class="hex-img"><img src="{img(image_key, 700)}" alt="" width="320" height="370"></div>
    </div>
  </div>
</section>
"""


def cta(title, text, primary=("Start a conversation", "contact.html"), secondary=None):
    sec = f'<a class="btn btn-ghost-light" href="{secondary[1]}">{secondary[0]}</a>' if secondary else ""
    return f"""<section class="cta-band">
  <div class="container cta-inner">
    <div><h2>{title}</h2><p>{text}</p></div>
    <div class="btn-row"><a class="btn btn-light" href="{primary[1]}"><span>{primary[0]}</span>{ARROW}</a>{sec}</div>
  </div>
</section>
"""


def partners_block(title="Trusted by clients and partners"):
    items = "".join(f'<div class="partner"><div>{n}{f"<small>{s}</small>" if s else ""}</div></div>' for n, s in PARTNERS)
    return f"""<section class="section">
  <div class="container">
    <div class="section-head stack"><h2 class="h2">{title}</h2>
    <p class="lead">Government agencies, manufacturers and professional bodies we work with across training, equipment and construction.</p></div>
    <div class="partners">{items}</div>
  </div>
</section>
"""


def companies_block():
    cards = ""
    for c in COMPANIES:
        tags = "".join(f"<li>{t}</li>" for t in c["tags"])
        ext = ' target="_blank" rel="noopener"' if c["ext"] else ""
        ic = icon("external") if c["ext"] else ARROW
        cards += f"""<article class="company">
      <span class="abbr">{c['abbr']}</span>
      <h3>{c['name']}</h3>
      <p>{c['desc']}</p>
      <ul>{tags}</ul>
      <a class="text-link" href="{c['href']}"{ext}>{c['label']}{ic}</a>
    </article>"""
    return cards


# ---------------------------------------------------------------- pages
def page_home():
    sectors = "".join(f"""<a class="sector" href="services.html#{s['id']}">
      {hexi(s['icon'])}
      <h3>{s['title']}</h3>
      <p>{s['short']}</p>
      <span class="text-link">Learn more{ARROW}</span>
    </a>""" for s in SERVICES)
    return head("Home", "Honeytreat Group is a Lagos-based multi-industry group delivering construction, vocational training, equipment leasing, real estate, mining and CNG energy since 2009.", "index.html") + header("index.html") + f"""<main id="main">
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-seq">
      <h1 class="display"><span>Building the future.</span> <span>Empowering people.</span></h1>
      <p class="lead">Honeytreat Group delivers construction, vocational training, equipment leasing, real estate, mining and CNG energy from one accountable group, helping businesses grow and communities thrive.</p>
      <div class="btn-row">
        <a class="btn btn-light" href="contact.html"><span>Partner with us</span>{ARROW}</a>
        <a class="btn btn-ghost-light" href="services.html">Explore our services</a>
      </div>
      <div class="hero-values" aria-label="Our values"><span>God</span><i></i><span>Humanity</span><i></i><span>Value</span></div>
    </div>
    <div class="hex-media">
      <div class="hex-outline" aria-hidden="true"></div>
      <div class="hex-img"><img src="{img('site_team', 1000)}" alt="Honeytreat construction team on site" width="520" height="600" fetchpriority="high"></div>
      <div class="hex-badge">{hexi('training', 'solid')}<div><strong>7,000+</strong><span>professionals trained through our academy</span></div></div>
    </div>
  </div>
</section>

<section class="facts" aria-label="Group at a glance">
  <div class="container facts-grid">
    <div class="fact"><strong>2009</strong><span>Founded as a construction company in Lagos</span></div>
    <div class="fact"><strong>7,000+</strong><span>Skilled professionals trained</span></div>
    <div class="fact"><strong>6</strong><span>Industry sectors served</span></div>
    <div class="fact"><strong>3</strong><span>Operating companies and one foundation</span></div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="mosaic">
      <div class="media ratio-3-4"><img src="{img('site_team', 700)}" alt="Construction crew reviewing plans" loading="lazy" width="350" height="467"></div>
      <div class="media ratio-1"><img src="{img('training', 500)}" alt="Trainees in a classroom session" loading="lazy" width="250" height="250"></div>
      <div class="media ratio-1"><img src="{img('building', 500)}" alt="Completed commercial building" loading="lazy" width="250" height="250"></div>
    </div>
    <div>
      <span class="kicker">Who we are</span>
      <h2 class="h2">We started with a simple goal: build quality projects people can trust.</h2>
      <div class="prose" style="margin-top:20px">
        <p>Today Honeytreat Group serves construction, training, energy, real estate and mining. We don't only deliver services. We create opportunities, support growth and build lasting value for the people and communities we work with.</p>
        <p>Every decision is guided by three values: God, Humanity and Value.</p>
      </div>
      <ul class="checks">
        <li>{icon('check-circle')}<span>Results you can measure, not promises</span></li>
        <li>{icon('check-circle')}<span>Six industries under one accountable group</span></li>
        <li>{icon('check-circle')}<span>Support for businesses and individuals alike</span></li>
      </ul>
      <div class="btn-row" style="margin-top:32px"><a class="btn btn-primary" href="about.html"><span>About the group</span>{ARROW}</a></div>
    </div>
  </div>
</section>

<section class="section section-mist">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker">What we do</span><h2 class="h2">Practical solutions across six industries</h2></div>
      <p class="lead">From the first foundation to the people who operate the equipment, our companies cover the full cycle of building and industry.</p>
    </div>
    <div class="sectors">{sectors}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker">Our companies</span><h2 class="h2">One group, three operating companies</h2></div>
      <p class="lead">Each company focuses on what it does best, backed by shared standards, people and resources.</p>
    </div>
    <div class="companies">{companies_block()}</div>
  </div>
</section>

<section class="section section-ink">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker on-dark">Our values</span><h2 class="h2">What guides every project</h2></div>
      <p class="lead">Three commitments shape how we work with clients, partners, staff and communities.</p>
    </div>
    <div class="values">
      <div class="value">{hexi('sun', 'on-ink')}<h3>God</h3><p>We operate with integrity and accountability in every contract and every relationship.</p></div>
      <div class="value">{hexi('users', 'on-ink')}<h3>Humanity</h3><p>We put people first: safe sites, fair opportunity and real support for our communities.</p></div>
      <div class="value">{hexi('gem', 'on-ink')}<h3>Value</h3><p>We deliver work that holds its worth long after handover, for clients and investors.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div>
      <span class="kicker">Our work</span>
      <h2 class="h2">Real projects. Real impact.</h2>
      <p class="lead" style="margin-top:18px">See our construction sites, training sessions and field operations, and the difference they make across Lagos and beyond.</p>
      <div class="btn-row" style="margin-top:32px"><a class="btn btn-primary" href="work.html"><span>View our work</span>{ARROW}</a></div>
    </div>
    <div class="mosaic">
      <div class="media ratio-3-4"><img src="{img('industrial', 700)}" alt="Industrial operations" loading="lazy" width="350" height="467"></div>
      <div class="media ratio-1"><img src="{img('equipment', 500)}" alt="Heavy equipment on site" loading="lazy" width="250" height="250"></div>
      <div class="media ratio-1"><img src="{img('welding', 500)}" alt="Welding and fabrication work" loading="lazy" width="250" height="250"></div>
    </div>
  </div>
</section>
""" + partners_block().replace('class="section"', 'class="section section-mist"', 1) + cta(
        "Have a project or idea? We're here to help.",
        "Tell us what you need and the right company in the group will get back to you.",
        secondary=("Explore careers", "careers.html")) + "</main>\n" + footer()


def page_about():
    return head("About us", "Learn how Honeytreat Group grew from a Lagos construction company founded in 2009 into a multi-industry group across training, real estate, mining and energy.", "about.html") + header("about.html") + '<main id="main">' + page_hero(
        "A multi-industry group built on trust",
        "Since 2009, Honeytreat Group has grown from a single construction company into a group serving construction, training, equipment, real estate, mining and energy.",
        "team") + f"""
<section class="section">
  <div class="container split top">
    <div>
      <span class="kicker">Our story</span>
      <h2 class="h2">From one construction company to a group that builds people as well as projects</h2>
      <div class="prose" style="margin-top:20px">
        <p>We started in 2009 as a construction company focused on quality and reliability. As we grew, we saw that the industry needed more skilled people, so we created a training academy.</p>
        <p>Over time we expanded into equipment leasing, real estate, mining and energy, building a group that serves different industries with one goal: growth and impact.</p>
        <p>Today Honeytreat Group is a trusted name across Nigeria's construction and industrial landscape, with companies that create value for businesses, individuals and communities.</p>
      </div>
    </div>
    <ol class="timeline" aria-label="Our history">
      <li><span class="year">2009</span><div class="body"><h3>Founded in Lagos</h3><p>Honeytreat begins as a construction company with a focus on quality and reliability.</p></div></li>
      <li><span class="year">Growth</span><div class="body"><h3>Training academy launched</h3><p>Honeytreat Trade Academy opens to close the skills gap in construction trades.</p></div></li>
      <li><span class="year">Expansion</span><div class="body"><h3>New sectors</h3><p>Honeytreat Global Services adds equipment leasing, real estate, mining and CNG energy.</p></div></li>
      <li><span class="year">Today</span><div class="body"><h3>A multi-industry group</h3><p>Three operating companies, a foundation and more than 7,000 professionals trained.</p></div></li>
    </ol>
  </div>
</section>

<section class="section section-mist">
  <div class="container">
    <div class="mv">
      <div class="mv-item">{hexi('target')}<h3>Our mission</h3><p>To empower communities and industries through innovative education, sustainable construction and comprehensive service solutions, fostering growth and excellence in every project we undertake.</p></div>
      <div class="mv-item">{hexi('eye')}<h3>Our vision</h3><p>To be a global leader in integrated services, driving progress and creating lasting value for our clients, employees and society across every sector we serve.</p></div>
    </div>
  </div>
</section>

<section class="section section-ink">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker on-dark">Our values</span><h2 class="h2">God. Humanity. Value.</h2></div>
      <p class="lead">These three pillars define who we are, how we operate and what we stand for in every project, partnership and community.</p>
    </div>
    <div class="values">
      <div class="value">{hexi('sun', 'on-ink')}<h3>God</h3><p>Integrity, honesty and accountability in how we do business.</p></div>
      <div class="value">{hexi('users', 'on-ink')}<h3>Humanity</h3><p>Safety, dignity and opportunity for our people and communities.</p></div>
      <div class="value">{hexi('gem', 'on-ink')}<h3>Value</h3><p>Quality that lasts and returns that matter to clients and investors.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker">Group structure</span><h2 class="h2">How the group is organised</h2></div>
      <p class="lead">Honeytreat Group is the parent company. Each subsidiary runs its own operations under shared standards and leadership.</p>
    </div>
    <div class="org">
      <div class="org-parent"><img src="assets/img/htg-logo-white.png" alt="Honeytreat Group" width="171" height="56" loading="lazy"></div>
      <div class="org-stem" aria-hidden="true"></div>
      <div class="org-children">
        <div class="org-node"><strong>Honeytreat Limited</strong><span>Construction and engineering</span></div>
        <div class="org-node"><strong>Honeytreat Global Services</strong><span>Equipment leasing, real estate, mining and CNG energy</span></div>
        <div class="org-node"><strong>Honeytreat Trade Academy</strong><span>Vocational training and certification</span></div>
        <div class="org-node"><strong>Samson Soyebi Foundation</strong><span>Corporate social responsibility</span></div>
      </div>
    </div>
  </div>
</section>

<section class="facts" aria-label="Group at a glance" style="border-top:1px solid var(--line)">
  <div class="container facts-grid">
    <div class="fact"><strong>16+</strong><span>Years of experience</span></div>
    <div class="fact"><strong>7,000+</strong><span>Skilled professionals trained</span></div>
    <div class="fact"><strong>6</strong><span>Industry sectors</span></div>
    <div class="fact"><strong>4</strong><span>Group entities</span></div>
  </div>
</section>
""" + partners_block("Partners who trust us") + cta(
        "Work with a group that delivers.",
        "Whether you need a building, a trained workforce or equipment on site, we can help.",
        secondary=("View our services", "services.html")) + "</main>\n" + footer()


def page_services():
    sub = "".join(f'<a href="#{s["id"]}">{icon(s["icon"])}{s["title"]}</a>' for s in SERVICES)
    blocks = ""
    for i, s in enumerate(SERVICES):
        offer = "".join(f"<li>{icon('check')}<span>{o}</span></li>" for o in s["offer"])
        prose = "".join(f"<p>{p}</p>" for p in s["long"])
        blocks += f"""<section class="section service-block{' flip' if i % 2 else ''}{' section-mist' if i % 2 else ''}" id="{s['id']}">
  <div class="container split">
    <div class="media ratio-4-3"><img src="{img(s['img'], 1000)}" alt="{s['title']}" loading="lazy" width="600" height="450"></div>
    <div>
      <div class="service-meta">{hexi(s['icon'], 'solid')}<small>Delivered by {s['by']}</small></div>
      <h2>{s['title']}</h2>
      <div class="prose">{prose}</div>
      <ul class="offer">{offer}</ul>
      <div class="btn-row"><a class="btn btn-primary" href="contact.html?enquiry={s['id']}"><span>Enquire about {s['title'].lower()}</span>{ARROW}</a></div>
    </div>
  </div>
</section>
"""
    return head("Services", "Construction and engineering, vocational training, equipment leasing, real estate investment, mining and CNG energy from Honeytreat Group.", "services.html") + header("services.html") + '<main id="main">' + page_hero(
        "Services built on experience and reliability",
        "Six specialist services, delivered by the companies of Honeytreat Group, with one standard of quality across all of them.",
        "industrial",
        f'<a class="btn btn-light" href="contact.html"><span>Discuss your project</span>{ARROW}</a>') + f"""
<nav class="subnav" aria-label="Services on this page"><div class="container subnav-inner">{sub}</div></nav>
{blocks}
<section class="section section-ink">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker on-dark">How we work</span><h2 class="h2">A clear process from first call to handover</h2></div>
      <p class="lead">The same four steps apply whether you're commissioning a building, training a team or leasing equipment.</p>
    </div>
    <ol class="process">
      <li><h3>Understand your needs</h3><p>We listen first, learning your goals, timeline and constraints before recommending anything.</p></li>
      <li><h3>Plan the right solution</h3><p>Our specialists design a tailored approach with the right team, tools and resources.</p></li>
      <li><h3>Execute with care</h3><p>Skilled teams deliver with precision and keep you informed at every stage.</p></li>
      <li><h3>Deliver lasting results</h3><p>We confirm the work meets your standard and stay available after handover.</p></li>
    </ol>
  </div>
</section>
""" + cta("Not sure which service fits?", "Describe your project and we'll connect you with the right team.") + "</main>\n" + footer()


WORK = [
    ("construction", "Construction", "Site team coordination", "site_team"),
    ("equipment", "Equipment", "Industrial equipment operations", "industrial"),
    ("training", "Training", "Classroom and theory sessions", "classroom"),
    ("realestate", "Real estate", "Commercial property development", "building"),
    ("energy", "Energy", "Fabrication for energy projects", "welding"),
    ("equipment", "Equipment", "Heavy equipment on site", "equipment"),
    ("training", "Training", "Skills development workshop", "training"),
    ("construction", "Construction", "Project planning with clients", "team"),
    ("training", "Training", "Group learning and mentorship", "workshop"),
]


def page_work():
    chips = [("all", "All work"), ("construction", "Construction"), ("training", "Training"), ("equipment", "Equipment"), ("realestate", "Real estate"), ("energy", "Energy")]
    chip_html = "".join(f'<button class="chip" type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{t}</button>' for k, t in chips)
    cards = "".join(f"""<article class="work-card" data-sector="{k}">
      <button type="button" aria-label="Enlarge: {title}"><img src="{img(ik, 700)}" data-full="{img(ik, 1600)}" alt="{title}" loading="lazy" width="400" height="300"></button>
      <div class="cap"><small>{label}</small><h3>{title}</h3></div>
    </article>""" for k, label, title, ik in WORK)
    return head("Our work", "Projects, training programmes and field operations delivered by Honeytreat Group across construction, equipment, real estate and energy.", "work.html") + header("work.html") + '<main id="main">' + page_hero(
        "Our work in action",
        "From construction sites to training rooms and field operations, our work shows our commitment to quality and impact.",
        "equipment") + f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <div><h2 class="h2">Project gallery</h2></div>
      <p class="lead">Filter by sector and select any image to view it larger.</p>
    </div>
    <div class="filters" id="work-filters" role="group" aria-label="Filter projects by sector">{chip_html}</div>
    <div class="gallery" id="gallery">{cards}</div>
    <p class="empty-state" id="gallery-empty">No projects in this sector yet. Choose another filter to keep browsing.</p>
  </div>
</section>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
  <button class="lb-btn lb-close" type="button" aria-label="Close viewer">{icon('close')}</button>
  <button class="lb-btn lb-prev" type="button" aria-label="Previous image">{ARROW}</button>
  <figure><img src="" alt=""><figcaption></figcaption></figure>
  <button class="lb-btn lb-next" type="button" aria-label="Next image">{ARROW}</button>
</div>
""" + partners_block("Clients and partners").replace('class="section"', 'class="section section-mist"', 1) + cta(
        "Want results like these on your project?", "Talk to our team about scope, timelines and budget.") + "</main>\n" + footer()


def page_csr():
    programs = [
        ("utensils", "Feed A Friend", "Food support for individuals and families facing hardship in our host communities."),
        ("book", "Student Scholarship Initiative", "Scholarships that help promising students from low-income families stay in school and complete their education."),
        ("home", "Orphanage & Elderly Homes Feeding", "Regular food and supplies for orphanages and homes for the elderly."),
        ("heart", "Catering for Widows", "Practical care and provisions for widows and their households."),
    ]
    prog = "".join(f'<article class="program">{hexi(i)}<div><h3>{t}</h3><p>{d}</p></div></article>' for i, t, d in programs)
    return head("Corporate social responsibility", "Through the Samson Soyebi Foundation, Honeytreat Group supports families, students, orphanages, elderly homes and widows across Nigeria.", "csr.html") + header("csr.html") + '<main id="main">' + page_hero(
        "Corporate social responsibility",
        "Through the Samson Soyebi Foundation, we turn business success into lasting support for the communities around us.",
        "workshop",
        f'<a class="btn btn-light" href="contact.html?enquiry=csr"><span>Partner with the foundation</span>{ARROW}</a>') + f"""
<section class="section">
  <div class="container split">
    <div class="media ratio-4-3"><img src="{img('classroom', 1000)}" alt="Students supported by the foundation" loading="lazy" width="600" height="450"></div>
    <div>
      <span class="kicker">Samson Soyebi Foundation</span>
      <h2 class="h2">Giving back to the communities that make us</h2>
      <div class="prose" style="margin-top:20px">
        <p>The Samson Soyebi Foundation is the corporate social responsibility arm of Honeytreat Group. It was set up to make sure our growth translates into real change for people who need it most.</p>
        <p>The foundation focuses on food security, education and care for vulnerable groups, working directly with families, schools and care homes.</p>
      </div>
      <ul class="checks">
        <li>{icon('check-circle')}<span>Direct support, delivered by our own teams and volunteers</span></li>
        <li>{icon('check-circle')}<span>Long-term programmes, not one-off events</span></li>
        <li>{icon('check-circle')}<span>Free trade skills through Honeytreat Trade Academy</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-mist">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker">Our programmes</span><h2 class="h2">Where the foundation focuses</h2></div>
      <p class="lead">Four ongoing programmes address everyday needs: food, education and care.</p>
    </div>
    <div class="programs">{prog}</div>
  </div>
</section>

<section class="section section-ink">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker on-dark">Get involved</span><h2 class="h2">Join us in making a difference</h2></div>
      <p class="lead">Volunteer, donate or partner with the foundation. Every form of support moves the work forward.</p>
    </div>
    <div class="ways">
      <div class="way">{hexi('users', 'on-ink')}<h3>Volunteer</h3><p>Give your time at outreach events, feeding programmes and mentoring sessions.</p><a class="text-link" href="contact.html?enquiry=csr">Offer your time{ARROW}</a></div>
      <div class="way">{hexi('handcoins', 'on-ink')}<h3>Donate</h3><p>Fund meals, scholarships and supplies for the people our programmes serve.</p><a class="text-link" href="contact.html?enquiry=csr">Make a donation{ARROW}</a></div>
      <div class="way">{hexi('briefcase', 'on-ink')}<h3>Partner</h3><p>Sponsor a programme or collaborate as an organisation on shared community goals.</p><a class="text-link" href="contact.html?enquiry=csr">Become a partner{ARROW}</a></div>
    </div>
  </div>
</section>
""" + cta("Help us reach more people.", "Contact us to support a programme or propose a partnership.", ("Contact the foundation", "contact.html?enquiry=csr")) + "</main>\n" + footer()


JOBS = [
    ("Site Engineer, Construction & Engineering", "full-time", "Full-time", "htl", "Honeytreat Limited", "Lagos"),
    ("Vocational Training Instructor (Welding & Fabrication)", "full-time", "Full-time", "hta", "Honeytreat Trade Academy", "Lagos"),
    ("Equipment Operations Supervisor", "contract", "Contract", "hgsl", "Honeytreat Global Services", "Lagos"),
    ("Business Development Executive", "full-time", "Full-time", "htg", "Honeytreat Group", "Lagos"),
    ("Graduate Intern, Finance & Administration", "internship", "Internship", "htg", "Honeytreat Group", "Lagos"),
    ("Trade Skills Training, 2026 cohort (tiling, electrical, plumbing)", "training", "Training", "hta", "Honeytreat Trade Academy", "Lagos"),
    ("Real Estate Sales Associate", "full-time", "Full-time", "hgsl", "Honeytreat Global Services", "Lagos"),
    ("HSE Officer, Construction Sites", "full-time", "Full-time", "htl", "Honeytreat Limited", "Lagos"),
    ("Digital Marketing & Communications Officer", "full-time", "Full-time", "htg", "Honeytreat Group", "Lagos (hybrid)"),
]


def page_careers():
    from urllib.parse import quote
    jobs = ""
    for title, tkey, tlabel, ckey, cname, loc in JOBS:
        enquiry = "training-enrol" if tkey == "training" else "career"
        action = "Enrol" if tkey == "training" else "Apply"
        jobs += f"""<li class="job" data-type="{tkey}" data-company="{ckey}">
      <div>
        <h3>{title}</h3>
        <div class="job-meta"><span class="tag t-{tkey}">{tlabel}</span><span>{icon('briefcase')}{cname}</span><span>{icon('pin')}{loc}</span></div>
      </div>
      <a class="btn btn-outline" href="contact.html?enquiry={enquiry}&amp;role={quote(title)}"><span>{action}</span>{ARROW}</a>
    </li>"""
    paths = [
        ("training", "Graduate trainee programme", "A structured one-year programme where graduates rotate across business units and build a career with the group.", "Recent graduates"),
        ("briefcase", "Internships", "Three- to six-month placements in construction, administration, HR, finance, marketing and technical teams.", "Students and recent graduates"),
        ("wrench", "Trade skills academy", "Certifications in welding, tiling, electrical, plumbing, painting and equipment operation through Honeytreat Trade Academy.", "Aspiring tradespeople"),
        ("trending", "Capacity development", "Technical upskilling, management training and professional certifications for current staff.", "Current employees"),
        ("award", "Leadership accelerator", "Executive mentorship and stretch assignments for high-potential employees preparing for senior roles.", "High-potential staff"),
        ("laptop", "Hybrid and remote roles", "Selected hybrid positions in administration, marketing, communications and technology.", "Experienced professionals"),
    ]
    path_html = "".join(f'<article class="path">{hexi(i)}<h3>{t}</h3><p>{d}</p><span class="who">For: {w}</span></article>' for i, t, d, w in paths)
    return head("Careers", "Explore jobs, internships, graduate programmes and trade training across Honeytreat Group's construction, training, equipment, real estate and energy companies.", "careers.html") + header("careers.html") + '<main id="main">' + page_hero(
        "Build your career where impact matters",
        "Join driven professionals building the future across construction, training, energy, real estate and more.",
        "workshop",
        f'<a class="btn btn-light" href="#open-roles"><span>View open roles</span>{icon("chevron")}</a>') + f"""
<section class="section">
  <div class="container split">
    <div>
      <span class="kicker">Why join us</span>
      <h2 class="h2">We invest in people as much as projects</h2>
      <div class="prose" style="margin-top:20px">
        <p>Whether you're starting out, changing direction or ready to lead, there's a path for you here. Six industries under one group means varied work and real room to progress.</p>
        <p>We back our people with continuous training, mentorship and a culture that values excellence, integrity and community.</p>
      </div>
    </div>
    <div class="media ratio-4-3"><img src="{img('team', 1000)}" alt="Honeytreat team collaborating" loading="lazy" width="600" height="450"></div>
  </div>
  <div class="container" style="margin-top:72px">
    <div class="culture">
      <div class="culture-item">{hexi('trending')}<h3>Room to grow</h3><p>Training, mentorship and promotion from within.</p></div>
      <div class="culture-item">{hexi('users')}<h3>One team</h3><p>We collaborate across departments and companies to get the best result.</p></div>
      <div class="culture-item">{hexi('bulb')}<h3>New ideas welcome</h3><p>Initiative is encouraged and rewarded at every level.</p></div>
      <div class="culture-item">{hexi('heart')}<h3>Community first</h3><p>Our work changes lives, and we hire people who care about that.</p></div>
    </div>
  </div>
</section>

<section class="section section-mist">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker">Development programmes</span><h2 class="h2">Pathways to growth</h2></div>
      <p class="lead">Entry points for talent at every stage, from students to experienced professionals.</p>
    </div>
    <div class="paths">{path_html}</div>
  </div>
</section>

<section class="section" id="open-roles" style="scroll-margin-top:var(--header-h)">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker">Open positions</span><h2 class="h2">Current opportunities</h2></div>
      <p class="lead">Select a role to apply. We'll ask for a short summary and follow up by email.</p>
    </div>
    <div class="jobs-toolbar">
      <strong id="job-count" aria-live="polite">{len(JOBS)} open roles</strong>
      <div class="btn-row" style="gap:10px">
        <label class="select-wrap"><span class="sr-only">Role type</span>
          <select id="job-type"><option value="all">All role types</option><option value="full-time">Full-time</option><option value="contract">Contract</option><option value="internship">Internship</option><option value="training">Training</option></select>{icon('chevron')}
        </label>
        <label class="select-wrap"><span class="sr-only">Company</span>
          <select id="job-company"><option value="all">All companies</option><option value="htg">Honeytreat Group</option><option value="htl">Honeytreat Limited</option><option value="hgsl">Honeytreat Global Services</option><option value="hta">Honeytreat Trade Academy</option></select>{icon('chevron')}
        </label>
      </div>
    </div>
    <ul class="jobs" id="jobs">{jobs}</ul>
    <p class="empty-state" id="jobs-empty" style="margin-top:24px">No roles match these filters. Change a filter or send an open application below.</p>
    <div class="open-app">
      <div><h3>Don't see your role?</h3><p>Send your CV and a short cover note. We keep strong profiles on file for future openings.</p></div>
      <a class="btn btn-primary" href="contact.html?enquiry=career"><span>Send an open application</span>{ARROW}</a>
    </div>
  </div>
</section>
</main>
""" + footer()


def page_contact():
    options = [
        ("construction", "Construction & engineering project"), ("training", "Vocational training"), ("training-enrol", "Training enrolment"),
        ("leasing", "Equipment leasing"), ("real-estate", "Real estate investment"), ("mining", "Mining services"),
        ("cng", "CNG energy"), ("partnership", "Partnership"), ("csr", "Samson Soyebi Foundation (CSR)"),
        ("career", "Careers and job applications"), ("general", "General enquiry"),
    ]
    opt = "".join(f'<option data-key="{k}" value="{t}">{t}</option>' for k, t in options)
    phones = "".join(f'<a href="tel:{p.replace(" ", "")}">{p}</a>' for p in PHONES)
    emails = "".join(f'<a href="mailto:{e}">{e}</a>' for e in EMAILS)
    map_q = "9A+Bankole+Street,+Magodo+Phase+1,+Lagos"
    return head("Contact us", "Contact Honeytreat Group in Magodo, Lagos by phone, email or our enquiry form for construction, training, equipment, real estate, mining and CNG.", "contact.html") + header("contact.html") + '<main id="main">' + page_hero(
        "Have a project or idea? We're here to help.",
        "Reach out about a project, partnership, training or career, and we'll route your message to the right team.",
        "team") + f"""
<section class="section">
  <div class="container contact-grid">
    <div>
      <h2 class="h2" style="font-size:1.8rem;margin-bottom:32px">Get in touch</h2>
      <div class="channels">
        <div class="channel">{hexi('phone')}<div><h3>Call us</h3>{phones}</div></div>
        <div class="channel">{hexi('mail')}<div><h3>Email us</h3>{emails}</div></div>
        <div class="channel">{hexi('pin')}<div><h3>Visit us</h3><p>{ADDRESS}</p></div></div>
      </div>
    </div>

    <div class="form-card">
      <h2>Send us a message</h2>
      <p>Tell us what you need and we will route your message to the right team.</p>
      <form id="contact-form" novalidate>
        <div class="form-grid">
          <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" type="text" autocomplete="name" required><span class="err"></span></div>
          <div class="field"><label for="f-phone">Phone number</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" placeholder="+234" required><span class="err"></span></div>
          <div class="field"><label for="f-email">Email address</label><input id="f-email" name="email" type="email" autocomplete="email" required><span class="err"></span></div>
          <div class="field"><label for="f-company">Company <span class="opt">(optional)</span></label><input id="f-company" name="company" type="text" autocomplete="organization"></div>
          <div class="field full"><label for="f-enquiry">What is your enquiry about?</label>
            <div class="select-wrap"><select id="f-enquiry" name="enquiry" required style="width:100%;padding:13px 40px 13px 14px;font-weight:500;font-size:1rem"><option value="">Choose a topic</option>{opt}</select>{icon('chevron')}</div>
            <span class="err"></span></div>
          <div class="field full"><label for="f-message">Message</label><textarea id="f-message" name="message" required placeholder="Tell us about your project, timeline or question"></textarea><span class="err"></span></div>
          <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
        </div>
        <div class="form-foot">
          <button class="btn btn-primary btn-block" type="submit"><span>Send message</span>{icon('send')}</button>
          <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
          <p class="form-note">We only use your details to respond to this enquiry.</p>
        </div>
      </form>
    </div>
  </div>
</section>

<section class="section section-mist">
  <div class="container">
    <div class="section-head">
      <div><h2 class="h2">Find our office</h2></div>
      <p class="lead">{ADDRESS}</p>
    </div>
    <div class="map"><iframe title="Map showing Honeytreat Group office in Magodo, Lagos" src="https://www.google.com/maps?q={map_q}&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head stack"><h2 class="h2">Group directory</h2><p class="lead">Contact a company directly for service-specific enquiries.</p></div>
    <div class="directory">
      <div class="dir-item">{hexi('construction')}<strong>Honeytreat Limited</strong><span>Construction and engineering</span><a class="text-link" href="services.html#construction">Services{ARROW}</a></div>
      <div class="dir-item">{hexi('layers')}<strong>Honeytreat Global Services</strong><span>Equipment, real estate, mining, CNG</span><a class="text-link" href="https://honeytreatglobal.com" target="_blank" rel="noopener">Website{icon('external')}</a></div>
      <div class="dir-item">{hexi('training')}<strong>Honeytreat Trade Academy</strong><span>Vocational training</span><a class="text-link" href="https://honeytreatacademy.com" target="_blank" rel="noopener">Website{icon('external')}</a></div>
      <div class="dir-item">{hexi('heart')}<strong>Samson Soyebi Foundation</strong><span>Corporate social responsibility</span><a class="text-link" href="csr.html">Programmes{ARROW}</a></div>
    </div>
  </div>
</section>
</main>
""" + footer()


PAGES = {
    "index.html": page_home, "about.html": page_about, "services.html": page_services,
    "work.html": page_work, "csr.html": page_csr, "careers.html": page_careers, "contact.html": page_contact,
}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        (ROOT / name).write_text(fn(), encoding="utf-8")
        print("built", name)
    # sitemap + robots
    urls = "".join(f"<url><loc>{SITE_URL}/{'' if n == 'index.html' else n}</loc></url>" for n in PAGES)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
