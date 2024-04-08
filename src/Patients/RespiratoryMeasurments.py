import pandas as pd

class RepiratoryMeasurements():
    def __init__(self, patient_id, patient_data) -> None:
        self.patient_id = patient_id        # Patient's encounter ID
        self.patient_data = patient_data    # Dictionary of patient's data

    def fetch_dietary_req_data(self) -> list:
        """
        Fetches specific patient's data from CSV file using Parser

        Returns:
            respiratory_data (dict): a dictionary containing the respiratory data of the patient
        """
    
        respiratory_data = {"patient_id": self.patient_id,
                        "fio2": self.patient_data['fio2'][0],
                        "fio2_ratio": self.patient_data['fio2_ratio'][0],
                        "o2_flow_rate": self.patient_data['o2_flow_rate'][0],
                        "respiratory_rate": self.patient_data['repiratory_rate'][0],
                        "sip": self.patient_data['sip'][0]}
        
        return respiratory_data