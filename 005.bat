@echo off
newman run EmployeeDataPy.postman_collection.json -r htmlextra --reporter-htmlextra-export ./final_execution_report.html