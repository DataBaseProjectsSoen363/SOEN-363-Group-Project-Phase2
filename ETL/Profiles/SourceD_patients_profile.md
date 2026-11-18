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
     patientId                                    name  dobTimestamp gender                                           contact
452        453  {'first': 'Yuki', 'last': 'Takahashi'}    1029325266      M  {'phone': '+81-80-1324-7673', 'city': 'Sapporo'}
772        773     {'first': 'Hina', 'last': 'Suzuki'}     593696466      F   {'phone': '+81-80-4102-2608', 'city': 'Nagoya'}
238        239   {'first': 'Aoi', 'last': 'Takahashi'}    -793023533      F    {'phone': '+81-82-9949-9753', 'city': 'Tokyo'}
350        351      {'first': 'Ren', 'last': 'Tanaka'}    -182434733      F   {'phone': '+81-89-1615-7109', 'city': 'Nagoya'}
191        192         {'first': 'Aoi', 'last': 'Ito'}    -591279533      F  {'phone': '+81-87-9785-4452', 'city': 'Sapporo'}

===== SUMMARY STATISTICS =====
        patientId                                  name  dobTimestamp gender                           contact
count    800.0000                                   800  8.000000e+02    800                               800
unique        NaN                                    48           NaN      2                               772
top           NaN  {'first': 'Ren', 'last': 'Watanabe'}           NaN      M  {'phone': None, 'city': 'Osaka'}
freq          NaN                                    26           NaN    410                                 9
mean     400.5000                                   NaN  1.745488e+08    NaN                               NaN
std      231.0844                                   NaN  5.746581e+08    NaN                               NaN
min        1.0000                                   NaN -7.970843e+08    NaN                               NaN
25%      200.7500                                   NaN -3.441755e+08    NaN                               NaN
50%      400.5000                                   NaN  1.760389e+08    NaN                               NaN
75%      600.2500                                   NaN  6.669205e+08    NaN                               NaN
max      800.0000                                   NaN  1.230983e+09    NaN                               NaN
