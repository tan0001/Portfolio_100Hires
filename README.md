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

| Codex extension not found in Cursor's marketplace | Installed CLI directly via npm instead |

| Codex authentication required billing | Used OpenAI API key |

| "Git: Clone" not visible in Command Palette | Used `git clone` in terminal instead |

