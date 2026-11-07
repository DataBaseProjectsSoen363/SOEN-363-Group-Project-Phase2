# AI Usage Disclosure

In accordance with the SOEN 363 course guidelines, we disclose the use of Artificial Intelligence (AI) in the completion of this project. 

## 1. Tools Used
- **Large Language Model:** Claude 3.5 Sonnet (via web interface).
- **Code Editor:** Visual Studio Code with Python and Pandas.


**How AI was utilized:**
AI was used as an interactive pair-programming assistant in generating the intial data source from 4 different sources

1. **Synthetic Data Generation:** AI assisted in drafting the Python scripts (`SourceA_Generator.py`, `SourceB_Generator.py`, etc.) to generate the required 20,000–40,000 synthetic hospital records. 
2. **Injecting Data-Quality Anomalies:** AI helped brainstorm the types of realistic anomalies to inject (e.g., broken foreign keys, chronological errors, mixed-case text, and impossible dates like February 31st).

**How AI was NOT utilized:**
- AI did not design the Phase 1 database schema.
- AI did not write the final Task 1 profiling report; all data analysis and documentation in `Task1_Report.md` was written and verified by the student.
- All generated code was manually reviewed, executed, and validated by the student in a local environment.


## 2. Prompts Used

- *"Here is my Phase 1 Schema and the Python script I used to generate Source A. Can we break this down into modular scripts to generate the data incrementally (Patient, Admission, etc.) instead of one massive file?"*
- *"How do I load a pipe-delimited TXT file in Pandas compared to a CSV file? The TXT file has a weird `--- [PATIENT] ---` header on the first line."*

## 3. Review and Validation Process
The student remained fully responsible for the correctness and suitability of the data. The generated scripts and data were reviewed using the following steps:

1. **Code Comprehension:** Every generated Python script was read line-by-line to ensure it accurately targeted the local file structures (e.g., correcting the AI's initial mistake where it tried to use `.txt` extensions for Source B CSVs).
2. **Environment Execution:** All scripts were executed locally in VS Code. Errors (such as the `lxml` missing dependency for XML parsing) were caught manually, and solutions were applied and verified.
3. **Data Validation via Profiling:** The generated data was not blindly trusted. The `profile.py` script was written and run to generate 30 distinct Markdown profiles. These profiles were manually inspected to verify that the AI-generated anomalies (e.g., "N/A" strings in Source B, and impossible dates like `31/02/2026`) were actually present in the data.
4. **Logging:** A `try/except` block was implemented in the loaders to catch malformed records and log them to `malformed_records_log.txt`, ensuring no silent data loss occurred.