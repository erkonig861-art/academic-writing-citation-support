# Academic Writing Citation Support

Academic Writing Citation Support is a Codex skill for strengthening academic manuscripts with verified scholarly citations and APA-style references.

It helps an AI writing assistant read an academic draft, identify unsupported claims, search for relevant scholarly literature, verify source metadata, insert in-text citations conservatively, and produce a traceable APA reference list. The goal is not to decorate a paper with citations, but to connect each important claim to sources that actually support it.

## Why This Skill Exists

Academic writing often fails at the citation stage for three reasons:

- Sources are found by broad keywords instead of the exact claim in the manuscript.
- References are inserted because they look related, even when they do not directly support the sentence.
- The final reference list is not checked against in-text citations, source metadata, DOI links, and claim-source fit.

This skill is designed to make citation work more rigorous. It treats citation insertion as an evidence alignment task: every cited source should have a clear role, every inserted citation should support the nearby claim, and every final reference should be verifiable.

## What It Does

- Finds claims in academic writing that need scholarly support.
- Builds search queries from the manuscript's actual concepts, methods, population, outcomes, and theory.
- Routes literature searches across suitable platforms such as Consensus, Elicit, Semantic Scholar, Crossref, Google Scholar, CNKI, Wanfang, Scite, PubMed, ERIC, IEEE Xplore, ACM Digital Library, PsycINFO, JSTOR, and other field databases.
- Verifies sources before citation insertion.
- Inserts APA in-text citations without disrupting the author's argument.
- Produces an APA reference list and a source trace.
- Flags weak, unverifiable, or mismatched sources instead of inventing citations.

## Detailed Workflow

### 1. Read the Manuscript

The skill starts from the user's original text. It does not rely only on a broad topic label such as "education technology" or "student motivation." Instead, it reads the paragraph-level argument and identifies the actual constructs, methods, populations, contexts, outcomes, and theoretical claims that need support.

For DOCX, PDF, or long text files, the original writing should be preserved. The first pass is used to understand the manuscript, not to rewrite it.

### 2. Identify Citation Targets

The skill looks for claims that normally require evidence, including:

- definitions and conceptual claims
- theory and mechanism claims
- intervention or treatment claims
- research design and method claims
- instrument, rubric, or validity claims
- prior findings and literature review claims
- contextual, policy, historical, or factual claims
- statistical or comparative claims

It does not try to cite every sentence. The focus is on claims where a citation would materially improve academic credibility.

### 3. Build a Citation Map

Before inserting citations, the skill builds a citation map. This map links each claim to:

- the manuscript location
- the original sentence or shortened claim
- the evidence type needed
- the search concepts
- candidate sources
- final selected source
- source verification link
- claim-fit note

This makes the process reproducible. A reader can see why a source was chosen and which claim it supports.

### 4. Route the Search Across Platforms

Different claims need different search tools. The skill uses a source-routing strategy rather than searching every platform in the same way.

| Need | Recommended platforms | Purpose |
|---|---|---|
| Fast peer-reviewed discovery | Consensus, Elicit, Semantic Scholar | Find likely relevant scholarly papers from claim-based queries |
| Systematic extraction | Elicit, Scopus, Web of Science | Compare samples, methods, findings, outcomes, and study types |
| Citation graph and related work | Semantic Scholar, Google Scholar, Scite | Find influential papers, later studies, supporting or contrasting citations |
| Metadata verification | Crossref, publisher pages, DOI records | Verify title, authors, journal, volume, issue, pages, DOI, and year |
| Field-specific literature | PubMed, ERIC, IEEE Xplore, ACM Digital Library, PsycINFO, JSTOR, Business Source, SSRN, HeinOnline | Match the manuscript's academic discipline |
| Chinese-language scholarship | CNKI, Wanfang, VIP | Find Chinese-language studies, local context, and China-specific literature |

The general rule is: use discovery tools to find candidates, then use authoritative indexes or publisher pages to verify final references.

### 5. Screen Candidate Sources

Candidate sources are ranked by fit:

1. Direct fit: same construct plus very similar population, context, method, or outcome.
2. Strong adjacent fit: same construct and outcome, but a nearby population or context.
3. Theory or review support: useful for mechanisms, definitions, or field-level consensus.
4. Background only: useful for general context, but not enough for a specific empirical claim.

Sources are rejected when they only match keywords, cannot be verified, appear in questionable venues, contradict the claim, or would require overstating the evidence.

### 6. Verify Sources Before Insertion

Before a citation is inserted, the skill checks:

- whether the source exists
- whether title, author, year, journal, and DOI metadata are reliable
- whether the abstract or full text supports the claim
- whether the evidence strength matches the sentence wording
- whether the source is being used for the correct purpose

This matters because a real reference can still be a bad citation if it supports only a nearby topic rather than the exact claim.

### 7. Insert Citations Conservatively

The skill inserts APA-style citations without changing the author's argument or voice. It prefers:

- one or two high-fit sources over long citation piles
- narrative citations when the author is part of the sentence
- parenthetical citations when the source supports a claim
- minimal sentence changes only when needed for readability

If the source fit is uncertain, the skill should flag the claim instead of forcing a weak citation.

### 8. Audit the Final Draft

After insertion, the skill checks:

- every in-text citation has a reference entry
- every reference entry is cited in the manuscript
- APA formatting is consistent
- DOI links are included where available
- high-value claims have adequate support
- no source is being used beyond what it can support

The final output should include both the revised text and a short source trace.

## Key Advantages

### Claim-Level Search

The skill searches from the actual manuscript sentence, not from broad topic labels. This makes the retrieved literature more relevant to the paper's argument.

### Multi-Platform Coverage

No single literature platform is complete. The skill separates discovery, citation chasing, source verification, field-specific search, and Chinese-language search so that each platform is used for what it does best.

### Stronger Citation Integrity

The skill checks whether a source supports the exact claim near the citation. This reduces weak citation placement, source padding, and accidental overclaiming.

### APA-Focused Output

The default style is APA 7. The skill supports in-text citation insertion, reference list generation, DOI formatting, and citation-reference consistency checks.

### Traceable Decisions

The citation map and source trace show where each source came from, which query found it, how it was verified, and why it was selected.

### Original Writing Preservation

The skill is designed to strengthen the manuscript without rewriting the author's argument, paragraph order, terminology, or academic voice.

### Safer Handling of Uncertain Evidence

If a reliable source cannot be found, the skill should mark the claim as needing support instead of inventing a reference or inserting a loosely related paper.

## Expected Deliverables

When used on a manuscript, the skill can produce:

- a revised manuscript or marked-up text with inserted citations
- an APA reference list containing only cited sources
- a citation map showing claim-to-source alignment
- a source trace with discovery and verification details
- a citation audit summary
- a list of unresolved claims that still need stronger sources

When used only for research, it can produce:

- recommended references grouped by purpose
- one-sentence relevance notes
- DOI or verification links
- candidate sources to keep, reject, or reserve for background

## Example Use Cases

- Strengthen a literature review with more relevant sources.
- Check whether a paragraph contains unsupported academic claims.
- Add APA citations to a DOCX article draft.
- Build a citation map before revising a manuscript.
- Verify that all in-text citations appear in the reference list.
- Replace weak or generic citations with better-matched sources.
- Search both English-language and Chinese-language literature for the same research problem.

## Repository Structure

```text
academic-writing-citation-support/
├── README.md
├── LICENSE
├── .gitignore
└── literature-citation-aggregator/
    ├── SKILL.md
    ├── agents/
    ├── references/
    └── scripts/
```

## Installation

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R literature-citation-aggregator ~/.codex/skills/
```

After installation, restart Codex or refresh the skills list if needed.

## Usage

Example prompt:

```text
Use literature-citation-aggregator to check this academic manuscript for unsupported claims, find relevant scholarly literature, insert APA citations, and generate an APA reference list with source traces.
```

More example prompts:

```text
Use literature-citation-aggregator to identify which claims in this paragraph need citations and recommend APA references for each claim.
```

```text
Use literature-citation-aggregator to add APA citations to this literature review without changing the author's structure or argument.
```

```text
Use literature-citation-aggregator to verify whether the existing citations in this draft actually support the claims they are attached to.
```

You can use it with:

- DOCX drafts
- PDF drafts
- plain text manuscripts
- literature review sections
- article drafts
- research proposals
- individual paragraphs that need citation support

## Citation Integrity Principles

This skill is designed to avoid decorative or weak citations. A source should be included only when it supports the exact claim near the citation. If a reliable source cannot be found, the claim should be marked as needing support instead of forcing a citation.

## Scope and Limits

This skill can guide search, verification, insertion, and APA formatting, but it does not replace the author's academic judgment. Some sources may require library access, institutional database access, or manual full-text review. For high-stakes academic submission, the final manuscript should still be reviewed by the author or supervisor.

The skill should not upload a private full manuscript to third-party websites unless the user explicitly approves that destination and content. When possible, it should search with short claim-based queries or minimal excerpts.

## License

MIT License.
