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
      visitId  patientId  admitTimestamp admissionType               reason  doctorId  dischargeTimestamp                                                                                                                                                                                                                                                                             diagnoses
802       803        507      1776783600     EMERGENCY           Chest Pain         4        1.777216e+09                                                                                                                                                                                                                                                                                   NaN
391       392        270      1774634400        URGENT           Chest Pain         8        1.774721e+09                                                                                                                                                                                           [{'icd9Code': '272.4', 'isPrimary': True, 'doctorId': 1, 'diagnosisTimestamp': 1774666800}]
350       351         20      1768878000     EMERGENCY  Shortness of Breath         2        1.769310e+09  [{'icd9Code': '272.4', 'isPrimary': True, 'doctorId': 6, 'diagnosisTimestamp': 1768896000}, {'icd9Code': '250.00', 'isPrimary': False, 'doctorId': 7, 'diagnosisTimestamp': 1768888800}, {'icd9Code': '410.9', 'isPrimary': False, 'doctorId': 1, 'diagnosisTimestamp': 1768896000}]
1111     1112         16      1772060400      ELECTIVE           Chest Pain         6        1.772320e+09                                                                                                                                                                                          [{'icd9Code': '410.9', 'isPrimary': True, 'doctorId': 12, 'diagnosisTimestamp': 1772085600}]
723       724        369      1784775600     EMERGENCY           Chest Pain        11        1.785640e+09                                                                                                                                                                                           [{'icd9Code': '272.4', 'isPrimary': True, 'doctorId': 9, 'diagnosisTimestamp': 1784811600}]

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
