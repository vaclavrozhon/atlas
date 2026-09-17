# TCS-7366: scope choice pending, 17 September 2026

Claimed by recovery-20260916. No card or completion-queue write has been made.
The existing target is O(n) words with O(m + log(n)^c(k) + occ) queries over
alphabet [0,n), deterministic polynomial preprocessing and linear query workspace.

Read Kociumaka–Radoszewski arXiv:2510.26264v1 (30 October 2025), SODA 2026
DOI 10.1137/1.9781611978971.68 (7 January 2026), Introduction, Table 1,
Theorems 1.1, 1.2, 1.5 and Conclusions pp. 31–32. The main improvement keeps
O(m + log(n)^k log log n + occ) query time. The conclusion asks to reduce
space further at this scale. Table 1 also attributes O(n) space with a larger
polylogarithmic query exponent to Chan et al. 2011, without a separate alphabet
comment for that row. Its existence alone therefore cannot certify our weak
target as a new open problem.

Read the original authors' CPM 2006 talk (cpm.cs.helsinki.fi/cpm06/03-tam.pdf):
the problem setup explicitly assumes a constant-size alphabet. Read the Springer
primary chapter abstract and two-page preview, DOI 10.1007/11780441_6, and the
2011 Journal of Discrete Algorithms abstract/metadata DOI 10.1016/j.jda.2011.04.004.
The matching bound is O(m + occ + log(n)^(k(k+1)) log log n). The 2011 full
paper was not accessible, so a general-alphabet extension was not verified.
Read Cohen-Addad–Feuilloley–Starikovskaya SODA 2019 primary paper, Introduction
and Figure 3: it repeats the older linear-space bound but does not resolve this
alphabet-scope ambiguity. Its growing-k lower bounds do not settle fixed k.
Tam's 2010 thesis was located at hub.hku.hk/handle/10722/65311; the full-text
link returned 403 and its contents were not read. Do not claim otherwise.

An asynchronous user question asks whether to retain the sharper source-style
query time O(m + log(n)^k log log n + occ) together with O(n) words (recommended),
or retain the existing arbitrary-polylog target with explicitly uncertain status.
No response yet. Do not change the target merely because time has elapsed.
Source PDFs/texts are cached under the usual recovery-20260916 source directory.
