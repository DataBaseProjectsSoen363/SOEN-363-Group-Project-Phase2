# Phase 2 Final Report: ETL Pipeline and Data Integration

## Executive Summary

This project involved building an end-to-end ETL (Extract, Transform, Load) pipeline to consolidate fragmented healthcare data from four distinct source systems (A, B, C, and D). Each source presented unique data quality challenges, including varying file formats (CSV, XML, JSON, TXT), inconsistent date representations, and disjointed identifier systems. The final deliverable is a unified, relational database schema in PostgreSQL that preserves source traceability and ensures referential integrity.

## Task1 & 2: Extraction,Load and Transform

The first phase of the pipeline focused on understanding and standardizing the raw data.

- Data Profiling: We generated data profiles for every table across all four sources to identify anomalies, missing values, and data type inconsistencies.A modular Python pipeline(profile_all.py) was developed to profile each source with helper modules such as ETL_Load_Source(X) where X was replaced with A,B,C or D.

- Harmonization & Cleaning: A modular Python pipeline (clean_all.py) was developed to process each source independently. Key cleaning operations included:

    - Date Standardization: Converting UNIX timestamps (Source D) and European date formats (Source B) into standard ISO YYYY-MM-DD formats.

    - Categorical Mapping: Standardizing gender codes (e.g., 'M'/'F' to 'Male'/'Female') and mapping numeric codes to readable text.

    - Error Quarantine: Records with fatal flaws (e.g., future birthdates, out-of-bounds vitals, invalid foreign keys) were extracted and saved to a Quarantine folder for auditing rather than being deleted outright.

## Task 3: Data Integration and Schema Refinement

The core challenge of Task 3 was merging records from four independent systems into a single, cohesive relational model without causing identifier collisions.

### Identifier Management (Rubric 6.1)

Because local identifiers (e.g., patient_id, patient_mrn) were only unique within their respective sources, we could not simply concatenate the tables.
- Global Surrogate Keys: We introduced auto-incrementing global surrogate keys (e.g., global_patient_id, global_admission_id) to guarantee uniqueness across the unified tables.
- ID Mapping Tables: For every entity, we generated a mapping table (e.g., Map_Patients, Map_Admissions). These tables act as a bridge, holding the global_id, the source_system name, and the original source_id. This ensures we do not merge patients solely based on matching names.

### Source Traceability (Rubric 6.2)
By retaining the source_system and source_id columns in the mapping tables, the final database allows any record to be traced back to its original continent and source system. When several source records were merged into the unified tables, the mapping tables preserved the exact lineage.

### Challenges

During the initial integration run, a significant data anomaly was discovered: the row counts for child tables (like Triage and Diagnoses) inflated to over 4 million rows.

- The Problem: The pd.merge() function was performing a many-to-many join because the source admission IDs were not perfectly unique in the mapping table (due to type-casting differences between floats and strings).

- The Solution: We resolved this by applying .drop_duplicates(subset=['source_system', 'source_admission_id']) on the mapping table before merging. Furthermore, we enforced validate='many_to_one' in the Pandas merge function. This guaranteed that every child record mapped to exactly one parent admission record, restoring the row counts to their correct, realistic numbers.

##  Task 4: Database Loading
The cleaned and integrated CSVs were loaded into a PostgreSQL database using Python (psycopg and SQLAlchemy).

- Referential Integrity: The loading script strictly adhered to dependency rules. Referenced parent tables (Unified_Patients) were loaded first, followed by dependent child tables (Unified_Admissions), and finally the grandchild tables (Triage, Notes, etc.).

- Idempotency: The script includes a DROP TABLE ... CASCADE routine at the start of execution. This ensures that rerunning the pipeline safely rebuilds the database from scratch, preventing accidental duplication of data.

- Final Schema: The resulting database contains 18 tables (9 unified tables and 9 mapping tables) with full foreign key constraints.

## Task 5:

### Part 1: The SQL Constraints 

When we generated our 18 tables, we used basic PRIMARY KEY and FOREIGN KEY constraints. 

- Primary keys are unique and non-null.
By defining PRIMARY KEY on all global_id columns. PostgreSQL automatically enforces uniqueness and non-null.

- Foreign keys reference existing records / Every admission belongs to a patient.
By defining FOREIGN KEY (global_patient_id) REFERENCES Unified_Patients(global_patient_id).

- Required values and categorical domains.
By adding NOT NULL and CHECK constraints. (For example, adding a CHECK (admission_type IN ('Emergency', 'Elective', 'Urgent', 'Observation')) to the Admissions table).

### Part 2: The Post-Import Validation 
Some rules from the rubric cannot be enforced with standard constraints (like "Discharge time must occur after admission time" because it involves comparing two different columns). For these, we Validation Queries.If a query returns 0 rows, it means our data is perfect and there are no violations.

## Conclusion
The completed pipeline demonstrates a robust, scalable approach to data integration. By utilizing surrogate keys and mapping tables, we successfully navigated the complexities of multi-source integration while maintaining absolute source traceability. The final PostgreSQL database is fully populated, consistent, and ready for analytical querying.

** see output file for more details on the queries