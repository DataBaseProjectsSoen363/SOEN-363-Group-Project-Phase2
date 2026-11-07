===== RECORD COUNT =====
355

===== SHAPE =====
(355, 9)

===== FIELD NAMES =====
['unit_stay_id', 'admission_id', 'responsible_physician_id', 'unit_type', 'room_number', 'bed_number', 'entry_date_time', 'exit_date_time', 'reason_transfer']

===== DATA TYPES =====
unit_stay_id                int64
admission_id                int64
responsible_physician_id    int64
unit_type                     str
room_number                   str
bed_number                    str
entry_date_time               str
exit_date_time                str
reason_transfer               str

===== MISSING VALUES =====
unit_stay_id                 0
admission_id                 0
responsible_physician_id     0
unit_type                    0
room_number                  0
bed_number                   0
entry_date_time              0
exit_date_time              11
reason_transfer              0

===== HIDDEN MISSING VALUES (String 'N/A') =====
unit_stay_id                0
admission_id                0
responsible_physician_id    0
unit_type                   0
room_number                 0
bed_number                  0
entry_date_time             0
exit_date_time              0
reason_transfer             0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     unit_stay_id  admission_id  responsible_physician_id unit_type room_number bed_number      entry_date_time       exit_date_time          reason_transfer
274           275           939                        11      MICU      Room B      Bed 3  2026-01-05 18:30:00  2026-01-11 04:30:00  Post-operative recovery
270           271           929                        10       ICU      Room C      Bed 4  2026-08-05 05:45:00  2026-08-11 14:45:00       Cardiac arrhythmia
236           237           794                         6      SICU      Room A      Bed 1  2026-02-14 13:45:00  2026-02-21 22:45:00  Post-operative recovery
298           299          1019                         6       CCU      Room C      Bed 2  2026-06-16 14:00:00  2026-06-23 15:00:00  Post-operative recovery
198           199           677                        10      MICU      Room A      Bed 2  2026-01-31 13:30:00  2026-02-04 00:30:00       Cardiac arrhythmia

===== SUMMARY STATISTICS =====
        unit_stay_id  admission_id  responsible_physician_id unit_type room_number bed_number      entry_date_time       exit_date_time       reason_transfer
count     355.000000    355.000000                355.000000       355         355        355                  355                  344                   355
unique           NaN           NaN                       NaN        11           3          4                  352                  340                    15
top              NaN           NaN                       NaN      SICU      Room C      Bed 2  2026-03-08 22:45:00  2026-07-27 09:45:00  Respiratory distress
freq             NaN           NaN                       NaN       109         121         96                    2                    2                    73
mean      178.000000    811.357746                  7.597183       NaN         NaN        NaN                  NaN                  NaN                   NaN
std       102.623909   1439.516927                  4.262369       NaN         NaN        NaN                  NaN                  NaN                   NaN
min         1.000000      8.000000                  1.000000       NaN         NaN        NaN                  NaN                  NaN                   NaN
25%        89.500000    315.500000                  4.000000       NaN         NaN        NaN                  NaN                  NaN                   NaN
50%       178.000000    602.000000                  7.000000       NaN         NaN        NaN                  NaN                  NaN                   NaN
75%       266.500000    932.000000                 11.000000       NaN         NaN        NaN                  NaN                  NaN                   NaN
max       355.000000   9999.000000                 15.000000       NaN         NaN        NaN                  NaN                  NaN                   NaN
