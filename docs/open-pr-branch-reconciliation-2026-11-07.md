# Open PR and Branch Reconciliation — 2026-11-07

## Scope and snapshot
GitHub organization/account search returned **46 open pull requests** across the 12-repository inventory at the time of this snapshot. This is a snapshot, not a complete lifetime PR count. A search result is not itself a review decision.

## Repeated PR families

### 1. YCI ownership-intent / CATBOT 100 discovery handoff
Matching review-only PRs:
- `claritymathpi-website#2`
- `stein-claritymathpi-website#2`
- `infofaqs-home#28`
- `trusted-links#3`
- `clarity#5`
- `infoFAQs#7`
- `chatgpt#5`
- `con.way.twit.t#17`
- `redx#15`
- `one.uni#2`
- `JON.ANON#4`

**Disposition:** Treat as a synchronized evidence/intent family, not 11 independent approvals. Compare each PR's changed files, branch head, and receipt. Retain one canonical source record and repository-specific pointers where needed. Do not close or merge copies until their unique content is reconciled. These are explicitly review-only; no release authorization is implied.

### 2. A YO!™ licensing notice
Matching draft PRs:
- `claritymathpi-website#1`
- `stein-claritymathpi-website#1`
- `infofaqs-home#23`
- `trusted-links#2`
- `clarity#4`
- `infoFAQs#6`
- `chatgpt#4`
- `con.way.twit.t#16`
- `redx#14`
- `one.uni#1`
- `JON.ANON#3`
- `Richard.Richard#56`

**Disposition:** One legal-text source of truth should be reviewed for scope, owner, mark usage, and rights evidence. Do not treat a repeated notice as proof of registration, ownership, or legal clearance. Preserve repository-specific attribution and licensing differences. Do not merge until counsel/owner-approved wording and rights evidence are established.

### 3. 1of1 Marketplace asset/layout family
- `clarity#2` — Asset-tab marketplace and QR layouts
- `Richard.Richard#54` — same titled marketplace and QR layout work
- `infoFAQs#8` — Meta Metal marketplace and QR/UPC collectible studio
- `chatgpt#3` — DROOT/DGEO/TikTokClock marketplace sync checkpoint

**Disposition:** Compare source files and artifact hashes to distinguish duplicated design assets from app-specific implementations and synchronization records. The two identically titled layout PRs are likely mirrors, but this must be confirmed by diff and head-commit comparison. Do not merge both blindly.

## InfoFAQs-specific open PR inventory
- `infofaqs-home#33` — repository maturity ledger (this audit branch; draft)
- `infofaqs-home#32` — Edition 2 release gates/checksum checklist (draft)
- `infofaqs-home#31` — ECHO copyright metadata (draft)
- `infofaqs-home#30` — Sacramento HVAC/Villara content (draft)
- `infofaqs-home#28` — ownership/CATBOT handoff (review only)
- `infofaqs-home#23` — A YO! notice (draft)
- `infofaqs-home#22` — InfoFx V2 separate-brand specification (review only/HOLD)
- `infofaqs-home#21` — Edition 1 five-card engine/release bundle
- `infofaqs-home#19` — under-construction landing page
- `infofaqs-home#12` — Meta Direct connection verification (HOLD)
- `infofaqs-home#11` — Instagram link (HOLD)
- `infofaqs-home#10` — public fan spotlight
- `infofaqs-home#6` — CATBOT email receipt preview
- `infofaqs-home#5` — CATBOT homepage cover
- `infofaqs-home#4` — alpha login/order preview
- `infofaqs-home#2` — QA1 marketplace prototype

**Disposition:** These PRs have different purposes and must not be collapsed into a single release. Review file changes, tests, merge base, and current relevance individually. Keep auth/payment previews distinct from production functionality. Preserve explicitly protected Edition 0 material.

## Other open PRs requiring individual treatment
- `infoFAQs#11` — restore public Writing Assistant route
- `infoFAQs#10` — preserve homepage bytes through Cloudflare (draft)
- `chatgpt#3` — marketplace synchronization checkpoint
- `clarity#1` — TXGE test.8 proposal and offline verification
- `redx#12` — PR team release gates/evidence review
- `Richard.Richard#48` — public frontend hub preview and REDx team sync

These are not duplicates merely because they mention release, marketplace, or evidence.

## Branch reconciliation snapshot
The `infofaqs-home` repository currently has a large set of long-lived branches, including `dev`, `staging`, `qa1`, `production1`, `main`, multiple `feature/*`, `fix/*`, `repair/*`, `release/*`, `review/*`, and record branches. The audit branch is separate and does not change `main`.

The `trusted-links`, `clarity`, and `infoFAQs` repositories also contain parallel record/release/review branches. Branch names alone cannot establish staleness. Each branch must be compared to its default branch for ahead/behind commits, unique file changes, and open-PR references before retirement.

## Decisions deliberately not taken
- No PR closed.
- No PR merged.
- No branch deleted or force-pushed.
- No default branch changed.
- No licensing or ownership assertion upgraded to approved.
- No production deployment or public release performed.

## Next reconciliation steps
1. Fetch diffs and head/base SHAs for every open PR, paginating beyond first-page results where applicable.
2. Compare the ownership-intent and licensing families byte-for-byte; identify canonical source and mirrors.
3. Compare `clarity#2` vs `Richard.Richard#54` and `infoFAQs#8` for overlap and unique deliverables.
4. For every long-lived branch, calculate ahead/behind and list unique commits/files.
5. Inspect workflow files and latest run status per repository; identify missing triggers and required checks.
6. Only then prepare explicit close/merge/retarget recommendations for review.

## Audit boundary
This report classifies PR families by title and scope. It does not claim complete diff-level deduplication, branch retirement readiness, or CI/security completion. Those remain unverified until exact PR diffs, commit comparisons, branch comparisons, workflow runs, and repository settings are examined.
