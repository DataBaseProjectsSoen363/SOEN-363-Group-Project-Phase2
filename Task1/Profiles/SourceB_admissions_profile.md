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
713        714   MRN-61683        MRN-10001  08/09/2026 05:00  10/09/2026 05:00      SURG  Douleur thoracique
165        166   MRN-99836        MRN-10001  27/04/2026 19:00  29/04/2026 19:00      PEDS              Fièvre
381        382   MRN-68553        MRN-10005  26/06/2026 23:00  27/06/2026 23:00      SURG         Traumatisme
1053      1054   MRN-99999        MRN-10008  21/04/2026 20:00  25/04/2026 20:00      PEDS              Fièvre
389        390   MRN-50641        MRN-10004  15/01/2026 02:00  23/01/2026 02:00      PEDS  Douleur thoracique

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
