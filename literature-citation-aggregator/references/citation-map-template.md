# Citation Map Template

Use this table while reading the user's source text and before editing a manuscript. For long, humanities, Chinese-language, dissertation, or project-based work, build the evidence architecture first and read `evidence-governance-workflow.md`.

## Task Triage Record

| Field | Value |
|---|---|
| User request mode | citation-gap scan / evidence architecture / source discovery / source-fit audit / citation insertion / reference formatting / project evidence memory |
| Manuscript type | article / dissertation / thesis chapter / research proposal / literature review / report / other |
| Language and citation style | APA 7 / GB/T 7714 / Chicago / MLA / IEEE / Vancouver / user-specified |
| Editing permission | map only / comment only / insert citations into copy / edit original |
| Sensitive material rule | local-only / short queries allowed / full upload explicitly approved |

## Evidence Architecture Registry

| ID | Location | Claim summary | Evidence class | Suitable evidence | Do-not-substitute warning | Status |
|---|---|---|---|---|---|---|
| E1 | Chapter 2, para 4 | [short claim] | theory / findings / method / factual / interpretive / case-material / project-specific | [source type needed] | [what would be a mismatch] | open |

## Claim Registry

| ID | Location | Original claim | Claim type | Evidence class | Evidence needed | Search concepts | Status |
|---|---|---|---|---|---|---|---|
| C1 | Section 2, para 3 | [exact or shortened claim] | theory / intervention / method / instrument / context | theory / findings / method / factual / interpretive / case-material / project-specific | review / empirical / validation / critical edition / archive / score / interview / official record | [keywords] | open |

Claim types:
- definition
- theory/mechanism
- intervention effect
- research design/method
- instrument/rubric/validity
- contextual/background claim
- statistical/factual claim
- interpretive/humanities claim
- case-material claim
- project-specific claim

## Candidate Source Screen

| Claim ID | Candidate source | Discovery source/query | Evidence role | Fit | Verification source | Decision | Note |
|---|---|---|---|---|---|---|---|
| C1 | Author (Year) | Consensus: query... | empirical / theory / review / instrument | Direct | Crossref DOI... | include | directly supports the manuscript claim |

Fit values:
- Direct
- Strong adjacent
- Theory/review
- Weak adjacent
- Contradictory
- Unverified

Decision values:
- include
- include with cautious wording
- reserve for background
- reject
- needs primary evidence
- needs full text
- needs user/library access
- unresolved gap

## Rejected Source Log

| Claim ID | Rejected source | Reason | Future instruction |
|---|---|---|---|
| C1 | [Author, Year] | weak adjacent / unverifiable / evidence-type mismatch / contradictory / predatory-looking | do not reuse for this claim |

## Insertion Log

| Claim ID | Original sentence/action | Revised sentence/action | Inserted citation | Rationale |
|---|---|---|---|---|
| C1 | [before] | [after] | (Author, Year) | direct empirical support |

## Project Source Library

Use this section for long-running projects so future passes do not restart from zero.

| Source ID | Source | Evidence role | Verified by | Supports locations/claims | Use caveat | Access status |
|---|---|---|---|---|---|---|
| S1 | [full citation draft] | theory / method / context / primary text / archive / score / interview | DOI / Crossref / CNKI / library / publisher / local file | C1, C5 | [scope limits] | open / local / library required |

## Final Audit Summary

| Metric | Count / Status |
|---|---|
| Claims reviewed | [N] |
| Claims cited | [N] |
| Claims marked needs source | [N] |
| Final references | [N] |
| In-text orphan citations | [N] |
| Orphan reference entries | [N] |
| Metadata verified | [N/N] |
| Claim-source alignment issues | [N] |
| Claims intentionally not cited because they need primary evidence | [N] |
| Rejected sources logged | [N] |
