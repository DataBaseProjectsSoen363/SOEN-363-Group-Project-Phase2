===== RECORD COUNT =====
299

===== SHAPE =====
(299, 6)

===== FIELD NAMES =====
['orderId', 'visitId', 'doctorId', 'examType', 'orderTimestamp', 'radiologyExam']

===== DATA TYPES =====
orderId           int64
visitId           int64
doctorId          int64
examType            str
orderTimestamp    int64
radiologyExam       str

===== MISSING VALUES =====
orderId           0
visitId           0
doctorId          0
examType          0
orderTimestamp    0
radiologyExam     0

===== HIDDEN MISSING VALUES (String 'N/A') =====
orderId           0
visitId           0
doctorId          0
examType          0
orderTimestamp    0
radiologyExam     0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     orderId  visitId  doctorId examType  orderTimestamp                                                                                                                      radiologyExam
265      266     1077        14  CT Scan      1769583600        {'examTimestamp': 1769590800, 'technician': 'Tech_5', 'report': {'findings': 'Normal', 'conclusion': 'No acute findings.'}}
98        99      341        15  CT Scan      1773478800        {'examTimestamp': 1773486000, 'technician': 'Tech_9', 'report': {'findings': 'Normal', 'conclusion': 'No acute findings.'}}
48        49      157        15  CT Scan      1787745600        {'examTimestamp': 1787752800, 'technician': 'Tech_3', 'report': {'findings': 'Normal', 'conclusion': 'No acute findings.'}}
25        26       83        13  CT Scan      1783998000  {'examTimestamp': 1784005200, 'technician': 'Tech_4', 'report': {'findings': 'Mild opacity', 'conclusion': 'No acute findings.'}}
15        16       53         8  CT Scan      1788246000        {'examTimestamp': 1788253200, 'technician': 'Tech_8', 'report': {'findings': 'Normal', 'conclusion': 'No acute findings.'}}

===== SUMMARY STATISTICS =====
           orderId      visitId    doctorId examType  orderTimestamp                                                                                                                radiologyExam
count   299.000000   299.000000  299.000000      299    2.990000e+02                                                                                                                          299
unique         NaN          NaN         NaN        3             NaN                                                                                                                          299
top            NaN          NaN         NaN    X-Ray             NaN  {'examTimestamp': 1772197200, 'technician': 'Tech_2', 'report': {'findings': 'Normal', 'conclusion': 'No acute findings.'}}
freq           NaN          NaN         NaN      108             NaN                                                                                                                            1
mean    150.000000   572.668896    7.729097      NaN    1.777964e+09                                                                                                                          NaN
std      86.458082   360.068693    4.351601      NaN    6.268047e+06                                                                                                                          NaN
min       1.000000     1.000000    1.000000      NaN    1.767337e+09                                                                                                                          NaN
25%      75.500000   249.500000    4.000000      NaN    1.772352e+09                                                                                                                          NaN
50%     150.000000   546.000000    7.000000      NaN    1.777882e+09                                                                                                                          NaN
75%     224.500000   887.500000   12.000000      NaN    1.783544e+09                                                                                                                          NaN
max     299.000000  1200.000000   15.000000      NaN    1.788847e+09                                                                                                                          NaN
