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
     note_id  visit_id author_mrn        note_format  created_datetime                                                                                                                                                                                                                                      note_text
796      797       910  MRN-10011               SOAP  11/02/2026 10:00  Subjective: Patient presents with acute discomfort.\r\nObjective: Vitals show mild elevation. Patient is alert.\r\nAssessment: Suspected acute condition requiring observation.\r\nPlan: Admit for further testing and continuous monitoring.
265      266       301  MRN-10015  Discharge Summary  14/06/2026 03:00  Subjective: Patient presents with acute discomfort.\r\nObjective: Vitals show mild elevation. Patient is alert.\r\nAssessment: Suspected acute condition requiring observation.\r\nPlan: Admit for further testing and continuous monitoring.
860      861       983  MRN-10012          Narrative  14/04/2026 07:00  Subjective: Patient presents with acute discomfort.\r\nObjective: Vitals show mild elevation. Patient is alert.\r\nAssessment: Suspected acute condition requiring observation.\r\nPlan: Admit for further testing and continuous monitoring.
361      362       414  MRN-10008               SOAP  21/04/2026 12:00  Subjective: Patient presents with acute discomfort.\r\nObjective: Vitals show mild elevation. Patient is alert.\r\nAssessment: Suspected acute condition requiring observation.\r\nPlan: Admit for further testing and continuous monitoring.
855      856       978  MRN-10008  Discharge Summary  16/03/2026 17:00  Subjective: Patient presents with acute discomfort.\r\nObjective: Vitals show mild elevation. Patient is alert.\r\nAssessment: Suspected acute condition requiring observation.\r\nPlan: Admit for further testing and continuous monitoring.

===== SUMMARY STATISTICS =====
           note_id     visit_id author_mrn note_format  created_datetime                                                                                                                                                                                                                                      note_text
count   1053.00000  1053.000000       1053        1053              1053                                                                                                                                                                                                                                           1024
unique         NaN          NaN         15           3               959                                                                                                                                                                                                                                              1
top            NaN          NaN  MRN-10002        SOAP  28/08/2026 06:00  Subjective: Patient presents with acute discomfort.\r\nObjective: Vitals show mild elevation. Patient is alert.\r\nAssessment: Suspected acute condition requiring observation.\r\nPlan: Admit for further testing and continuous monitoring.
freq           NaN          NaN         87         359                 3                                                                                                                                                                                                                                           1024
mean     527.00000   874.622032        NaN         NaN               NaN                                                                                                                                                                                                                                            NaN
std      304.11922  1626.109066        NaN         NaN               NaN                                                                                                                                                                                                                                            NaN
min        1.00000     1.000000        NaN         NaN               NaN                                                                                                                                                                                                                                            NaN
25%      264.00000   304.000000        NaN         NaN               NaN                                                                                                                                                                                                                                            NaN
50%      527.00000   619.000000        NaN         NaN               NaN                                                                                                                                                                                                                                            NaN
75%      790.00000   922.000000        NaN         NaN               NaN                                                                                                                                                                                                                                            NaN
max     1053.00000  9999.000000        NaN         NaN               NaN                                                                                                                                                                                                                                            NaN
