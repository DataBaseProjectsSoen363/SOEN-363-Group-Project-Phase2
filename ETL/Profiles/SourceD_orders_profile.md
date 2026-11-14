===== RECORD COUNT =====
307

===== SHAPE =====
(307, 9)

===== FIELD NAMES =====
['orderId', 'visitId', 'doctorId', 'examType', 'orderTimestamp', 'examTimestamp', 'technician', 'report_findings', 'report_conclusion']

===== DATA TYPES =====
orderId              int64
visitId              int64
doctorId             int64
examType               str
orderTimestamp       int64
examTimestamp        int64
technician             str
report_findings        str
report_conclusion      str

===== MISSING VALUES =====
orderId               0
visitId               0
doctorId              0
examType              0
orderTimestamp        0
examTimestamp         0
technician            0
report_findings      15
report_conclusion    15

===== HIDDEN MISSING VALUES (String 'N/A') =====
orderId              0
visitId              0
doctorId             0
examType             0
orderTimestamp       0
examTimestamp        0
technician           0
report_findings      0
report_conclusion    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     orderId  visitId  doctorId examType  orderTimestamp  examTimestamp technician report_findings   report_conclusion
250      251      991         4    X-Ray      1780729200     1780736400     Tech_2           Clear  No acute findings.
268      269     1057         3      MRI      1774497600     1774504800     Tech_8           Clear  No acute findings.
159      160      605        13  CT Scan      1785920400     1785927600     Tech_1          Normal  No acute findings.
229      230      897        12      MRI      1770429600     1770436800     Tech_1           Clear  No acute findings.
305      306     1185         3    X-Ray      1783587600     1783594800     Tech_1           Clear  No acute findings.

===== SUMMARY STATISTICS =====
           orderId      visitId    doctorId examType  orderTimestamp  examTimestamp technician report_findings   report_conclusion
count   307.000000   307.000000  307.000000      307    3.070000e+02   3.070000e+02        307             292                 292
unique         NaN          NaN         NaN        3             NaN            NaN         10               3                   1
top            NaN          NaN         NaN    X-Ray             NaN            NaN     Tech_3          Normal  No acute findings.
freq           NaN          NaN         NaN      108             NaN            NaN         39             103                 292
mean    154.000000   585.374593    8.302932      NaN    1.777701e+09   1.777709e+09        NaN             NaN                 NaN
std      88.767487   357.883922    4.160516      NaN    6.333364e+06   6.333364e+06        NaN             NaN                 NaN
min       1.000000     1.000000    1.000000      NaN    1.767262e+09   1.767269e+09        NaN             NaN                 NaN
25%      77.500000   288.500000    5.000000      NaN    1.772190e+09   1.772197e+09        NaN             NaN                 NaN
50%     154.000000   586.000000    8.000000      NaN    1.777432e+09   1.777439e+09        NaN             NaN                 NaN
75%     230.500000   902.500000   12.000000      NaN    1.783373e+09   1.783381e+09        NaN             NaN                 NaN
max     307.000000  1197.000000   15.000000      NaN    1.788869e+09   1.788876e+09        NaN             NaN                 NaN
