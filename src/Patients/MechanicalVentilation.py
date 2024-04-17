import pandas as pd


class MechanicalVentilation():
    def __init__(self, patient_id, patient_data) -> None:
        self.patient_id = patient_id  # Patient's encounter ID
        self.patient_data = patient_data  # Dictionary of patient's data

    def fetch_mechanical_data(self) -> dict:
        """
        Fetches specific patient's mechanical data from CSV file using Parser

        Returns:
            mechanical_vent_data (dict): a dictionary containing the data of the patient
        """
        mechanical_vent_data = {"patient_id": self.patient_id,
                        "end_tidal_co2": self.patient_data['end_tidal_co2'][0],
                        "peep": self.patient_data['peep'][0],
                        "pip": self.patient_data['pip'][0],
                        "tidal_vol": self.patient_data['tidal_vol'][0],
                        "tidal_vol_actual": self.patient_data['tidal_vol_actual'][0],
                        "tidal_vol_kg": self.patient_data['tidal_vol_kg'][0],
                        "tidal_vol_spon": self.patient_data['tidal_vol_spon'][0],
                        "insp_time": self.patient_data['insp_time'][0]}

        return mechanical_vent_data
