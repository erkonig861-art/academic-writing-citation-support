# Upgrade Notes: Evidence Governance Workflow

## Summary

This upgrade changes `literature-citation-aggregator` from a linear citation-support workflow into an evidence-governance workflow.

Previous default logic:

```text
read text -> find citation targets -> search literature -> verify -> insert citation -> make references
```

New default logic:

```text
task triage -> evidence architecture -> source routing -> integrity gate -> insertion or gap report -> project evidence memory
```

The core question is now:

> What kind of evidence would make this claim legitimate?

not:

> Which source can be attached to this sentence?

## Why This Upgrade Was Needed

The original workflow worked well for ordinary article drafts that need verified APA citations. It was weaker for large academic projects where claims depend on different evidence types:

- theory and definitions
- empirical findings
- methods and instruments
- official records and policy texts
- critical editions and commentaries
- local gazetteers and archives
- interviews, scripts, scores, field notes, and project files
- long-running project source memory

Without an evidence-governance layer, an agent may wrongly attach a broad scholarly source to a claim that actually requires primary evidence, or use a local interview to support field-wide theory.

## Main Changes

### 1. Task Triage

The skill now classifies the request before acting:

- citation-gap scan
- evidence architecture
- source discovery
- source-fit audit
- citation insertion
- reference formatting
- project evidence memory

High-risk or ambiguous tasks should produce a citation map before editing the manuscript.

### 2. Evidence Architecture

Each claim now gets an evidence class:

- theory/definition
- prior findings
- method/instrument
- factual/contextual
- humanities/interpretive
- case-material
- project-specific

This prevents premature web searching and reduces weak citation insertion.

### 3. Source Routing

`source-routing.md` now includes:

- local/project corpus first
- library catalogs and WorldCat-style routing
- official and archival sources
- Chinese humanities keywords
- evidence-class routing table

The workflow now recognizes that non-DOI sources can be authoritative when they are the correct evidence type.

### 4. Integrity Gates

`integrity-gates.md` now includes:

- Gate 0: task and evidence-class fit
- evidence-type mismatch rejection
- primary/case evidence fit
- final status counts for `needs primary evidence`, `needs user/library access`, rejected sources, and unresolved gaps

### 5. Citation Map Expansion

`citation-map-template.md` now includes:

- task triage record
- evidence architecture registry
- evidence class column
- rejected source log
- project source library
- final counts for uncited primary-evidence gaps

### 6. Style Awareness

`apa-checklist.md` now clarifies that APA 7 is the default, not a universal requirement. Chinese-language humanities manuscripts may require GB/T 7714, footnotes, or another local style.

## Pressure Scenarios Added by This Upgrade

Use these as behavioral checks when revising the skill again.

### Scenario A: Local Case Claim

Input:

> The manuscript says a specific opera score repeats a theme across three scenes.

Expected behavior:

- Classify as `case-material`.
- Search local/project corpus for the score or audio evidence.
- Do not cite a general paper on opera themes as proof of the specific score claim.
- Mark as `needs primary evidence` if no score/audio/page evidence is available.

### Scenario B: Chinese Humanities Manuscript

Input:

> A Chinese dissertation chapter needs sources for Su Shi text variants and local heritage claims.

Expected behavior:

- Classify as `humanities/interpretive` and `factual/contextual`.
- Prefer critical editions, commentaries, gazetteers, official records, CNKI/Wanfang, and library catalogs.
- Do not rely only on Crossref or DOI metadata.
- Ask about GB/T 7714 or other citation style before final insertion if style is unspecified.

### Scenario C: Weak Source Fit

Input:

> A source shares the same keywords but studies a different population, method, and outcome.

Expected behavior:

- Mark as `weak adjacent` or `reject`.
- Record it in the rejected-source log.
- Do not insert it to make the paragraph look more scholarly.

### Scenario D: Long-Running Project

Input:

> The user returns with chapters 7-8 after chapters 1-6 were already mapped.

Expected behavior:

- Reuse project source library.
- Check rejected-source log before repeating searches.
- Add new sources with verification and reuse caveats.

## Files Changed

- `literature-citation-aggregator/SKILL.md`
- `literature-citation-aggregator/references/evidence-governance-workflow.md`
- `literature-citation-aggregator/references/citation-map-template.md`
- `literature-citation-aggregator/references/source-routing.md`
- `literature-citation-aggregator/references/integrity-gates.md`
- `literature-citation-aggregator/references/apa-checklist.md`
- `README.md`
- `UPGRADE.md`

## Deployment Note

After changing the repository version, copy the `literature-citation-aggregator` directory into the active Codex skills directory:

```bash
cp -R literature-citation-aggregator ~/.codex/skills/
```

Then refresh or restart Codex if the runtime does not immediately pick up the updated skill.
