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
201      202      795        13  CT Scan      1782388800     1782396000     Tech_8    Mild opacity  No acute findings.
181      182      705        15  CT Scan      1783846800     1783854000     Tech_2          Normal  No acute findings.
110      111      399        12      MRI      1767837600     1767844800     Tech_9          Normal  No acute findings.
275      276     1070         3      MRI      1775804400     1775811600     Tech_4    Mild opacity  No acute findings.
23        24       73        11    X-Ray      1774526400     1774533600     Tech_4    Mild opacity  No acute findings.

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
