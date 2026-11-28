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

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     patient_id           name health_insurance_number life_status                                    address  date_birth  gender emergency_contact_number  phone_number
16           17     John Brown              RAMQ585100       Alive             2146 Sherbrooke St, Sherbrooke  1959-09-06    Male             514-555-4872  514-555-4872
693         694   Amelie Brown              RAMQ238320       Alive     1006 SAINTE-CATHERINE ST, LONGUEUIL     1973-08-28  Female             514-555-3626  514-555-3626
599         600   Emily Miller              RAMQ633618       Alive              2199 Papineau Ave, Sherbrooke  1953-05-09    Male             514-555-1722  514-555-1722
410         411  Amelie Taylor              RAMQ318379       Alive               4830 Papineau Ave, Longueuil  1995-08-29    Male             514-555-7147  514-555-7147
387         388   Amelie Brown              RAMQ192059       Alive              3231 Atwater Ave, Quebec City  1947-06-19    Male             514-555-7987  514-555-7987

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
