===== RECORD COUNT =====
358

===== SHAPE =====
(358, 6)

===== FIELD NAMES =====
['id', 'admission_ref', 'WardType', 'DoctorId', 'EntryDate', 'ExitDate']

===== DATA TYPES =====
id               int64
admission_ref    int64
WardType           str
DoctorId         int64
EntryDate          str
ExitDate           str

===== MISSING VALUES =====
id                0
admission_ref     0
WardType          0
DoctorId          0
EntryDate         0
ExitDate         17

===== HIDDEN MISSING VALUES (String 'N/A') =====
id               0
admission_ref    0
WardType         0
DoctorId         0
EntryDate        0
ExitDate         0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      id  admission_ref WardType  DoctorId            EntryDate             ExitDate
131  132            470      ICU         2  2026-09-06T10:00:00  2026-09-10T10:00:00
211  212            741      CCU         2  2026-05-21T05:00:00  2026-05-22T05:00:00
141  142            509      CCU         3  2026-08-28T17:00:00                  NaN
227  228            767     MICU        15  2026-09-04T01:00:00  2026-09-06T01:00:00
279  280            951      CCU         6  2026-04-30T18:00:00                  NaN

===== SUMMARY STATISTICS =====
                id  admission_ref WardType    DoctorId            EntryDate             ExitDate
count   358.000000     358.000000      358  358.000000                  358                  341
unique         NaN            NaN        3         NaN                  347                  331
top            NaN            NaN     MICU         NaN  2026-03-17T16:00:00  2026-05-04T16:00:00
freq           NaN            NaN      132         NaN                    3                    2
mean    179.500000     618.631285      NaN    8.053073                  NaN                  NaN
std     103.489935     345.853863      NaN    4.414768                  NaN                  NaN
min       1.000000       3.000000      NaN    1.000000                  NaN                  NaN
25%      90.250000     317.500000      NaN    4.000000                  NaN                  NaN
50%     179.500000     635.500000      NaN    8.000000                  NaN                  NaN
75%     268.750000     924.250000      NaN   12.000000                  NaN                  NaN
max     358.000000    1200.000000      NaN   15.000000                  NaN                  NaN
