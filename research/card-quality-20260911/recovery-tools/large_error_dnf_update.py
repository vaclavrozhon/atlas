from review import card,write,DATE
p,c=card('TCS-3799')
for r in c['references']:
 if r['id']=='bounded':
  r['year']=2019
  r['locator']='SIAM Journal on Computing 49(4), online 22 October 2019, print issue 2020; FOCS 2017 precursor. Constant-error approximate-degree result.'
c['references'].append(dict(id='dnf',title='The Approximate Degree of DNF and CNF Formulas',authors='Alexander A. Sherstov',year=2025,url='https://doi.org/10.1137/23M1557593',pdf_url='https://arxiv.org/pdf/2209.01584v1',locator='STOC 2022 precursor; expanded preprint 4 September 2022, Theorems 1.1–1.2, Corollary 1.3 and Section 1.2; SIAM Journal on Computing 54(3), 702–774, online 10 June 2025. Publisher abstract and preprint theorem scope checked.'))
c['context_blocks'].insert(2,dict(title='Depth-two results reach inverse-polynomial advantage',text='Sherstov’s STOC 2022 work, published in expanded journal form in 2025, proves near-linear approximate degree for polynomial-size constant-width DNF and CNF formulas. Its large-error theorem allows error 1/2−n^{-C} in the {0,1}-valued convention, for every fixed C; after rescaling to ±1 outputs this is 1−2n^{-C}. That gap is inverse polynomial, whereas this card demands an exponentially small gap. The theorem therefore does not resolve this question.',citation='dnf'))
c['context']='\n\n'.join(b['text'] for b in c['context_blocks'])
c['progress'].append(dict(date='2025-06-10',text='The journal version of Sherstov’s 2022 result gives depth-two near-linear bounds at constant error and inverse-polynomial advantage. Its Section 1.2 explicitly distinguishes that attainable error scale from smaller advantages.',citation='dnf'))
c['status_note']='Checked the full 2021 journal definitions and remaining question, the 2022 Bun–Thaler survey Section 8.3, and Sherstov’s expanded 2022 preprint Theorems 1.1–1.2 and Corollary 1.3 together with its June 2025 journal publication. The latter reaches inverse-polynomial rather than exponentially small advantage. Searches through 12 September 2026 found no resolution of the precise logarithmic-depth, exponentially-small-gap target; searches are not exhaustive.'
c['working_summary']['sentences'][-1]='Later depth-two DNF/CNF results reach inverse-polynomial advantage, leaving the exponentially small advantage in this question outside their guarantees.'
c['working_summary']['source_refs'].append('dnf')
c['quality_review']['changes'].append('Added the 2022/2025 depth-two DNF/CNF result, with its exact {0,1}-to-±1 error normalization and inverse-polynomial gap; corrected online-versus-print dates for the earlier journal result.')
c['quality_review']['checked_sources'] += ['https://doi.org/10.1137/23M1557593','https://arxiv.org/abs/2209.01584','https://doi.org/10.1561/0400000107','https://par.nsf.gov/servlets/purl/10417632']
write(p,c)
print('TCS-3799 subsequent-work update')
