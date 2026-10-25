"""Offline QA checks for the public-safe marketplace preview.
Run: python3 -m unittest discover -s tests -v
No network, credentials, or production services required.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "marketplace-preview.html"

class MarketplacePreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = PAGE.read_text(encoding="utf-8")

    def test_accessible_landmarks(self):
        for tag in ("<main>", "<header>", "<footer>", 'aria-label="Main navigation"', 'aria-live="polite"'):
            with self.subTest(tag=tag):
                self.assertIn(tag, self.page)

    def test_demo_cart_has_clear_and_save_controls(self):
        self.assertIn('id="clear"', self.page)
        self.assertGreaterEqual(self.page.count('data-item='), 3)
        self.assertIn('items.length=0', self.page)
        self.assertIn("list.replaceChildren()", self.page)

    def test_no_live_commerce_or_registration(self):
        self.assertIn('disabled>Sign up', self.page)
        self.assertIn('Prototype only.', self.page)
        self.assertNotRegex(self.page, r'(?i)stripe\.com|paypal\.com|checkout\.sessions|/api/(pay|order|signup)')

    def test_no_private_network_calls(self):
        self.assertNotRegex(self.page, r'\bfetch\s*\(|\bXMLHttpRequest\b|\blocalStorage\b|\bsessionStorage\b')
        self.assertNotRegex(self.page, r'<script[^>]+src=')

    def test_no_false_security_claim(self):
        self.assertIn('enforced on the server', self.page)
        self.assertIn('no owner login', self.page)
        self.assertIn('0 HOLD', self.page)
        self.assertIn('noindex,nofollow', self.page)

    def test_no_sensitive_literals(self):
        self.assertNotRegex(self.page, r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')
        self.assertNotRegex(self.page, r'(?i)(?:api[_-]?key|secret[_-]?key|password)\s*[:=]\s*["\'][^"\']{8,}')

if __name__ == "__main__":
    unittest.main()
