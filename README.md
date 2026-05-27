# Academic Writing Citation Support

Academic Writing Citation Support is a Codex skill for strengthening academic manuscripts with verified scholarly citations and APA-style references.

It helps an AI writing assistant read an academic draft, identify unsupported claims, search for relevant scholarly literature, verify source metadata, insert in-text citations conservatively, and produce a traceable APA reference list.

## What It Does

- Finds claims in academic writing that need scholarly support.
- Builds search queries from the manuscript's actual concepts, methods, population, outcomes, and theory.
- Routes literature searches across suitable platforms such as Consensus, Elicit, Semantic Scholar, Crossref, Google Scholar, CNKI, Wanfang, Scite, PubMed, ERIC, IEEE Xplore, ACM Digital Library, PsycINFO, JSTOR, and other field databases.
- Verifies sources before citation insertion.
- Inserts APA in-text citations without disrupting the author's argument.
- Produces an APA reference list and a source trace.
- Flags weak, unverifiable, or mismatched sources instead of inventing citations.

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

## License

MIT License.
