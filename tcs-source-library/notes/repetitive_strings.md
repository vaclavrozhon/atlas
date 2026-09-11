# Indexing Highly Repetitive String Collections

Gonzalo Navarro

**Source year/version:** 2021. arXiv v10, 23 November 2022; survey associated with the 2021 publication.

[Source page](https://arxiv.org/abs/2004.02781) · [Local PDF](../pdf/repetitive_strings.pdf) · [Extracted text](../text/repetitive_strings.txt) · [Back to library](../README.md)

## Why included

A major synthesis of compressed indexing for repetitive texts and genomic collections.

## Reading scope

Whole-document pass for explicit unresolved questions, conjectures and research directions, including topics outside the selection category. Numbered lists and unnumbered statements are both included; related variants may share an entry.

This is a source inventory. The entries describe what this version presents as unresolved. Current open status has not been checked. Summaries can group related variants and are not substitutes for the source definitions.

The specialist pass aims to collect all explicit unresolved statements throughout the downloaded work, including outside its selection category. Exhaustiveness for implicit questions or every passage of a long book is not certified.

**Selected for:** S11. [Category coverage](../AREA_COVERAGE.md).

The broad implementation challenges have no single fixed mathematical resolution criterion. The BWT conjecture mentioned in the bibliography is already identified there as resolved. The resolved Burrows–Wheeler-transform conjecture is excluded. The construction entry covers the BWT, Lempel–Ziv and grammar subcases across pp.58–60; dynamism is recorded separately.

## Open questions and directions in the source

1. **Question:** Support fast random access to a string using O(r) words, where r counts BWT runs. — §3, BWT runs. [PDF p. 20](../pdf/repetitive_strings.pdf#page=20)

2. **Question:** Can run-length grammars be balanced with the guarantees available for ordinary grammars? — §4.1. [PDF p. 31](../pdf/repetitive_strings.pdf#page=31)

3. **Conjecture:** Extend the cited alignment-based representation to support most suffix-tree operations. — §7, alignment-based indexes. [PDF p. 57](../pdf/repetitive_strings.pdf#page=57)

4. **Research direction:** Turn the surveyed theoretical compressed indexes into competitive practical implementations. — §8.1. [PDF p. 57](../pdf/repetitive_strings.pdf#page=57)

5. **Research direction:** Build indexes for very large repetitive collections using resources proportional to compressed size. — §8.2, continues pp.59–60. [PDF p. 58](../pdf/repetitive_strings.pdf#page=58)

6. **Question:** Are there string families with non-overlapping Lempel–Ziv phrase count z_no=o(z_e), where z_e is the stated LZ-End variant? — §3, LZ-End measure. [PDF p. 14](../pdf/repetitive_strings.pdf#page=14)

7. **Question:** Are there string families with collage-system size c=o(z), even allowing general collage systems? — §3.5, collage systems. [PDF p. 19](../pdf/repetitive_strings.pdf#page=19)

8. **Question:** Are there string families with Lempel–Ziv size z=o(v), where v is the lexicographic parsing measure? — §3.7, lexicographic parsing. [PDF p. 22](../pdf/repetitive_strings.pdf#page=22)

9. **Question:** Can every string be represented in O(γ) words, where γ is its smallest attractor size? Can the O(γ log n) scale always be improved asymptotically? — §3.9, string attractors; also pp.24–25. [PDF p. 23](../pdf/repetitive_strings.pdf#page=23)

10. **Question:** What is the smallest reachable repetitiveness measure supporting efficient access or indexing? Specifically, obtain access in O(z_no) space and indexing in O(z_no) or O(v) space. — §3.10, reachability of repetitiveness measures. [PDF p. 26](../pdf/repetitive_strings.pdf#page=26)

11. **Research direction:** Develop efficient repetitive indexes supporting arbitrary text modifications, beyond appending/prepending and the restricted practical performance of existing constructions. — §8.2, dynamism. [PDF p. 60](../pdf/repetitive_strings.pdf#page=60)

## Further inspection

The following page list comes from a mechanical full-text marker scan. It includes false positives, historical questions, bibliography entries and solved conjectures; it is not an additional reviewed problem list.

[6](../pdf/repetitive_strings.pdf#page=6), [20](../pdf/repetitive_strings.pdf#page=20), [31](../pdf/repetitive_strings.pdf#page=31), [57](../pdf/repetitive_strings.pdf#page=57), [68](../pdf/repetitive_strings.pdf#page=68)

## Download provenance

- Retrieved: 2026-09-10T17:13:12.445596+00:00
- Pages: 76; bytes: 1,168,176
- SHA-256: `7b50e0287518458ab0cd51e10dce37633e9011d40e756f252e4b433347d57bf1`
- Final URL: https://arxiv.org/pdf/2004.02781

PDF pages are counted from one, including front matter. They may differ from printed page numbers. This local copy is for personal research; retain the original author/publisher distribution terms.
