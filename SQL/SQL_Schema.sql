
-- TASK 3: REVISED & INTEGRATED RELATIONAL SCHEMA (PostgreSQL)


-- 0. SOURCE SYSTEMS & CONTINENT TRACEABILITY (Section 3.2)
CREATE TABLE "Source_Systems" (
    source_system VARCHAR(20) PRIMARY KEY,
    continent VARCHAR(50) NOT NULL
);

-- 1. REFERENCE & STAFF TABLES
CREATE TABLE "Unified_ICD9_Dict" (
    icd9_code VARCHAR(20) PRIMARY KEY,
    official_diagnosis_title TEXT NOT NULL,
    description TEXT,
    disease_category VARCHAR(100)
);

CREATE TABLE "Unified_Physicians" (
    global_physician_id BIGINT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    role VARCHAR(50),
    specialty VARCHAR(100),
    license_number VARCHAR(50)
);

CREATE TABLE "Map_Physicians" (
    global_physician_id BIGINT PRIMARY KEY REFERENCES "Unified_Physicians"(global_physician_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_physician_id VARCHAR(50) NOT NULL
);

CREATE TABLE "Unified_Nurses" (
    global_nurse_id BIGINT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    role VARCHAR(50),
    specialty VARCHAR(100),
    license_number VARCHAR(50)
);

CREATE TABLE "Map_Nurses" (
    global_nurse_id BIGINT PRIMARY KEY REFERENCES "Unified_Nurses"(global_nurse_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_nurse_id VARCHAR(50) NOT NULL
);

-- 2. CORE ENTITIES: PATIENTS & ADMISSIONS
CREATE TABLE "Unified_Patients" (
    global_patient_id BIGINT PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    dob DATE,
    gender VARCHAR(20),
    health_insurance_number VARCHAR(50),
    life_status VARCHAR(30),
    phone_number VARCHAR(50),
    emergency_contact_number VARCHAR(50),
    address VARCHAR(255),
    city VARCHAR(100)
);

CREATE TABLE "Map_Patients" (
    global_patient_id BIGINT PRIMARY KEY REFERENCES "Unified_Patients"(global_patient_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    continent VARCHAR(50) NOT NULL,
    source_id VARCHAR(50) NOT NULL
);

CREATE TABLE "Unified_Admissions" (
    global_admission_id BIGINT PRIMARY KEY,
    global_patient_id BIGINT NOT NULL REFERENCES "Unified_Patients"(global_patient_id),
    admission_date_time TIMESTAMPTZ NOT NULL,
    discharge_date_time TIMESTAMPTZ,
    admission_type VARCHAR(50),
    admission_source VARCHAR(50),
    reason_admission TEXT,
    insurance_information VARCHAR(100),
    current_condition VARCHAR(50),
    ward_code VARCHAR(50),
    admitting_professional_id VARCHAR(50),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    CONSTRAINT chk_admission_dates CHECK (discharge_date_time IS NULL OR discharge_date_time >= admission_date_time)
);

CREATE TABLE "Map_Admissions" (
    global_admission_id BIGINT PRIMARY KEY REFERENCES "Unified_Admissions"(global_admission_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_admission_id VARCHAR(50) NOT NULL
);

-- 3. CLINICAL & ENCOUNTER CHILD TABLES
CREATE TABLE "Unified_Triage" (
    global_triage_id BIGINT PRIMARY KEY,
    global_admission_id BIGINT NOT NULL REFERENCES "Unified_Admissions"(global_admission_id),
    nurse_id VARCHAR(50),
    heart_rate INT,
    respiratory_rate NUMERIC,
    body_temperature NUMERIC,
    temp_fahrenheit NUMERIC,
    oxygen_saturation INT,
    blood_pressure VARCHAR(30),
    bp_systolic NUMERIC,
    bp_diastolic NUMERIC,
    pain_level NUMERIC,
    triage_priority_level VARCHAR(50),
    triage_scheme VARCHAR(30),
    reported_symptoms TEXT,
    symptoms TEXT,
    known_allergies TEXT,
    current_medications TEXT,
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system)
);

CREATE TABLE "Map_Triage" (
    global_triage_id BIGINT PRIMARY KEY REFERENCES "Unified_Triage"(global_triage_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_triage_id VARCHAR(50) NOT NULL
);

CREATE TABLE "Unified_Diagnoses" (
    global_diagnosis_id BIGINT PRIMARY KEY,
    global_admission_id BIGINT NOT NULL REFERENCES "Unified_Admissions"(global_admission_id),
    patient_id VARCHAR(50),
    icd9_code VARCHAR(20) NOT NULL,
    diagnosis_date_time TIMESTAMPTZ NOT NULL,
    primary_diagnosis BOOLEAN,
    secondary_diagnosis BOOLEAN,
    diagnosing_physician_id VARCHAR(50),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system)
);

CREATE TABLE "Map_Diagnoses" (
    global_diagnosis_id BIGINT PRIMARY KEY REFERENCES "Unified_Diagnoses"(global_diagnosis_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_diagnosis_id VARCHAR(50) NOT NULL
);

CREATE TABLE "Unified_ICU_Stays" (
    global_icu_id BIGINT PRIMARY KEY,
    global_admission_id BIGINT NOT NULL REFERENCES "Unified_Admissions"(global_admission_id),
    responsible_physician_id VARCHAR(50),
    unit_type VARCHAR(50) NOT NULL,
    room_number VARCHAR(30),
    bed_number VARCHAR(30),
    entry_date_time TIMESTAMPTZ NOT NULL,
    exit_date_time TIMESTAMPTZ,
    ventilator_used BOOLEAN,
    reason_transfer TEXT,
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    CONSTRAINT chk_icu_dates CHECK (exit_date_time IS NULL OR exit_date_time >= entry_date_time)
);

CREATE TABLE "Map_ICU_Stays" (
    global_icu_id BIGINT PRIMARY KEY REFERENCES "Unified_ICU_Stays"(global_icu_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_icu_id VARCHAR(50) NOT NULL
);

CREATE TABLE "Unified_Clinical_Notes" (
    global_note_id BIGINT PRIMARY KEY,
    global_admission_id BIGINT NOT NULL REFERENCES "Unified_Admissions"(global_admission_id),
    physician_id VARCHAR(50),
    type VARCHAR(50),
    creation_date TIMESTAMPTZ NOT NULL,
    patient_symptoms TEXT,
    physical_examination TEXT,
    initial_clinical_findings TEXT,
    suspected_condition TEXT,
    planned_diagnostic_examinations TEXT,
    initial_treatment TEXT,
    note_text TEXT,
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system)
);

CREATE TABLE "Map_Clinical_Notes" (
    global_note_id BIGINT PRIMARY KEY REFERENCES "Unified_Clinical_Notes"(global_note_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_note_id VARCHAR(50) NOT NULL
);

CREATE TABLE "Unified_Diagnostic_Orders" (
    global_order_id BIGINT PRIMARY KEY,
    global_admission_id BIGINT NOT NULL REFERENCES "Unified_Admissions"(global_admission_id),
    patient_id VARCHAR(50),
    requesting_physician_id VARCHAR(50),
    requested_examination VARCHAR(100),
    request_date_time TIMESTAMPTZ,
    clinical_reason_examination TEXT,
    priority VARCHAR(50),
    priority_scheme VARCHAR(30),
    order_status VARCHAR(50),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system)
);

CREATE TABLE "Map_Diagnostic_Orders" (
    global_order_id BIGINT PRIMARY KEY REFERENCES "Unified_Diagnostic_Orders"(global_order_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_order_id VARCHAR(50) NOT NULL
);

CREATE TABLE "Unified_Radiology_Examinations" (
    global_examination_id BIGINT PRIMARY KEY,
    global_order_id BIGINT NOT NULL REFERENCES "Unified_Diagnostic_Orders"(global_order_id),
    examination_type VARCHAR(100),
    examination_date_time TIMESTAMPTZ,
    body_area_examined VARCHAR(100),
    referring_physician_id VARCHAR(50),
    radiology_technician VARCHAR(100),
    examination_status VARCHAR(50),
    contrast_used BOOLEAN,
    medical_images TEXT,
    findings_text TEXT,
    radiologist_conclusion TEXT,
    "report.findings" TEXT,
    "report.conclusion" TEXT,
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system)
);

CREATE TABLE "Map_Radiology_Examinations" (
    global_examination_id BIGINT PRIMARY KEY REFERENCES "Unified_Radiology_Examinations"(global_examination_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_examination_id VARCHAR(50) NOT NULL
);

CREATE TABLE "Unified_Discharge_Records" (
    global_discharge_id BIGINT PRIMARY KEY,
    global_admission_id BIGINT NOT NULL REFERENCES "Unified_Admissions"(global_admission_id),
    discharge_date_time TIMESTAMPTZ NOT NULL,
    discharge_destination VARCHAR(100),
    condition_at_discharge VARCHAR(100),
    discharge_status VARCHAR(50) NOT NULL,
    followup_instructions TEXT,
    followup_appointments DATE,
    responsible_physician VARCHAR(50),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system)
);

CREATE TABLE "Map_Discharge_Records" (
    global_discharge_id BIGINT PRIMARY KEY REFERENCES "Unified_Discharge_Records"(global_discharge_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_discharge_id VARCHAR(50) NOT NULL
);

CREATE TABLE "Unified_Surgical_Procedures" (
    global_procedure_id BIGINT PRIMARY KEY,
    global_admission_id BIGINT NOT NULL REFERENCES "Unified_Admissions"(global_admission_id),
    patient_id VARCHAR(50),
    procedure_code VARCHAR(50),
    procedure_name VARCHAR(255) NOT NULL,
    body_site VARCHAR(100),
    procedure_date_time TIMESTAMPTZ NOT NULL,
    surgeon_id VARCHAR(50),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system)
);

CREATE TABLE "Map_Surgical_Procedures" (
    global_procedure_id BIGINT PRIMARY KEY REFERENCES "Unified_Surgical_Procedures"(global_procedure_id),
    source_system VARCHAR(20) NOT NULL REFERENCES "Source_Systems"(source_system),
    source_procedure_id VARCHAR(50) NOT NULL
);


