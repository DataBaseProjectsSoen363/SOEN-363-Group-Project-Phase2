===== RECORD COUNT =====
2133

===== SHAPE =====
(2133, 6)

===== FIELD NAMES =====
['diag_id', 'visit_id', 'icd9_code', 'diag_datetime', 'is_primary', 'attending_doctor']

===== DATA TYPES =====
diag_id               int64
visit_id              int64
icd9_code           float64
diag_datetime           str
is_primary              str
attending_doctor        str

===== MISSING VALUES =====
diag_id             0
visit_id            0
icd9_code           0
diag_datetime       0
is_primary          0
attending_doctor    0

===== HIDDEN MISSING VALUES (String 'N/A') =====
diag_id             0
visit_id            0
icd9_code           0
diag_datetime       0
is_primary          0
attending_doctor    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      diag_id  visit_id  icd9_code     diag_datetime is_primary attending_doctor
1786     1787      1000      250.0  09/03/2026 15:00         No        MRN-10010
227       228       123      272.4  28/01/2026 20:00        Yes        MRN-10002
845       846       482      272.4  31/05/2026 00:00        Yes        MRN-10012
1362     1363       774      401.9  11/06/2026 02:00        Yes        MRN-10003
1288     1289       730      410.9  16/04/2026 13:00        Yes        MRN-10015

===== SUMMARY STATISTICS =====
            diag_id     visit_id    icd9_code     diag_datetime is_primary attending_doctor
count   2133.000000  2133.000000  2133.000000              2133       2133             2133
unique          NaN          NaN          NaN               976          5               15
top             NaN          NaN          NaN  19/03/2026 01:00         No        MRN-10011
freq            NaN          NaN          NaN                 7       1030              175
mean    1067.000000   805.268636   335.298734               NaN        NaN              NaN
std      615.888383  1407.456955    72.983544               NaN        NaN              NaN
min        1.000000     1.000000   250.000000               NaN        NaN              NaN
25%      534.000000   314.000000   272.400000               NaN        NaN              NaN
50%     1067.000000   623.000000   401.900000               NaN        NaN              NaN
75%     1600.000000   925.000000   410.900000               NaN        NaN              NaN
max     2133.000000  9999.000000   410.900000               NaN        NaN              NaN
