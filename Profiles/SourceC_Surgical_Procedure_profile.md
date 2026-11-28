===== RECORD COUNT =====
224

===== SHAPE =====
(224, 5)

===== FIELD NAMES =====
['id', 'admission_ref', 'name', 'Date', 'SurgeonId']

===== DATA TYPES =====
id                 int64
admission_ref      int64
name                 str
Date                 str
SurgeonId        float64

===== MISSING VALUES =====
id               0
admission_ref    0
name             0
Date             0
SurgeonId        3

===== HIDDEN MISSING VALUES (String 'N/A') =====
id               0
admission_ref    0
name             0
Date             0
SurgeonId        0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      id  admission_ref             name                 Date  SurgeonId
87    88            435             CABG  2026-08-07T03:00:00       14.0
116  117            634             CABG  2026-03-10T14:00:00       15.0
46    47            276  Cholecystectomy  2026-04-21T02:00:00       14.0
54    55            306  Cholecystectomy  2026-06-26T00:00:00       14.0
192  193           1051  Cholecystectomy  2026-06-11T01:00:00        2.0

===== SUMMARY STATISTICS =====
                id  admission_ref          name                 Date   SurgeonId
count   224.000000     224.000000           224                  224  221.000000
unique         NaN            NaN             3                  221         NaN
top            NaN            NaN  Appendectomy  2026-06-05T15:00:00         NaN
freq           NaN            NaN            77                    2         NaN
mean    112.500000     606.209821           NaN                  NaN    7.597285
std      64.807407     350.035022           NaN                  NaN    4.283774
min       1.000000       2.000000           NaN                  NaN    1.000000
25%      56.750000     311.500000           NaN                  NaN    4.000000
50%     112.500000     617.000000           NaN                  NaN    7.000000
75%     168.250000     889.750000           NaN                  NaN   11.000000
max     224.000000    1194.000000           NaN                  NaN   15.000000
