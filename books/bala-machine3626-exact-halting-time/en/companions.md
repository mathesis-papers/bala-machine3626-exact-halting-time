# What else the powers of two count

The paper's §3 follows a simple idea: once the signed Möbius sum has cancelled on all divisors except powers of two, you can change the weight of each surviving divisor. The formulas below are for $n\ge1$ and $v=\nu_2(n)$; a sum with no terms is zero.

::: {.remark #rem-weights title="Arbitrary divisor weights" mathesis="collected:bala-machine3626-exact-halting-time:3:s5"}
For each integer $r\ge1$ and any complex-valued weight $w$ on the positive integers,
$$\sum_{d\mid n}m(d)^r w(d)=w(1)+2^r\sum_{j=1}^v w(2^j).$$
The surviving weights at $1$ and at $2^j$ are multiplied by $1$ and $2^r$, respectively.
:::

::: {.remark #rem-mixed title="Totient weights and a cancellation" mathesis="collected:bala-machine3626-exact-halting-time:3:s6"}
For integers $r\ge1$ and $s\ge0$, the sum $\sum_{d\mid n}m(d)^r\varphi(d)^s$ is $1+2^rv$ if $s=0$, and $1+2^r(2^{sv}-1)/(2^s-1)$ if $s>0$. These are the constant-weight and geometric-sum cases. For every integer $k\ge1$, $\sum_{d\mid n}(2m(d)^k-m(d)^{k+1})=1$: a term with $m(d)=0$ or $2$ contributes zero.
:::

::: {.remark #rem-signed title="Parity and a one-place shift" mathesis="collected:bala-machine3626-exact-halting-time:3:s7"}
For integer $r\ge1$, the weight $\mu(d)$ gives $\sum_{d\mid n}m(d)^r\mu(d)=1-2^r\mathbf 1_{2\mid n}$; the weight $(-1)^{d+1}\mu(d)$ gives $1+2^r\mathbf 1_{2\mid n}$. Here the indicator equals one on even inputs and zero otherwise. Only $1$ and $2$ can contribute since $\mu(2^j)=0$ for $j>1$. The second sum at $r=1$, and $(-1)^{n+1}\sum_{d\mid n}m(d)^2\mu(d)$, give 1 on odd inputs and 3 on even inputs. They are [A010684](https://oeis.org/A010684)$(n-1)$, not the term at $n$ that machine 3197 gives.
:::

::: {.remark #rem-companions title="Reading the same digits in another base" mathesis="collected:bala-machine3626-exact-halting-time:3:s8"}
Put $B(n)=(2\cdot4^v+1)/3$ and $D(n)=2^{v+1}-1$ (A276391 and A038712). For positive $n$, $B(2n)=4B(n)-1$, $D(2n)=2D(n)+1$, and $B(2n-1)=D(2n-1)=1$. If $G(x)=\sum_{n\ge1}B(n)x^n$, the odd/even split gives $G(x)=4G(x^2)+x/(1+x)$, hence $G(x)=\sum_{j\ge0}4^j x^{2^j}/(1+x^{2^j})$ for $|x|<1$. For binary digits $\epsilon_i$ of $N$, $\sum_{n=1}^N B(n)=\sum_{i\ge0}\epsilon_i4^i$: changing $N-1$ to $N$ adds one base-four digit and removes its lower ones.

For $S(N)=\sum_{n=1}^N D(n)$, with $S(0)=0$, the paper gives $S(N)=N+2\sum_{j\ge1}2^{j-1}\lfloor N/2^j\rfloor=N+2S(\lfloor N/2\rfloor)=\sum_{i\ge0}\epsilon_i(i+1)2^i$. In particular $S(2^h-1)=(h-1)2^h+1$ and $S(N)=N\log_2N+O(N)$. Each weight $(i+1)2^i$ exceeds the sum of the preceding weights, so changing the highest differing digit orders the sums. This yields $\prod_{i\ge0}(1+x^{(i+1)2^i})=\sum_{N\ge0}x^{S(N)}$ as a formal series. The paper credits Bannister et al. for prior proof of the asymptotic and digit formula, and Bala for the A080277 product identity.
:::

::: {.remark #rem-series title="Two series for the power weights" mathesis="collected:bala-machine3626-exact-halting-time:3:s9"}
For real $a\ge0$, write $F_a(n)=\sum_{j=0}^{\nu_2(n)}2^{aj}$. A term with index $j$ occurs exactly at the positive multiples of $2^j$, so geometric sums give
$$\sum_{n\ge1}F_a(n)x^n=\sum_{j\ge0}\frac{2^{aj}x^{2^j}}{1-x^{2^j}}\quad (|x|<1),$$
$$\sum_{n\ge1}\frac{F_a(n)}{n^s}=\frac{\zeta(s)}{1-2^{a-s}}\quad (\Re s>\max\{1,a\}).$$
The respective powers $a=1,2,3$ give A038712, A296306 and A318935; $F_0=v+1$ and $\sum_{d\mid n}m(d)=2F_0(n)-1=H_{3589}(n)$. Ralf Stephan's 2003 result already gives the ordinary series for positive-integer weights $c=2^a$.
:::

::: {.remark #rem-ratio title="A divisor ratio at any prime" mathesis="collected:bala-machine3626-exact-halting-time:3:s10"}
For a prime $p$ and $n=p^u q$ with $p\nmid q$, every divisor is uniquely $p^je$, with $0\le j\le u$ and $e\mid q$. Factoring the common positive sum over $e$ gives, for real $s\ge0$,
$$\frac{\sum_{d\mid n}d^s}{\sum_{e\mid n,\ p\nmid e}e^s}=\sum_{j=0}^u p^{js}.$$
This ratio is integral at nonnegative integer exponents. At $p=2,s=2$, put $R(n)=(4^{v+1}-1)/3$. Its value set is exactly $(4^h-1)/3$ for integers $h\ge1$. For $1\le j<2^h$, $R(2^h-j)=R(j)$ since the two arguments have the same valuation. Counting each valuation in this prefix gives $\sum_{j=1}^{2^h-1}R(j)=(2^h-1)(2^{h+1}-1)/3$. These are the four A296306 claims; the paper credits David Radcliffe's earlier formula and M. F. Hasler's earlier explanations.
:::

::: {.remark #rem-cubic title="The cubic companion" mathesis="collected:bala-machine3626-exact-halting-time:3:s11"}
For $p=2$ and $s=3$, the ratio of the sum of cubes of all divisors to the sum of cubes of the odd divisors is $Q(n)=(8^{v+1}-1)/7$. Equivalently, $Q(n)=1+4\sum_{d\mid n,\ d>1}m(d)\varphi(d)^3$: each $2^j$ with $1\le j\le v$ contributes $8^j$ after multiplication by four. See A318935 and the antecedents credited in §3: Lamont, Sloane, Wu and Eldar.
:::

Source: Haobo Ma and Wenlin Zhang, [version 3, §3](https://doi.org/10.5281/zenodo.24405774). These are arithmetic consequences, not additional claims about machine 3626's tape.
