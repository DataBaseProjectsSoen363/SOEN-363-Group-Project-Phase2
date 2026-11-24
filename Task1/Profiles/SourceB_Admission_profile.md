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
864       865   MRN-66846        MRN-10003  16/01/2026 05:00  17/01/2026 05:00      SURG  Douleur thoracique
432       433   MRN-17364        MRN-10004  31/07/2026 02:00  05/08/2026 02:00       MED         Traumatisme
850       851   MRN-47337        MRN-10009  05/01/2026 17:00  08/01/2026 17:00      PEDS              Fièvre
742       743   MRN-89169        MRN-10012  18/02/2026 19:00  23/02/2026 19:00       OBS       Essoufflement
152       153   MRN-80873        MRN-10007  27/07/2026 02:00           Unknown       OBS  Douleur thoracique

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
