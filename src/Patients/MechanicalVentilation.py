import pandas as pd


class MechanicalVentilation():
    def __init__(self, patient_id, patient_data) -> None:
        self.patient_id = patient_id  # Patient's encounter ID
        self.patient_data = patient_data  # Dictionary of patient's data

    def fetch_dietary_req_data(self) -> list:
        mechanical_vent_data = [["Patient ID", "End Tidal\nCO2", "PEEP",
                                 "PIP", "Tidal Vol.", "Tidal Vol.\nActual",
                                 "Tidal Vol.\nKg", "Tidal Vol.\nSpon.", "INSP Time"],
                                [self.patient_id, self.patient_data['end_tidal_co2'][0],
                                 self.patient_data['peep'][0], self.patient_data['pip'][0],
                                 self.patient_data['tidal_vol'][0],
                                 self.patient_data['tidal_vol_actual'][0],
                                 self.patient_data['tidal_vol_kg'][0],
                                 self.patient_data['tidal_vol_spon'][0],
                                 self.patient_data['insp_time'][0]]]

        return mechanical_vent_data
