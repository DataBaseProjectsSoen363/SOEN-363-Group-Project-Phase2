===== RECORD COUNT =====
1175

===== SHAPE =====
(1175, 10)

===== FIELD NAMES =====
['triage_id', 'visit_id', 'nurse_mrn', 'bp_systolic', 'bp_diastolic', 'hr_bpm', 'temp_fahrenheit', 'o2_sat', 'esi_priority', 'allergy_note']

===== DATA TYPES =====
triage_id            int64
visit_id             int64
nurse_mrn              str
bp_systolic          int64
bp_diastolic         int64
hr_bpm               int64
temp_fahrenheit    float64
o2_sat               int64
esi_priority           str
allergy_note           str

===== MISSING VALUES =====
triage_id            0
visit_id             0
nurse_mrn            0
bp_systolic          0
bp_diastolic         0
hr_bpm               0
temp_fahrenheit      0
o2_sat               0
esi_priority         0
allergy_note       211

===== HIDDEN MISSING VALUES (String 'N/A') =====
triage_id          0
visit_id           0
nurse_mrn          0
bp_systolic        0
bp_diastolic       0
hr_bpm             0
temp_fahrenheit    0
o2_sat             0
esi_priority       0
allergy_note       0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     triage_id  visit_id  nurse_mrn  bp_systolic  bp_diastolic  hr_bpm  temp_fahrenheit  o2_sat esi_priority allergy_note
483        484       493  MRN-10016          121            72      97             98.1      97        ESI-4          UNK
787        788       804  MRN-10018          112            85      80             99.6      95        ESI-2        Sulfa
243        244       247  MRN-10025          140            65      84            100.1      95        ESI-4        Sulfa
835        836       854  MRN-10018          102            90      67            100.9      99        ESI-2          UNK
281        282       286  MRN-10018          105            74      66            100.0      96        ESI-2          UNK

===== SUMMARY STATISTICS =====
         triage_id     visit_id  nurse_mrn  bp_systolic  bp_diastolic       hr_bpm  temp_fahrenheit       o2_sat esi_priority allergy_note
count   1175.00000  1175.000000       1175  1175.000000   1175.000000  1175.000000      1175.000000  1175.000000         1175          964
unique         NaN          NaN         10          NaN           NaN          NaN              NaN          NaN            5            4
top            NaN          NaN  MRN-10024          NaN           NaN          NaN              NaN          NaN        ESI-3        Latex
freq           NaN          NaN        140          NaN           NaN          NaN              NaN          NaN          259          263
mean     588.00000   750.330213        NaN   120.350638     74.869787    73.461277        99.544851    97.466383          NaN          NaN
std      339.33759  1235.309954        NaN    11.900837      8.932030    36.283546         2.913902     1.731171          NaN          NaN
min        1.00000     1.000000        NaN   100.000000     60.000000   -99.000000        97.000000    95.000000          NaN          NaN
25%      294.50000   299.500000        NaN   110.000000     67.000000    69.000000        98.000000    96.000000          NaN          NaN
50%      588.00000   608.000000        NaN   121.000000     75.000000    80.000000        99.100000    97.000000          NaN          NaN
75%      881.50000   915.500000        NaN   131.000000     83.000000    90.000000       100.100000    99.000000          NaN          NaN
max     1175.00000  9999.000000        NaN   140.000000     90.000000   100.000000       113.000000   100.000000          NaN          NaN
