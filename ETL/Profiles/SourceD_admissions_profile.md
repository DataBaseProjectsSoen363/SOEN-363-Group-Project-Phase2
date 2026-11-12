===== RECORD COUNT =====
1200

===== SHAPE =====
(1200, 8)

===== FIELD NAMES =====
['visitId', 'patientId', 'admitTimestamp', 'admissionType', 'reason', 'doctorId', 'dischargeTimestamp', 'diagnoses']

===== DATA TYPES =====
visitId                 int64
patientId               int64
admitTimestamp          int64
admissionType             str
reason                    str
doctorId                int64
dischargeTimestamp    float64
diagnoses                 str

===== MISSING VALUES =====
visitId                 0
patientId               0
admitTimestamp          0
admissionType           0
reason                  0
doctorId                0
dischargeTimestamp     44
diagnoses             138

===== HIDDEN MISSING VALUES (String 'N/A') =====
visitId               0
patientId             0
admitTimestamp        0
admissionType         0
reason                0
doctorId              0
dischargeTimestamp    0
diagnoses             0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      visitId  patientId  admitTimestamp admissionType               reason  doctorId  dischargeTimestamp                                                                                                                                                                                                                                                                               diagnoses
859       860        293      1773093600        URGENT           Chest Pain         6        1.773439e+09                                                                                                                                                                                            [{'icd9Code': '410.9', 'isPrimary': True, 'doctorId': 11, 'diagnosisTimestamp': 1773118800}]
1189     1190         89      1779278400        URGENT                Fever         2        1.779538e+09                                                                                                 [{'icd9Code': '272.4', 'isPrimary': True, 'doctorId': 7, 'diagnosisTimestamp': 1779303600}, {'icd9Code': '410.9', 'isPrimary': False, 'doctorId': 3, 'diagnosisTimestamp': 1779314400}]
956       957        580      1785913200        URGENT                Fever         2        1.786777e+09  [{'icd9Code': '250.00', 'isPrimary': True, 'doctorId': 11, 'diagnosisTimestamp': 1785931200}, {'icd9Code': '272.4', 'isPrimary': False, 'doctorId': 15, 'diagnosisTimestamp': 1785942000}, {'icd9Code': '401.9', 'isPrimary': False, 'doctorId': 4, 'diagnosisTimestamp': 1785938400}]
1133     1134        532      1782082800        URGENT  Shortness of Breath         9        1.782515e+09                                                                                                                                                                                                                                                                                     NaN
248       249        276      1780653600     EMERGENCY                Fever         1        1.781345e+09                                                                                               [{'icd9Code': '401.9', 'isPrimary': True, 'doctorId': 11, 'diagnosisTimestamp': 1780657200}, {'icd9Code': '410.9', 'isPrimary': False, 'doctorId': 14, 'diagnosisTimestamp': 1780657200}]

===== SUMMARY STATISTICS =====
            visitId    patientId  admitTimestamp admissionType               reason     doctorId  dischargeTimestamp                                                                                     diagnoses
count   1200.000000  1200.000000    1.200000e+03          1200                 1200  1200.000000        1.156000e+03                                                                                          1062
unique          NaN          NaN             NaN             3                    3          NaN                 NaN                                                                                          1060
top             NaN          NaN             NaN     EMERGENCY  Shortness of Breath          NaN                 NaN  [{'icd9Code': '272.4', 'isPrimary': True, 'doctorId': 10, 'diagnosisTimestamp': 1771016400}]
freq            NaN          NaN             NaN           427                  429          NaN                 NaN                                                                                             2
mean     600.500000   620.759167    1.778087e+09           NaN                  NaN     8.269167        1.778538e+09                                                                                           NaN
std      346.554469  1441.241564    6.350979e+06           NaN                  NaN     4.459442        6.353231e+06                                                                                           NaN
min        1.000000     1.000000    1.767233e+09           NaN                  NaN     1.000000        1.767460e+09                                                                                           NaN
25%      300.750000   213.000000    1.772266e+09           NaN                  NaN     4.000000        1.772770e+09                                                                                           NaN
50%      600.500000   417.000000    1.778092e+09           NaN                  NaN     8.000000        1.778533e+09                                                                                           NaN
75%      900.250000   606.500000    1.783564e+09           NaN                  NaN    12.000000        1.784057e+09                                                                                           NaN
max     1200.000000  9999.000000    1.788905e+09           NaN                  NaN    15.000000        1.789740e+09                                                                                           NaN
