# A restoring and divisor-sum proof of Bala's machine-3626 conjecture

Sequence Machine's archived A393210 record of 18 April 2026 already gives
the zero-based answer `a(k)=2*xor(k,k+1)-1`, with 10,000-term comparisons:
`https://github.com/jonmaiga/sequence-machine-data/blob/adf7a8346dc74ed9fec9462652611d740e33ec0b/oeis/A393/A393210.programs.json`.
For `n=k+1` this is `4*2**v2(n)-3`. The note supplies the all-input
restoring proof and its signed Möbius–totient identity, rather than claiming
discovery of the pointwise expression.

This extends Stephen Wolfram's 2026 worst-case timing analysis with an
individual-input restoring proof and the signed divisor-sum identity at
OEIS A393210, Comments revision 18, dated 11 September 2026. The maximum
time on length-`l` inputs, `2**(l+1)-3`, reproduces Wolfram's earlier closed
form. See his article's sections
"Runtimes in s = 2, k = 2 Machines" and "Computing the Same Functions at
Different Speeds":
`https://writings.stephenwolfram.com/2026/01/p-vs-np-and-the-difficulty-of-computation-a-ruliological-approach/`.

The divisor-power ordinary generating series reproduce Ralf Stephan's 2003
theorem, section 2, equation (2.1), for positive integer parameter `c=2**a`;
the same coefficient argument permits real `a>=0` here:
`https://arxiv.org/abs/math/0307027`.
The cubic power sum underlying A318935 already appears as `T` on page 102 of
P. J. C. Lamont's 1982 paper,
`https://doi.org/10.1017/S001309150000420X`.
Bannister, Cheng, Devanny and Eppstein's 2013 preprint already proves both
the exact binary-digit partial-sum formula and its asymptotic; its journal
version has the same result in section 2.3, Lemma 9, page 182:
`https://doi.org/10.7155/jgaa.00318`.

For every positive integer `n`, the first boundary-crossing time is
`4 * 2**v2(n) - 3`, and every tape symbol is restored. The note proves that this
equals Bala's signed Möbius–totient divisor sum, stated on 11 September 2026 in
OEIS A393210 (Comments revision 18) and A069517 (Formula revision 31).
It also proves `H_3589(n)=2*v2(n)+1` and `H_3197(n)=2-(-1)**n`, exact
timing distributions, arbitrary-weight divisor identities, and the four
statements labelled conjectures in A296306, with earlier formulas credited.
The A296306 support formula is corrected to `m(2**j)=2` for every `j>=1`.
The note distinguishes A010684's declared one-based arithmetic indexing
from its usual zero-based sequence indexing. The cubic companion A318935
and the A080277/A000695 partial-sum relations are included.

## Files and rebuilding

- `note.tex`: complete written proofs, references, and coverage table.
- `note.pdf`: typeset note.
- `metadata.json`: scientific identity, creators, license, and mathematical evidence.
- `verify.py`: Python 3 standard-library exact finite checks.
- `finite-checks.json`: the numerical ranges and comparison results.
- `reference-prefixes.json`: indexed numerical prefixes of the cited OEIS entries,
  with source URLs and entry revision numbers.
- `b393210.txt`: Sean A. Irvine's 1000-term OEIS reference table.

Build with Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, with a standard LaTeX distribution:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is included in the TeX source; BibTeX is unnecessary.
The source archive has no required external figures or bibliography files.

Run the exact finite checks:

```sh
python3 verify.py --output finite-checks.json
```

The included reference table from `https://oeis.org/A393210/b393210.txt` contains
1000 terms and is compared by default. Its path can also be selected explicitly:

```sh
python3 verify.py --oeis-bfile b393210.txt --output finite-checks.json
```

The checks simulate inputs from 1 through 65536 for each of machines 3626,
3589 and 3197 directly from their transition rules. They test tape restoration
and 2250 short higher/right contexts, and evaluate the signed divisor formulas
for inputs from 1 through 4096. The same range covers signed transforms,
arbitrary polynomial weights, quadratic generating coefficients, binary digit
sums and the cubic weighted identity. Divisor-power ratios are compared for
primes 2, 3, 5 and 7 and exponents 0 through 4. Exact length-class means and
maxima are compared through binary length 16. Every term in the included
OEIS prefixes is compared, preserving each entry's actual offset. The
proofs in `note.tex` establish the unrestricted statements; the finite checks
are additional exact comparisons.

## Lean declarations

The fixed mathematical source is
`https://github.com/the-omega-institute/trureturing/blob/3d88df0f99ef3c8bfb034fa52be669b13746a844/D5/S0/Computability/BinaryMachine/Machine3626.lean`.
In namespace `D5.S0.Computability.BinaryMachine.Machine3626`,
`block_first_crossing` supplies the trace of length `4*2**k-3` from a block
`0**k 1 higher` with empty right context to its first actual crossing.
`positive_input_first_crossing` supplies the block decomposition and trace
for every positive input. `result` supplies a terminating trace whose natural
length, cast to the integers, equals the signed Möbius–totient sum.
These statements have a terminal `none` endpoint rather than a final-tape
value. The written block lemma proves restoration in arbitrary right contexts;
the comparison machines and all arithmetic generalizations also have written
proofs. The finite checker concerns the explicit numerical ranges above.

## Creators and license

1. Haobo Ma — ChronoAI Pte Ltd, Singapore.
2. Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

Copyright 2026 Haobo Ma and Wenlin Zhang. CC BY 4.0
(Creative Commons Attribution 4.0 International).
