===== RECORD COUNT =====
251

===== SHAPE =====
(251, 5)

===== FIELD NAMES =====
['surgeryId', 'visitId', 'procedureCode', 'surgeonId', 'surgeryTimestamp']

===== DATA TYPES =====
surgeryId           int64
visitId             int64
procedureCode         str
surgeonId           int64
surgeryTimestamp    int64

===== MISSING VALUES =====
surgeryId           0
visitId             0
procedureCode       0
surgeonId           0
surgeryTimestamp    0

===== HIDDEN MISSING VALUES (String 'N/A') =====
surgeryId           0
visitId             0
procedureCode       0
surgeonId           0
surgeryTimestamp    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     surgeryId  visitId procedureCode  surgeonId  surgeryTimestamp
130        131      654      PROC-APP          9        1782518400
173        174      862     PROC-CHOL          4        1776297600
1            2        2     PROC-CABG         10        1769212800
50          51      223     PROC-CABG          6        1778457600
171        172      857     PROC-CABG         10        1778716800

===== SUMMARY STATISTICS =====
         surgeryId      visitId procedureCode   surgeonId  surgeryTimestamp
count   251.000000   251.000000           251  251.000000      2.510000e+02
unique         NaN          NaN             3         NaN               NaN
top            NaN          NaN      PROC-APP         NaN               NaN
freq           NaN          NaN            85         NaN               NaN
mean    126.000000   609.780876           NaN    7.709163      1.778237e+09
std      72.601653   350.752887           NaN    4.455006      6.305017e+06
min       1.000000     1.000000           NaN    1.000000      1.767571e+09
25%      63.500000   307.000000           NaN    4.000000      1.772453e+09
50%     126.000000   606.000000           NaN    8.000000      1.778458e+09
75%     188.500000   915.500000           NaN   11.000000      1.783382e+09
max     251.000000  1197.000000           NaN   15.000000      1.788826e+09
