===== RECORD COUNT =====
800

===== SHAPE =====
(800, 9)

===== FIELD NAMES =====
['patient_id', 'name', 'health_insurance_number', 'life_status', 'address', 'date_birth', 'gender', 'emergency_contact_number', 'phone_number']

===== DATA TYPES =====
patient_id                  int64
name                          str
health_insurance_number       str
life_status                   str
address                       str
date_birth                    str
gender                        str
emergency_contact_number      str
phone_number                  str

===== MISSING VALUES =====
patient_id                   0
name                         0
health_insurance_number      0
life_status                  0
address                      0
date_birth                   0
gender                       1
emergency_contact_number    19
phone_number                19

===== HIDDEN MISSING VALUES (String 'N/A') =====
patient_id                  0
name                        0
health_insurance_number     0
life_status                 0
address                     0
date_birth                  0
gender                      0
emergency_contact_number    0
phone_number                0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     patient_id              name health_insurance_number life_status                             address  date_birth  gender emergency_contact_number  phone_number
686         687      Daniel Brown              RAMQ866296       Alive             1217 Guy St, Sherbrooke  1948-05-03    Male             514-555-4115  514-555-4115
283         284  Jessica Charette              RAMQ178501       Alive            4127 Papineau Ave, Laval  1984-02-06    Male             514-555-7203  514-555-7203
91           92  Michael Tremblay              RAMQ836833       Alive     2631 PAPINEAU AVE, LONGUEUIL     1996-03-14  Female             514-555-1502  514-555-1502
717         718       David Smith              RAMQ215485       Alive       1939 Sherbrooke St, Longueuil  1953-10-25  Female             514-555-2389  514-555-2389
412         413   Amelie Charette              RAMQ417329       Alive         1870 Atwater Ave, Longueuil  1975-06-25    Male             514-555-8270  514-555-8270

===== SUMMARY STATISTICS =====
        patient_id           name health_insurance_number life_status                        address  date_birth gender emergency_contact_number  phone_number
count     800.0000            800                     800         800                            800         800    799                      781           781
unique         NaN            100                     784           1                            798         778      4                      751           751
top            NaN  Michael Smith              RAMQ900581       Alive  1295 Sherbrooke St, Longueuil  2027-11-06   Male             514-555-9151  514-555-9151
freq           NaN             15                       2         800                              2           8    410                        3             3
mean      400.5000            NaN                     NaN         NaN                            NaN         NaN    NaN                      NaN           NaN
std       231.0844            NaN                     NaN         NaN                            NaN         NaN    NaN                      NaN           NaN
min         1.0000            NaN                     NaN         NaN                            NaN         NaN    NaN                      NaN           NaN
25%       200.7500            NaN                     NaN         NaN                            NaN         NaN    NaN                      NaN           NaN
50%       400.5000            NaN                     NaN         NaN                            NaN         NaN    NaN                      NaN           NaN
75%       600.2500            NaN                     NaN         NaN                            NaN         NaN    NaN                      NaN           NaN
max       800.0000            NaN                     NaN         NaN                            NaN         NaN    NaN                      NaN           NaN
