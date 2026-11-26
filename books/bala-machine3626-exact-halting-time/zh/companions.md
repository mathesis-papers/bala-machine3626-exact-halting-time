# 二的幂还能数什么？

论文第 3 节利用一个简单的想法：带符号的 Möbius 和已在二的幂以外抵消，便可改变留下来的每个除数所带的权重。下文始终取 $n\ge1$、$v=\nu_2(n)$；空和为零。

::: {.remark #rem-weights title="任意除数权重" mathesis="collected:bala-machine3626-exact-halting-time:3:s5"}
对整数 $r\ge1$ 和任意定义在正整数上的复数值权重 $w$，
$$\sum_{d\mid n}m(d)^r w(d)=w(1)+2^r\sum_{j=1}^v w(2^j).$$
留下来的 $1$ 与各个 $2^j$ 分别带系数 $1$ 和 $2^r$。
:::

::: {.remark #rem-mixed title="互素计数的权重与一项抵消" mathesis="collected:bala-machine3626-exact-halting-time:3:s6"}
对整数 $r\ge1$、$s\ge0$，$\sum_{d\mid n}m(d)^r\varphi(d)^s$ 在 $s=0$ 时等于 $1+2^rv$；在 $s>0$ 时等于 $1+2^r(2^{sv}-1)/(2^s-1)$。前者数项数，后者求等比和。对每个整数 $k\ge1$，$\sum_{d\mid n}(2m(d)^k-m(d)^{k+1})=1$：$m(d)$ 为 0 或 2 的项都抵消。
:::

::: {.remark #rem-signed title="奇偶与错开一位的下标" mathesis="collected:bala-machine3626-exact-halting-time:3:s7"}
对整数 $r\ge1$，用权重 $\mu(d)$ 得 $\sum_{d\mid n}m(d)^r\mu(d)=1-2^r\mathbf 1_{2\mid n}$；改用 $(-1)^{d+1}\mu(d)$ 则得 $1+2^r\mathbf 1_{2\mid n}$。指示量在 $n$ 为偶数时等于 1，否则为 0。由于 $j>1$ 时 $\mu(2^j)=0$，只有 1 和 2 可能有贡献。第二个和在 $r=1$ 时，与 $(-1)^{n+1}\sum_{d\mid n}m(d)^2\mu(d)$ 一样，奇数给 1，偶数给 3。这是 [A010684](https://oeis.org/A010684)$(n-1)$，并不是 3197 号机器给出的第 $n$ 项。
:::

::: {.remark #rem-companions title="把同一串数字换一种进制来读" mathesis="collected:bala-machine3626-exact-halting-time:3:s8"}
令 $B(n)=(2\cdot4^v+1)/3$、$D(n)=2^{v+1}-1$（A276391 与 A038712）。对正整数 $n$，$B(2n)=4B(n)-1$、$D(2n)=2D(n)+1$，而 $B(2n-1)=D(2n-1)=1$。若 $G(x)=\sum_{n\ge1}B(n)x^n$，分开奇偶项得 $G(x)=4G(x^2)+x/(1+x)$，所以 $|x|<1$ 时 $G(x)=\sum_{j\ge0}4^j x^{2^j}/(1+x^{2^j})$。若 $\epsilon_i$ 是 $N$ 的二进制位，则 $\sum_{n=1}^N B(n)=\sum_{i\ge0}\epsilon_i4^i$：从 $N-1$ 到 $N$，按四进制读会增加一个高位的 1，消去比它低的那些 1。

令 $S(N)=\sum_{n=1}^N D(n)$、$S(0)=0$，论文给出 $S(N)=N+2\sum_{j\ge1}2^{j-1}\lfloor N/2^j\rfloor=N+2S(\lfloor N/2\rfloor)=\sum_{i\ge0}\epsilon_i(i+1)2^i$。特别地，$S(2^h-1)=(h-1)2^h+1$，且 $S(N)=N\log_2N+O(N)$。每个权重 $(i+1)2^i$ 都超过前面所有权重之和，因此最高的不同位决定和的大小。作为形式级数，$\prod_{i\ge0}(1+x^{(i+1)2^i})=\sum_{N\ge0}x^{S(N)}$。论文注明 Bannister 等人先前已证明渐近式与数位公式，并注明 A080277 乘积恒等式源自 Bala。
:::

::: {.remark #rem-series title="幂权重的两种级数" mathesis="collected:bala-machine3626-exact-halting-time:3:s9"}
对实数 $a\ge0$，令 $F_a(n)=\sum_{j=0}^{\nu_2(n)}2^{aj}$。下标 $j$ 对应的贡献恰好出现在 $2^j$ 的正倍数上，因此求等比和得到
$$\sum_{n\ge1}F_a(n)x^n=\sum_{j\ge0}\frac{2^{aj}x^{2^j}}{1-x^{2^j}}\quad (|x|<1),$$
$$\sum_{n\ge1}\frac{F_a(n)}{n^s}=\frac{\zeta(s)}{1-2^{a-s}}\quad (\Re s>\max\{1,a\}).$$
取 $a=1,2,3$ 分别得到 A038712、A296306、A318935；$F_0=v+1$，且 $\sum_{d\mid n}m(d)=2F_0(n)-1=H_{3589}(n)$。当权重 $c=2^a$ 为正整数时，普通生成级数已见于 Ralf Stephan 2003 年的结果。
:::

::: {.remark #rem-ratio title="任意素数下的除数比" mathesis="collected:bala-machine3626-exact-halting-time:3:s10"}
对素数 $p$，将 $n$ 写作 $p^u q$，其中 $p\nmid q$。每个除数唯一写成 $p^je$，其中 $0\le j\le u$、$e\mid q$。约去关于 $e$ 的共同正和，对实数 $s\ge0$ 得
$$\frac{\sum_{d\mid n}d^s}{\sum_{e\mid n,\ p\nmid e}e^s}=\sum_{j=0}^u p^{js}.$$
指数为非负整数时，比值为整数。取 $p=2,s=2$，记 $R(n)=(4^{v+1}-1)/3$。其值域正好是所有 $(4^h-1)/3$（整数 $h\ge1$）。当 $1\le j<2^h$ 时，两项的 2 进赋值相同，故 $R(2^h-j)=R(j)$。数出这段前缀中每种赋值出现的次数，得 $\sum_{j=1}^{2^h-1}R(j)=(2^h-1)(2^{h+1}-1)/3$。这些是 A296306 的四个结论；论文注明 David Radcliffe 的先前公式以及 M. F. Hasler 的先前解释。
:::

::: {.remark #rem-cubic title="立方伴随式" mathesis="collected:bala-machine3626-exact-halting-time:3:s11"}
取 $p=2,s=3$，所有除数的立方和与奇除数的立方和之比为 $Q(n)=(8^{v+1}-1)/7$。也可写成 $Q(n)=1+4\sum_{d\mid n,\ d>1}m(d)\varphi(d)^3$：对 $1\le j\le v$，$2^j$ 对应的项乘四后恰为 $8^j$。参见 A318935 与论文第 3 节所列的 Lamont、Sloane、Wu 和 Eldar 的先前工作。
:::

出处：Haobo Ma、Wenlin Zhang，[论文第 3 版，第 3 节](https://doi.org/10.5281/zenodo.24405774)。这一章讨论的是算术推论，不是 3626 号机器的额外磁带结论。
