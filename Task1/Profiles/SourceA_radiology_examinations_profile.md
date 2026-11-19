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
250             251       251             MRI Brain   2026-04-17 21:45:00               Head                      13     Tech D. Tremblay          Finalized     DICOM-6295
157             158       158             MRI Brain   2026-07-08 23:00:00               Head                       1          Tech A. Roy            Pending     DICOM-1657
222             223       223  Abdominal Ultrasound   2026-05-20 01:45:00            Abdomen                       3     Tech D. Tremblay            Pending     DICOM-6980
196             197       197             MRI Brain   2026-01-01 16:15:00               Head                       9          Tech A. Roy          Finalized     DICOM-6551
133             134       134       CT Scan - Chest   2026-02-27 07:45:00              Chest                      14       Tech B. Gagnon          Finalized            NaN

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
