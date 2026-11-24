
-- TASK 3: UNIFIED SCHEMA

-- 1. PATIENTS
CREATE TABLE Unified_Patients (
    global_patient_id INT PRIMARY KEY,
    full_name VARCHAR(150),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    dob DATE,
    gender VARCHAR(20),
    phone_number VARCHAR(50),
    address VARCHAR(255),
    city VARCHAR(100)
);

-- 2. ADMISSIONS
CREATE TABLE Unified_Admissions (
    global_admission_id INT PRIMARY KEY,
    global_patient_id INT,
    admission_date_time DATETIME,
    discharge_date_time DATETIME,
    admission_type VARCHAR(50),
    admission_source VARCHAR(50),
    reason_admission VARCHAR(255),
    insurance_information VARCHAR(100),
    current_condition VARCHAR(50),
    admitting_professional_id INT,
    FOREIGN KEY (global_patient_id) REFERENCES Unified_Patients(global_patient_id)
);

-- 3. TRIAGE
CREATE TABLE Unified_Triage (
    global_triage_id INT PRIMARY KEY,
    global_admission_id INT,
    professional_id INT,
    heart_rate INT,
    oxygen_saturation INT,
    blood_pressure VARCHAR(50),
    esi_priority VARCHAR(20),
    FOREIGN KEY (global_admission_id) REFERENCES Unified_Admissions(global_admission_id)
);

-- 4. DIAGNOSES
CREATE TABLE Unified_Diagnoses (
    global_diagnosis_id INT PRIMARY KEY,
    global_admission_id INT,
    diagnosis_code VARCHAR(50),
    diagnosis_date_time DATETIME,
    primary_diagnosis BOOLEAN,
    professional_id INT,
    FOREIGN KEY (global_admission_id) REFERENCES Unified_Admissions(global_admission_id)
);

-- 5. ICU STAYS
CREATE TABLE Unified_ICU_Stays (
    global_icu_id INT PRIMARY KEY,
    global_admission_id INT,
    professional_id INT,
    icu_unit VARCHAR(50),
    entry_date_time DATETIME,
    exit_date_time DATETIME,
    FOREIGN KEY (global_admission_id) REFERENCES Unified_Admissions(global_admission_id)
);

-- 6. CLINICAL NOTES
CREATE TABLE Unified_Clinical_Notes (
    global_note_id INT PRIMARY KEY,
    global_admission_id INT,
    professional_id INT,
    creation_date DATETIME,
    note_format VARCHAR(50),
    note_text TEXT,
    FOREIGN KEY (global_admission_id) REFERENCES Unified_Admissions(global_admission_id)
);

-- 7. DIAGNOSTIC ORDERS
CREATE TABLE Unified_Diagnostic_Orders (
    global_order_id INT PRIMARY KEY,
    global_admission_id INT,
    professional_id INT,
    exam_type VARCHAR(100),
    order_status VARCHAR(50),
    request_date_time DATETIME,
    exam_date_time DATETIME,
    FOREIGN KEY (global_admission_id) REFERENCES Unified_Admissions(global_admission_id)
);

-- 8. DISCHARGE RECORDS
CREATE TABLE Unified_Discharge_Records (
    global_discharge_id INT PRIMARY KEY,
    global_admission_id INT,
    discharge_date_time DATETIME,
    discharge_destination VARCHAR(100),
    condition_at_discharge VARCHAR(100),
    FOREIGN KEY (global_admission_id) REFERENCES Unified_Admissions(global_admission_id)
);

-- 9. SURGICAL PROCEDURES
CREATE TABLE Unified_Surgical_Procedures (
    global_procedure_id INT PRIMARY KEY,
    global_admission_id INT,
    professional_id INT,
    procedure_name VARCHAR(255),
    category VARCHAR(100),
    procedure_date_time DATETIME,
    FOREIGN KEY (global_admission_id) REFERENCES Unified_Admissions(global_admission_id)
);

-- IDENTIFIER MAPPING TABLES (Rubric 6.1 & 6.2)


CREATE TABLE Map_Patients (
    global_patient_id INT PRIMARY KEY,
    source_system VARCHAR(50),
    source_id VARCHAR(50),
    FOREIGN KEY (global_patient_id) REFERENCES Unified_Patients(global_patient_id)
);

CREATE TABLE Map_Admissions (
    global_admission_id INT PRIMARY KEY,
    source_system VARCHAR(50),
    source_admission_id VARCHAR(50),
    FOREIGN KEY (global_admission_id) REFERENCES Unified_Admissions(global_admission_id)
);

CREATE TABLE Map_Triage (
    global_triage_id INT PRIMARY KEY,
    source_system VARCHAR(50),
    source_triage_id VARCHAR(50),
    FOREIGN KEY (global_triage_id) REFERENCES Unified_Triage(global_triage_id)
);

CREATE TABLE Map_Diagnoses (
    global_diagnosis_id INT PRIMARY KEY,
    source_system VARCHAR(50),
    source_diagnosis_id VARCHAR(50),
    FOREIGN KEY (global_diagnosis_id) REFERENCES Unified_Diagnoses(global_diagnosis_id)
);

CREATE TABLE Map_ICU_Stays (
    global_icu_id INT PRIMARY KEY,
    source_system VARCHAR(50),
    source_icu_id VARCHAR(50),
    FOREIGN KEY (global_icu_id) REFERENCES Unified_ICU_Stays(global_icu_id)
);

CREATE TABLE Map_Clinical_Notes (
    global_note_id INT PRIMARY KEY,
    source_system VARCHAR(50),
    source_note_id VARCHAR(50),
    FOREIGN KEY (global_note_id) REFERENCES Unified_Clinical_Notes(global_note_id)
);

CREATE TABLE Map_Diagnostic_Orders (
    global_order_id INT PRIMARY KEY,
    source_system VARCHAR(50),
    source_order_id VARCHAR(50),
    FOREIGN KEY (global_order_id) REFERENCES Unified_Diagnostic_Orders(global_order_id)
);

CREATE TABLE Map_Discharge_Records (
    global_discharge_id INT PRIMARY KEY,
    source_system VARCHAR(50),
    source_discharge_id VARCHAR(50),
    FOREIGN KEY (global_discharge_id) REFERENCES Unified_Discharge_Records(global_discharge_id)
);

CREATE TABLE Map_Surgical_Procedures (
    global_procedure_id INT PRIMARY KEY,
    source_system VARCHAR(50),
    source_procedure_id VARCHAR(50),
    FOREIGN KEY (global_procedure_id) REFERENCES Unified_Surgical_Procedures(global_procedure_id)
);