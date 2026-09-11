"""Editorial dispositions after reading retrieval candidates and source locators.

Unlisted entries become dated source drafts. Similarity scores never merge cards.
Existing cards keep their identity and status; additional source notes are attached.
"""
REUSE = {}
MERGE = {}
CATEGORIES = {}
REASONS = {}

def reuse(n, *ids, reason='Same question or identified source formulation; preserve the existing problem ID and add the dated source note.'):
    REUSE[n] = [f'TCS-{i:04}' if isinstance(i,int) else i for i in ids]
    REASONS[n] = reason

def merge(n, other, reason='Repeated formulation of the same target in another downloaded source.'):
    MERGE[n] = other
    REASONS[n] = reason

def category(numbers, name):
    for n in numbers: CATEGORIES[n] = name

for n,identifier in {
    2:3,4:1004,6:1005,7:1006,8:1007,11:1008,12:1009,14:1010,
    15:1011,16:1012,18:1015,19:1016,20:1017,22:1018,23:1019,
    25:1020,29:1021,30:1022,31:1023,33:1024,
    41:6581,43:6543,46:6605,51:6603,53:1063,56:1041,57:1043,
    58:1047,63:1054,64:1056,66:6,70:5307,73:6638,77:771,86:6594,
    88:1025,89:1026,92:1029,93:1030,97:1033,107:1,
    111:4675,140:6500,151:1115,152:11,153:1116,154:1117,157:1118,
    158:1119,159:1120,187:1,188:4,194:6603,
    308:1,310:557,322:6503,328:1,329:2,330:18,331:6,
    332:12,334:21,335:14,336:25,337:24,338:3,
    359:1,360:21,361:2,362:25,365:6,366:3,367:37,
}.items(): reuse(n,identifier)
reuse(17,1013,1014,reason='The library groups the paired expander/condenser formulations; both already have separate saved IDs, so attach the note to both without merging those existing records.')
reuse(62,1052,1053,reason='This library entry groups two numbered depth-three lower-bound targets already represented by separate IDs.')
reuse(91,1027,1028,reason='The source annotation groups the bipartiteness tester question and its vertex-sampling conjecture; both existing targets are retained.')
reuse(95,1031,1032,reason='The grouped local-reduction question has two previously saved source variants.')
merge(364,38)
reuse(84,6593,6595,reason='The source groups deterministic ETH and SETH, already represented by two individually reviewed cards. Retain both IDs.')
reuse(386,6558)
reuse(520,163,reason='The existing word-equation complexity question is the associative-unification complexity gap; attach the dated survey direction without claiming a new resolution.')
reuse(524,6648)
reuse(549,4577,reason='Both ask decidability of the discrete Skolem problem; the survey additionally identifies the unresolved order-five case.')
reuse(550,6565)
# Do not identify integer randomized 3SUM with an older, unspecified 3SUM
# index label, or recovery below sqrt(n) with fixed-power detection hardness.
REUSE.pop(310)
REASONS.pop(310)

# Topic assignments are about the individual statements, not every topic of a book.
category([14,15,16,25,36,98,99], 'Coding and information theory')
category([21], 'Cryptography')
category([34,52,55,103,107,108,190,195,205], 'Computational complexity')
category([35], 'Pseudorandomness and derandomization')
category([38,39,40], 'Beyond worst-case and average-case analysis')
category([43], 'Learning theory')
category([44], 'Pseudorandomness and derandomization')
category([57,58], 'Communication complexity and Boolean function analysis')
category([69,73,74], 'Scheduling and packing')
category([84], 'Fine-grained complexity')
category([110,111], 'Parameterized and exact algorithms')
category([116,117,118,119], 'Approximation algorithms and hardness of approximation')
category([140,*range(161,171),*range(246,253)], 'Structural graph theory')
category([253], 'Computational geometry and metric spaces')
category([196], 'Quantum computation')
category([192,193], 'Counting and enumeration')
category([286], 'Distributed, parallel and sublinear algorithms')
category([326], 'Cryptography')
category([329,361,362], 'Proof complexity')
category([332,364], 'Beyond worst-case and average-case analysis')
category([333], 'Cryptography')
category([384], 'Quantum computation')
category([403], 'Communication complexity and Boolean function analysis')
category([404], 'Distributed, parallel and sublinear algorithms')
category([453], 'Computational geometry and metric spaces')
category([493], 'Constraint satisfaction')
category([497,498,507], 'Algebraic computation')
category([547,548], 'Learning theory')
