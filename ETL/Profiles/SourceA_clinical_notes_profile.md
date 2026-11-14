===== RECORD COUNT =====
1113

===== SHAPE =====
(1113, 11)

===== FIELD NAMES =====
['note_id', 'admission_id', 'physician_id', 'type', 'creation_date', 'patient_symptoms', 'physical_examination', 'initial_clinical_findings', 'suspected_condition', 'planned_diagnostic_examinations', 'initial_treatment']

===== DATA TYPES =====
note_id                            int64
admission_id                       int64
physician_id                       int64
type                                 str
creation_date                        str
patient_symptoms                     str
physical_examination                 str
initial_clinical_findings            str
suspected_condition                  str
planned_diagnostic_examinations      str
initial_treatment                    str

===== MISSING VALUES =====
note_id                             0
admission_id                        0
physician_id                        0
type                                0
creation_date                       0
patient_symptoms                    0
physical_examination                0
initial_clinical_findings          30
suspected_condition                 0
planned_diagnostic_examinations     0
initial_treatment                  34

===== HIDDEN MISSING VALUES (String 'N/A') =====
note_id                            0
admission_id                       0
physician_id                       0
type                               0
creation_date                      0
patient_symptoms                   0
physical_examination               0
initial_clinical_findings          0
suspected_condition                0
planned_diagnostic_examinations    0
initial_treatment                  0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     note_id  admission_id  physician_id               type        creation_date                                       patient_symptoms                          physical_examination                        initial_clinical_findings                 suspected_condition                    planned_diagnostic_examinations       initial_treatment
453      454           497            11     Admission Note  2026-02-25 16:00:00   Fever and chills, accompanied by a persistent cough.      Heart rate regular, no murmurs detected.               Mild elevation in troponin levels.  Acute coronary syndrome suspected.                     ECG and chest imaging ordered.                     NaN
317      318           354            10  Consultation Note  2026-09-04 22:00:00                               ERROR - STRING TRUNCATED  Mild discomfort on palpation of the abdomen.         Slight leukocytosis noted in blood work.       Likely viral gastroenteritis.                     ECG and chest imaging ordered.  Antibiotics initiated.
524      525           567            10      Progress Note  2026-05-19 13:45:00  Shortness of breath and mild dizziness upon standing.            Vitals stable, alert and oriented.         Slight leukocytosis noted in blood work.  Acute coronary syndrome suspected.                     ECG and chest imaging ordered.  Antibiotics initiated.
992      993          1069             2      Progress Note  2026-05-10 23:00:00   Fever and chills, accompanied by a persistent cough.            Vitals stable, alert and oriented.  No acute abnormalities found on initial review.  Acute coronary syndrome suspected.  Awaiting lab results before further intervention.  Antibiotics initiated.
393      394           438            12     Admission Note  2026-01-04 21:30:00  Shortness of breath and mild dizziness upon standing.            Vitals stable, alert and oriented.  No acute abnormalities found on initial review.        Rule out pulmonary embolism.  Awaiting lab results before further intervention.      IV fluids started.

===== SUMMARY STATISTICS =====
           note_id  admission_id  physician_id            type        creation_date                                       patient_symptoms                physical_examination                        initial_clinical_findings              suspected_condition         planned_diagnostic_examinations                         initial_treatment
count   1113.00000   1113.000000   1113.000000            1113                 1113                                                   1113                                1113                                             1083                             1113                                    1113                                      1079
unique         NaN           NaN           NaN              12                 1060                                                      5                                   4                                                4                                4                                       4                                         4
top            NaN           NaN           NaN  Admission Note  2026-07-24 15:00:00  Shortness of breath and mild dizziness upon standing.  Vitals stable, alert and oriented.  No acute abnormalities found on initial review.  Possible early-stage pneumonia.  Basic metabolic panel and CBC ordered.  Analgesics provided for pain management.
freq           NaN           NaN           NaN             379                    3                                                    303                                 298                                              276                              285                                     286                                       271
mean     557.00000    830.272237      8.050314             NaN                  NaN                                                    NaN                                 NaN                                              NaN                              NaN                                     NaN                                       NaN
std      321.43973   1485.598958      4.337720             NaN                  NaN                                                    NaN                                 NaN                                              NaN                              NaN                                     NaN                                       NaN
min        1.00000      1.000000      1.000000             NaN                  NaN                                                    NaN                                 NaN                                              NaN                              NaN                                     NaN                                       NaN
25%      279.00000    315.000000      4.000000             NaN                  NaN                                                    NaN                                 NaN                                              NaN                              NaN                                     NaN                                       NaN
50%      557.00000    620.000000      8.000000             NaN                  NaN                                                    NaN                                 NaN                                              NaN                              NaN                                     NaN                                       NaN
75%      835.00000    918.000000     12.000000             NaN                  NaN                                                    NaN                                 NaN                                              NaN                              NaN                                     NaN                                       NaN
max     1113.00000   9999.000000     15.000000             NaN                  NaN                                                    NaN                                 NaN                                              NaN                              NaN                                     NaN                                       NaN
