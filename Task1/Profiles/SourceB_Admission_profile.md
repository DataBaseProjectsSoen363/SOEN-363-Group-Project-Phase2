===== RECORD COUNT =====
1200

===== SHAPE =====
(1200, 7)

===== FIELD NAMES =====
['visit_id', 'patient_mrn', 'admitting_doctor', 'admit_date', 'discharge_date', 'ward_code', 'reason_text']

===== DATA TYPES =====
visit_id            int64
patient_mrn           str
admitting_doctor      str
admit_date            str
discharge_date        str
ward_code             str
reason_text           str

===== MISSING VALUES =====
visit_id            0
patient_mrn         0
admitting_doctor    0
admit_date          0
discharge_date      0
ward_code           0
reason_text         0

===== HIDDEN MISSING VALUES (String 'N/A') =====
visit_id            0
patient_mrn         0
admitting_doctor    0
admit_date          0
discharge_date      0
ward_code           0
reason_text         0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      visit_id patient_mrn admitting_doctor        admit_date    discharge_date ward_code         reason_text
862        863   MRN-41426        MRN-10001  26/02/2026 10:00  27/02/2026 10:00      PEDS         Traumatisme
1084      1085   MRN-61280        MRN-10010  04/09/2026 12:00  14/09/2026 12:00       MED  Douleur thoracique
510        511   MRN-63433        MRN-10005  03/06/2026 22:00  09/06/2026 22:00       MED  Douleur thoracique
293        294   MRN-30948        MRN-10011  21/03/2026 06:00  27/03/2026 06:00      EMER         Traumatisme
42          43   MRN-38091        MRN-10014  06/01/2026 16:00  16/01/2026 16:00      PEDS  Douleur thoracique

===== SUMMARY STATISTICS =====
           visit_id patient_mrn admitting_doctor        admit_date discharge_date ward_code         reason_text
count   1200.000000        1200             1200              1200           1200      1200                1200
unique          NaN         617               15              1090           1062         5                   8
top             NaN   MRN-99999        MRN-10007  07/06/2026 23:00        Unknown       MED  Douleur thoracique
freq            NaN          25               98                 3             17       266                 300
mean     600.500000         NaN              NaN               NaN            NaN       NaN                 NaN
std      346.554469         NaN              NaN               NaN            NaN       NaN                 NaN
min        1.000000         NaN              NaN               NaN            NaN       NaN                 NaN
25%      300.750000         NaN              NaN               NaN            NaN       NaN                 NaN
50%      600.500000         NaN              NaN               NaN            NaN       NaN                 NaN
75%      900.250000         NaN              NaN               NaN            NaN       NaN                 NaN
max     1200.000000         NaN              NaN               NaN            NaN       NaN                 NaN
