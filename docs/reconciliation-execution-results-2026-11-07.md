# Reconciliation execution results — 2026-11-07

## Exact duplicate confirmation: ownership/CATBOT handoff
Diffs fetched for:
- `claritymathpi-website#2`
- `stein-claritymathpi-website#2`
- `infofaqs-home#28`
- `trusted-links#3`
- `clarity#5`

All five returned the same 2,320-character unified diff (35 added lines) with identical text, same referenced public issue, same ZIP size and SHA-256, same JPEG hashes, same stated limitations, and same Edition 0 HOLD. This confirms these five are byte-identical PR content at diff level. Other PRs in the family still require diff retrieval before classifying as exact duplicates.

**Disposition:** Five confirmed mirrors of one record. Do not merge all five as separate substantive deliverables. Retain the canonical public evidence reference and repository-specific preservation copies where required. Any closure should occur only after confirming whether the user's explicit multi-repository preservation instruction requires the copies to remain open or whether merged copies are desired.

## Licensing notice comparison
Diffs fetched for:
- `claritymathpi-website#1`
- `stein-claritymathpi-website#1`
- `infofaqs-home#23`
- `trusted-links#2`
- `clarity#4`

Two content variants were found:
- Variant A: `claritymathpi-website#1`, `infofaqs-home#23`, `clarity#4` (1,029-character diff): detailed notice, fair-use carveout, no executed license, CATBOT binder/Edition 0 status.
- Variant B: `stein-claritymathpi-website#1`, `trusted-links#2` (798-character diff): shorter notice, same basic non-registration/non-license disclaimer, different wording.

**Disposition:** Not exact duplicates. Both are drafts and neither establishes registration, title, assignment, or authority. Keep unmerged pending one owner-approved canonical wording and legal-entity/rights verification. Do not silently replace one with the other.

## Marketplace layout PR comparison
- `clarity#2` and `Richard.Richard#54` returned identical opening diff content and the same 29 KB-class page implementation; these are strong duplicate candidates. Full binary assets and complete diff equality have not been verified.
- `infoFAQs#8` is a different implementation: changes GitHub Pages workflow to copy `marketplace/index.html`, `marketplace/collectible-studio/index.html`, CSS/JS/SVG assets, updates homepage navigation to `/marketplace/`, and changes expected artifact file count. It is not the same PR as the standalone 1of1 page/layout.
- `infoFAQs#11` is a separate Writing Assistant route restoration, including Pages allowlist and sitemap updates. It is not a Marketplace duplicate.
- `infoFAQs#10` is a homepage-byte preservation change and does not constitute the Marketplace implementation.

## Branch divergence comparisons
GitHub compare results against each repository's `main`:

| Repository / branch | Ahead | Behind | Status | Files in comparison |
|---|---:|---:|---|---:|
| `infofaqs-home:review/edition-2-release-plan-2026` | 3 | 0 | ahead | 2 |
| `infofaqs-home:feature/cube-controls-20261027` | 6 | 25 | diverged | 4 |
| `infoFAQs:feature/marketplace-collectible-studio-20261106` | 1 | 23 | diverged | 8 |
| `infoFAQs:fix/gate5-homepage-byte-integrity` | 1 | 16 | diverged | 1 |
| `clarity:review/1of1-marketplace-assets-20261101` | 1 | 7 | diverged | 17 |

**Disposition:** No branch is deleted. The Edition 2 branch is a small forward-only candidate for review. The other four are materially behind and diverged; cherry-pick/rebase decisions require inspecting the unique commits and file contents, not simply merging the branch. The marketplace collectible branch contains a distinct multi-file route and workflow change; it needs test/review against the current base before integration.

## Workflow evidence
A PR-triggered workflow-run query for current `infofaqs-home:main` commit `fb3831ec169200ea2513e39da73e55da9a46b681` returned an empty list. This means no PR-triggered runs were returned by that endpoint; it does **not** prove that no push, Pages, or other workflow runs exist. Complete Actions run history and repository security settings remain NOT AUDITED.

## Actions completed in this pass
- Compared five ownership/CATBOT PR diffs and confirmed exact textual identity.
- Compared five licensing notice PR diffs and identified two variants.
- Compared Marketplace PR implementations and separated standalone design from Pages route implementation.
- Compared five selected long-lived branches against main and recorded ahead/behind counts.
- Queried PR-triggered workflow runs for the current InfoFAQs main commit; none returned.

## Actions intentionally not taken
No PRs were merged or closed. No branch was deleted, rebased, or force-pushed. No workflow was re-run. No deployment, DNS, payment, licensing, or visibility setting was changed.

## Remaining
- Fetch diffs for remaining six ownership/CATBOT family PRs and seven licensing family PRs.
- Compare all 46 open PRs, including current head/base SHA and review/check state.
- Compare every branch across all 12 repositories, not only the five selected samples above.
- Enumerate workflows from repository trees and inspect run history via supported Actions endpoints.
- Audit dependency manifests, lockfiles, security alerts, secret-scanning status, and branch protection where permissions allow.
