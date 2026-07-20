# Task: Run the Codex Coordinator open-source decision simulation

## Goal

Create a local working copy at `C:\projects\MiroShark` and run one real MiroShark simulation comparing the decision to open-source Codex Coordinator with the counterfactual of keeping it proprietary.

## Guardrails

- Windows 11 with Docker Desktop/WSL available.
- The machine has 32 GB RAM and other heavy projects, so **do not run a local 30B/32B Ollama model**.
- Use OpenRouter/cloud models and start **Neo4j only** in Docker.
- Never print, log, commit, or paste API keys into GitHub.
- Keep `.env` ignored.
- Do not modify application code unless setup exposes a genuine defect.
- Stop MiroShark and its Neo4j container after the report is saved.

## Setup

1. If the folder does not exist:

   ```powershell
   cd C:\projects
   git clone https://github.com/eyeinthesky6/MiroShark.git
   cd MiroShark
   git remote add upstream https://github.com/MiroShark/MiroShark.git
   git fetch origin chatgpt/codex-coordinator-simulation
   git switch chatgpt/codex-coordinator-simulation
   ```

2. If it exists, verify the remotes instead of recloning.
3. Copy `.env.example` to `.env`.
4. Ask the user to enter their OpenRouter key **locally** when required. Do not request it in chat or echo it.
5. Configure the OpenRouter cloud preset documented in `docs/INSTALL.md`.
6. Set a strong local `NEO4J_PASSWORD`.
7. Start only Neo4j:

   ```powershell
   docker compose up -d neo4j
   ```

8. Run `./miroshark` from WSL/Git Bash, open the local UI, and verify frontend, backend, and Neo4j health.

## Simulation seed

On July 20, 2026, a solo founder publicly open-sources Codex Coordinator: a working coordination layer built specifically for OpenAI Codex. It enables persistent, goal-based multi-agent development through project-scoped documents, task boundaries, inter-agent messaging, restart recovery, autonomous coordination, and safeguards against cross-project contamination. The core product is open source, while advanced team and commercial capabilities may remain paid.

Simulate the following 12 months and compare the actual open-source decision against the counterfactual of keeping Codex Coordinator proprietary.

Include Codex users, independent developers, open-source maintainers, AI coding startups, competing agent frameworks, enterprise engineering teams, OpenAI, potential investors, and commercial customers.

Evaluate adoption and GitHub growth; credibility and founder reputation; community contributions; likelihood of OpenAI noticing or supporting it; consulting, sponsorship and paid-team-plan opportunities; copying and commoditization risk; support burden; long-term defensibility; and whether open-sourcing the core increases or destroys commercial value.

Deliver a clear verdict, specify what should remain open versus paid, and identify the first 90-day actions most likely to determine success.

## Pinned prediction-market question

> By July 20, 2027, will open-sourcing Codex Coordinator produce greater overall strategic and commercial value for its founder than keeping it proprietary?

## Counterfactual branch

The founder keeps the entire product closed-source and launches it as a paid SaaS.

## Completion criteria

- A real MiroShark run completes successfully.
- Record run cost, duration, agent count, action count, final direction/confidence, and the public/local report URL.
- Save a concise comparison of base versus counterfactual.
- Clearly distinguish simulated evidence from real-world evidence.
- Stop local services after capturing results.
