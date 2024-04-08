import pandas as pd

class DietaryRequirements():
    def __init__(self, patient_id, patient_data) -> None:
        self.patient_id = patient_id        # Patient's encounter ID
        self.patient_data = patient_data    # Dictionary of patient's data

    def fetch_dietary_req_data(self) -> list:
        dietary_data = [["Patient ID", "Feed Vol.", "Feed Vol. ADM", "BMI"],
                            [self.patient_id, self.patient_data['feed_vol'][0],
                            self.patient_data['feed_vol_adm'][0], self.patient_data['bmi'][0]]]
        
        return dietary_data