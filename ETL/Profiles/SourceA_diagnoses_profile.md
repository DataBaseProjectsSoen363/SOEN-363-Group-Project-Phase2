===== RECORD COUNT =====
2119

===== SHAPE =====
(2119, 8)

===== FIELD NAMES =====
['diagnosis_id', 'patient_id', 'admission_id', 'icd9_code', 'diagnosis_date_time', 'primary_diagnosis', 'secondary_diagnosis', 'diagnosing_physician_id']

===== DATA TYPES =====
diagnosis_id                 int64
patient_id                   int64
admission_id                 int64
icd9_code                  float64
diagnosis_date_time            str
primary_diagnosis             bool
secondary_diagnosis           bool
diagnosing_physician_id      int64

===== MISSING VALUES =====
diagnosis_id               0
patient_id                 0
admission_id               0
icd9_code                  0
diagnosis_date_time        0
primary_diagnosis          0
secondary_diagnosis        0
diagnosing_physician_id    0

===== HIDDEN MISSING VALUES (String 'N/A') =====
diagnosis_id               0
patient_id                 0
admission_id               0
icd9_code                  0
diagnosis_date_time        0
primary_diagnosis          0
secondary_diagnosis        0
diagnosing_physician_id    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      diagnosis_id  patient_id  admission_id  icd9_code  diagnosis_date_time  primary_diagnosis  secondary_diagnosis  diagnosing_physician_id
579            580         613           334      410.9  2026-06-19 21:15:00              False                False                       10
1199          1200         800           689      401.9  2026-05-30 10:45:00               True                False                        6
1608          1609         277           914      272.4  2026-04-11 16:30:00               True                False                       11
3                4         633             5      250.0  2026-04-08 12:15:00              False                 True                        5
226            227         571           135      410.9  2026-03-17 06:00:00              False                 True                       13

===== SUMMARY STATISTICS =====
        diagnosis_id   patient_id  admission_id    icd9_code  diagnosis_date_time primary_diagnosis secondary_diagnosis  diagnosing_physician_id
count    2119.000000  2119.000000   2119.000000  2119.000000                 2119              2119                2119              2119.000000
unique           NaN          NaN           NaN          NaN                 1908                 2                   2                      NaN
top              NaN          NaN           NaN          NaN  2026-03-08 18:45:00             False                True                      NaN
freq             NaN          NaN           NaN          NaN                    4              1072                1060                      NaN
mean     1060.000000   400.814063    852.539405   334.236621                  NaN               NaN                 NaN                 7.883436
std       611.846931   239.139726   1545.270825    73.147292                  NaN               NaN                 NaN                 4.210704
min         1.000000     1.000000      2.000000   250.000000                  NaN               NaN                 NaN                 1.000000
25%       530.500000   185.500000    313.000000   272.400000                  NaN               NaN                 NaN                 4.000000
50%      1060.000000   407.000000    626.000000   401.900000                  NaN               NaN                 NaN                 8.000000
75%      1589.500000   619.000000    924.500000   410.900000                  NaN               NaN                 NaN                11.000000
max      2119.000000   800.000000   9999.000000   410.900000                  NaN               NaN                 NaN                15.000000
