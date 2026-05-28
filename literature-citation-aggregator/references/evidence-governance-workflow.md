# Evidence Governance Workflow

Use this reference when citation work is bigger than "find a source for this sentence." It is required for long manuscripts, multilingual projects, humanities/social-science arguments, Chinese-language scholarship, local case studies, dissertations, or projects that rely on primary materials.

## Core Shift

Do not run a linear workflow of `claim -> search -> citation`.

Use:

```text
task triage -> evidence architecture -> source routing -> decision gate -> insertion or gap report -> project memory
```

The central question is not "Which citation can I add?" but "What kind of evidence would make this claim legitimate?"

## Task Triage

Classify the user's intent before working:

| Mode | Use when | Primary output |
|---|---|---|
| citation-gap scan | The draft has unsupported claims, red notes, TODOs, comments, or "needs source" markers. | Claim registry and evidence needs. |
| evidence architecture | The manuscript is early-stage, conceptual, or mixed-method. | Evidence map by section and claim type. |
| source discovery | The user wants literature recommendations without document edits. | Verified source shortlist with fit notes. |
| source-fit audit | The draft already has citations. | Weak/misaligned/orphan citation report. |
| citation insertion | The user wants citations placed into text. | Revised copy, references, audit. |
| reference formatting | The user only needs reference cleanup. | Normalized reference list and mismatch report. |
| project evidence memory | The project spans chapters or sessions. | Reusable source library and rejected-source log. |

If the mode is unclear, default to mapping and ask before editing the manuscript.

## Evidence Architecture

For each claim, assign one evidence class before searching:

| Evidence class | Suitable sources | Do not substitute with |
|---|---|---|
| Theory / definition | Seminal books, theory papers, review chapters, field handbooks. | Random empirical papers that only mention the term. |
| Prior findings | Empirical studies, systematic reviews, meta-analyses, field-specific reviews. | General background articles. |
| Method / instrument | Methodology texts, validation papers, reporting standards, instrument manuals. | Studies that merely used the method. |
| Factual / contextual | Official records, statistics, policy texts, gazetteers, archives, institutional documents. | Opinion essays or unrelated reviews. |
| Humanities / interpretive | Primary texts, critical editions, commentaries, reception history, close-reading scholarship. | Broad social-science papers with matching keywords. |
| Case-material | Interviews, scripts, scores, field notes, recordings, programs, archival documents. | General literature about the field. |
| Project-specific | User-provided corpus, local files, project notes, previous source library. | Web search results that cannot see the project evidence. |

## Decision Statuses

Use explicit statuses in the citation map:

- `cite`: source directly supports the sentence.
- `cite cautiously`: source supports the claim only if wording stays qualified.
- `background only`: useful for literature review/context, not the exact sentence.
- `needs primary evidence`: ordinary literature cannot prove the claim.
- `needs user/library access`: likely source exists but requires login, PDF, archive, or institutional access.
- `reject`: source is weak, unverifiable, predatory-looking, mismatched, or contradictory.
- `unresolved gap`: no adequate source found yet.

## Humanities and Local-Archive Projects

For humanities, performance studies, local-history, ethnography, arts, law, policy, and area-studies work, treat primary materials as first-class evidence. A journal article is not automatically stronger than a score, manuscript, archive record, field interview, official notice, or critical edition. Match evidence to claim.

Examples:

- A claim about a performer's recollection needs interview evidence.
- A claim about a melody, motive, meter, or score marking needs score/audio evidence.
- A claim about a local custom or institution may need gazetteers, archives, official records, or fieldwork.
- A claim about theory or disciplinary framing needs scholarly literature.
- A claim about historical text wording needs a critical edition and page/juan information.

## Local Corpus First

When the user provides project files, search local materials before web search for project-specific claims. Build a local source index with:

- file path or archive identifier
- source type
- date/version
- relevant section/page
- claim it can support
- verification caveat

Do not upload full private files to third-party systems. Use minimal query phrases or bibliographic metadata unless the user explicitly authorizes more.

## Insertion Gate

Only insert a citation when all are true:

1. The source exists and metadata is verified.
2. The source supports the exact sentence or clause.
3. The evidence type matches the claim type.
4. The manuscript wording does not overstate the source.
5. The reference can be added consistently in the chosen citation style.

If any condition fails, do not insert. Mark the claim with the most precise gap status.

## Project Evidence Memory

For long-running projects, maintain a reusable source library with:

- source ID
- full citation draft
- evidence role
- verified metadata source
- sections/claims supported
- usage caveat
- access status
- rejected/duplicate notes

Also maintain a rejected-source log. Rejections save time and prevent weak sources from reappearing in later chapters.

## Output Ladder

Choose the lightest output that answers the user:

1. Evidence gap list.
2. Citation map.
3. Candidate-source screen.
4. Source-fit audit.
5. Revised citation-inserted manuscript.
6. Reference list.
7. Project source library.
8. Full citation audit report.

For high-risk work, deliver 1-4 before 5.
