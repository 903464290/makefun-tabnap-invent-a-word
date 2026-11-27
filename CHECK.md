# CHECK — Invent a Word We Need (`u-deranalabs-invent-a-word-we-need-17a020e0`)

Checked 2026-11-25 (UTC ~04:52-05:00) against the live kit and requirements.
Nothing has been submitted, pushed, or registered. No keypair exists.

## 1. Sources used
- Kit: `GET https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0/kit` (.tar.gz, unpacked to `/tmp/makefun/kits/u-deranalabs-invent-a-word-we-need-17a020e0-kit/u-deranalabs-invent-a-word-we-need-17a020e0-kit/`)
  - `kit.json`: format `agent-fun/kit/v1`, phase `dev`, protocol `agent-fun/program/v1`
  - bundle_sha256 `93ffcba13b8daed2e6efd8d922a5da6e783ab3b518c2443b74924649b8ed6585` (matches requirements-side bundle hash in competition.yaml: `93ffcba13b8daed2…` — full value recorded in kit.json)
  - harness `harness@458c737ef56093a821b39889c49429a7141db57520a65d251579db6c18f35968 node v26.13.1`
  - scorer `scorer@d36068fc0eb38c78f4b2e1f21b11a32e957ede11b2be77f5d2db3d70df4cb9e6 program@49e164c1bcda970b1d451c8e371f5fe6c2f1b7dd483219cc1745c0493c9784e3`
  - CLI `cli/makefun.mjs` sha256 `38fa56630ff28c5336a551b72844b124a7ee6f11b312d81b6e2cb56f1f123836` (same in all 4 kits)
  - Kit verification: `node cli/makefun.mjs check` prints `kit u-deranalabs-invent-a-word-we-need-17a020e0 dev: verified 8 files` for this kit.
- Requirements: `GET https://make.fun/api/competitions/u-deranalabs-invent-a-word-we-need-17a020e0/requirements` (no key, 2026-11-25)
  - harness `program/v1`, status `open`, entry_fee `null`, quota `max_per_day 5` / `max_submissions_per_day 50` / `max_entries_per_account 40`
  - entries close `2026-11-27T09:55:00Z (2026-11-27 17:55 CST)`; payout total $5 (1st $2, 2nd $2, 3rd $1); 4 blind rounds, next 2026-11-25T17:24:41Z
  - 57 checks, identical check-id set across all 4 Minis; deliverables: `repo_url`, `commit_sha`, `bundle` (required), `title` (optional), `entry_message` + `entry_signature` (required), `LICENSE`, `main.ts or main.py`, `.makefun/owner.json` (required unless repo owner is the account's GitHub login)

## 2. Output gate — CONFIRMED, matches the earlier assumption exactly
- Kit `RULES.txt` (and `competition.yaml` rules, same wording):
  - `Your program writes one text to `/output/entry.txt`, and the judge below compares the entries two at a time by its brief, published here in full.`
  - `A sealed scorer checks that /output/entry.txt is UTF-8 text of 1 to 140 characters, not only white space, and gives the entry a Valid column of 1 or 0. Only a valid entry goes before the judge; an invalid one is listed with 0 and no rate, and takes no prize.`
  - i.e. limit is 1–140 characters for this competition.
- `main.py` enforces the same limit (`MAX_CHARS = 140`) and refuses leading/trailing whitespace. **No change to main.py was needed.**
- Harness source (`harness/harness-src.tar.gz`, `grader/sandbox/types.ts`, `k8s.ts:3398`): the grader sets `MAKEFUN_OUTPUT_DIR=/output` in the container and runs `python3 -P -s /bot/main.py` (python3.13, cwd `/bot`). `main.py` reads `MAKEFUN_OUTPUT_DIR` and falls back to relative `output/` locally — correct on both sides.

## 3. Local verification (2026-11-25, python3 3.12.3, grader-style `python3 -P -s main.py`, cwd = repo dir)
- Entry (100 / 140 chars): `Tabnap (n.): the micro-nap you take with fifteen browser tabs open, convinced you are still working.`
- Two runs to separate `MAKEFUN_OUTPUT_DIR`s: byte-identical (deterministic), UTF-8, no trailing newline, no leading/trailing whitespace, non-empty / not only whitespace. PASS.
- Default run (no env var) also writes `./output/entry.txt`. PASS.
- Note: local python is 3.12.3; the grader uses python3.13. `main.py` uses only `os` + `pathlib` stdlib, so no 3.13-only feature is involved.

## 4. Repo contents check
- `main.py` — present at root, entrypoint per requirements. ✓
- `README.md` — present; diffed against requirements `how_to_submit.readme_template`: identical except the two intended fill-ins (`{description}` → one-line description, `{run}` → `MAKEFUN_OUTPUT_DIR=output python3 main.py`). All 3 badges present; `{owner}` / `{repo}` / `{referral_code}` still placeholders (to fill at push/submit time). ✓
- `LICENSE` — MIT (`MIT License`, OSI-approved). ✓
- `.makefun/owner.json` — `{"wallet": "Hymj9Xqj7PQiLEFsjD7cgqkrWq2oTQGAqTtVgBofLWVd"}`. Address validated: 44 chars, base58, decodes to 32 bytes. ✓ (public address only; no keypair/private key involved)
- `.gitignore` — `output/`, `__pycache__/`, `*.pyc` (so local runs and bytecode are never committed). ✓
- `CANDIDATES.md` — present (notes only; see caveat in §6).
- `output/` / `__pycache__/` — not in the commit (ignored / removed).

## 5. Kit check (`node cli/makefun.mjs check --kit . --repo <dir>`, run 2026-11-25T04:54Z, no `--transcripts`)
- Kit integrity: `kit u-deranalabs-invent-a-word-we-need-17a020e0 dev: verified 8 files`. ✓
- Commit checked: `babab7664e08627101354ae0b8685536a674c0b1` — `repository … @ babab7664e08627101354ae0b8685536a674c0b1: 7 entries`.
- Result: **4 passed, 1 failed, 14 skipped, 5 checked at submission — verdict: `not ready: fix transcripts_present, then check again`**.
- Passed (4): `competition_open` (now is between opening 2026-11-25T03:54:35.000Z and the entry deadline); `snapshot` (7 files, 12,051 bytes, within intake caps); `license_osi` (LICENSE declares SPDX-License-Identifier: MIT, OSI-approved); `entrypoint` (main.py at root selects python3.13, accepted by this competition).
- Failed (1): `transcripts_present` — `no transcripts were uploaded`. Fix per the tool: bundle the agent sessions that built the entry (`node cli/makefun.mjs bundle --repo <repo> --system-prompt <file> --effort <level> --out transcripts.tar.gz`, with `--redact` for personal details), then re-run check with `--transcripts transcripts.tar.gz`. This is expected at this stage: no transcript bundle exists yet, and this subagent was told not to submit/register — bundling is part of the submit step, not done here.
- Skipped (14): `strategy_note` (not asked for), `committed_secret` (no --dotenv given), and 12 transcript-gate checks (`transcripts_recorded`, `thinking_wellformed`, `thinking_in_window`, `thinking_committed`, `thinking_reproduces`, `thinking_on_task`, `thinking_turns`, `thinking_priced`, `thinking_revised`, `thinking_fresh`, `transcripts_run_record`, `thinking_own_work`) — all skipped because no transcript session parsed.
- Checked at submission (5, not runnable locally): `repo_public` (repo must be public on GitHub at submit), `repo_owner` (GitHub owner must be the account's GitHub login, or the commit must carry `.makefun/owner.json` naming one of the account's entry wallets — ours does, see §4), `repo_created_after_open` (GitHub repo creation time must be at or after opening 2026-11-25T03:54:35.000Z — so the GitHub repo must be created fresh, not reused), `commit_in_repo` (this commit must be pushed to a branch), `duplicate_snapshot` (files must differ from every other account's earlier entry).
- No local grade exists for this competition (`RULES.txt`: "There is no local grade of this competition: the server grades every entry") — `grade-local` is not applicable to program/v1 here.

## 6. Caveats / still open before submit
- Kit check has NOT yet passed end-to-end: it needs (a) a local commit (done in §7) and (b) a transcripts bundle (`--transcripts transcripts.tar.gz`), which does not exist yet — the sessions that built this entry must be bundled with the kit CLI first. Expect transcript-gate checks to fail until the bundle exists.
- `CHECK.md` and `CANDIDATES.md` are committed in this repo (per prep instructions). They are notes, not part of the graded program; if a minimal repo is wanted, remove them before push — the graded program (`main.py`) is unaffected either way.
- No remote is configured and nothing has been pushed. Still needed before submit: create one public GitHub repo per entry (after the competition opened), push this commit, set the repo About from requirements `how_to_submit.repo_about` (`gh repo edit … --add-topic 'makefun,ai-agents,bounties,growth'`), fill `{owner}` / `{repo}` / `{referral_code}` in README.md, link the wallet to the make.fun account and sign the entry message with it, bundle transcripts, then submit via the kit CLI.

## 7. Local git status
- `git init` (branch `main`), working tree clean, **no remote configured, nothing pushed**.
- The kit check in §5 ran against commit `babab7664e08627101354ae0b8685536a674c0b1`. After the check, this CHECK.md file itself was updated with the check results and the commit was amended to include it, so the current HEAD differs from the checked commit only in CHECK.md (verify with `git diff babab7664e08627101354ae0b8685536a674c0b1 HEAD --stat`). The graded files (`main.py`, `README.md`, `LICENSE`, `.makefun/owner.json`) are byte-identical between the two commits, so the §5 check result still stands.
- Committed files (7): `.gitignore`, `.makefun/owner.json`, `CANDIDATES.md`, `CHECK.md`, `LICENSE`, `README.md`, `main.py`.
- Commit author is the placeholder `makefun-prep <prep@localhost>` (set with `-c` for this local commit only, no global git config was changed). Before pushing, set the real GitHub identity as the commit author if desired — the commit can be amended; the graded program is unaffected. The repo's GitHub *owner* (not the commit author) is what the `repo_owner` check reads.
- `git remote -v` is empty. `git log --oneline -1` shows the commit above; `git status --short` is empty.

## 8. README placeholders filled (2026-11-25 13:34 CST)
- GitHub repo name chosen: `makefun-tabnap-invent-a-word` (owner `903464290`, referral `3cnb9n7s`). Name adopted from SUBMIT_PLAN.md; the `makefun-` prefix keeps it distinctive — the generic `invent-a-word-minis` alternative would be far more likely to collide. Local collision check is impossible; the browser must verify the name is free on GitHub at creation time, and pick a suffix variant if taken.
- README.md: `{owner}` → `903464290`, `{repo}` → `makefun-tabnap-invent-a-word`, `{referral_code}` → `3cnb9n7s`. `{description}` and `{run}` unchanged from the earlier fill. Verified: 0 placeholders remain; title line is `# makefun-tabnap-invent-a-word`; badge URLs carry owner/repo.
- Commit amended to include the filled README (same single commit, author still placeholder `makefun-prep`). Final HEAD SHA is recorded in ~/workspace/makefun-minis/SUBMIT_CHECKLIST.md (kept outside this repo, so the record stays accurate after the amend).
- NOTE: amending changed the commit SHA from the one kit-checked in §5 (`babab76…`). Graded files (`main.py`, `LICENSE`, `.makefun/owner.json`) are byte-identical; only `README.md` (and this `CHECK.md`) changed, so the §5 check conclusions still stand, but `node cli/makefun.mjs check` should be re-run against the final SHA before submitting (per SUBMIT_PLAN step 2).
- Next step: create the public empty GitHub repo `903464290/makefun-tabnap-invent-a-word` (must be created after the competition opened, 2026-11-25 03:54:35Z — a fresh repo now satisfies this), add it as remote, push HEAD, set repo About/topics `makefun, ai-agents, bounties, growth`, homepage = bounty page. No remote configured yet; nothing pushed.

## 9. Final HEAD
The final commit SHA for this repo (single commit, clean tree, no remote) is recorded in ~/workspace/makefun-minis/SUBMIT_CHECKLIST.md and SUBMIT_PLAN.md. Use that SHA when submitting; do not quote a SHA from inside this file, which predates the final amend.
