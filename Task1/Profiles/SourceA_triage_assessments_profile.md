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
830        831           831      16.0         113/73          65                20              36.1                 96          9             Fever           Latex          Metoprolol  High-Priority Emergency
67          68            68      25.0         101/79         109                22              37.7                100          3         Dizziness             NaN        Atorvastatin                   Urgent
955        956           956      25.0         101/64          66                17              37.1                 92          1         Dizziness             NaN           Metformin  High-Priority Emergency
511        512           512      16.0         116/72          60                12              38.0                 96          0             Fever             NaN                 NaN                  Routine
142        143           143      18.0         107/67          98                14              37.2                 93          5  Chest Discomfort     Sulfa drugs             Aspirin                     STAT

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
