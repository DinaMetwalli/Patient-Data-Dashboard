from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import PCMYKColor
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing

import os

from .ReportGenerator import Report

class PatientReport():
    def __init__(self) -> None:
        self.report = Report()

    def fetch_patient_data(self, patient_id, csv_file) -> dict:
        """
        Fetches specific patient's data from CSV file using Parser

        Parameters:
            csv_file (str): name of CSV file to be parsed
            patient_id (int): ID of patient to fetch data of

        Returns:
            patient_data (dict): a dictionary of the patient data
                                 maps column to its cell value
        """
        data = self.report.parse_csv_data(csv_file)
        self.averages = self.report.caculate_average_data()

        filtered_data = data[data["encounterId"] == patient_id]
        
        patient_data = {}

        if not filtered_data.empty:
            for column in filtered_data.columns:
                if (column != "encounterId") and (column != "referral"):
                    patient_data[column] = [filtered_data[column].iloc[0]]

            for value in patient_data:
                if patient_data[value][0] != None:
                    patient_data[value][0] = round(patient_data[value][0], 2)
            
            return patient_data
        else:
            raise Exception(f"No matching records found for patient {patient_id}.")
        
    def generate_patient_data_report(self, patient_id, csv_file, export_file) -> None:
        """
        Generates report for specific patient's analytics

        Parameters:
            csv_file (str): name of CSV file to be parsed
            export_file (str): desired name of export PDF file
            patient_id (int): ID of patient to fetch data of
        """
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        pdf_file = os.path.join(desktop_path, export_file)

        patient_data = self.fetch_patient_data(patient_id, csv_file)

        doc = SimpleDocTemplate(pdf_file, pagesize=letter)

        styles = getSampleStyleSheet()

        respiratory_data = [["Patient ID", "FIO2", "FIO2 Ratio", "O2 Flow Rate",
                            "Respiratory Rate", "SIP"],
                            [patient_id, patient_data['fio2'][0],patient_data['fio2_ratio'][0],
                            patient_data['oxygen_flow_rate'][0], patient_data['resp_rate'][0],
                            patient_data['sip'][0]]]

        mechanical_vent_data = [["Patient ID", "End Tidal\nCO2", "PEEP",
                                "PIP", "Tidal Vol.", "Tidal Vol.\nActual",
                                "Tidal Vol.\nKg", "Tidal Vol.\nSpon.", "INSP Time"],
                                [patient_id, patient_data['end_tidal_co2'][0],
                                patient_data['peep'][0], patient_data['pip'][0],
                                patient_data['tidal_vol'][0],
                                patient_data['tidal_vol_actual'][0],
                                patient_data['tidal_vol_kg'][0],
                                patient_data['tidal_vol_spon'][0],
                                patient_data['insp_time'][0]]]
        
        dietary_req_data = [["Patient ID", "Feed Vol.", "Feed Vol. ADM", "BMI"],
                            [patient_id, patient_data['feed_vol'][0],
                            patient_data['feed_vol_adm'][0], patient_data['bmi'][0]]]
        
        table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.darkcyan),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
                                ('GRID', (0, 0), (-1, -1), 1, colors.white),
                                ('FONTSIZE', (0, 0), (-1, -1), 9)])
        
        r_table = Table(respiratory_data, hAlign='LEFT')
        m_table = Table(mechanical_vent_data, hAlign='LEFT')
        d_table = Table(dietary_req_data, hAlign='LEFT')

        r_table.setStyle(table_style)
        m_table.setStyle(table_style)
        d_table.setStyle(table_style)        

        chart = Drawing(100, 150)

        data = [(patient_data['end_tidal_co2'][0], patient_data['oxygen_flow_rate'][0],
                patient_data['resp_rate'][0], patient_data['bmi'][0]),
                (self.averages['end_tidal_co2'], self.averages['oxygen_flow_rate'],
                self.averages['resp_rate'], self.averages['bmi'])]

        bc = VerticalBarChart()
        bc.x = 20
        bc.y = 5
        bc.height = 130
        bc.width = 330
        bc.data = data
        bc.bars.strokeColor = None
        bc.valueAxis.valueMin = 0
        bc.valueAxis.valueMax = 55
        bc.categoryAxis.labels.boxAnchor = 'ne'
        bc.categoryAxis.labels.dx = 8
        bc.categoryAxis.labels.dy = -2
        bc.categoryAxis.labels.angle = 30
        bc.barWidth = 1
        bc.categoryAxis.categoryNames = ['end_tidal_co2', 'oxygen_flow_rate', 'resp_rate', 'bmi']
        bc.barLabelFormat = '%d\n'
        bc.bars[0].fillColor = PCMYKColor(100, 67, 0, 23)
        bc.bars[1].fillColor = PCMYKColor(70,0,36,36)

        legend = Legend()
        legend.autoXPadding = 6
        legend.columnMaximum = 2
        legend.dx = 8
        legend.dxTextSpace = 4
        legend.dy = 6
        legend.fontSize = 10
        legend.strokeColor = None
        legend.x = 400
        legend.y = 130

        legend.colorNamePairs = [
            (PCMYKColor(100, 67, 0, 23), "Patient Data"),
            (PCMYKColor(70,0,36,36), "Average Data")
        ]

        chart.add(legend)
        chart.add(bc)

        report_content = []
        bold_style = ParagraphStyle(name='BoldStyle', fontName='Helvetica-Bold')
        
        report_content.append(Paragraph(f"Patient {patient_id} Data Analytics - Report", styles['Title']))
        report_content.append(Spacer(1, 50))

        report_content.append(Paragraph(f"This Patient's Encounter ID is {patient_id}.\n"))
        report_content.append(Spacer(1, 12))

        report_content.append(Paragraph("Patient's Mechanical Ventilation", bold_style))
        report_content.append(Spacer(1, 12))
        report_content.append(m_table)
        report_content.append(Spacer(1, 30))

        report_content.append(Paragraph("Patient's Respiratory Measurements", bold_style))
        report_content.append(Spacer(1, 12))
        report_content.append(r_table)
        report_content.append(Spacer(1, 30))

        report_content.append(Paragraph("Patient's Dietary Requirements", bold_style))
        report_content.append(Spacer(1, 12))
        report_content.append(d_table)
        report_content.append(Spacer(1, 50))

        report_content.append(Paragraph("Comparison of Patient Data With All Patients' Average", bold_style))
        report_content.append(chart)

        doc.build(report_content)