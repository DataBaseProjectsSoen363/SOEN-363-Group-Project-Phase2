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
     patient_id            name health_insurance_number life_status                               address  date_birth gender emergency_contact_number  phone_number
441         442   Rachel Gagnon              RAMQ810638       Alive     1573 PAPINEAU AVE, QUEBEC CITY     2008-04-17   Male             514-555-9605  514-555-9605
112         113      Amelie Roy              RAMQ400814       Alive  3970 Sainte-Catherine St, Sherbrooke  2008-07-31   Male             514-555-3449  514-555-3449
598         599   Jessica Brown              RAMQ749310       Alive            929 Papineau Ave, Montreal  1979-08-11   Male             514-555-2106  514-555-2106
486         487   Jessica Smith              RAMQ401663       Alive  3517 Sainte-Catherine St, Sherbrooke  1951-03-17   Male             514-555-9078  514-555-9078
479         480  Michael Miller              RAMQ938416       Alive                4730 Guy St, Longueuil  1966-01-30   Male             514-555-2914  514-555-2914

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
