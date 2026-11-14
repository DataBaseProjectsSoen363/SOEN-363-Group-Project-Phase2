===== RECORD COUNT =====
260

===== SHAPE =====
(260, 4)

===== FIELD NAMES =====
['radiology_report_id', 'radiologist_findings', 'interpretation', 'clinical_conclusion']

===== DATA TYPES =====
radiology_report_id     int64
radiologist_findings      str
interpretation            str
clinical_conclusion       str

===== MISSING VALUES =====
radiology_report_id     0
radiologist_findings    0
interpretation          9
clinical_conclusion     0

===== HIDDEN MISSING VALUES (String 'N/A') =====
radiology_report_id     0
radiologist_findings    0
interpretation          0
clinical_conclusion     0

===== DUPLICATE ROWS =====
0

===== SAMPLE RECORDS =====
     radiology_report_id                            radiologist_findings                                                interpretation                                    clinical_conclusion
190                  200   Mild cardiomegaly noted. No pleural effusion.        Likely benign etiology. Routine follow-up recommended.      Further evaluation suggested if symptoms persist.
195                  205  Mild degenerative changes in the lumbar spine.  Findings are consistent with early congestive heart failure.      Further evaluation suggested if symptoms persist.
146                  152  Mild degenerative changes in the lumbar spine.        Likely benign etiology. Routine follow-up recommended.    Further evaluation suggested if symptoms persist.  
72                    75   Mild cardiomegaly noted. No pleural effusion.        Likely benign etiology. Routine follow-up recommended.                              Normal structural limits.
235                  250   Mild cardiomegaly noted. No pleural effusion.                                           Unremarkable study.                        Recommend clinical correlation.

===== SUMMARY STATISTICS =====
        radiology_report_id                           radiologist_findings                                                interpretation                clinical_conclusion
count            260.000000                                            260                                                           251                                260
unique                  NaN                                              5                                                             5                                 16
top                     NaN  Mild cardiomegaly noted. No pleural effusion.  Findings are consistent with early congestive heart failure.  Stable compared to prior imaging.
freq                    NaN                                             68                                                            55                                 53
mean             287.023077                                            NaN                                                           NaN                                NaN
std             1218.901759                                            NaN                                                           NaN                                NaN
min                1.000000                                            NaN                                                           NaN                                NaN
25%               67.750000                                            NaN                                                           NaN                                NaN
50%              135.500000                                            NaN                                                           NaN                                NaN
75%              207.250000                                            NaN                                                           NaN                                NaN
max             9999.000000                                            NaN                                                           NaN                                NaN
