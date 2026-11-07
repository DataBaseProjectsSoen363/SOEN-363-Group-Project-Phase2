# Initial Profiling Report

## 1. Delimiter and Record Layout
* **Source A (TXT)** uses a pipe `|` delimiter. The record layout is flat, but the files use section headers like `--- [PATIENT] ---` which requires skipping the first row during the load phase (`skiprows=1`).
* **Source B (CSV)** uses a comma `,` delimiter with standard column headers included in the first row.

## 2. Correctly Extract Nested Records
* **Source C (XML)**: Extracted specific nested tags using the `xpath` parameter in `pd.read_xml` (e.g., `.//Patient` and `.//Admission`), which automatically flattened the nested `<Address>` tags into columns.
* **Source D (JSON)**: Utilized `pd.read_json`, which automatically converted nested JSON objects into dictionary-like columns in Pandas (e.g., the `name` object).

## 3. Record Counts by Entity
*See the individual `Profiles/*.md` files for exact row counts.*
* **Source A**: 800 Patients, 1,200 Admissions.
* **Source B**: 800 Patients, 1,200 Admissions.
* **Source C**: 800 Patients, 1,200 Admissions.
* **Source D**: 800 Patients, 1,200 Admissions.

## 4. Field Names and Inferred Data Types
The field names vary significantly between sources, demonstrating the need for a unified schema:
* **Source A Patient**: `patient_id`, `name`, `date_birth` (Inferred as `str`).
* **Source B Patient**: `mrn`, `full_name`, `dob` (Inferred as `str`), `gender_cd`.
* **Data Types**: Dates across all sources were inferred as strings (`str` or `object`) due to varying formats (e.g., `YYYY-MM-DD` in Source A vs `DD/MM/YYYY` in Source B).

## 5. Missing-Value Counts
Standard Pandas `NaN` values were detected:
* **Source A Admissions**: 24 missing `discharge_date_time` (open admissions), 303 missing `insurance_information`.
* **Source A Patients**: 19 missing `phone_number`, 1 missing `gender`.
* **Source B Patients**: 39 missing `contact_phone`.
* **Source B Admissions**: 0 standard missing values, but hidden missing values exist (see Section 7).

## 6. Duplicate Counts
* **Source A & B Patients and Admissions**: 0 exact duplicates found in the sampled files.
* *Note: Duplicate checks were handled by casting complex objects (dictionaries/lists) to strings to prevent `TypeError` crashes during profiling.*

## 7. Examples of Formatting Differences and Invalid Values
* **Hidden Missing Values (Source B)**: String placeholders like `"N/A"` were used instead of blanks. For example, `SourceB_Patient.csv` had `"N/A"` in the `contact_phone` column.
* **Date Formatting Differences**: Source A uses `2026-08-13 18:00:00`. Source B uses `16/05/2026 00:00`.
* **Invalid/Impossible Values (Source B Admissions)**: The `discharge_date` column contains string anomalies like `"Unknown"` and impossible dates (e.g., `31/02/2026`) which will cause parsing errors.
* **Categorical Messiness**: Mixed casing and whitespace (e.g., `M`, `male`, ` Male`) were identified in text columns.
* **Duplicate Local Identifiers**: In Source A, `health_insurance_number` had a frequency of 2 for the top value (`RAMQ900581`), indicating duplicate local IDs across different patient records.

## 8. Malformed or Unreadable Records
Malformed records that fail to parse or load (e.g., missing files or broken XML/JSON structures) are caught using `try/except` blocks and logged to a file called `malformed_records_log.txt`. This ensures no unreadable data is silently discarded.

## 9. Execution
To run the entire Task 1 profiling pipeline, execute the `run_all.py` script in the `ETL` directory. It will automatically load all four sources and generate the profile markdown files.