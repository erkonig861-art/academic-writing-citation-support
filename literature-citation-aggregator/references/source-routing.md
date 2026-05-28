# Source Routing

Use this guide when deciding where to search and how to verify literature.

## Discovery Tools

- Local/project corpus: first stop for project-specific claims, unpublished materials, red notes, interviews, archives, scripts, field notes, scores, datasets, user-provided PDFs, and earlier chapter drafts. Use local search before web search when the claim depends on materials the public web cannot know.
- Consensus: best first stop for quick peer-reviewed discovery, research summaries, study-type filtering, and broad evidence searches. Use short claim-based queries, then open references and verify externally.
- Elicit: best for systematic-review style extraction tables. Use when the user needs sample, intervention, outcome, method, or finding columns across many papers.
- Semantic Scholar: broad free discovery and citation graph. Use to find related papers, influential works, and recent papers missed by AI summary tools.
- OpenAlex or The Lens: broad bibliographic search and metadata backup. Use when coverage or DOI metadata is uncertain.
- Scite: use for high-stakes or central claims to inspect whether later papers support, contrast, or merely mention the candidate source.
- Google Scholar: useful for broad backup search and citation chasing, but verify metadata elsewhere because scraping and formatting are inconsistent.
- Crossref: verification source for DOI metadata, journal, volume, issue, pages, and publisher. Crossref is not enough to prove relevance; it verifies identity.
- Publisher pages: use as final authority when Crossref metadata is missing or inconsistent.
- CNKI, Wanfang, VIP: use for Chinese-language scholarship, local policy/context, China-specific studies, and Chinese-language disciplinary literature.
- ERIC / Education Source / JSTOR: use for education, pedagogy, higher education, and learning theory claims.
- Discipline-specific databases: use field databases appropriate to the paper's discipline, such as PubMed for medicine, ERIC for education, IEEE Xplore/ACM Digital Library for computing and engineering, PsycINFO for psychology, Business Source/ABI-INFORM for business, JSTOR/Project MUSE for humanities and social sciences, SSRN/HeinOnline for law and policy, or other institutional library databases when accessible.
- Web of Science / Scopus: use when the task needs a reproducible database-style search, citation chasing, or journal-quality screening.
- Library catalogs / WorldCat / national libraries / university libraries: use for books, edited volumes, theses, critical editions, local gazetteers, theater yearbooks, archive catalogs, and humanities sources that may not have DOI records.
- Official and archival sources: use for policy, law, statistics, institutional facts, performance programs, festival records, intangible-cultural-heritage records, gazetteers, and project-specific factual claims.

## Platform Access and User Inputs

The skill selects platforms and builds queries, but it must not imply that Codex can bypass logins, subscriptions, paywalls, CAPTCHAs, institutional access, or download limits. Use the least sensitive input needed for each search. Do not upload a private manuscript to a third-party platform unless the user explicitly authorizes that destination.

| Platform group | How to use it | What the user may need to provide |
|---|---|---|
| Local/project corpus | Search user-provided files, project folders, PDFs, DOCX drafts, interviews, scripts, scores, notes, and prior source tables before external search for project-specific claims. | File paths, corpus folders, permission to inspect local documents, or extracted text when files are inaccessible. |
| Consensus / Elicit | Run short claim-based queries to discover candidate studies, summaries, and extraction tables. | Logged-in browser session for paid or personalized features; exported table, screenshot, titles, DOI list, or copied results if direct access is unavailable. |
| Semantic Scholar / OpenAlex / Crossref | Search metadata, DOI records, authors, years, publication venue, and citation relationships. | Usually no account; provide more precise title, author, DOI, or year when metadata is ambiguous. |
| Google Scholar | Use as a backup discovery and citation-chasing source. | User may need to handle CAPTCHA, login, or region restrictions manually; verify final metadata elsewhere. |
| Scite | Check whether later papers support, contrast, or mention a candidate source. | User account or subscription when required; copied Scite results or exported notes if Codex cannot access the page. |
| Scopus / Web of Science | Use for database-style searches, citation chasing, reproducible screening, and journal-quality checks. | Institutional login, library access, VPN, or exported RIS/BibTeX/CSV/search results. |
| CNKI / Wanfang / VIP | Search Chinese-language scholarship, local context, policy background, and China-specific studies. | Logged-in browser session, institutional access, exported citation records, abstracts, PDFs, or screenshots. |
| Library catalogs / WorldCat / national libraries | Verify books, critical editions, local gazetteers, dissertations, theater yearbooks, and non-DOI humanities sources. | Library links, ISBN, call numbers, scans of copyright pages, or local PDF/book access when metadata is inconsistent. |
| Official records / archives | Verify factual, policy, historical, legal, local-institution, and performance-event claims. | Archive identifiers, official URLs, scans, field notes, program booklets, recordings, or user-provided documents. |
| PubMed / ERIC | Search public biomedical, health, education, and learning-science records. | Usually no account for metadata; user-provided full text or institutional access if needed. |
| IEEE Xplore / ACM Digital Library | Search computing, engineering, systems, algorithm, HCI, and technical evaluation papers. | Institutional login or user-provided DOI, PDF, BibTeX/RIS, or exported citation data for full text. |
| PsycINFO / Education Source / JSTOR / HeinOnline / Business Source | Search psychology, education, humanities, law, policy, and business databases. | Institutional subscription, library login, VPN, or exported records and PDFs. |
| Publisher pages / DOI resolver | Verify final title, authors, year, venue, volume, issue, pages, DOI, and publication status. | Usually no account for metadata; user-provided PDF or institutional access for paywalled full text. |

Default routing pattern: use one discovery source to find candidates and one verification source to confirm identity and metadata. For central claims, add a citation-context check through abstracts, methods, full text, or a user-provided PDF. For project-specific claims, reverse the order: check the local/project corpus first, then use external sources only for framing, comparison, or metadata verification.

## Evidence-Class Routing

| Claim evidence class | Start with | Verify with | Typical stop condition |
|---|---|---|---|
| Theory / definition | Seminal books, handbooks, review articles, field theory papers | Publisher page, DOI/Crossref, library catalog, Google Books, JSTOR/Project MUSE | Stable concept source supports the definition without overextension. |
| Prior findings | Reviews, meta-analyses, empirical databases, discipline indexes | DOI/Crossref, publisher page, PubMed/ERIC/Semantic Scholar/OpenAlex | Source matches construct, population/context, method, and certainty level. |
| Method / instrument | Methodology texts, validation papers, instrument manuals, reporting standards | DOI/publisher page, manual, organization site, library catalog | Source directly supports the method or validity claim. |
| Factual / contextual | Official records, statistics, policy texts, gazetteers, archives | Government site, archive record, library catalog, official publication | Source is authoritative for the fact and date/context. |
| Humanities / interpretive | Critical editions, primary texts, commentaries, reception history, monographs | Publisher/library catalog, JSTOR/Project MUSE, CNKI/Wanfang, copyright page | Source supports textual wording, interpretation, or reception claim. |
| Case-material | Interviews, scripts, scores, programs, recordings, field notes, archival folders | Local file, archive ID, transcript metadata, program scan, score page | Case evidence directly supports the specific case claim. |
| Project-specific | User corpus, prior chapter source map, local notes, project source library | Local path, version/date, user-provided metadata | Project evidence is identified or the claim is marked as needing primary evidence. |

## Query Construction

Build queries from the source paragraph:
- Construct: the central concept, theory, variable, framework, or phenomenon.
- Population/context: the target participants, setting, country/region, institution type, or field.
- Method/intervention: the research design, instructional approach, treatment, instrument, analytical method, or implementation process.
- Outcome: the dependent variable, performance indicator, attitude, behaviour, skill, experience, or measured effect.

Use 2-4 search variants per important claim:
- exact construct + population + outcome
- theory/model + construct
- instrument/rubric + outcome
- broader review/meta-analysis variant

For discipline-specific manuscripts, include at least one query variant using the field's own vocabulary. Examples:
- education: `pedagogical intervention`, `student achievement`, `learning outcomes`, `formative assessment`
- psychology: `self-efficacy`, `motivation`, `cognitive load`, `validated scale`
- health/medicine: `clinical trial`, `intervention`, `patient outcomes`, `systematic review`
- business/management: `organizational performance`, `strategy`, `leadership`, `case study`
- computing/engineering: `algorithm`, `system evaluation`, `usability`, `benchmark`
- humanities/social sciences: `discourse`, `identity`, `practice`, `interpretive analysis`
- Chinese humanities: `版本`, `校注`, `接受史`, `地方志`, `曲谱`, `剧本`, `声腔`, `曲牌`, `口述史`, `非物质文化遗产`

## Evidence Matching

Rank candidate sources:
1. Direct match: same construct plus same or very similar population/intervention/outcome.
2. Strong adjacent match: same construct and outcome, adjacent population or discipline.
3. Theory/review support: explains mechanism or field-level consensus.
4. Background context only: useful in literature review, not enough for a specific empirical claim.

Reject candidates when:
- The title matches but abstract/methods do not support the claim.
- The source is unverifiable, lacks stable metadata, or appears in a questionable venue.
- The paper is outside the field and only loosely analogous.
- It would require overstating findings.
- The source has the wrong evidence class, such as using a broad review to prove a local archive fact, using a local interview to prove field-wide consensus, or using a general theory text to prove a specific score/performance detail.

## Trace Record

For each final source, record:
- claim or paragraph location
- exact inserted citation
- discovery platform and query
- verification source, DOI, or URL
- reason for selection
- caveat, if any
