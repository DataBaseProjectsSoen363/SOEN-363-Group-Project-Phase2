===== RECORD COUNT =====
307

===== SHAPE =====
(307, 7)

===== FIELD NAMES =====
['order_id', 'visit_id', 'doctor_mrn', 'exam_type', 'order_datetime', 'priority_level', 'order_status']

===== DATA TYPES =====
order_id          int64
visit_id          int64
doctor_mrn          str
exam_type           str
order_datetime      str
priority_level    int64
order_status        str

===== MISSING VALUES =====
order_id           0
visit_id           0
doctor_mrn         0
exam_type          0
order_datetime     0
priority_level     0
order_status      12

===== HIDDEN MISSING VALUES (String 'N/A') =====
order_id          0
visit_id          0
doctor_mrn        0
exam_type         0
order_datetime    0
priority_level    0
order_status      0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     order_id  visit_id doctor_mrn               exam_type    order_datetime  priority_level order_status
194       195      9999  MRN-10012  Echographie Abdominale  31/05/2026 22:00               2    Cancelled
216       217       818  MRN-10011            X-Ray Thorax  26/05/2026 15:00               2      Pending
50         51       177  MRN-10001             IRM Cerveau  21/06/2026 00:00               3      PENDING
284       285      1122  MRN-10005          CT Scan Thorax  29/07/2026 15:00               1    Completed
155       156       585  MRN-10007          CT Scan Thorax  03/04/2026 19:00               2      Pending

===== SUMMARY STATISTICS =====
          order_id     visit_id doctor_mrn    exam_type    order_datetime  priority_level order_status
count   307.000000   307.000000        307          307               307      307.000000          295
unique         NaN          NaN         15            4               300             NaN            8
top            NaN          NaN  MRN-10012  IRM Cerveau  22/05/2026 16:00             NaN    Cancelled
freq           NaN          NaN         28           87                 2             NaN           95
mean    154.000000   785.289902        NaN          NaN               NaN        2.537459          NaN
std      88.767487  1347.448517        NaN          NaN               NaN        1.063843          NaN
min       1.000000     6.000000        NaN          NaN               NaN        1.000000          NaN
25%      77.500000   315.500000        NaN          NaN               NaN        2.000000          NaN
50%     154.000000   590.000000        NaN          NaN               NaN        3.000000          NaN
75%     230.500000   935.500000        NaN          NaN               NaN        3.000000          NaN
max     307.000000  9999.000000        NaN          NaN               NaN        4.000000          NaN
