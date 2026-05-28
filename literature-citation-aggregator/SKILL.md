---
name: literature-citation-aggregator
description: Use when the user provides an academic manuscript, article draft, DOCX/PDF/text, paragraph, or research topic and asks Codex to strengthen paper writing with relevant scholarly literature, in-text citations, verified sources, and APA references.
---

# Academic Writing Citation Support

## Overview

Use this skill to govern the evidence behind academic writing, not merely to add citations. It first determines what citation task is actually needed, builds an evidence architecture for the manuscript, routes each claim to the right kind of source, and only then searches, verifies, inserts, audits, or marks gaps.

Default citation style is APA 7 unless the user specifies another style.

## Core Rules

- Preserve the author's argument, paragraph order, terminology, and voice. Do not rewrite beyond what is required to place citations smoothly.
- Search from the user's original text, not from generic topic labels. Derive queries from the actual constructs, intervention, population, methods, outcomes, and theoretical claims in each paragraph.
- Transmit only minimal search queries or short excerpts to third-party AI/search sites. Do not upload a full private file or long sensitive passages unless the user explicitly approves that destination and content.
- Prefer peer-reviewed journal articles, systematic reviews, meta-analyses, seminal theory papers/books, and validated instruments. Avoid weak keyword matches, unverifiable papers, predatory-looking venues, or citations that only share broad terms.
- Never invent references. If no reliable source is found, mark the claim as `needs source` and explain the gap.
- Treat "do not cite yet" as a valid scholarly outcome when a claim requires primary data, archive records, field notes, scores, interviews, legal texts, local gazetteers, or other evidence that ordinary journal literature cannot replace.
- Verify every included reference with DOI metadata, publisher page, Crossref, Semantic Scholar, Google Scholar, CNKI, or another authoritative index before finalizing.
- Treat citation insertion as an integrity task, not a decoration task: a citation must support the exact sentence where it is inserted.
- Keep a reproducible search trail for important claims: platform, query, filters, candidate count if visible, final selection rationale, and verification source.

## Workflow

### Phase 0: Task triage

Do not assume the user wants direct citation insertion. First classify the request:
- citation-gap scan: identify unsupported claims, red notes, TODOs, comments, or citation placeholders
- source discovery: recommend and verify literature without editing the manuscript
- source-fit audit: check whether existing citations support their sentences
- evidence architecture: map what kind of evidence each claim needs before searching
- citation insertion: insert verified citations and references into a new manuscript copy
- reference formatting: normalize in-text citations and reference list entries
- project evidence memory: update a reusable source library for a long-running project

When the request is ambiguous or high-risk, produce a citation map or evidence plan before editing the manuscript.

### Phase 1: Evidence architecture

Before searching, classify claims by the kind of evidence needed:
- theory/definition: seminal theory, conceptual framework, field review, validated definition
- prior findings: empirical studies, systematic reviews, meta-analyses, field-specific literature
- method/instrument: methodology literature, validation studies, reporting standards, rubrics
- factual/contextual: official records, policy documents, statistics, gazetteers, archive records
- interpretive/humanities: primary texts, critical editions, commentaries, reception history, field-specific scholarship
- case-material: interviews, field notes, scores, scripts, programs, performance recordings, archival documents
- project claim: user-provided local corpus or project memory

Read `references/evidence-governance-workflow.md` when the manuscript is long, multidisciplinary, humanities-oriented, Chinese-language, project-based, or includes primary materials.

### Phase 2: Read and map the source text

   - For DOCX, use the Documents skill or reliable text extraction. Keep the original file unchanged until insertion strategy is clear.
   - Build a citation map with: paragraph/claim, claim type, evidence class, evidence needed, search concepts, candidate sources, decision status, and verification link.
   - Read `references/citation-map-template.md` before large document work or when the user wants citations inserted into a manuscript.
   - If the document contains red text, comments, TODOs, bracketed notes, or "needs source" markers, map those first and preserve them unless the user asks to resolve or remove them.

### Phase 3: Identify citation targets

   - Prioritize claims about definitions, theory, mechanisms, intervention design, research design, instruments/rubrics, outcome constructs, prior findings, and contextual claims.
   - Do not cite every sentence. Add citations where they strengthen a specific claim or protect the manuscript from unsupported assertions.
   - Distinguish claims that need literature from claims that need primary/source-material verification.

### Phase 4: Search with a source-routing strategy

   - Read `references/source-routing.md` when selecting tools or when a task mentions Consensus, Elicit, Semantic Scholar, Scite, Crossref, Google Scholar, CNKI, Wanfang, or similar sites.
   - Use multiple platforms for important claims: one discovery tool plus one verification/index source.
   - Select platforms according to the claim type, discipline, and language of the manuscript. Start with a discovery tool, then verify with Crossref, publisher pages, or other authoritative indexes.
   - For discipline-specific claims, include field databases where available; do not rely only on general AI search.
   - Respect platform access limits. If a platform requires login, subscription, institutional access, CAPTCHA, or download permission, ask the user to provide an authenticated browser session, exported records, DOI/title lists, BibTeX/RIS files, screenshots, PDFs, or copied results instead of assuming direct access.
   - Search the user's local/project corpus first when the claim depends on project-specific sources, unpublished materials, or user-provided documents.

### Phase 5: Select sources by relevance and strength

   - Match the source to the exact claim: same construct, population or education level where possible, comparable method, and compatible outcome.
   - Use recent reviews for broad field claims; use original empirical studies for intervention effects; use foundational theory for conceptual frameworks; use validation studies for rubrics and instruments.
   - Prefer sources whose abstracts/methods show direct relevance, not just titles.
   - Assign each selected source an evidence role: theory, review, empirical intervention, instrument/validation, context, or counterpoint.
   - Assign each claim a decision status: `cite`, `cite cautiously`, `background only`, `needs primary evidence`, `needs user/library access`, `reject`, or `unresolved gap`.

### Phase 6: Run the pre-insertion integrity gate

   - Read `references/integrity-gates.md`.
   - Verify reference existence and metadata for every selected source.
   - Check claim-source fit before inserting: the source must support the sentence's construct, population/context, method, and level of certainty.
   - Reject sources that require overclaiming, such as using a broad review to support a narrow effect claim that the review does not directly address.
   - Reject evidence-type mismatches, such as using a general literature review to prove a local archival fact or using a project interview to prove broad disciplinary consensus.

### Phase 7: Insert in-text citations

   - Place citations at the end of the supported clause or sentence, before the period in APA style.
   - Use narrative citations when the author is part of the sentence; use parenthetical citations for supporting evidence.
   - Avoid citation piles. Use one or two best sources for ordinary claims; use three only when showing convergence across research types.
   - Preserve transitions. If insertion makes a sentence heavy, split the sentence minimally.
   - For uncertain fit, insert a comment or note rather than forcing a weak citation.
   - Insert into a new copy unless the user explicitly asks to edit the original.

### Phase 8: Run the post-insertion audit

   - Confirm zero citation orphans: every in-text citation has a reference entry, and every reference entry is cited.
   - Run a claim-source alignment check for high-value claims and any newly inserted citation.
   - Use a reviewer-style sanity pass:
     - methodology lens: does the source's design support the strength of the claim?
     - domain lens: are key field sources missing?
     - devil's advocate lens: could the citation be interpreted as weaker, contradictory, or only adjacent?
   - For long manuscripts, sample at least 30% of citation contexts during draft work and 100% before final delivery.

### Phase 9: Produce references and traceability

   - Read `references/apa-checklist.md` before final formatting.
   - Include DOI as `https://doi.org/...` when available.
   - Provide a source trace table or short note showing which platform found the source and which source verified it.
   - Separate final references from optional/background sources that were searched but not cited.
   - If the user specifies another style, use that style. If a Chinese-language thesis or humanities manuscript does not specify a style, ask or provide APA/GB/T 7714 options before final formatting.

## Deliverables

When editing a document, return:
- A revised DOCX or marked-up text with citations inserted.
- An APA reference list containing only cited works unless the user asks for a bibliography.
- A citation map or concise source trace: claim/location, citation, discovery source, verification source, and claim-fit note.
- A citation audit summary: orphan count, metadata verification status, claim-source alignment issues, unresolved gaps.
- A short list of unresolved citation gaps, if any.
- A separate list of claims intentionally left uncited because they require primary/source-material evidence.

When only researching, return:
- Recommended APA references grouped by purpose.
- One-sentence relevance notes tied to the user's text.
- Verification links or DOI links.

When building project evidence memory, return:
- A reusable source library grouped by concept, section, claim type, evidence role, verification source, and reuse caveat.
- A rejected-source log for weak, unverifiable, or mismatched sources so future passes do not repeat the same search mistake.

## Useful Script

Use `scripts/crossref_lookup.py` to verify DOI/title metadata and generate APA-like reference drafts from Crossref. Treat its output as a draft; still check capitalization, names, and source fit before inserting into a final manuscript.

Use `scripts/apa_intext_ref_check.py` on plain-text or Markdown drafts to detect likely APA in-text/reference mismatches. Treat its output as a heuristic report; manually review complex citations, edited books, translated works, organization authors, and non-APA styles.

## Integration With Academic Skills

- With `academic-paper`: this skill can supply the literature matrix, recommended sources by section, citation insertion log, and APA-compliant reference list for citation-check or revision work.
- With `academic-pipeline`: this skill should behave like a lightweight integrity sub-stage for citation insertion. It must not skip reference existence, citation-context, or claim-source checks.
- With `academic-paper-reviewer`: use reviewer-style lenses to challenge weak citation fit before delivery, especially for methodology, evidence sufficiency, literature integration, and overclaiming.
