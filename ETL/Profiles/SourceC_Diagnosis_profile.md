===== RECORD COUNT =====
2195

===== SHAPE =====
(2195, 4)

===== FIELD NAMES =====
['ICD9Code', 'Date', 'IsPrimary', 'DoctorId']

===== DATA TYPES =====
ICD9Code     float64
Date             str
IsPrimary       bool
DoctorId       int64

===== MISSING VALUES =====
ICD9Code      0
Date         50
IsPrimary     0
DoctorId      0

===== HIDDEN MISSING VALUES (String 'N/A') =====
ICD9Code     0
Date         0
IsPrimary    0
DoctorId     0

===== DUPLICATE ROWS =====
11

===== SAMPLE RECORDS =====
      ICD9Code                 Date  IsPrimary  DoctorId
2089     272.4  2026-03-05T20:00:00      False         3
920      250.0  2026-06-11T07:00:00       True        14
285      272.4  2026-06-28T16:00:00       True         8
1007     272.4  2026-08-30T11:00:00      False         5
2058     272.4  2026-08-02T21:00:00       True        15

===== SUMMARY STATISTICS =====
           ICD9Code                 Date IsPrimary     DoctorId
count   2195.000000                 2145      2195  2195.000000
unique          NaN                 1762         2          NaN
top             NaN  2026-07-05T08:00:00     False          NaN
freq            NaN                    4      1102          NaN
mean     335.794351                  NaN       NaN     7.878360
std       72.914419                  NaN       NaN     4.314891
min      250.000000                  NaN       NaN     1.000000
25%      272.400000                  NaN       NaN     4.000000
50%      401.900000                  NaN       NaN     8.000000
75%      410.900000                  NaN       NaN    12.000000
max      410.900000                  NaN       NaN    15.000000
