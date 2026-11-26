# Two trips, no lasting change

Write 6 and 10 in binary: $110$ and $1010$. Both end in one zero. Feed them to Turing machine 3626, and both runs end after five steps with the tape exactly as it started. Try 12 ($1100$): one more trailing zero, but thirteen steps. This machine doesn't compute a new number. The interesting question is how long it takes to leave the old one intact.

## The exit is on the right

Number the cells $0,1,2,\ldots$ from right to left; cell $j$ holds the bit worth $2^j$. The tape extends left forever, with zeros in all unused cells. The head starts at cell 0 in state $A$. Each step writes a bit, moves one cell and updates the state. Moving right from cell 0 ends the run, and **that move counts**.

| State | Reads 0 | Reads 1 |
|---|---|---|
| $A$ | Write 0, move left, stay in $A$ | Write 1, move right, enter $B$ |
| $B$ | Write 1, move left, enter $A$ | Write 0, move right, stay in $B$ |

For 6, the tape reads `0 1 1` from the head leftward. The first two steps pass the zero and return from the first one. On step three, state $B$ changes the zero to a temporary one and sends the head left again. On step four, the same first one sends the head back. Step five erases the temporary mark and exits. The farther one is never touched. For 10 the higher bits are different, but the trip is the same.

## What makes the machine take two trips?

Let $u_k=0^k1w$, where $w$ is any finite string of higher bits followed by implicit zeros. There may or may not be cells to the right of the starting cell. Watch for a local event: **the first move right past the starting cell**, whether or not that move halts the whole machine.

::: {.lemma #lem-restoring-block title="Restoring first crossing" mathesis="collected:bala-machine3626-exact-halting-time:3:s2" status="written-proof" proof="proof-restoring-block" doi="10.5281/zenodo.24405774" source="Lemma 1, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/530"}
Start in state $A$ on the first cell of $u_k$, for any $k\ge0$, any higher bits $w$, and any finite right context $r$. At the first rightward crossing of the starting cell, all tape symbols have been restored. If $r$ is empty, the move exits; if $r=br'$ (nearest bit first), the state is $B$ with the head on $b$, leftward string $bu_k$, and remaining right context $r'$. The time is independent of both strings:

$$T_0=1,\qquad T_{k+1}=2T_k+3,\qquad T_k=4\cdot2^k-3.$$
:::

::: {.proof #proof-restoring-block}
Following Ma and Zhang, §2: with no zero before the first one, rule $A1$ crosses immediately without changing the bit. For $0u_k$, rule $A0$ enters $u_k$. The induction hypothesis brings the head back to the saved zero in state $B$ after $T_k$ moves; the presence of that extra cell prevents any earlier exit from the full tape. Rule $B0$ writes a temporary one and re-enters $u_k$ in state $A$. A second full $T_k$-step trip returns to the same cell, now marked one. Rule $B1$ changes it back to zero and makes the first crossing of the original starting cell. Each trip restores its block and never passes its own start before its final move. The three single moves and the two trips give the recurrence. Adding three gives $T_{k+1}+3=2(T_k+3)$, with $T_0+3=4$.
:::

## Why does a divisor sum give the same answer?

Every positive integer is uniquely $2^vq$ with $q$ odd. The exponent $v$, written $\nu_2(n)$, counts how many times you can divide by 2, or how many zeros end the binary numeral. For example, $12=2^2\cdot3$, so $v=2$. Zero is excluded: there is no first one on an all-zero tape, and state $A$ moves left forever.

Euler's totient $\varphi(d)$ counts integers from 1 to $d$ that are coprime to $d$. For $2^j$ with $j\ge1$, just the odd ones qualify, so $\varphi(2^j)=2^{j-1}$. The Möbius function $\mu(e)$ gives zero if a prime square divides $e$; otherwise it gives a sign according to the number of distinct primes, with $\mu(1)=1$. Bala's two sums are

$$m(n)=\sum_{e\mid n}(-1)^{e+1}\mu(e),\qquad C(n)=\sum_{d\mid n}m(d)^2\varphi(d).$$

::: {.remark #rem-exact-time title="The paper’s main theorem" mathesis="collected:bala-machine3626-exact-halting-time:3:s1"}
For every positive $n$, the machine halts, restores every tape bit, and its first boundary-crossing time satisfies $H(n)=C(n)=4\cdot2^{\nu_2(n)}-3$. The machine half of this result is the restoring argument with $k=\nu_2(n)$ and an empty right context.
:::

Pair each odd divisor $e$ with $2e$ when $n$ is even. Both the Möbius sign and the sign from parity flip, so the pair contributes $2\mu(e)$. Terms divisible by 4 give zero. If the odd part $q$ exceeds 1, choosing whether to include each distinct prime of $q$ gives the expansion of $\prod_{p\mid q}(1-1)$, and the contributions cancel. Only $m(1)=1$ and $m(2^j)=2$ for $j\ge1$ survive. In particular, $m(4)=2$, not 4: this is the paper's correction to a comment in [A296306](https://oeis.org/A296306).

For 12 the divisors are 1, 2, 3, 4, 6 and 12, but only the powers of two $1,2,4$ count. So $C(12)=1+4\cdot1+4\cdot2=13$. In general, $C(n)=1+4\sum_{j=1}^v2^{j-1}=4\cdot2^v-3$. On odd inputs the sum is empty and the answer is one. The run and the divisor sum see the same feature of the input: how many factors of 2 can be peeled off.

::: {.film src="001-restoring-block"}
Watch how temporarily marking one zero turns one trip into two.
:::

## From one input to a whole range

::: {.remark #rem-distribution title="Timing distribution" mathesis="collected:bala-machine3626-exact-halting-time:3:s4"}
Among $1,\ldots,N$ ($N\ge1$), there are $\lfloor N/2^k\rfloor-\lfloor N/2^{k+1}\rfloor$ inputs with exactly $k\ge0$ trailing zeros and time $4\cdot2^k-3$: subtract the multiples with at least one extra zero. Split $2^v$ as $1+\sum_{j=1}^{v}2^{j-1}$, and the total time is $N+4\sum_{j\ge1}2^{j-1}\lfloor N/2^j\rfloor$. Among the $2^{\ell-1}$ inputs of binary length $\ell\ge1$, the average is $2\ell-1$ and the maximum is $2^{\ell+1}-3$, reached only by $2^{\ell-1}$. The average grows linearly in the number of bits, but the slowest runs grow much faster.
:::

::: {.remark #rem-comparison-machines title="The comparison machines" mathesis="collected:bala-machine3626-exact-halting-time:3:s3"}
Under the same initialization and boundary convention, both other machines restore all bits for positive inputs. Machine 3589 turns at the first one and exits directly in $2v+1$ steps. Machine 3197 takes $2-(-1)^n$ steps: one on even inputs, three on odd inputs. The recurrence for 3626 does not carry over to different rules.
:::

## Sources and scope

Haobo Ma and Wenlin Zhang, [paper, version 3](https://doi.org/10.5281/zenodo.24405774), §§1–4, CC BY 4.0. Peter Bala posed the question on September 11, 2026, in [A393210](https://oeis.org/A393210), Comments revision 18, and [A069517](https://oeis.org/A069517), Formula revision 31. The paper credits Sequence Machine's April 18, 2026 record of the equivalent pointwise XOR formula and Stephen Wolfram's 2026 worst-case formula. The contribution is not the first appearance of the answer: it is a proof for every positive input that connects a restoring trace to the signed divisor sum. The paper also credits Antti Karttunen and Amiram Eldar for prior descriptions of the support of the signed Möbius sum in A069517.

The pinned Lean code proves that the first boundary-crossing trace on positive inputs has length equal to the divisor sum. Its public halting endpoint does not carry the final tape. This does not certify the restoring lemma with arbitrary right context or all of the paper's corollaries. The [restoring-lemma request](https://github.com/the-omega-institute/trureturing-requests/issues/530) describes the missing statement and the proof it can reuse. The examples illustrate the proof, not replace it. The paper does not address the A000695 tree conjecture or the behavior of machine 924.
