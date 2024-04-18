from src.api.main import main
from src.Reports.ReportGenerator import Report
from src.Reports.AverageReport import AverageReport
from src.Patients.Patients import Patient
from src.ccu.CCU import CCU
from src.ccu.Authenticator import Authenticator
import os

# Start server:
main()

ccu = CCU()
filters = ccu.filter()
data = filtered_data = filters.filter_by_referral(True, "ExportedData.csv")
print(data)

# Generate average data report:
report = Report()
avg_report = report.average("Data.csv")
avg_report.generate_report("Average_data_report.pdf")

# Generate patient report:
rep = Report()
patient_rep = rep.patient("Data.csv")
patient_rep.generate_patient_data_report(2906, "Patient_Report.pdf")

# Access Report Generation through CCU:
ccu = CCU()
report = ccu.reports()
avg_report = report.average("Data.csv")
avg_report.generate_report("Average_data_report.pdf")
patient_rep = report.patient(2906, "Data.csv")
patient_rep.generate_patient_report("Patient_Report.pdf")

# Fetch Patient's Dietary Requirements Data:
patient = Patient("Data.csv", 2956)
dietary_data = patient.dietary_req()
data = dietary_data.fetch_dietary_req_data()
print(data)

# Fetch Patient's Respiratory Measurements Data:
patient = Patient("Data.csv", 2956)
resp_data = patient.resp_measurments()
data = resp_data.fetch_resp_measurements_data()
print(data)

# Fetch all patient data:
patient = Patient("Data.csv")
data = patient.fetch_all_patient_data()
print(data)