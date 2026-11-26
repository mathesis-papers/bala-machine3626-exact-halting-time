# A restoring and divisor-sum proof of Bala's machine-3626 conjecture of 11 September 2026, OEIS A393210, Comments, revision 18: extending Sequence Machine (2026) and Wolfram (2026)

**Authors:** Haobo Ma, Wenlin Zhang

Extending the pointwise formula recorded by Sequence Machine (18 April 2026) and Wolfram's (2026) worst-case analysis, we prove Peter Bala's conjecture dated 11 September 2026 in the Comments of OEIS A393210, revision 18, also stated in A069517, Formula, revision 31. For every positive integer n, the one-sided Turing machine 3626 halts after 4*2^v2(n)-3 transitions, including its final boundary crossing. A restoring block computation gives the recurrence T_(k+1)=2*T_k+3; the signed Möbius–totient divisor sum in the conjecture has the same value. The proof also gives exact timing statistics and the formulas for the two comparison machines in the same comment. A general weighted divisor identity gives the companion formulas in A069517 and A296306, including a correction to the latter entry's stated value on powers of two. The companion ordinary generating series recover Stephan's (2003) family.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24405774](https://doi.org/10.5281/zenodo.24405774)
- Concept DOI: [https://doi.org/10.5281/zenodo.24405773](https://doi.org/10.5281/zenodo.24405773)
- License: CC-BY-4.0
- Version: 3
- Mathesis record: [bala-machine3626-exact-halting-time](https://mathesis-omega-research.apps.chrono-ai.fun/papers/bala-machine3626-exact-halting-time?version=3)

## How to cite

Haobo Ma, Wenlin Zhang (2026). A restoring and divisor-sum proof of Bala's machine-3626 conjecture of 11 September 2026, OEIS A393210, Comments, revision 18: extending Sequence Machine (2026) and Wolfram (2026). Mathesis, version 3. https://doi.org/10.5281/zenodo.24405774

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |
| Corollary (s10) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |
| Corollary (s11) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |
| Corollary (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |
| Corollary (s8) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |
| Corollary (s9) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/bala-machine3626-exact-halting-time/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/bala-machine3626-exact-halting-time/bala-machine3626-exact-halting-time/zh/) · [Read in English](https://papers.trureturing.org/bala-machine3626-exact-halting-time/bala-machine3626-exact-halting-time/en/)

[Slides](https://papers.trureturing.org/bala-machine3626-exact-halting-time/bala-machine3626-exact-halting-time/slides/) ([sources](books/bala-machine3626-exact-halting-time/slides/)) · [Videos](https://papers.trureturing.org/bala-machine3626-exact-halting-time/bala-machine3626-exact-halting-time/films/) ([sources](books/bala-machine3626-exact-halting-time/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/bala-machine3626-exact-halting-time/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `rem-exact-time` | variant | `D5/S0/Computability/BinaryMachine/Machine3626.result` |
| `lem-restoring-block` | special case | `D5/S0/Computability/BinaryMachine/Machine3626.block_first_crossing` |
| `rem-comparison-machines` | none | — |
| `rem-distribution` | none | — |
| `rem-weights` | none | — |
| `rem-mixed` | variant | `D5/S0/Computability/BinaryMachine/Machine3626.result` |
| `rem-signed` | none | — |
| `rem-companions` | none | — |
| `rem-series` | none | — |
| `rem-ratio` | none | — |
| `rem-cubic` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/review.json).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/bala-machine3626-exact-halting-time/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
