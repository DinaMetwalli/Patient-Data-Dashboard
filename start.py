from example.src.api.main import main
from src.Reports.ReportGenerator import Report
from src.Reports.PatientReport import PatientReport
from src.Reports.AverageReport import AverageReport
from src.Patients.Patients import Patient
from src.ccu.CCU import CCU

# # Start server:
# main()

# # Generate average data report:
# instance = AverageReport()
# instance.generate_average_data_report("Data.csv", "Average_data.pdf")

# # Generate patient report:
# rep = PatientReport()
# rep.generate_patient_data_report(2906, "Data.csv", "Patient_data.pdf")

# # Fetch Patient's Dietary Requirements Data:
# patient = Patient("Data.csv", 2956)
# dietary_data = patient.dietary_req()
# data = dietary_data.fetch_dietary_req_data()
# print(data)

# # Fetch Patient's Respiratory Measurements Data:
# patient = Patient("Data.csv", 2956)
# resp_data = patient.resp_measurments()
# data = resp_data.fetch_resp_measurements_data()
# print(data)

# # Fetch all patient data:
# patient = Patient("Data.csv")
# data = patient.fetch_all_patient_data()
# print(data)