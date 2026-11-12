===== RECORD COUNT =====
1200

===== SHAPE =====
(1200, 10)

===== FIELD NAMES =====
['admission_id', 'patient_id', 'admission_date_time', 'discharge_date_time', 'admission_type', 'admission_source', 'reason_admission', 'insurance_information', 'current_condition', 'admitting_professional_id']

===== DATA TYPES =====
admission_id                 int64
patient_id                   int64
admission_date_time            str
discharge_date_time            str
admission_type                 str
admission_source               str
reason_admission               str
insurance_information          str
current_condition              str
admitting_professional_id    int64

===== MISSING VALUES =====
admission_id                   0
patient_id                     0
admission_date_time            0
discharge_date_time           24
admission_type                 0
admission_source               0
reason_admission               0
insurance_information        303
current_condition              0
admitting_professional_id      0

===== HIDDEN MISSING VALUES (String 'N/A') =====
admission_id                 0
patient_id                   0
admission_date_time          0
discharge_date_time          0
admission_type               0
admission_source             0
reason_admission             0
insurance_information        0
current_condition            0
admitting_professional_id    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      admission_id  patient_id  admission_date_time  discharge_date_time admission_type    admission_source     reason_admission insurance_information current_condition  admitting_professional_id
119            120         777  2026-03-30 01:30:00  2026-04-01 01:30:00      EMERGENCY             Walk-in               Trauma         Public (RAMQ)       Observation                         11
580            581          47  2026-08-07 12:15:00  2026-08-12 12:15:00       Elective  Physician Referral       Abdominal Pain              Self-pay         Improving                         13
666            667         554  2026-02-22 21:15:00  2026-02-27 21:15:00      Emergency      Emergency Room           Chest Pain              Self-pay         Improving                          8
916            917         361  2026-07-07 00:30:00  2026-07-11 00:30:00       Elective            Transfer  Shortness of Breath     Private Insurance          Critical                          7
1040          1041          85  2026-08-19 14:45:00  2026-08-26 14:45:00         Urgent      Emergency Room              Syncope         Public (RAMQ)            Stable                          3

===== SUMMARY STATISTICS =====
        admission_id   patient_id  admission_date_time  discharge_date_time admission_type admission_source reason_admission insurance_information current_condition  admitting_professional_id
count    1200.000000  1200.000000                 1200                 1176           1200             1200             1200                   897              1200                1200.000000
unique           NaN          NaN                 1171                 1156             16                4               11                     3                 4                        NaN
top              NaN          NaN  2026-01-15 04:15:00  2026-08-22 05:45:00       Elective         Transfer            Fever              Self-pay            Stable                        NaN
freq             NaN          NaN                    2                    2            297              309              206                   307               321                        NaN
mean      600.500000   406.338333                  NaN                  NaN            NaN              NaN              NaN                   NaN               NaN                   7.725833
std       346.554469   240.621340                  NaN                  NaN            NaN              NaN              NaN                   NaN               NaN                   4.316966
min         1.000000     1.000000                  NaN                  NaN            NaN              NaN              NaN                   NaN               NaN                   1.000000
25%       300.750000   196.750000                  NaN                  NaN            NaN              NaN              NaN                   NaN               NaN                   4.000000
50%       600.500000   403.000000                  NaN                  NaN            NaN              NaN              NaN                   NaN               NaN                   8.000000
75%       900.250000   622.500000                  NaN                  NaN            NaN              NaN              NaN                   NaN               NaN                  11.000000
max      1200.000000   844.000000                  NaN                  NaN            NaN              NaN              NaN                   NaN               NaN                  15.000000
