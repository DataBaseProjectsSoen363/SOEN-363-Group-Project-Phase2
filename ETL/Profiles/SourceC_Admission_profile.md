===== RECORD COUNT =====
1200

===== SHAPE =====
(1200, 8)

===== FIELD NAMES =====
['id', 'patient_ref', 'AdmissionDate', 'DischargeDate', 'AdmissionType', 'Reason', 'DoctorId', 'Diagnoses']

===== DATA TYPES =====
id               int64
patient_ref      int64
AdmissionDate      str
DischargeDate      str
AdmissionType      str
Reason             str
DoctorId         int64
Diagnoses          str

===== MISSING VALUES =====
id                 0
patient_ref        0
AdmissionDate      0
DischargeDate     26
AdmissionType      0
Reason             0
DoctorId           0
Diagnoses        107

===== HIDDEN MISSING VALUES (String 'N/A') =====
id               0
patient_ref      0
AdmissionDate    0
DischargeDate    0
AdmissionType    0
Reason           0
DoctorId         0
Diagnoses        0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
        id  patient_ref        AdmissionDate        DischargeDate AdmissionType  Reason  DoctorId   Diagnoses
1107  1108          744  2026-09-06T12:00:00  2026-09-11T12:00:00      Elective  Fiebre         3  \n        
1084  1085           49  2026-02-28T12:00:00  2026-03-01T12:00:00      Elective  Fiebre         7  \n        
481    482          419  2026-07-15T06:00:00  2026-07-18T06:00:00     Emergency  Fiebre         2  \n        
208    209          732  2026-04-24T17:00:00  2026-04-27T17:00:00      Elective  Fiebre         7  \n        
410    411          792  2026-05-31T09:00:00  2026-06-02T09:00:00      Elective  Fiebre        11  \n        

===== SUMMARY STATISTICS =====
                 id  patient_ref        AdmissionDate        DischargeDate AdmissionType  Reason     DoctorId   Diagnoses
count   1200.000000  1200.000000                 1200                 1174          1200    1200  1200.000000        1093
unique          NaN          NaN                 1087                 1066             3       6          NaN           1
top             NaN          NaN  2026-08-27T06:00:00  2026-02-31T14:00:00        Urgent  Fiebre          NaN  \n        
freq            NaN          NaN                    3                    7           417     388          NaN        1093
mean     600.500000   566.194167                  NaN                  NaN           NaN     NaN     7.870000         NaN
std      346.554469  1280.069815                  NaN                  NaN           NaN     NaN     4.399155         NaN
min        1.000000     1.000000                  NaN                  NaN           NaN     NaN     1.000000         NaN
25%      300.750000   199.750000                  NaN                  NaN           NaN     NaN     4.000000         NaN
50%      600.500000   402.000000                  NaN                  NaN           NaN     NaN     8.000000         NaN
75%      900.250000   610.250000                  NaN                  NaN           NaN     NaN    12.000000         NaN
max     1200.000000  9999.000000                  NaN                  NaN           NaN     NaN    15.000000         NaN
