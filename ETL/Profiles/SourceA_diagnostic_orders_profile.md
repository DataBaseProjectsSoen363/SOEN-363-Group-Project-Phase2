===== RECORD COUNT =====
275

===== SHAPE =====
(275, 9)

===== FIELD NAMES =====
['order_id', 'admission_id', 'patient_id', 'requesting_physician_id', 'requested_examination', 'request_date_time', 'clinical_reason_examination', 'priority', 'order_status']

===== DATA TYPES =====
order_id                       int64
admission_id                   int64
patient_id                     int64
requesting_physician_id        int64
requested_examination            str
request_date_time                str
clinical_reason_examination      str
priority                         str
order_status                     str

===== MISSING VALUES =====
order_id                       0
admission_id                   0
patient_id                     0
requesting_physician_id        0
requested_examination          0
request_date_time              0
clinical_reason_examination    0
priority                       0
order_status                   4

===== HIDDEN MISSING VALUES (String 'N/A') =====
order_id                       0
admission_id                   0
patient_id                     0
requesting_physician_id        0
requested_examination          0
request_date_time              0
clinical_reason_examination    0
priority                       0
order_status                   0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     order_id  admission_id  patient_id  requesting_physician_id requested_examination    request_date_time    clinical_reason_examination priority order_status
128       129           506         243                        6             MRI Brain  2026-05-19 06:00:00  Evaluate for acute pathology.  Routine    Cancelled
23         24           105         190                        9           Chest X-Ray  2026-05-02 16:30:00  Evaluate for acute pathology.     STAT      Pending
85         86           322         578                        5       CT Scan - Chest  2026-01-28 10:45:00   Rule out pulmonary embolism.  Routine    Completed
86         87           325         709                       10       CT Scan - Chest  2026-01-12 21:30:00   Rule out pulmonary embolism.     STAT    Completed
103       104          9999         800                       11             MRI Brain  2026-03-22 03:30:00  Evaluate for acute pathology.     STAT    Cancelled

===== SUMMARY STATISTICS =====
          order_id  admission_id  patient_id  requesting_physician_id requested_examination    request_date_time    clinical_reason_examination priority order_status
count   275.000000    275.000000  275.000000               275.000000                   275                  275                            275      275          271
unique         NaN           NaN         NaN                      NaN                     4                  274                              2        9            3
top            NaN           NaN         NaN                      NaN       CT Scan - Chest  2026-08-17 19:00:00  Evaluate for acute pathology.  Routine      Pending
freq           NaN           NaN         NaN                      NaN                    76                    2                            199       97           92
mean    138.000000    780.672727  383.640000                 8.276364                   NaN                  NaN                            NaN      NaN          NaN
std      79.529869   1423.536291  237.854517                 4.212857                   NaN                  NaN                            NaN      NaN          NaN
min       1.000000      2.000000    2.000000                 1.000000                   NaN                  NaN                            NaN      NaN          NaN
25%      69.500000    260.500000  186.000000                 5.000000                   NaN                  NaN                            NaN      NaN          NaN
50%     138.000000    588.000000  349.000000                 9.000000                   NaN                  NaN                            NaN      NaN          NaN
75%     206.500000    920.500000  606.000000                12.000000                   NaN                  NaN                            NaN      NaN          NaN
max     275.000000   9999.000000  800.000000                15.000000                   NaN                  NaN                            NaN      NaN          NaN
