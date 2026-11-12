===== RECORD COUNT =====
1121

===== SHAPE =====
(1121, 5)

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
983           984     1052          1781222400       REHAB  Critical
598           599      638          1780358400         SNF  Critical
1107         1108     1187          1772409600        HOME  Critical
260           261      272          1769644800       REHAB  Critical
1059         1060     1133          1775692800         SNF    Stable

===== SUMMARY STATISTICS =====
        dischargeId      visitId  dischargeTimestamp destination condition
count   1121.000000  1121.000000        1.121000e+03        1121      1121
unique          NaN          NaN                 NaN           3         3
top             NaN          NaN                 NaN        HOME  Improved
freq            NaN          NaN                 NaN         398       406
mean     561.000000   596.241748        1.778378e+09         NaN       NaN
std      323.749131   347.598274        6.350706e+06         NaN       NaN
min        1.000000     1.000000        1.767485e+09         NaN       NaN
25%      281.000000   293.000000        1.772669e+09         NaN       NaN
50%      561.000000   597.000000        1.777939e+09         NaN       NaN
75%      841.000000   896.000000        1.783987e+09         NaN       NaN
max     1121.000000  1200.000000        1.789603e+09         NaN       NaN
