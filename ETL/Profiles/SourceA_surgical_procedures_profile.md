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
     procedure_id  admission_id  patient_id                procedure_name        body_site  procedure_date_time  surgeon_id
172           173           840         166  Coronary Artery Bypass Graft            Heart  2026-08-24 06:30:00           3
116           117           553         314               Cholecystectomy      Gallbladder  2026-03-03 22:15:00          14
1               2            23          19               Bowel Resection  Small Intestine  2026-08-12 17:45:00           3
155           156           774         410              Knee Replacement        Left Knee  2026-03-31 19:15:00           2
203           204          1011         590                  Appendectomy         Appendix  2026-06-04 04:30:00           9

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
