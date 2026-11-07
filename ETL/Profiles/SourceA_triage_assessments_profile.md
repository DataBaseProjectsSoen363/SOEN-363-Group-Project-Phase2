===== RECORD COUNT =====
1200

===== SHAPE =====
(1200, 13)

===== FIELD NAMES =====
['triage_id', 'admission_id', 'nurse_id', 'blood_pressure', 'heart_rate', 'respiratory_rate', 'body_temperature', 'oxygen_saturation', 'pain_level', 'reported_symptoms', 'known_allergies', 'current_medications', 'triage_priority_level']

===== DATA TYPES =====
triage_id                  int64
admission_id               int64
nurse_id                 float64
blood_pressure               str
heart_rate                 int64
respiratory_rate           int64
body_temperature         float64
oxygen_saturation          int64
pain_level                   str
reported_symptoms            str
known_allergies              str
current_medications          str
triage_priority_level        str

===== MISSING VALUES =====
triage_id                  0
admission_id               0
nurse_id                  28
blood_pressure             0
heart_rate                 0
respiratory_rate           0
body_temperature           0
oxygen_saturation          0
pain_level                 0
reported_symptoms          0
known_allergies          240
current_medications      197
triage_priority_level      0

===== HIDDEN MISSING VALUES (String 'N/A') =====
triage_id                0
admission_id             0
nurse_id                 0
blood_pressure           0
heart_rate               0
respiratory_rate         0
body_temperature         0
oxygen_saturation        0
pain_level               0
reported_symptoms        0
known_allergies          0
current_medications      0
triage_priority_level    0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
      triage_id  admission_id  nurse_id blood_pressure  heart_rate  respiratory_rate  body_temperature  oxygen_saturation pain_level reported_symptoms known_allergies current_medications    triage_priority_level
1103       1104          1104      18.0         121/82          81                18              38.5                 97         10         Dizziness      Penicillin           Metformin                   Urgent
1053       1054          1054      24.0         102/65          70                15              36.0                100          3    Abdominal Pain      Penicillin           Metformin                  Routine
175         176           176      22.0         112/89          75                20              38.1                 96          3  Chest Discomfort      Penicillin        Atorvastatin  High-Priority Emergency
413         414           414      16.0         133/89          68                17              37.9                 94          1             Fever             NaN             Aspirin                   Urgent
488         489           489      18.0         128/60          67                20              37.3                 96          4         Dizziness      Penicillin             Aspirin                     STAT

===== SUMMARY STATISTICS =====
          triage_id  admission_id     nurse_id blood_pressure   heart_rate  respiratory_rate  body_temperature  oxygen_saturation pain_level    reported_symptoms known_allergies current_medications triage_priority_level
count   1200.000000   1200.000000  1172.000000           1200  1200.000000       1200.000000       1200.000000        1200.000000       1200                 1200             960                1003                  1200
unique          NaN           NaN          NaN            770          NaN               NaN               NaN                NaN         21                    5               4                   5                    15
top             NaN           NaN          NaN         128/63          NaN               NaN               NaN                NaN          9  Shortness of Breath         Peanuts           Metformin               Routine
freq            NaN           NaN          NaN              5          NaN               NaN               NaN                NaN        125                  251             263                 211                   299
mean     600.500000    805.145833    20.546075            NaN    80.915833         16.974167         37.436917          93.546667        NaN                  NaN             NaN                 NaN                   NaN
std      346.554469   1410.884529     2.860030            NaN    32.331897          3.137414          1.435048          15.207637        NaN                  NaN             NaN                 NaN                   NaN
min        1.000000      1.000000    16.000000            NaN   -99.000000         12.000000         36.000000           0.000000        NaN                  NaN             NaN                 NaN                   NaN
25%      300.750000    310.750000    18.000000            NaN    71.000000         14.000000         36.600000          94.000000        NaN                  NaN             NaN                 NaN                   NaN
50%      600.500000    615.500000    21.000000            NaN    85.000000         17.000000         37.200000          96.000000        NaN                  NaN             NaN                 NaN                   NaN
75%      900.250000    920.250000    23.000000            NaN    98.000000         20.000000         37.900000          98.000000        NaN                  NaN             NaN                 NaN                   NaN
max     1200.000000   9999.000000    25.000000            NaN   110.000000         22.000000         45.200000         100.000000        NaN                  NaN             NaN                 NaN                   NaN
