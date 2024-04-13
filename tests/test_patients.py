import pytest
from src.Patients.Patients import Patient, DietaryRequirements, RespiratoryMeasurments

import pandas as pd

import os

def test_create_instance():
    global patient
    patient_id = 2906

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    csv_file = os.path.join(desktop_path, "ExportedData.csv")

    patient = Patient(csv_file, patient_id)
    assert isinstance(patient, Patient)

def test_cant_create_instance_with_wrong_file_path():
    global patient
    patient_id = 2906
    csv_file = "DoesNotExist.csv"
    with pytest.raises(Exception):
        patient = Patient(csv_file, patient_id)

def test_dietary_req():
    dietary_data = patient.dietary_req()
    assert isinstance(dietary_data, DietaryRequirements)
    data = dietary_data.fetch_dietary_req_data()
    assert isinstance(data, dict)

def test_resp_measurements():
    resp_data = patient.resp_measurments()
    assert isinstance(resp_data, RespiratoryMeasurments)
    data = resp_data.fetch_resp_measurements_data()
    assert isinstance(data, dict)

def test_parse_csv_data():
    csv_data = patient.parse_csv_data()
    assert isinstance(csv_data, pd.DataFrame)

def test_fetch_all_patient_data():
    all_patient_data = patient.fetch_all_patient_data()
    assert isinstance(all_patient_data, list)
    assert len(all_patient_data) == 5386

def test_calculate_average_data():
    average_data = patient.calculate_average_data()
    assert isinstance(average_data, dict)
    assert len(average_data) == 16

def test_get_referral_status():
    referral_status = patient.get_referral_status()
    assert isinstance(referral_status, bool)