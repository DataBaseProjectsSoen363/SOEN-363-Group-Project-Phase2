===== RECORD COUNT =====
301

===== SHAPE =====
(301, 7)

===== FIELD NAMES =====
['exam_id', 'order_id', 'technician_name', 'scan_datetime', 'contrast_used', 'findings_text', 'radiologist_conclusion']

===== DATA TYPES =====
exam_id                   int64
order_id                  int64
technician_name             str
scan_datetime               str
contrast_used               str
findings_text               str
radiologist_conclusion      str

===== MISSING VALUES =====
exam_id                    0
order_id                   0
technician_name            0
scan_datetime              0
contrast_used              0
findings_text             16
radiologist_conclusion    16

===== HIDDEN MISSING VALUES (String 'N/A') =====
exam_id                   0
order_id                  0
technician_name           0
scan_datetime             0
contrast_used             0
findings_text             0
radiologist_conclusion    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     exam_id  order_id  technician_name     scan_datetime contrast_used                            findings_text             radiologist_conclusion
78        79        82   Tech B. Martin  05/06/2026 15:00             Y                Aucune anomalie détectée.                            Normal.
11        12        12  Tech C. Bernard  01/08/2026 07:00             Y                Aucune anomalie détectée.                            Normal.
198      199       204  Tech C. Bernard  26/02/2026 01:00             N                Aucune anomalie détectée.                            Normal.
136      137       141  Tech C. Bernard  04/07/2026 11:00             Y  Légère opacité au lobe inférieur droit.  Corrélation clinique recommandée.
254      255       261   Tech B. Martin  30/04/2026 03:00             N           Fracture non déplacée visible.  Corrélation clinique recommandée.

===== SUMMARY STATISTICS =====
           exam_id     order_id technician_name     scan_datetime contrast_used                   findings_text             radiologist_conclusion
count   301.000000   301.000000             301               301           301                             285                                285
unique         NaN          NaN               3               293             2                               4                                  2
top            NaN          NaN  Tech A. Dupont  28/07/2026 16:00             Y  Fracture non déplacée visible.  Corrélation clinique recommandée.
freq           NaN          NaN             110                 2           155                              76                                216
mean    151.000000   351.109635             NaN               NaN           NaN                             NaN                                NaN
std      87.035433  1381.018295             NaN               NaN           NaN                             NaN                                NaN
min       1.000000     1.000000             NaN               NaN           NaN                             NaN                                NaN
25%      76.000000    82.000000             NaN               NaN           NaN                             NaN                                NaN
50%     151.000000   158.000000             NaN               NaN           NaN                             NaN                                NaN
75%     226.000000   236.000000             NaN               NaN           NaN                             NaN                                NaN
max     301.000000  9999.000000             NaN               NaN           NaN                             NaN                                NaN
