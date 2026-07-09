# Portfolio\_100Hires

Portfolio Project



\# AI Coding Tools Setup — Cursor, Claude Code, and Codex



\## Tools Installed

\- \*\*Cursor IDE\*\* — AI-powered code editor

\- \*\*Claude Code CLI\*\* — Anthropic's agentic coding tool (installed via CLI; extension unavailable in Cursor's marketplace)

\- \*\*Codex CLI\*\* — OpenAI's agentic coding tool (installed via CLI; extension unavailable in Cursor's marketplace)



\## Steps Completed



\### 1. Cursor IDE

\- Installed Cursor IDE and signed up for a personal account.



\### 2. Claude Code

\- Opened Cursor's extensions panel (via "Customize") and searched for "Claude Code."

\- Extension did not appear. Restarted Cursor and searched again — still not found.

\- Installed Claude Code manually via CLI:

```powershell

&#x20; irm https://claude.ai/install.ps1 | iex

```

\- Added the install path to Windows Environment Variables (PATH).

\- Ran `claude` in Cursor's terminal — got "command not recognized."

\- Restarted Cursor to apply PATH changes, ran `claude` again — launched successfully.

\- Prompted to sign in. Since I don't have a paid Claude subscription, I stopped here without completing authentication.



\### 3. Codex

\- Searched for "Codex" in Cursor's extensions panel — not found.

\- Installed manually via npm:

```powershell

&#x20; npm install -g @openai/codex

```

\- Ran `codex` in Cursor's terminal, chose API key authentication.

\- Generated an API key at console.openai.com and entered it when prompted.

\- Set up the default sandbox for file/network protection.



\### 4. GitHub Setup

\- Logged in to GitHub, created a new public repository: \[Portfolio\_100Hires](https://github.com/tan0001/Portfolio\_100Hires.git)

\- Tried Command Palette (`Ctrl+Shift+P`) → "Git: Clone" — option wasn't showing.

\- Cloned via terminal instead:

```powershell

&#x20; cd <target-directory>

&#x20; git clone https://github.com/tan0001/Portfolio\_100Hires.git

```



\### 5. README and Push to GitHub

\- Created this `README.md` file documenting the setup.

\- Committed and pushed it to GitHub:

```powershell

&#x20; git add README.md

&#x20; git commit -m "Add README documenting Cursor, Claude Code, and Codex setup"

&#x20; git push origin main

```



\## Issues Encountered \& Solutions

| Issue | Solution |

|---|---|

| Claude Code extension not found in Cursor's marketplace | Installed CLI directly instead |

| `claude` command not recognized after install | Added install directory to PATH, restarted Cursor |

| Claude Code login required paid plan | No paid subscription available; left authentication incomplete |


---

## Research: Newsletter / Email Marketing for B2B SaaS

**Topic chosen:** Newsletter/Email Marketing for B2B SaaS

**Reason for choosing this topic:** I have experience writing newsletters for brand value building as well as subtle marketing with a focus on content, giving me a practiced instinct for evaluating what does and doesn't work at capturing an audience.

### Candidate Research Process
- Started with a pool of 25 candidates (own research + AI provided suggestions).
- Triaged all 25 against three signals: **(1) active practice** — do they currently run a real email/newsletter program, tool, or client work; **(2) content relevance** — is recent output still substantively about email/newsletter marketing rather than adjacent topics; **(3) recency** — active on their primary channel within the last ~4-6 months.
- Engagement metrics were used only as a tie-breaker between similarly-scored candidates, not as a primary filter.
- Several strong-looking candidates (e.g. Hiten Shah, April Dunford, Rand Fishkin) were cut after review showed their recent content had drifted toward adjacent topics (AI/GTM, positioning, audience research) despite strong general marketing credibility.

### Final 10 Experts Selected

| # | Name | Why Selected |
|---|---|---|
| 1 | Brennan Dunn | Founder of RightMessage (active product); strong client case studies with concrete metrics (personalization, opt-in rate lifts) |
| 2 | Val Geisler | SaaS retention/lifecycle email specialist, ex-ConvertKit; strong YouTube presence |
| 3 | Chad S. White | Author of Email Marketing Rules; email trends and B2B benchmarks content |
| 4 | Jimmy Daly | Content/email strategy for SaaS via Superpath; strong content-strategy thinking |
| 5 | Kevan Lee | Prior newsletter/growth operator background; current content has shifted toward brand strategy at Bonfire — included for historical practitioner credibility |
| 6 | Samar Owais | SaaS-only email conversion strategist; named enterprise clients, detailed audit process |
| 7 | Brendan Hufford | Rebuilds newsletter functions for B2B SaaS companies; cites real newsletter metrics (47% open rate, 13,000+ subscribers) |
| 8 | Jay Schwedelson | Runs SubjectLine.com; data-backed subject line testing with specific performance percentages |
| 9 | Adam Schoenfeld | Ex-CMO with strong SaaS marketing credibility; current content is broader B2B/AI-GTM commentary rather than email-specific |
| 10 | Wes Bush | Product-led growth specialist; available recent LinkedIn content skews toward broader PLG strategy rather than email-specific |

**Honesty note:** Not all 10 finalists had recent content that was purely email/newsletter-focused. Kevan Lee, Adam Schoenfeld, and Wes Bush in particular showed topic drift toward brand strategy, AI/GTM, and PLG respectively in their most recent output. They were kept in the list based on demonstrated practitioner credibility and available email-adjacent content, and this is flagged transparently rather than glossed over.


### What Was Collected
- YouTube video transcripts collected programmatically via the `youtube-transcript-api` Python library (free method, no official API key required) — stored in `/research/youtube-transcripts/`
- LinkedIn posts collected manually (2-3 representative recent posts per expert) due to platform restrictions on automated scraping — stored in `/research/linkedin-posts/`
- Full candidate research, cut reasoning, and annotations in `/research/sources.md`
- Note: Val Geisler had no recent LinkedIn content specifically on-topic; her YouTube transcripts serve as her primary evidence.

### Tools Used for Collection
- `fetch_transcript.py` — fetches a single YouTube video transcript
- `batch_fetch_transcripts.py` — reads a `videos.json` file and batch-fetches transcripts for multiple experts/videos at once, with per-video success/failure logging
