# Aurevue — Completed One Year Roadmap

**Owner:** Bradley (Founder / Creative Director)  
**Timeframe:** Today → New Year (rolling ~10 weeks)  
**Objective:** Ship a *functional, presentable prototype* of Aurevue with **MagMotion** and **Expandable Tiles → Pages**, backed by clean architecture, brand cohesion, and investor‑ready storytelling.

> **Planning rule:** You do **not** need quotas every day. Each week has clear outcomes. Critical sprints list *daily quotas*; light weeks emphasize review, polish, or recovery.

---

## 0) Guiding Principles
- **Build like a company, legally act as a student.** Treat docs, structure, and hygiene as investor‑grade.
- **Design clarity > feature count.** A small set of interactions that *feel inevitable* beats a cluttered toolkit.
- **Motion serves meaning.** MagMotion should guide attention and encode hierarchy, not decorate.
- **Write it down.** Every decision goes into `docs/` (devlog, brand notes, roadmap updates).
- **Protect energy.** Planned buffers and review days are part of the system.

---

## 1) Architecture & Repos (Baseline)
```
Aurevue/
├─ Projects/
│  └─ Aurevue_Rebuild_2025/
│     ├─ core/ (navigation.py, motion.py, variables.py, mood_system.py)
│     ├─ ui/ (topbar.py, sidebar.py, tile.py, pages/…)
│     ├─ assets/ (symlink or absolute paths to C:\Users\<Name>\Aurevue\Assets)
│     ├─ docs/ (this roadmap, devlog, brand, investor_prep)
│     └─ README.md
├─ Assets/ (Images, Icons, Fonts, Sounds)
└─ Foundation/ (company-sim docs: vision, roadmap, internal memos)
```
**Branching:** `main` (stable) ← `dev` (integration) ← `feature/*` (short‑lived).  
**Tags:** `v0.x_*` for milestones; `v0.1_prototype`, `v0.2_motion`, etc.

---

## 2) The Big Milestones (Today → New Year)
1. **Prototype Core** (Now → Nov 1): foundational UI, tiles grid, first MagMotion.
2. **Tiles → Pages** (Nov 2–9): expansion animation + back/restore; multi‑tile routing.
3. **Motion Language** (Nov 10–17): systematize timings/easing; hover/press/transition specs; ambient shadows.
4. **Mood & Visual Cohesion** (Nov 18–24): light/midnight palettes, typography, splash; investor prep v1.
5. **Thanksgiving Demo** (Week of Nov 24): internal demo + screen capture; feedback loop.
6. **Post‑Demo Hardening** (Dec 1–8): refactors, stability, perf tune; lazy load; input edge‑cases.
7. **Feature Rounds** (Dec 9–22): 2–3
   focused tiles with genuine content (e.g., Weather, Notes, System Monitor) that expand to pages.
8. **Holiday Polish & Docs** (Dec 23–29): branding warmth, micro‑copy, README + investor one‑pager v2.
9. **New Year Cut** (Dec 30–Jan 1): freeze, tag `NYE_Prototype_Cut`, export demo package & reel.

---

## 3) Week‑by‑Week Plan (with targeted daily quotas during sprints)

### Week 1 — **Prototype Core** (Today → Nov 1)
**Outcome:** Window shell, outer/inner containers, TileBoard grid, asset paths, first MagMotion hover.

**Daily quotas (sprint):**
- **Day 1:** Project skeleton + `config.py` paths; frameless window + translucent outer; commit.  
  *Deliverable:* `window_boot_ok.mp4` 5–10s capture.
- **Day 2:** TileBoard grid (3×2 or responsive); `TileWidget` stub; styles; commit.
- **Day 3:** MagMotion v0 (hover scale + ambient shadow deepen, press feedback); constants in `motion.py`.
- **Day 4:** Page container stub + transition scaffold (opacity + size anim groups) — no routing yet.
- **Day 5:** Backlog grooming + code hygiene; write **Motion Map v0** (elements, timings, easings).
- **Day 6–7 (buffer/light):** Bug fixes, screenshot set, short demo clip; tag `v0.1_prototype`.

**Weekly success criteria:** grid renders; 1 tile hover feels “magnetic”; window loads from external assets.

---

### Week 2 — **Tiles → Pages** (Nov 2–9)
**Outcome:** Click tile → expand full‑page → back collapse. Multi‑tile routing table.

**Daily quotas (critical days only):**
- **Mon/Tue:** Expansion animation: animate geometry + fade siblings; back animation parity.
- **Wed:** Routing registry (tile_id → page class); 2 tiles wired to placeholder pages.
- **Thu (QA day):** Reverse‑motion visual parity; no flicker/tearing; resize‑safe.
- **Weekend:** Light polish + record a 15–30s walkthrough; tag `v0.2_tiles_to_pages`.

**Weekly success criteria:** at least 2 tiles reliably expand to pages and return with mirrored motion.

---

### Week 3 — **Motion Language** (Nov 10–17)
**Outcome:** Canonical motion spec + reusable helpers.

**Focus:**
- `motion.py` helpers: `fade_in`, `fade_out`, `slide_in`, `expand_to_fill`, `parallel_group`, `sequential_group`.
- **QEasingCurve set:** OutCubic (toggle), OutQuad (tile appear), Linear (hover sheen), InOutCubic (page).
- **Shadows:** QGraphicsDropShadowEffect; ambient (0,0 offset), tuned blur/opacity; state‑based depth.

**Quotas (first 3 days):** formalize and demo each helper with tiny UI examples (one per day).  
**End‑week deliverables:** `Motion_Spec.md` (timings, states, examples) + tag `v0.3_motion_system`.

---

### Week 4 — **Mood & Visual Cohesion** (Nov 18–24)
**Outcome:** Light/Midnight modes; type scale; spacing rhythm; splash intro moment.

**Targets:**
- Variables: `PALETTE`, `TYPE_SCALE`, `RADIUS`, `SHADOWS` (dicts in `variables.py`).
- Mood toggle + persistence; minor motion speed shift by mood (Serene slower, Focus faster).
- Splash: logo fade/slide (≤ 1.2s) into TileBoard.

**Quotas (Mon–Thu):**
- Colors & typography day;
- Mood state + stylesheet day;
- Splash day;
- Integration QA day.  
**Weekend:** Record **Thanksgiving Demo v1**; compile notes for feedback.

**Weekly success criteria:** 2 moods working live; splash feels intentional; fonts render consistently.

---

### Week 5 — **Thanksgiving Demo & Feedback** (Nov 24–Dec 1)
**Outcome:** Present, collect feedback, triage.

**Checklist:**
- Capture 45–60s demo reel (tile hover, expand, page content, back, mood toggle, splash).
- Share with trusted testers; collect notes (UX, perf, clarity).
- Create `feedback_triage.md` with P1/P2/P3 buckets; open issues.

**Quotas:** none daily; focus on presentation and honest notes.

**Weekly success criteria:** concrete list of improvements, no crashes in demo path.

---

### Week 6 — **Post‑Demo Hardening** (Dec 1–8)
**Outcome:** Stability, refactors, perf tuning.

**Focus Areas:**
- Navigation state machine sanity; abort‑safe transitions (ignore double‑click spamming).
- Lazy load heavy page content; pre‑warm light assets.
- Resize policies and min/max sizes; prevent geometry jumps.
- Error handling & logs (developer‑friendly console output).

**Daily quotas (first half of week):**
- Mon: Transition robustness;
- Tue: Lazy‑load pass;
- Wed: Resize policies;
- Thu: Error/logs + perf profiling snapshot.

**End‑week:** tag `v0.4_hardening` + short “what changed” memo.

---

### Week 7 — **Feature Round I** (Dec 9–15)
**Outcome:** 1–2 real tiles with meaningful content.

**Candidates:**
- **Weather** (API‑free stub today; real later) with animated temperature card.
- **Notes** (local markdown scratch) with smooth editor reveal.

**Quotas:**
- Mon/Tue: Tile content UX sketches → implement first tile.
- Wed/Thu: Second tile; ensure page depth uses MagMotion language.
- Weekend: QA + capture feature clips; tag `v0.5_features_1`.

---

### Week 8 — **Feature Round II** (Dec 16–22)
**Outcome:** Third tile or deepen an existing page; refine back/forward nav affordances.

**Options:**
- **System Monitor** (CPU/RAM stub UI; animating bars)
- **Notifications Center** (mock feed + smooth slide drawer)

**Quotas:**
- Early week: Implement;
- Midweek: Interaction polish;
- Weekend: Stability pass.

**Weekly success criteria:** three tiles feel “real,” pages feel coherent, nav is obvious.

---

### Week 9 — **Holiday Polish & Docs** (Dec 23–29)
**Outcome:** Cohesive build; brand warmth; documentation you’re proud of.

**Focus:**
- Micro‑copy (empty states, tooltips), friendly errors.
- README with architecture diagram and run steps.
- `investor_onepager_v2.md` (Problem → Solution → Why Now → Product → Vision).
- Asset sweep (icons, spacing, shadow consistency).

**Quotas:** Only two *focused* days (docs & visual pass). Rest = buffer/recovery.

**Weekly success criteria:** repo looks professional at a glance; demo path is crisp.

---

### Week 10 — **New Year Cut** (Dec 30–Jan 1)
**Outcome:** Freeze a clean build; export artifacts.

**Checklist:**
- Version tag: `NYE_Prototype_Cut`.
- Export runnable package and a short demo reel (.mp4 + GIF).
- Write `CHANGELOG.md` highlights for the whole period.
- Internal Memo: Lessons learned + Q1 focus preview.

---

## 4) Success Criteria (Global)
- **Prototype UX:** Boots cleanly; tiles hover magnetically; expand to pages; back smoothly.
- **Motion System:** Documented helpers; timings/easing consistent; shadows tuned by state.
- **Visual Identity:** Two moods; type & spacing scale; brand‑aligned splash.
- **Reliability:** No crashes in core flows; transitions robust against spam; resize‑safe.
- **Docs:** Clear README, Motion Spec, Investor One‑Pager, CHANGELOG, Memovault.

---

## 5) Risk & Buffer Plan
- **Scope creep:** Use a *parking lot* section in the devlog; don’t add mid‑week.
- **Performance dips:** Prefer opacity transforms over expensive repaints; lazy‑load heavy UI.
- **Design fatigue:** Enforce light weekends after sprint weeks; schedule **Review Days**.
- **Tooling pain:** Keep assets outside IDE; script path constants; keep repo lean (LFS only if needed).

---

## 6) Operating Rituals
- **Nightly micro‑log** (3 bullets: did / pain / next).  
- **Weekly recap** (what shipped, what slipped, what I learned).  
- **Tag each milestone** with a 10–20s screen capture.

---

## 7) Glossary
- **MagMotion:** Aurevue’s motion language: magnetic proximity cues, easing families, depth shifts via ambient shadows, and continuity in tile→page transitions.
- **Expandable Tile:** Home‑grid module that animates to full‑page context with mirrored return.

---

### Final Note
This is a *living* roadmap. Update checkboxes, add dated notes, and keep momentum humane. When in doubt: **clarity over complexity, rhythm over rush.**

