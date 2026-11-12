===== RECORD COUNT =====
1176

===== SHAPE =====
(1176, 9)

===== FIELD NAMES =====
['discharge_record_id', 'admission_id', 'discharge_date_time', 'discharge_destination', 'condition_at_discharge', 'discharge_status', 'followup_instructions', 'followup_appointments', 'responsible_physician']

===== DATA TYPES =====
discharge_record_id       int64
admission_id              int64
discharge_date_time         str
discharge_destination       str
condition_at_discharge      str
discharge_status            str
followup_instructions       str
followup_appointments       str
responsible_physician     int64

===== MISSING VALUES =====
discharge_record_id         0
admission_id                0
discharge_date_time         0
discharge_destination       0
condition_at_discharge      0
discharge_status            0
followup_instructions       0
followup_appointments     119
responsible_physician       0

===== HIDDEN MISSING VALUES (String 'N/A') =====
discharge_record_id       0
admission_id              0
discharge_date_time       0
discharge_destination     0
condition_at_discharge    0
discharge_status          0
followup_instructions     0
followup_appointments     0
responsible_physician     0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      discharge_record_id  admission_id  discharge_date_time discharge_destination condition_at_discharge discharge_status                    followup_instructions followup_appointments  responsible_physician
519                   520           531  2026-07-16 02:15:00        Rehab Facility                 Stable       Discharged  Follow up with primary care in 2 weeks.                   NaN                      5
663                   664           679  2026-07-21 23:45:00        long-term care               Improved       Discharged  Follow up with primary care in 2 weeks.            2026-08-04                      9
452                   453           462  2026-08-11 02:45:00                  Home               Improved       Discharged  Follow up with primary care in 2 weeks.            2026-08-25                      6
266                   267           273  2026-05-22 16:45:00                  Home        Fully Recovered       Discharged  Follow up with primary care in 2 weeks.            2026-06-05                     14
1043                 1044          1065  2026-05-25 21:30:00        Long-Term Care                 Stable       Discharged  Follow up with primary care in 2 weeks.                   NaN                      3

===== SUMMARY STATISTICS =====
        discharge_record_id  admission_id  discharge_date_time discharge_destination condition_at_discharge discharge_status                    followup_instructions followup_appointments  responsible_physician
count           1176.000000    1176.00000                 1176                  1176                   1176             1176                                     1176                  1057            1176.000000
unique                  NaN           NaN                 1154                    17                      3                2                                        1                   254                    NaN
top                     NaN           NaN  2026-08-22 05:45:00        Long-Term Care                 Stable       Discharged  Follow up with primary care in 2 weeks.            2026-07-11                    NaN
freq                    NaN           NaN                    2                   290                    413             1148                                     1176                    11                    NaN
mean             588.500000     761.17517                  NaN                   NaN                    NaN              NaN                                      NaN                   NaN               8.119048
std              339.626265    1263.54636                  NaN                   NaN                    NaN              NaN                                      NaN                   NaN               4.316947
min                1.000000       1.00000                  NaN                   NaN                    NaN              NaN                                      NaN                   NaN               1.000000
25%              294.750000     303.75000                  NaN                   NaN                    NaN              NaN                                      NaN                   NaN               5.000000
50%              588.500000     614.50000                  NaN                   NaN                    NaN              NaN                                      NaN                   NaN               8.000000
75%              882.250000     919.25000                  NaN                   NaN                    NaN              NaN                                      NaN                   NaN              12.000000
max             1176.000000    9999.00000                  NaN                   NaN                    NaN              NaN                                      NaN                   NaN              15.000000
