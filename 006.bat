@echo off
newman run DataDrivenTests.postman_collection.json -d ./data_file.csv -r htmlextra --reporter-htmlextra-export ./final_datadriven_execution_report.html
