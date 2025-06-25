# InfoFAQs Repository Overview

This repository contains the core components of the InfoFAQs system, split across development, staging, and production-ready main branches.

---

## 🚧 InfoFAQs – Dev Branch

This is the staging and testbed environment for upcoming features and changes.

### ⚙️ Use Cases
- Inject or revise FAQs
- Test GPT fusion logic
- Build experimental UI components

### 📁 Suggested Files
- `index_dev.html`
- `gpt_fusion_tool.py`
- `autoload_infofaqs.patch`
- `/drafts` folder for test content

> Always test here before merging to `main`.

---

## 🌐 InfoFAQs – Main Branch

This is the public-facing deployment of the InfoFAQs system.

### 📁 Files Included
- `index.html`: Main landing page
- `echo_mining_dashboard.html`: Interactive FAQ viewer
- `updated_infofaqs_echo_mining.json`: Public FAQ database
- `echo_mining_faq.md`: Markdown export
- `netlify.toml` / `vercel.json`: Deployment configs
- `.nojekyll`, `CNAME`: GitHub Pages support and custom domain

### 🌐 Live URL
Deployed at: https://infofaqs.com

> Do not modify this branch directly. Use `dev` for edits and pull requests.
