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
     discharge_record_id  admission_id  discharge_date_time         discharge_destination condition_at_discharge discharge_status                    followup_instructions followup_appointments  responsible_physician
121                  122           124  2026-08-28 21:30:00                Long-Term Care                 Stable       Discharged  Follow up with primary care in 2 weeks.            2026-09-11                     10
63                    64            65  2026-06-04 08:15:00                LONG-TERM CARE                 Stable       Discharged  Follow up with primary care in 2 weeks.            2026-06-18                      5
472                  473           483  2026-04-04 11:15:00  Transfer to Another Hospital               Improved       Discharged  Follow up with primary care in 2 weeks.            2026-04-18                     11
947                  948           967  2026-04-07 23:30:00  Transfer to Another Hospital        Fully Recovered       Discharged  Follow up with primary care in 2 weeks.                   NaN                     14
107                  108           110  2026-08-03 05:00:00                          Home        Fully Recovered       Discharged  Follow up with primary care in 2 weeks.            2026-08-17                      3

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
