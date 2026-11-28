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
940        941   MRN-96669        MRN-10012  12/01/2026 05:00  20/01/2026 05:00      PEDS  Douleur thoracique
1127      1128   MRN-13112        MRN-10007  22/03/2026 15:00  24/03/2026 15:00      PEDS  Douleur thoracique
461        462   MRN-73342        MRN-10007  14/04/2026 17:00  15/04/2026 17:00      EMER  Douleur thoracique
412        413   MRN-38997        MRN-10001  24/08/2026 05:00  25/08/2026 05:00       MED       Essoufflement
565        566   MRN-87168        MRN-10006  04/03/2026 16:00  14/03/2026 16:00       MED       ESSOUFFLEMENT

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
