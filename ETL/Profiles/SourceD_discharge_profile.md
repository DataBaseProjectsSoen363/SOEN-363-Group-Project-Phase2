===== RECORD COUNT =====
1136

===== SHAPE =====
(1136, 5)

===== FIELD NAMES =====
['dischargeId', 'visitId', 'dischargeTimestamp', 'destination', 'condition']

===== DATA TYPES =====
dischargeId           int64
visitId               int64
dischargeTimestamp    int64
destination             str
condition               str

===== MISSING VALUES =====
dischargeId           0
visitId               0
dischargeTimestamp    0
destination           0
condition             0

===== HIDDEN MISSING VALUES (String 'N/A') =====
dischargeId           0
visitId               0
dischargeTimestamp    0
destination           0
condition             0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     dischargeId  visitId  dischargeTimestamp destination condition
223          224      234          1772064000       REHAB  Improved
509          510      535          1768867200         SNF  Improved
456          457      481          1767830400        HOME  Critical
201          202      212          1787702400       REHAB  Improved
358          359      375          1780790400        HOME    Stable

===== SUMMARY STATISTICS =====
        dischargeId      visitId  dischargeTimestamp destination condition
count   1136.000000  1136.000000        1.136000e+03        1136      1136
unique          NaN          NaN                 NaN           3         3
top             NaN          NaN                 NaN        HOME    Stable
freq            NaN          NaN                 NaN         406       394
mean     568.500000   597.878521        1.778301e+09         NaN       NaN
std      328.079259   346.266892        6.316570e+06         NaN       NaN
min        1.000000     1.000000        1.767312e+09         NaN       NaN
25%      284.750000   298.750000        1.772669e+09         NaN       NaN
50%      568.500000   598.500000        1.778026e+09         NaN       NaN
75%      852.250000   893.250000        1.783901e+09         NaN       NaN
max     1136.000000  1199.000000        1.789603e+09         NaN       NaN
