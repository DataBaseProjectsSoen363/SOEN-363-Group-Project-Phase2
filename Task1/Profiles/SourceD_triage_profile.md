===== RECORD COUNT =====
1200

===== SHAPE =====
(1200, 6)

===== FIELD NAMES =====
['triageId', 'visitId', 'nurseId', 'vitals', 'symptoms', 'triagePriority']

===== DATA TYPES =====
triageId            int64
visitId             int64
nurseId           float64
vitals                str
symptoms              str
triagePriority        str

===== MISSING VALUES =====
triageId           0
visitId            0
nurseId           24
vitals             0
symptoms           0
triagePriority     0

===== HIDDEN MISSING VALUES (String 'N/A') =====
triageId          0
visitId           0
nurseId           0
vitals            0
symptoms          0
triagePriority    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      triageId  visitId  nurseId                                                                 vitals                            symptoms triagePriority
432        433      433     16.0   {'heartRate': 66, 'oxygenSaturation': 95, 'bloodPressure': '114/69'}             ['Shortness of Breath']          ESI-5
123        124      124     25.0   {'heartRate': 78, 'oxygenSaturation': 99, 'bloodPressure': '138/72'}  ['Nausea', 'Dizziness', 'Fatigue']          ESI-3
1111      1112     1112     16.0  {'heartRate': 78, 'oxygenSaturation': 100, 'bloodPressure': '138/84'}            ['Fatigue', 'Dizziness']          ESI-4
904        905      905     17.0   {'heartRate': 72, 'oxygenSaturation': 96, 'bloodPressure': '101/60'}                          ['Nausea']          ESI-4
257        258      258     23.0   {'heartRate': 91, 'oxygenSaturation': 98, 'bloodPressure': '117/77'}                       ['Dizziness']          ESI-5

===== SUMMARY STATISTICS =====
           triageId      visitId      nurseId                                                                vitals       symptoms triagePriority
count   1200.000000  1200.000000  1176.000000                                                                  1200           1200           1200
unique          NaN          NaN          NaN                                                                  1197             85              5
top             NaN          NaN          NaN  {'heartRate': 68, 'oxygenSaturation': 99, 'bloodPressure': '138/90'}  ['Dizziness']          ESI-1
freq            NaN          NaN          NaN                                                                     2             94            262
mean     600.500000   764.449167    20.441327                                                                   NaN            NaN            NaN
std      346.554469  1279.714328     2.907064                                                                   NaN            NaN            NaN
min        1.000000     1.000000    16.000000                                                                   NaN            NaN            NaN
25%      300.750000   305.750000    18.000000                                                                   NaN            NaN            NaN
50%      600.500000   610.500000    20.000000                                                                   NaN            NaN            NaN
75%      900.250000   914.250000    23.000000                                                                   NaN            NaN            NaN
max     1200.000000  9999.000000    25.000000                                                                   NaN            NaN            NaN
