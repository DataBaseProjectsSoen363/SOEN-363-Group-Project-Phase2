===== RECORD COUNT =====
351

===== SHAPE =====
(351, 6)

===== FIELD NAMES =====
['stayId', 'visitId', 'wardType', 'doctorId', 'entryTimestamp', 'exitTimestamp']

===== DATA TYPES =====
stayId              int64
visitId             int64
wardType              str
doctorId            int64
entryTimestamp      int64
exitTimestamp     float64

===== MISSING VALUES =====
stayId             0
visitId            0
wardType           0
doctorId           0
entryTimestamp     0
exitTimestamp     17

===== HIDDEN MISSING VALUES (String 'N/A') =====
stayId            0
visitId           0
wardType          0
doctorId          0
entryTimestamp    0
exitTimestamp     0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     stayId  visitId wardType  doctorId  entryTimestamp  exitTimestamp
312     313     1038     SICU         5      1772334000   1.772939e+09
152     153      527      CCU         4      1786978800   1.787584e+09
337     338     1156     MICU         9      1786770000   1.787288e+09
206     207      707      ICU         9      1788775200   1.789294e+09
162     163      583      CCU        14      1786024800   1.786007e+09

===== SUMMARY STATISTICS =====
            stayId      visitId wardType    doctorId  entryTimestamp  exitTimestamp
count   351.000000   351.000000      351  351.000000    3.510000e+02   3.340000e+02
unique         NaN          NaN        4         NaN             NaN            NaN
top            NaN          NaN     MICU         NaN             NaN            NaN
freq           NaN          NaN      100         NaN             NaN            NaN
mean    176.000000   844.017094      NaN    7.792023    1.778001e+09   1.778346e+09
std     101.469207  1521.363751      NaN    4.398642    6.239599e+06   6.302814e+06
min       1.000000     4.000000      NaN    1.000000    1.767229e+09   1.767402e+09
25%      88.500000   327.000000      NaN    4.000000    1.772822e+09   1.773170e+09
50%     176.000000   643.000000      NaN    8.000000    1.777579e+09   1.777804e+09
75%     263.500000   881.500000      NaN   12.000000    1.783345e+09   1.783822e+09
max     351.000000  9999.000000      NaN   15.000000    1.788912e+09   1.789294e+09
