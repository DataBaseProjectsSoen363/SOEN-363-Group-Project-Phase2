===== RECORD COUNT =====
1053

===== SHAPE =====
(1053, 6)

===== FIELD NAMES =====
['note_id', 'visit_id', 'author_mrn', 'note_format', 'created_datetime', 'note_text']

===== DATA TYPES =====
note_id             int64
visit_id            int64
author_mrn            str
note_format           str
created_datetime      str
note_text             str

===== MISSING VALUES =====
note_id              0
visit_id             0
author_mrn           0
note_format          0
created_datetime     0
note_text           29

===== HIDDEN MISSING VALUES (String 'N/A') =====
note_id             0
visit_id            0
author_mrn          0
note_format         0
created_datetime    0
note_text           0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      note_id  visit_id author_mrn        note_format  created_datetime                                                                                                                                                                                                                                note_text
875       876       999  MRN-10004  Discharge Summary  26/08/2026 00:00  Subjective: Patient presents with acute discomfort.\nObjective: Vitals show mild elevation. Patient is alert.\nAssessment: Suspected acute condition requiring observation.\nPlan: Admit for further testing and continuous monitoring.
67         68        78  MRN-10006               SOAP  23/07/2026 06:00  Subjective: Patient presents with acute discomfort.\nObjective: Vitals show mild elevation. Patient is alert.\nAssessment: Suspected acute condition requiring observation.\nPlan: Admit for further testing and continuous monitoring.
622       623       714  MRN-10001  Discharge Summary  08/09/2026 06:00  Subjective: Patient presents with acute discomfort.\nObjective: Vitals show mild elevation. Patient is alert.\nAssessment: Suspected acute condition requiring observation.\nPlan: Admit for further testing and continuous monitoring.
589       590      9999  MRN-10015          Narrative  25/03/2026 13:00  Subjective: Patient presents with acute discomfort.\nObjective: Vitals show mild elevation. Patient is alert.\nAssessment: Suspected acute condition requiring observation.\nPlan: Admit for further testing and continuous monitoring.
1012     1013      1155  MRN-10014          Narrative  13/06/2026 14:00  Subjective: Patient presents with acute discomfort.\nObjective: Vitals show mild elevation. Patient is alert.\nAssessment: Suspected acute condition requiring observation.\nPlan: Admit for further testing and continuous monitoring.

===== SUMMARY STATISTICS =====
           note_id     visit_id author_mrn note_format  created_datetime                                                                                                                                                                                                                                note_text
count   1053.00000  1053.000000       1053        1053              1053                                                                                                                                                                                                                                     1024
unique         NaN          NaN         15           3               959                                                                                                                                                                                                                                        1
top            NaN          NaN  MRN-10002        SOAP  28/08/2026 06:00  Subjective: Patient presents with acute discomfort.\nObjective: Vitals show mild elevation. Patient is alert.\nAssessment: Suspected acute condition requiring observation.\nPlan: Admit for further testing and continuous monitoring.
freq           NaN          NaN         87         359                 3                                                                                                                                                                                                                                     1024
mean     527.00000   874.622032        NaN         NaN               NaN                                                                                                                                                                                                                                      NaN
std      304.11922  1626.109066        NaN         NaN               NaN                                                                                                                                                                                                                                      NaN
min        1.00000     1.000000        NaN         NaN               NaN                                                                                                                                                                                                                                      NaN
25%      264.00000   304.000000        NaN         NaN               NaN                                                                                                                                                                                                                                      NaN
50%      527.00000   619.000000        NaN         NaN               NaN                                                                                                                                                                                                                                      NaN
75%      790.00000   922.000000        NaN         NaN               NaN                                                                                                                                                                                                                                      NaN
max     1053.00000  9999.000000        NaN         NaN               NaN                                                                                                                                                                                                                                      NaN
