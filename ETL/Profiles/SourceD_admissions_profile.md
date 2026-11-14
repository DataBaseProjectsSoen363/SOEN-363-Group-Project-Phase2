===== RECORD COUNT =====
1200

===== SHAPE =====
(1200, 10)

===== FIELD NAMES =====
['visitId', 'patientId', 'admitTimestamp', 'admissionType', 'reason', 'doctorId', 'dischargeTimestamp', 'diagnosis_codes', 'primary_diagnosis', 'diagnosis_timestamp']

===== DATA TYPES =====
visitId                  int64
patientId                int64
admitTimestamp           int64
admissionType              str
reason                     str
doctorId                 int64
dischargeTimestamp     float64
diagnosis_codes            str
primary_diagnosis      float64
diagnosis_timestamp    float64

===== MISSING VALUES =====
visitId                  0
patientId                0
admitTimestamp           0
admissionType            0
reason                   0
doctorId                 0
dischargeTimestamp      44
diagnosis_codes        134
primary_diagnosis      134
diagnosis_timestamp    153

===== HIDDEN MISSING VALUES (String 'N/A') =====
visitId                0
patientId              0
admitTimestamp         0
admissionType          0
reason                 0
doctorId               0
dischargeTimestamp     0
diagnosis_codes        0
primary_diagnosis      0
diagnosis_timestamp    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      visitId  patientId  admitTimestamp admissionType               reason  doctorId  dischargeTimestamp diagnosis_codes  primary_diagnosis  diagnosis_timestamp
1127     1128        606      1770451200        URGENT  Shortness of Breath         6        1.771315e+09          250.00              250.0         1.770458e+09
268       269        164      1772085600        URGENT           Chest Pain         2        1.772345e+09           410.9              410.9         1.772111e+09
453       454        739      1774249200     EMERGENCY                Fever         1        1.774336e+09   250.00, 401.9              250.0         1.774274e+09
1122     1123        623      1771214400     EMERGENCY           Chest Pain         9        1.771474e+09           272.4              272.4         1.771258e+09
554       555        657      1778266800     EMERGENCY           Chest Pain        13        1.778699e+09          250.00              250.0         1.778281e+09

===== SUMMARY STATISTICS =====
            visitId    patientId  admitTimestamp admissionType               reason     doctorId  dischargeTimestamp diagnosis_codes  primary_diagnosis  diagnosis_timestamp
count   1200.000000  1200.000000    1.200000e+03          1200                 1200  1200.000000        1.156000e+03            1066        1066.000000         1.047000e+03
unique          NaN          NaN             NaN             3                    3          NaN                 NaN              40                NaN                  NaN
top             NaN          NaN             NaN     EMERGENCY  Shortness of Breath          NaN                 NaN           272.4                NaN                  NaN
freq            NaN          NaN             NaN           427                  429          NaN                 NaN              90                NaN                  NaN
mean     600.500000   620.759167    1.778087e+09           NaN                  NaN     8.269167        1.778538e+09             NaN         334.124484         1.778170e+09
std      346.554469  1441.241564    6.350979e+06           NaN                  NaN     4.459442        6.353231e+06             NaN          72.870273         6.324291e+06
min        1.000000     1.000000    1.767233e+09           NaN                  NaN     1.000000        1.767460e+09             NaN         250.000000         1.767247e+09
25%      300.750000   213.000000    1.772266e+09           NaN                  NaN     4.000000        1.772770e+09             NaN         272.400000         1.772460e+09
50%      600.500000   417.000000    1.778092e+09           NaN                  NaN     8.000000        1.778533e+09             NaN         401.900000         1.778227e+09
75%      900.250000   606.500000    1.783564e+09           NaN                  NaN    12.000000        1.784057e+09             NaN         401.900000         1.783683e+09
max     1200.000000  9999.000000    1.788905e+09           NaN                  NaN    15.000000        1.789740e+09             NaN         410.900000         1.788898e+09
