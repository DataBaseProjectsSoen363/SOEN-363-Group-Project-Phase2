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
     patient_id             name health_insurance_number life_status                                address  date_birth  gender emergency_contact_number  phone_number
204         205   David Charette              RAMQ933197       Alive                862 Guy St, Quebec City  1946-09-23  Female             514-555-8996  514-555-8996
465         466       Rachel Roy              RAMQ105324       Alive           3522 Sherbrooke St, Montreal  1963-10-26  Female             514-555-2605  514-555-2605
151         152      David Smith              RAMQ247442       Alive            4011 PAPINEAU AVE, LAVAL     1974-08-23  Female             514-555-5947  514-555-5947
285         286   David Tremblay              RAMQ100177       Alive           844 Atwater Ave, Quebec City  1963-06-13  Female             514-555-6953  514-555-6953
388         389  Rachel Williams              RAMQ238173       Alive  1793 Sainte-Catherine St, Quebec City  1990-11-26  Female             514-555-9582  514-555-9582

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
