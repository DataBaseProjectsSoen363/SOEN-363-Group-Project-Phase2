===== RECORD COUNT =====
800

===== SHAPE =====
(800, 5)

===== FIELD NAMES =====
['patientId', 'name', 'dobTimestamp', 'gender', 'contact']

===== DATA TYPES =====
patientId       int64
name              str
dobTimestamp    int64
gender            str
contact           str

===== MISSING VALUES =====
patientId       0
name            0
dobTimestamp    0
gender          0
contact         0

===== HIDDEN MISSING VALUES (String 'N/A') =====
patientId       0
name            0
dobTimestamp    0
gender          0
contact         0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     patientId                                    name  dobTimestamp gender                                         contact
705        706      {'first': 'Ren', 'last': 'Tanaka'}    -149955583      F               {'phone': None, 'city': 'Nagoya'}
236        237   {'first': 'Yuki', 'last': 'Watanabe'}     807702016      M  {'phone': '+81-82-7787-1211', 'city': 'Kyoto'}
535        536   {'first': 'Sota', 'last': 'Watanabe'}     563967616      F  {'phone': '+81-90-5076-5974', 'city': 'Osaka'}
458        459        {'first': 'Sota', 'last': 'Ito'}    -184947583      F  {'phone': '+81-85-6617-3323', 'city': 'Osaka'}
121        122  {'first': 'Hina', 'last': 'Takahashi'}     -52841983      M  {'phone': '+81-89-4339-4662', 'city': 'Osaka'}

===== SUMMARY STATISTICS =====
        patientId                                  name  dobTimestamp gender                           contact
count    800.0000                                   800  8.000000e+02    800                               800
unique        NaN                                    48           NaN      2                               772
top           NaN  {'first': 'Ren', 'last': 'Watanabe'}           NaN      M  {'phone': None, 'city': 'Osaka'}
freq          NaN                                    26           NaN    410                                 9
mean     400.5000                                   NaN  1.745415e+08    NaN                               NaN
std      231.0844                                   NaN  5.746581e+08    NaN                               NaN
min        1.0000                                   NaN -7.970916e+08    NaN                               NaN
25%      200.7500                                   NaN -3.441828e+08    NaN                               NaN
50%      400.5000                                   NaN  1.760316e+08    NaN                               NaN
75%      600.2500                                   NaN  6.669132e+08    NaN                               NaN
max      800.0000                                   NaN  1.230976e+09    NaN                               NaN
