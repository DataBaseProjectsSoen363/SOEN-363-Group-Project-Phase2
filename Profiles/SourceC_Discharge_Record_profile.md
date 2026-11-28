===== RECORD COUNT =====
1167

===== SHAPE =====
(1167, 5)

===== FIELD NAMES =====
['id', 'admission_ref', 'DischargeDate', 'Destination', 'Condition']

===== DATA TYPES =====
id               int64
admission_ref    int64
DischargeDate      str
Destination        str
Condition          str

===== MISSING VALUES =====
id               0
admission_ref    0
DischargeDate    0
Destination      0
Condition        0

===== HIDDEN MISSING VALUES (String 'N/A') =====
id               0
admission_ref    0
DischargeDate    0
Destination      0
Condition        0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      id  admission_ref        DischargeDate Destination Condition
629  630            641  2026-06-26T02:00:00        Home  Improved
632  633            644  2026-09-12T16:00:00        Home    Stable
754  755            769  2026-04-30T21:00:00       Rehab  Improved
15    16             16  2026-08-02T12:00:00        Home    Stable
344  345            352  2026-03-01T11:00:00        Home    Stable

===== SUMMARY STATISTICS =====
                 id  admission_ref        DischargeDate Destination Condition
count   1167.000000    1167.000000                 1167        1167      1167
unique          NaN            NaN                 1065           3         2
top             NaN            NaN  2026-07-01T17:00:00        Home    Stable
freq            NaN            NaN                    3         405       610
mean     584.000000     596.430163                  NaN         NaN       NaN
std      337.028189     345.817420                  NaN         NaN       NaN
min        1.000000       1.000000                  NaN         NaN       NaN
25%      292.500000     296.000000                  NaN         NaN       NaN
50%      584.000000     594.000000                  NaN         NaN       NaN
75%      875.500000     893.500000                  NaN         NaN       NaN
max     1167.000000    1200.000000                  NaN         NaN       NaN
