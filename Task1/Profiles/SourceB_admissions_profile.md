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
1140      1141   MRN-92608        MRN-10004  18/04/2026 03:00  19/04/2026 03:00      SURG              Fièvre
1007      1008   MRN-60908        MRN-10008  23/06/2026 05:00  26/06/2026 05:00       MED  Douleur thoracique
699        700   MRN-61178        MRN-10003  07/04/2026 17:00  08/04/2026 17:00       OBS              Fièvre
1160      1161   MRN-86172        MRN-10002  27/07/2026 14:00  29/07/2026 14:00      PEDS              Fièvre
65          66   MRN-32795        MRN-10004  14/04/2026 21:00  20/04/2026 21:00      SURG              Fièvre

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
