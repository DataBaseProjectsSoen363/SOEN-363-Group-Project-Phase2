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
     patient_id              name health_insurance_number life_status                          address  date_birth  gender emergency_contact_number  phone_number
781         782     Daniel Miller              RAMQ169045       Alive    4459 Sherbrooke St, Longueuil  1953-05-30  Female             514-555-2659  514-555-2659
654         655      Daniel Smith              RAMQ930248       Alive          159 Guy St, Quebec City  1985-03-16  Female             514-555-8036  514-555-8036
282         283      Rachel Smith              RAMQ861949       Alive           2136 Guy St, Longueuil  1951-07-06    Male             514-555-3571  514-555-3571
309         310  Jessica Williams              RAMQ803904       Alive    2021 Sherbrooke St, Longueuil  1991-09-11  Female             514-555-6008  514-555-6008
573         574      Rachel Brown              RAMQ419987       Alive  2422 Sainte-Catherine St, Laval  2027-11-06  Female             514-555-1732  514-555-1732

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
