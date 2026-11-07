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
     patientId                                     name  dobTimestamp gender                                           contact
297        298       {'first': 'Ren', 'last': 'Suzuki'}    1185889225      F  {'phone': '+81-89-9926-8359', 'city': 'Sapporo'}
474        475          {'first': 'Aoi', 'last': 'Ito'}     931700425      M    {'phone': '+81-85-1565-7141', 'city': 'Osaka'}
94          95          {'first': 'Aoi', 'last': 'Ito'}    -739880374      F    {'phone': '+81-87-6060-9999', 'city': 'Tokyo'}
29          30  {'first': 'Sakura', 'last': 'Watanabe'}    -398686774      F    {'phone': '+81-80-6940-2194', 'city': 'Kyoto'}
539        540  {'first': 'Sakura', 'last': 'Watanabe'}    1065966025      F    {'phone': '+81-82-6924-5764', 'city': 'Tokyo'}

===== SUMMARY STATISTICS =====
        patientId                                  name  dobTimestamp gender                           contact
count    800.0000                                   800  8.000000e+02    800                               800
unique        NaN                                    48           NaN      2                               772
top           NaN  {'first': 'Ren', 'last': 'Watanabe'}           NaN      M  {'phone': None, 'city': 'Osaka'}
freq          NaN                                    26           NaN    410                                 9
mean     400.5000                                   NaN  1.740375e+08    NaN                               NaN
std      231.0844                                   NaN  5.746581e+08    NaN                               NaN
min        1.0000                                   NaN -7.975956e+08    NaN                               NaN
25%      200.7500                                   NaN -3.446868e+08    NaN                               NaN
50%      400.5000                                   NaN  1.755276e+08    NaN                               NaN
75%      600.2500                                   NaN  6.664092e+08    NaN                               NaN
max      800.0000                                   NaN  1.230472e+09    NaN                               NaN
