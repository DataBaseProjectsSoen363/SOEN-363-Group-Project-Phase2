===== RECORD COUNT =====
360

===== SHAPE =====
(360, 8)

===== FIELD NAMES =====
['stay_id', 'visit_id', 'doctor_mrn', 'ward_type', 'ventilator_used', 'in_date', 'out_date', 'transfer_reason']

===== DATA TYPES =====
stay_id            int64
visit_id           int64
doctor_mrn           str
ward_type            str
ventilator_used      str
in_date              str
out_date             str
transfer_reason      str

===== MISSING VALUES =====
stay_id             0
visit_id            0
doctor_mrn          0
ward_type           0
ventilator_used     0
in_date             0
out_date           18
transfer_reason     0

===== HIDDEN MISSING VALUES (String 'N/A') =====
stay_id            0
visit_id           0
doctor_mrn         0
ward_type          0
ventilator_used    0
in_date            0
out_date           0
transfer_reason    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     stay_id  visit_id doctor_mrn ward_type ventilator_used           in_date          out_date        transfer_reason
171      172       595  MRN-10015  WARD-ICU               Y  02/08/2026 11:00  04/08/2026 11:00  Détresse respiratoire
29        30        81  MRN-10001  WARD-ICU               Y  13/08/2026 05:00  15/08/2026 05:00  Détresse respiratoire
188      189       657  MRN-10013  WARD-ICU               N  19/07/2026 14:00  23/07/2026 14:00        Post-opératoire
340      341      1132  MRN-10007  WARD-CCU               Y  09/08/2026 23:00  16/08/2026 23:00  Surveillance continue
197      198       679  MRN-10010  WARD-ICU               N  06/04/2026 19:00  12/04/2026 19:00  SURVEILLANCE CONTINUE

===== SUMMARY STATISTICS =====
           stay_id     visit_id doctor_mrn ward_type ventilator_used           in_date          out_date        transfer_reason
count   360.000000   360.000000        360       360             360               360               342                    360
unique         NaN          NaN         15         3               2               348               328                      6
top            NaN          NaN  MRN-10011  WARD-ICU               Y  03/04/2026 06:00  21/07/2026 05:00  Détresse respiratoire
freq           NaN          NaN         31       131             203                 3                 2                    119
mean    180.500000   756.422222        NaN       NaN             NaN               NaN               NaN                    NaN
std     104.067286  1255.046371        NaN       NaN             NaN               NaN               NaN                    NaN
min       1.000000     1.000000        NaN       NaN             NaN               NaN               NaN                    NaN
25%      90.750000   280.750000        NaN       NaN             NaN               NaN               NaN                    NaN
50%     180.500000   639.000000        NaN       NaN             NaN               NaN               NaN                    NaN
75%     270.250000   929.250000        NaN       NaN             NaN               NaN               NaN                    NaN
max     360.000000  9999.000000        NaN       NaN             NaN               NaN               NaN                    NaN
