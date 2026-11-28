===== RECORD COUNT =====
237

===== SHAPE =====
(237, 6)

===== FIELD NAMES =====
['surgery_id', 'visit_id', 'surgeon_mrn', 'proc_code', 'proc_name', 'surgery_datetime']

===== DATA TYPES =====
surgery_id          int64
visit_id            int64
surgeon_mrn           str
proc_code             str
proc_name             str
surgery_datetime      str

===== MISSING VALUES =====
surgery_id          0
visit_id            0
surgeon_mrn         0
proc_code           0
proc_name           0
surgery_datetime    5

===== HIDDEN MISSING VALUES (String 'N/A') =====
surgery_id          0
visit_id            0
surgeon_mrn         0
proc_code           0
proc_name           0
surgery_datetime    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     surgery_id  visit_id surgeon_mrn   proc_code               proc_name  surgery_datetime
115         116       646   MRN-10003   PROC-CABG  Coronary Artery Bypass  17/03/2026 17:00
133         134       708   MRN-10013  PROC-BOWEL         Bowel Resection  20/06/2026 05:00
146         147       786   MRN-10008    PROC-APP            Appendectomy  07/01/2026 19:00
216         217      1087   MRN-10012   PROC-CABG  Coronary Artery Bypass  21/04/2026 00:00
90           91       495   MRN-10015  PROC-BOWEL         Bowel Resection  03/05/2026 02:00

===== SUMMARY STATISTICS =====
        surgery_id     visit_id surgeon_mrn   proc_code        proc_name  surgery_datetime
count   237.000000   237.000000         237         237              237               232
unique         NaN          NaN          15           5                5               229
top            NaN          NaN   MRN-10012  PROC-BOWEL  Bowel Resection  13/05/2026 01:00
freq           NaN          NaN          22          63               63                 2
mean    119.000000   784.308017         NaN         NaN              NaN               NaN
std      68.560193  1257.895250         NaN         NaN              NaN               NaN
min       1.000000     2.000000         NaN         NaN              NaN               NaN
25%      60.000000   326.000000         NaN         NaN              NaN               NaN
50%     119.000000   670.000000         NaN         NaN              NaN               NaN
75%     178.000000   937.000000         NaN         NaN              NaN               NaN
max     237.000000  9999.000000         NaN         NaN              NaN               NaN
