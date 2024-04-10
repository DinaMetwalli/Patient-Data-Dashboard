import pandas as pd

class DietaryRequirements():
    def __init__(self, patient_id, patient_data) -> None:
        self.patient_id = patient_id        # Patient's encounter ID
        self.patient_data = patient_data    # Dictionary of patient's data

    def fetch_dietary_req_data(self) -> dict:
        """
        Fetches specific patient's dietary data from CSV file using Parser

        Returns:
            dietary_data (dict): a dictionary containing the data of the patient
        """
        dietary_data = {"patient_id": self.patient_id,
                        "feed_vol": self.patient_data['feed_vol'][0],
                        "feed_vol_adm": self.patient_data['feed_vol_adm'][0],
                        "bmi": self.patient_data['bmi'][0]}
        return dietary_data