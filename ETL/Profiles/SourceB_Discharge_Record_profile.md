===== RECORD COUNT =====
1148

===== SHAPE =====
(1148, 6)

===== FIELD NAMES =====
['discharge_id', 'visit_id', 'discharge_datetime', 'disposition_code', 'followup_date', 'discharging_doctor_mrn']

===== DATA TYPES =====
discharge_id              int64
visit_id                  int64
discharge_datetime          str
disposition_code            str
followup_date               str
discharging_doctor_mrn      str

===== MISSING VALUES =====
discharge_id                0
visit_id                    0
discharge_datetime          0
disposition_code            0
followup_date             369
discharging_doctor_mrn      0

===== HIDDEN MISSING VALUES (String 'N/A') =====
discharge_id              0
visit_id                  0
discharge_datetime        0
disposition_code          0
followup_date             0
discharging_doctor_mrn    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      discharge_id  visit_id discharge_datetime disposition_code followup_date discharging_doctor_mrn
1087          1088      1134   26/06/2026 19:00              SNF    10/07/2026              MRN-10010
20              21        21   30/04/2026 22:00              SNF           NaN              MRN-10015
633            634       657   25/07/2026 11:00              SNF    08/08/2026              MRN-10001
431            432       448   28/06/2026 17:00            REHAB    12/07/2026              MRN-10008
1071          1072      1118   13/05/2026 09:00             HOME    27/05/2026              MRN-10009

===== SUMMARY STATISTICS =====
        discharge_id     visit_id discharge_datetime disposition_code followup_date discharging_doctor_mrn
count    1148.000000  1148.000000               1148             1148           779                   1148
unique           NaN          NaN               1039                4           243                     15
top              NaN          NaN   07/07/2026 05:00              SNF    20/04/2026              MRN-10015
freq             NaN          NaN                  3              308             9                     90
mean      574.500000   736.468641                NaN              NaN           NaN                    NaN
std       331.543361  1187.080519                NaN              NaN           NaN                    NaN
min         1.000000     1.000000                NaN              NaN           NaN                    NaN
25%       287.750000   299.750000                NaN              NaN           NaN                    NaN
50%       574.500000   605.500000                NaN              NaN           NaN                    NaN
75%       861.250000   910.250000                NaN              NaN           NaN                    NaN
max      1148.000000  9999.000000                NaN              NaN           NaN                    NaN
