#!/usr/bin/env python3
"""Offline, stdlib-only validation for public Edition 1 artifacts."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
import sys

root = Path(__file__).resolve().parents[1]
errors = []
def check(condition, message):
    if not condition:
        errors.append(message)

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
        self.titles = []
        self.links = []
        self.in_title = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href"))
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "title":
            self.in_title = True
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
    def handle_data(self, data):
        if self.in_title:
            self.titles.append(data.strip())

home = root / "index.html"
check(home.is_file(), "index.html missing")
if home.is_file():
    parser = Page()
    parser.feed(home.read_text(encoding="utf-8"))
    check(bool("".join(parser.titles).strip()), "Homepage title missing")
    if parser.canonicals:
        check(parser.canonicals == ["https://infofaqs.com/"], "Unexpected canonical homepage URL")
    for href in parser.links:
        if href.startswith(("mailto:", "tel:", "#", "https://", "http://", "//", "javascript:")):
            if href.startswith("javascript:"):
                errors.append("Unsafe javascript: link in homepage")
            continue
        local = href.split("?", 1)[0].split("#", 1)[0].lstrip("/")
        if local:
            check((root / local).exists(), f"Broken local homepage link: {href}")

robots = root / "robots.txt"
check(robots.is_file(), "robots.txt missing")
if robots.is_file():
    check("Sitemap: https://infofaqs.com/sitemap.xml" in robots.read_text(encoding="utf-8"), "Missing canonical sitemap declaration")

sitemap = root / "sitemap.xml"
check(sitemap.is_file(), "sitemap.xml missing")
if sitemap.is_file():
    try:
        tree = ET.parse(sitemap)
        ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
        check(tree.getroot().tag == ns + "urlset", "Invalid sitemap root")
        urls = [node.text for node in tree.findall(".//" + ns + "loc")]
        check("https://infofaqs.com/" in urls, "Canonical homepage absent from sitemap")
        check(all(url and urlparse(url).scheme == "https" and urlparse(url).netloc == "infofaqs.com" for url in urls), "Noncanonical or insecure sitemap URL")
        for url in urls:
            path = urlparse(url).path.lstrip("/")
            if path:
                check((root / path).is_file(), f"Sitemap path missing: {path}")
    except ET.ParseError as exc:
        errors.append(f"Sitemap XML invalid: {exc}")

if errors:
    print("FAIL:\n" + "\n".join("- " + e for e in errors))
    sys.exit(1)
print("PASS: local Edition 1 static checks; live DNS/TLS and browser checks remain separate.")
