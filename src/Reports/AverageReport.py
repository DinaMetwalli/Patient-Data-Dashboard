from reportlab.platypus import SimpleDocTemplate, Paragraph

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Drawing, String

import os

class AverageReport():
        def __init__(self, avg_data: dict) -> None:
              self.averages = avg_data

        def generate_report(self, export_file) -> None:
            """
            Generates report for overall average patient data

            Parameters:
                csv_file (str): name of CSV file to be parsed
                export_file (str): desired name of export PDF file
            """
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            pdf_file = os.path.join(desktop_path, export_file)

            doc = SimpleDocTemplate(pdf_file, pagesize=letter)
            styles = getSampleStyleSheet()

            # Drawing object to hold the bar chart graphs
            r_chart = Drawing(600, 200)
            m_chart = Drawing(600, 200)
            d_chart = Drawing(600, 200)

            respiratory_measurments = [(self.averages['fio2'], self.averages['fio2_ratio'],
                                        self.averages['oxygen_flow_rate'], self.averages['resp_rate'],
                                        self.averages['sip'])]
            
            mechanical_ventilation = [(self.averages['end_tidal_co2'], self.averages['peep'],
                                    self.averages['pip'], self.averages['tidal_vol'],
                                    self.averages['tidal_vol_actual'], self.averages['tidal_vol_kg'],
                                    self.averages['tidal_vol_spon'], self.averages['insp_time'])]
            
            dietary_requirements = [(self.averages['feed_vol'], self.averages['feed_vol_adm'],
                                    self.averages['bmi'])]

            # Create bar charts for measurements
            bc = VerticalBarChart()
            m_bc = VerticalBarChart()
            d_bc = VerticalBarChart()

            bc.x = m_bc.x = d_bc.x = 10
            bc.y = m_bc.y = d_bc.y = 5
            bc.height = m_bc.height = d_bc.height = 130
            bc.width = 330
            m_bc.width = 360
            d_bc.width = 300
            bc.data = respiratory_measurments
            m_bc.data = mechanical_ventilation
            d_bc.data = dietary_requirements
            bc.bars.strokeColor = m_bc.bars.strokeColor = d_bc.bars.strokeColor = None
            bc.valueAxis.valueMin = m_bc.valueAxis.valueMin = d_bc.valueAxis.valueMin = 0
            bc.valueAxis.valueMax = 300
            m_bc.valueAxis.valueMax = 500
            d_bc.valueAxis.valueMax = 850
            bc.categoryAxis.labels.boxAnchor = m_bc.categoryAxis.labels.boxAnchor = d_bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = m_bc.categoryAxis.labels.dx = d_bc.categoryAxis.labels.dx = 8
            bc.categoryAxis.labels.dy = m_bc.categoryAxis.labels.dy = d_bc.categoryAxis.labels.dy = -2
            bc.categoryAxis.labels.angle = m_bc.categoryAxis.labels.angle = d_bc.categoryAxis.labels.angle = 30
            bc.barWidth = d_bc.barWidth = 1
            m_bc.barWidth = 2

            bc.categoryAxis.categoryNames = ['fio2', 'fio2_ratio', 'oxygen_flow_rate',
                                            'resp_rate', 'sip']
            
            m_bc.categoryAxis.categoryNames = ['end_tidal_co2', 'peep', 'pip', 'tidal_vol',
                                            'tidal_vol_actual', 'tidal_vol_kg', 'tidal_vol_spon',
                                            'insp_time']
            
            d_bc.categoryAxis.categoryNames = ['feed_vol', 'feed_vol_adm', 'bmi']

            bc.barLabelFormat = m_bc.barLabelFormat = d_bc.barLabelFormat = '%d\n'

            bc.bars[0].fillColor = colors.teal
            d_bc.bars[0].fillColor = colors.orange

            label = String(5, 150, "Respiratory Measurements Average", fontSize=10, fontName="Helvetica-Bold")

            values = Label()
            values.setOrigin(440, 80)
            values.setText(f"FIO2: {self.averages['fio2']}\n\n"
                            f"FIO2 Ratio: {self.averages['fio2_ratio']}\n\n"
                            f"Oxygen Flow Rate: {self.averages['oxygen_flow_rate']}\n\n"
                            f"Respiratory Rate: {self.averages['resp_rate']}\n\n"
                            f"SIP: {self.averages['sip']}")
            values.fontName = "Helvetica"
            values.fontSize = 9

            # Add the bar chart to the drawing
            r_chart.add(bc)
            r_chart.add(label)
            r_chart.add(values)

            label = String(5, 150, "Mechanical Ventillation Average", fontSize=10, fontName="Helvetica-Bold")

            values = Label()
            values.setOrigin(450, 80)
            values.setText(f"End Tidal CO2: {self.averages['end_tidal_co2']}\n\n"
                            f"Peep: {self.averages['peep']}\n\n"
                            f"PIP: {self.averages['pip']}\n\n"
                            f"Tidal Vol.: {self.averages['tidal_vol']}\n\n"
                            f"Tidal Vol. Actual: {self.averages['tidal_vol_actual']}\n\n"
                            f"Tidal Vol. KG: {self.averages['tidal_vol_kg']}\n\n"
                            f"Tidal Vol. Spon.: {self.averages['tidal_vol_spon']}\n\n"
                            f"INSP Time: {self.averages['insp_time']}\n\n")
            values.fontName = "Helvetica"
            values.fontSize = 9

            m_chart.add(m_bc)
            m_chart.add(label)
            m_chart.add(values)

            label = String(5, 150, "Dietary Requirements Average", fontSize=10, fontName="Helvetica-Bold")

            values = Label()
            values.setOrigin(440, 80)
            values.setText(f"Feed Vol.: {self.averages['feed_vol']}\n\n"
                            f"Feed Vol. ADM: {self.averages['feed_vol_adm']}\n\n"
                            f"Body Mass Index: {self.averages['bmi']}\n\n")
            values.fontName = "Helvetica"
            values.fontSize = 9

            d_chart.add(d_bc)
            d_chart.add(label)
            d_chart.add(values)

            report_content = []
            report_content.append(Paragraph("Averages For Patient Data - Report\n", styles['Title']))
            report_content.append(r_chart)
            report_content.append(m_chart)
            report_content.append(d_chart)

            doc.build(report_content)