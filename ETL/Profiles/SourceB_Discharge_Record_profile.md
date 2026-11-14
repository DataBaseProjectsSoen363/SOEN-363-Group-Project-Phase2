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
1066          1067      1113   30/08/2026 07:00              SNF           NaN              MRN-10014
94              95        99   26/07/2026 23:00            REHAB    09/08/2026              MRN-10004
535            536       556   04/08/2026 08:00            REHAB    18/08/2026              MRN-10009
122            123       128   09/07/2026 22:00             HOME    23/07/2026              MRN-10012
607            608       631   29/06/2026 08:00              SNF    13/07/2026              MRN-10001

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
