from src.api.main import main
from src.Reports.ReportGenerator import Report
from src.Reports.PatientReport import PatientReport
from src.Reports.AverageReport import AverageReport

# Start server:
main()

# # Generate average data report:
# instance = AverageReport()
# instance.generate_average_data_report("Data.csv", "Huh.pdf")

# # Generate patient report:
# rep = PatientReport()
# rep.generate_patient_data_report(2906, "Data.csv", "Patient_data.pdf")