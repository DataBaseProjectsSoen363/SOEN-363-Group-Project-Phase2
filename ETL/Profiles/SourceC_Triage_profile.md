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
172  173            173       23         78                96    ESI-3
422  423            423       18         82                97    ESI-3
424  425            425       25         67               100    ESI-2
825  826            826       22         63                97    ESI-1
403  404            404       18         74                98    ESI-3

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
