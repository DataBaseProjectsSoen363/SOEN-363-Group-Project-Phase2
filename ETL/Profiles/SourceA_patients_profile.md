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
     patient_id            name health_insurance_number life_status                          address  date_birth  gender emergency_contact_number  phone_number
635         636     Emily Brown              RAMQ727959       Alive  4192 Sherbrooke St, Quebec City  1957-12-27    Male             514-555-7366  514-555-7366
567         568  Sarah Charette              RAMQ872652       Alive            142 Guy St, Longueuil  1956-11-16    Male             514-555-5661  514-555-5661
239         240    Amelie Jones              RAMQ265154       Alive           3678 Guy St, Longueuil  1958-08-21  Female             514-555-3872  514-555-3872
142         143     Emily Brown              RAMQ741181       Alive        3963 Sherbrooke St, Laval  1958-09-25  Female             514-555-6140  514-555-6140
790         791   John Charette              RAMQ648600       Alive    2473 Atwater Ave, Quebec City  1981-10-24    Male             514-555-1255  514-555-1255

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
