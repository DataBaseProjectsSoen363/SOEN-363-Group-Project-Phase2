===== RECORD COUNT =====
247

===== SHAPE =====
(247, 7)

===== FIELD NAMES =====
['procedure_id', 'admission_id', 'patient_id', 'procedure_name', 'body_site', 'procedure_date_time', 'surgeon_id']

===== DATA TYPES =====
procedure_id           int64
admission_id           int64
patient_id             int64
procedure_name           str
body_site                str
procedure_date_time      str
surgeon_id             int64

===== MISSING VALUES =====
procedure_id           0
admission_id           0
patient_id             0
procedure_name         0
body_site              0
procedure_date_time    0
surgeon_id             0

===== HIDDEN MISSING VALUES (String 'N/A') =====
procedure_id           0
admission_id           0
patient_id             0
procedure_name         0
body_site              0
procedure_date_time    0
surgeon_id             0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     procedure_id  admission_id  patient_id                procedure_name    body_site  procedure_date_time  surgeon_id
2               3            26         103  Coronary Artery Bypass Graft        Heart  2026-06-07 16:15:00           5
77             78           399         133               Cholecystectomy  Gallbladder  2026-03-16 04:30:00           1
102           103           500         691              KNEE REPLACEMENT    Left Knee  2026-03-11 15:45:00          14
114           115           543         630               Cholecystectomy  Gallbladder  2026-04-17 04:15:00           5
154           155           766         457  Coronary Artery Bypass Graft        Heart  2026-01-24 17:30:00          11

===== SUMMARY STATISTICS =====
        procedure_id  admission_id  patient_id procedure_name body_site  procedure_date_time  surgeon_id
count      247.00000    247.000000  247.000000            247       247                  247  247.000000
unique           NaN           NaN         NaN             14         5                  246         NaN
top              NaN           NaN         NaN   Appendectomy     Heart  2026-08-09 10:45:00         NaN
freq             NaN           NaN         NaN             56        60                    2         NaN
mean       124.00000    794.352227  402.226721            NaN       NaN                  NaN    8.048583
std         71.44695   1370.397928  242.513442            NaN       NaN                  NaN    4.380025
min          1.00000     17.000000    6.000000            NaN       NaN                  NaN    1.000000
25%         62.50000    311.000000  195.000000            NaN       NaN                  NaN    4.000000
50%        124.00000    602.000000  423.000000            NaN       NaN                  NaN    8.000000
75%        185.50000    936.500000  620.000000            NaN       NaN                  NaN   12.000000
max        247.00000   9999.000000  798.000000            NaN       NaN                  NaN   15.000000
