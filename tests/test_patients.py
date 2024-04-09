import pytest
from src.Patients.Patients import Patient, DietaryRequirements, RespiratoryMeasurments

def test_create_instance():
    global patient
    patient_id = 2906
    csv_file = "Data.csv"
    patient = Patient(patient_id, csv_file)
    assert isinstance(patient, Patient)

def test_cant_create_instance_with_wrong_file_path():
    global patient
    patient_id = 2906
    csv_file = "DoesNotExist.csv"
    with pytest.raises(Exception):
        patient = Patient(patient_id, csv_file)

def test_dietary_req():
    dietary_data = patient.dietary_req()
    assert isinstance(dietary_data, DietaryRequirements)
    data = dietary_data.fetch_dietary_req_data()
    assert isinstance(data, list)

def test_resp_measurements():
    resp_data = patient.resp_measurments()
    assert isinstance(resp_data, RespiratoryMeasurments)
    data = resp_data.fetch_resp_measurements_data()
    assert isinstance(data, dict)