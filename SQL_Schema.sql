CREATE TABLE Unified_Patients (
    global_patient_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    dob DATE,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
    -- other columns...
);

CREATE TABLE Unified_Admissions (
    global_admission_id INT PRIMARY KEY,
    global_patient_id INT,
    admission_date_time DATETIME,
    -- other columns...
    FOREIGN KEY (global_patient_id) REFERENCES Unified_Patients(global_patient_id)
);

CREATE TABLE Map_Admissions (
    global_admission_id INT,
    source_system VARCHAR(50),
    source_admission_id VARCHAR(50),
    FOREIGN KEY (global_admission_id) REFERENCES Unified_Admissions(global_admission_id)
);