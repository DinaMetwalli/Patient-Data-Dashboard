from CSVParser import ParseCSV
import pandas as pd


class Filter:
    def __init__(self, data):
        self.data = data

    def filter_by_referral(self, referral):
        # Convert the 'referral' column to float for comparison
        self.data['referral'] = self.data['referral'].astype(float)
        filtered_data = self.data[self.data['referral'] == referral]
        return filtered_data

    def filter_by_bmi(self, bmi):
        # Filter out empty strings in 'bmi' column
        filtered_data = self.data[self.data['bmi'].astype(str).str.strip() != '']
        filtered_data['bmi'] = pd.to_numeric(filtered_data['bmi'], errors='coerce')  # Convert to numeric, coerce errors
        filtered_data = filtered_data[round(filtered_data['bmi']) == round(bmi)]
        return filtered_data


class CCU:
    def __init__(self):
        self.patients = None
        self.parse_csv = ParseCSV()

    def ccu(self):
        # Import CSV data
        self.parse_csv.import_csv()
        self.patients = self.parse_csv.data

    def filter_by_referral(self, referral):
        if self.patients is None or len(self.patients) == 0:
            self.ccu()
        filter_instance = Filter(self.patients)
        return filter_instance.filter_by_referral(referral)

    def filter_by_bmi(self, bmi):
        if self.patients is None or len(self.patients) == 0:
            self.ccu()
        filter_instance = Filter(self.patients)
        return filter_instance.filter_by_bmi(bmi)


# Example usage:
ccu_instance = CCU()

# Retrieve CCU data
ccu_instance.ccu()

# Filter by referral
referral_filtered_data = ccu_instance.filter_by_referral(False)
print("Filtered Data by Referral:", referral_filtered_data)

# Filter by BMI
bmi_filtered_data = ccu_instance.filter_by_bmi(38)
print("Filtered Data by BMI:", bmi_filtered_data)
