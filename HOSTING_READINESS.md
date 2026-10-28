# InfoFAQs hosting repair readiness

Status: repository repair prepared; live DNS, HTTPS and redirects are not certified fixed.

## Intended hostname

Use https://infofaqs.com/ as the canonical homepage. The added root CNAME
contains only infofaqs.com and prepares the GitHub Pages publishing source
for that custom domain. A CNAME file alone does not verify the account's
Pages custom-domain setting, configure Cloudflare, issue a certificate,
or repair the live site.

## Existing evidence

Read-only inspection completed 2026-10-28 at approximately 05:12 UTC.

- Base main commit: efae480cbc3d5f0eedca08436adcf6f50baf89c5.
- GitHub Pages run 40579684018 reported successful build and deployment of that commit.
- Its deployment log reported https://eternalimit.github.io/infofaqs-home/ as the environment URL.
- The GitHub Pages URL displayed the current main homepage, including 10 FAQs.
- https://infofaqs.com/ displayed different content: CATBOT 100 and the Human Green Button.
- Apex A records: 104.21.89.13 and 172.67.155.130.
- Apex AAAA records: 2606:4700:3035::6815:590d and 2606:4700:3030::ac43:9b82.
- Authoritative nameservers: maria.ns.cloudflare.com and yoxall.ns.cloudflare.com.
- www.infofaqs.com CNAME: eternalimit.github.io; its A and AAAA answers resolved to GitHub Pages.
- The www HTTPS request and one reload failed in the available browser with an upstream connection error.
  This is a client-path observation, not proof of a particular certificate or origin failure.
- Browser navigation from each HTTP URL ended at its matching HTTPS URL.
  Response codes, redirect hops and browser upgrades were not independently distinguished.
- Apex CAA lookup returned NOERROR without a CAA answer.
- Actual certificate issuer, SANs, expiry, chain and TLS versions were not inspected.
- Instagram's actual iOS and Android in-app browsers were not tested.

The original README and historical release notes list files that were absent from
the inspected main tree: CNAME, .nojekyll, netlify.toml and vercel.json.
Those documents and every pre-existing file are preserved unchanged by this repair.

Sources:
- https://github.com/eternalimit/infofaqs-home/commit/efae480cbc3d5f0eedca08436adcf6f50baf89c5
- https://github.com/eternalimit/infofaqs-home/actions/runs/40579684018
- https://eternalimit.github.io/infofaqs-home/
- https://infofaqs.com/
- https://dns.google/query?name=infofaqs.com&type=A
- https://dns.google/query?name=www.infofaqs.com&rr_type=CNAME&ecs=

## Hosting steps requiring a separate production change

1. Inspect and record GitHub Settings > Pages publishing source, custom domain,
   DNS check, certificate provisioning and Enforce HTTPS state.
2. Inspect and record Cloudflare DNS proxy state, apex origin/Worker/Pages route,
   SSL/TLS mode, edge certificate coverage, redirect rules and cache rules.
   Public Cloudflare IPs do not reveal the configured origin.
3. Resolve which content is intended for production before switching the apex route.
   The repository's current homepage does not include the custom domain's CATBOT
   and Human Green Button additions; do not overwrite either version blindly.
4. If GitHub Pages is the chosen origin, bind infofaqs.com to this repository in
   Pages settings. Confirm www is associated with the same site.
   The published branch must retain the root CNAME.
5. For a direct GitHub Pages apex, GitHub documents A records
   185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153.
   Its optional AAAA records are 2606:50c0:8000::153 through
   2606:50c0:8003::153. Keep www CNAME pointed directly to eternalimit.github.io.
   These are conditional target records, not a recommendation to replace the
   observed Cloudflare addresses before the origin and intended content are known.
6. If Cloudflare stays in front, confirm the actual origin and hostname routing.
   Use a valid origin certificate and Full (strict) TLS where applicable.
   Ensure every public HTTPS endpoint has a trusted certificate covering its
   requested hostname before attempting any hostname redirect.
7. After both hosts have working HTTPS, use permanent redirects to the canonical
   HTTPS apex, preserving the path and query string. Avoid loops between
   Cloudflare and GitHub Pages. Enable HTTPS enforcement at the appropriate layer.
8. Validate the selected production content before cache invalidation or traffic
   changes. No cache purge, routing change or deployment is part of this commit.

GitHub reference:
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https

## Read-only acceptance checks after the production change

Run from an unrestricted network without any uploaded private key.

```sh
dig +noall +answer infofaqs.com A
dig +noall +answer infofaqs.com AAAA
dig +noall +answer infofaqs.com NS
dig +noall +answer infofaqs.com CAA
dig +noall +answer www.infofaqs.com CNAME
dig +noall +answer www.infofaqs.com A
dig +noall +answer www.infofaqs.com AAAA

curl --silent --show-error --location --max-redirs 5 --dump-header - --output /dev/null --write-out 'final=%{url_effective} status=%{http_code} redirects=%{num_redirects}\n' 'http://infofaqs.com/'
curl --silent --show-error --location --max-redirs 5 --dump-header - --output /dev/null --write-out 'final=%{url_effective} status=%{http_code} redirects=%{num_redirects}\n' 'https://infofaqs.com/'
curl --silent --show-error --location --max-redirs 5 --dump-header - --output /dev/null --write-out 'final=%{url_effective} status=%{http_code} redirects=%{num_redirects}\n' 'http://www.infofaqs.com/'
curl --silent --show-error --location --max-redirs 5 --dump-header - --output /dev/null --write-out 'final=%{url_effective} status=%{http_code} redirects=%{num_redirects}\n' 'https://www.infofaqs.com/'

openssl s_client -connect infofaqs.com:443 -servername infofaqs.com -verify_hostname infofaqs.com -verify_return_error -showcerts </dev/null
openssl s_client -connect www.infofaqs.com:443 -servername www.infofaqs.com -verify_hostname www.infofaqs.com -verify_return_error -showcerts </dev/null
```

Acceptance:
- Both hostnames resolve as intended over IPv4 and IPv6 where published.
- Both HTTPS connections pass trusted-chain and hostname validation.
- Served leaf certificates are within their validity period; record issuer,
  SANs, notBefore, notAfter, fingerprint, negotiated TLS version and chain result.
- Canonical HTTPS returns 200 with the intended content.
- The other three entry URLs converge on it with no loop; record each
  Location and 301/308 response. Repeat with an existing path and query string.
- Open the exact intended bio/story link inside actual Instagram on iOS and
  Android. Record app/OS versions, timestamp, final URL and any error.
  Verify navigation, scrolling, page layout and relevant public destination links.
- Mobile viewport, responsive CSS and absence of HTTP assets are favorable
  static signals only; a desktop browser or changed user-agent is not an
  Instagram compatibility test.

## Preservation and authorization

This branch adds only CNAME and this readiness document. Existing source,
archives, history, content, licenses and original files remain unchanged.
No private key is required, copied, read, committed or used.
No account settings, DNS, certificates, live deployments or publications are
changed as part of preparing this commit. Merging to the configured publishing
branch may trigger an automatic production deployment and requires separate
authorization under the current task scope.
