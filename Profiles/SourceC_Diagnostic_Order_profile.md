===== RECORD COUNT =====
290

===== SHAPE =====
(290, 5)

===== FIELD NAMES =====
['id', 'admission_ref', 'ExamType', 'DoctorId', 'OrderDate']

===== DATA TYPES =====
id               int64
admission_ref    int64
ExamType           str
DoctorId         int64
OrderDate          str

===== MISSING VALUES =====
id               0
admission_ref    0
ExamType         0
DoctorId         0
OrderDate        0

===== HIDDEN MISSING VALUES (String 'N/A') =====
id               0
admission_ref    0
ExamType         0
DoctorId         0
OrderDate        0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      id  admission_ref ExamType  DoctorId            OrderDate
255  256           1045      MRI         4  2026-01-20T15:00:00
268  269           1116  CT Scan         2  2026-07-04T23:00:00
38    39            164    X-Ray         6  2026-03-09T19:00:00
241  242            976      MRI         8  2026-01-29T17:00:00
112  113            477  CT Scan         9  2026-08-20T20:00:00

===== SUMMARY STATISTICS =====
                id  admission_ref ExamType    DoctorId            OrderDate
count   290.000000     290.000000      290  290.000000                  290
unique         NaN            NaN        3         NaN                  278
top            NaN            NaN    X-Ray         NaN  2026-03-09T21:00:00
freq           NaN            NaN      103         NaN                    3
mean    145.500000     601.603448      NaN    8.089655                  NaN
std      83.860002     338.158259      NaN    4.365510                  NaN
min       1.000000       5.000000      NaN    1.000000                  NaN
25%      73.250000     314.000000      NaN    4.000000                  NaN
50%     145.500000     603.500000      NaN    8.000000                  NaN
75%     217.750000     886.250000      NaN   12.000000                  NaN
max     290.000000    1197.000000      NaN   15.000000                  NaN
