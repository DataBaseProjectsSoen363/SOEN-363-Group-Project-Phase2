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
1108          1109          52  2026-01-06 10:30:00  2026-01-09 10:30:00       Elective  Physician Referral                Fever     Private Insurance            Stable                         14
916            917         361  2026-07-07 00:30:00  2026-07-11 00:30:00       Elective            Transfer  Shortness of Breath     Private Insurance          Critical                          7
159            160          44  2026-08-01 14:15:00  2026-08-05 14:15:00       Elective  Physician Referral                Fever     Private Insurance            Stable                         11
779            780         267  2026-08-04 16:30:00  2026-08-05 16:30:00         Urgent            Transfer              Syncope         Public (RAMQ)            Stable                          4
223            224         343  2026-08-23 12:45:00  2026-08-26 12:45:00       Elective  Physician Referral                Fever              Self-pay          Critical                         11

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
