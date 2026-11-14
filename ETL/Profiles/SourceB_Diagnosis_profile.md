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
1612     1613       911      401.9  06/01/2026 16:00         No        MRN-10013
788       789       450      410.9  30/03/2026 07:00        Yes        MRN-10011
2034     2035      1140      401.9  13/04/2026 01:00         No        MRN-10014
768       769       439      250.0  03/08/2026 12:00        Yes        MRN-10010
580       581       332      272.4  20/08/2026 14:00         No        MRN-10009

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
