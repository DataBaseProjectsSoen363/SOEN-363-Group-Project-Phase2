===== RECORD COUNT =====
275

===== SHAPE =====
(275, 9)

===== FIELD NAMES =====
['examination_id', 'order_id', 'examination_type', 'examination_date_time', 'body_area_examined', 'referring_physician_id', 'radiology_technician', 'examination_status', 'medical_images']

===== DATA TYPES =====
examination_id            int64
order_id                  int64
examination_type            str
examination_date_time       str
body_area_examined          str
referring_physician_id    int64
radiology_technician        str
examination_status          str
medical_images              str

===== MISSING VALUES =====
examination_id             0
order_id                   0
examination_type           0
examination_date_time      0
body_area_examined        11
referring_physician_id     0
radiology_technician       0
examination_status         0
medical_images             9

===== HIDDEN MISSING VALUES (String 'N/A') =====
examination_id            0
order_id                  0
examination_type          0
examination_date_time     0
body_area_examined        0
referring_physician_id    0
radiology_technician      0
examination_status        0
medical_images            0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     examination_id  order_id      examination_type examination_date_time body_area_examined  referring_physician_id radiology_technician examination_status medical_images
265             266       266  Abdominal Ultrasound   2026-07-24 22:00:00            Abdomen                       8       Tech B. Gagnon        In Progress     DICOM-2033
165             166       166           Chest X-Ray   2026-07-27 16:00:00              Chest                       3     Tech D. Tremblay          Finalized     DICOM-2440
269             270       270       CT Scan - Chest   2026-08-04 22:15:00              Chest                      14        Tech C. Smith            Pending     DICOM-5612
40               41        41             MRI Brain   2026-07-16 01:30:00               Head                      12        Tech C. Smith        In Progress     DICOM-3967
58               59        59             MRI Brain   2026-08-21 00:15:00               Head                       1        Tech C. Smith          Finalized            NaN

===== SUMMARY STATISTICS =====
        examination_id     order_id examination_type examination_date_time body_area_examined  referring_physician_id radiology_technician examination_status medical_images
count       275.000000   275.000000              275                   275                264              275.000000                  275                275            266
unique             NaN          NaN                4                   273                  3                     NaN                    4                 11            261
top                NaN          NaN  CT Scan - Chest   2026-06-13 14:00:00              Chest                     NaN        Tech C. Smith        In Progress     DICOM-7195
freq               NaN          NaN               76                     2                131                     NaN                   74                 92              2
mean        138.000000   209.934545              NaN                   NaN                NaN                8.130909                  NaN                NaN            NaN
std          79.529869   843.106185              NaN                   NaN                NaN                4.317376                  NaN                NaN            NaN
min           1.000000     1.000000              NaN                   NaN                NaN                1.000000                  NaN                NaN            NaN
25%          69.500000    70.500000              NaN                   NaN                NaN                4.000000                  NaN                NaN            NaN
50%         138.000000   139.000000              NaN                   NaN                NaN                8.000000                  NaN                NaN            NaN
75%         206.500000   208.000000              NaN                   NaN                NaN               12.000000                  NaN                NaN            NaN
max         275.000000  9999.000000              NaN                   NaN                NaN               15.000000                  NaN                NaN            NaN
