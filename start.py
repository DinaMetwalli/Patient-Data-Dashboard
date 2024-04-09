from example.src.main import main
from src.Reports.ReportGenerator import Report
from src.Reports.PatientReport import PatientReport
from src.Reports.AverageReport import AverageReport
from src.Patients.Patients import Patient

# Start server:
# main()

# # Generate average data report:
# instance = AverageReport()
# instance.generate_average_data_report("Data.csv", "Average_data.pdf")

# # Generate patient report:
# rep = PatientReport()
# rep.generate_patient_data_report(2906, "Data.csv", "Patient_data.pdf")

# # Fetch Patient's Dietary Requirements Data:
# patient = Patient(2956, "Data.csv")
# dietary_data = patient.dietary_req()
# data = dietary_data.fetch_dietary_req_data()
# print(data)

# Fetch Patient's Dietary Requirements Data:
# patient = Patient(2956, "Data.csv")
# resp_data = patient.resp_measurments()
# data = resp_data.fetch_resp_measurements_data()
# print(data)