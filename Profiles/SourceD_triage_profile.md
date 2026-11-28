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
      triageId  visitId  nurseId                                                                 vitals                                symptoms triagePriority
917        918      918     21.0  {'heartRate': 88, 'oxygenSaturation': 100, 'bloodPressure': '124/78'}  ['Dizziness', 'Fatigue', 'Chest Pain']          ESI-2
4            5        5     18.0   {'heartRate': 99, 'oxygenSaturation': 97, 'bloodPressure': '137/79'}   ['Shortness of Breath', 'Chest Pain']          ESI-5
230        231      231     23.0   {'heartRate': 62, 'oxygenSaturation': 95, 'bloodPressure': '104/76'}   ['Shortness of Breath', 'Chest Pain']          ESI-4
717        718      718     16.0   {'heartRate': 94, 'oxygenSaturation': 95, 'bloodPressure': '131/64'}                ['Fatigue', 'Dizziness']          ESI-1
1189      1190     1190     25.0  {'heartRate': 62, 'oxygenSaturation': 100, 'bloodPressure': '116/81'}                ['Nausea', 'Chest Pain']          ESI-3

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
