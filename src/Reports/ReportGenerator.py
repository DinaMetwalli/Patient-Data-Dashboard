from src.CSVParser.CSVParser import ParseCSV
import pandas as pd

class Report():
    def __init__(self) -> None:
        self.parser = ParseCSV()
    
    def parse_csv_data(self, csv_file) -> pd.DataFrame:
        """
        Uses Parser to parse provided CSV file.

        Parameters:
            csv_file (str): name of CSV file to be parsed

        Returns:
            self.data (DataFrame): parsed data
        """
        self.data = self.parser.import_csv(csv_file)

        return self.data

    def caculate_average_data(self) -> dict:
        """
        Calculates overall average of patient data

        Returns:
            averages (dict): a dictionary of calculated averages
                             maps the value to its total and count
        """
        measurements = {}
        for column in self.data.columns:
            if (column != "encounterId") and (column != "referral"):
                measurements[column] = {"total": 0, "count": 0}

        for index, row in self.data.iterrows():
            for variable, data in measurements.items():
                value = row[variable]
                if value is not None:
                    data["total"] += value
                    data["count"] += 1

        # Calculate averages
        averages = {variable: data["total"] / data["count"] if data["count"] != 0 else 0 for variable, data in measurements.items()}
        for data in averages:
            averages[data] = round(averages[data], 2)

        return averages