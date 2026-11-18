===== RECORD COUNT =====
1200

===== SHAPE =====
(1200, 6)

===== FIELD NAMES =====
['id', 'admission_ref', 'NurseId', 'HeartRate', 'OxygenSaturation', 'Priority']

===== DATA TYPES =====
id                  int64
admission_ref       int64
NurseId             int64
HeartRate           int64
OxygenSaturation    int64
Priority              str

===== MISSING VALUES =====
id                  0
admission_ref       0
NurseId             0
HeartRate           0
OxygenSaturation    0
Priority            0

===== HIDDEN MISSING VALUES (String 'N/A') =====
id                  0
admission_ref       0
NurseId             0
HeartRate           0
OxygenSaturation    0
Priority            0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
        id  admission_ref  NurseId  HeartRate  OxygenSaturation Priority
1012  1013           1013       24         77                96    ESI-4
6        7              7       21         90                99    ESI-2
735    736            736       17         81                99    ESI-4
760    761            761       19         81               100    ESI-4
554    555            555       24         86                98    ESI-2

===== SUMMARY STATISTICS =====
                 id  admission_ref      NurseId    HeartRate  OxygenSaturation Priority
count   1200.000000    1200.000000  1200.000000  1200.000000       1200.000000     1200
unique          NaN            NaN          NaN          NaN               NaN        5
top             NaN            NaN          NaN          NaN               NaN    ESI-5
freq            NaN            NaN          NaN          NaN               NaN      265
mean     600.500000     732.744167    20.568333    76.290000         96.030833      NaN
std      346.554469    1163.274240     2.931864    27.198052          2.584657      NaN
min        1.000000       1.000000    16.000000   -99.000000         92.000000      NaN
25%      300.750000     303.750000    18.000000    68.000000         94.000000      NaN
50%      600.500000     607.500000    21.000000    79.000000         96.000000      NaN
75%      900.250000     912.250000    23.000000    90.000000         98.000000      NaN
max     1200.000000    9999.000000    25.000000   100.000000        100.000000      NaN
