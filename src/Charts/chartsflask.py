from flask import Flask, render_template, jsonify
from CSVParser import ParseCSV  # Assuming ParseCSV is correctly defined

app = Flask(__name__)
parser = ParseCSV()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/import-csv", methods=["POST"])
def import_csv():
    try:
        import_name = "csvfile.csv"  
        parser.import_csv(import_name)
        data = { #The prob  
            "encounterId": parser.data["encounterId"].tolist(),
            "end_tidal_co2": parser.data["end_tidal_co2"].tolist(),
            "feed_vol": parser.data["feed_vol"].tolist(),
            "feed_vol_adm": parser.data["feed_vol_adm"].tolist(),
            "fio2": parser.data["fio2"].tolist(),
            "fio2_ratio": parser.data["fio2_ratio"].tolist(),
            "insp_time": parser.data["insp_time"].tolist(),
            "oxygen_flow_rate": parser.data["oxygen_flow_rate"].tolist(),
            "peep": parser.data["peep"].tolist(),
            "pip": parser.data["pip"].tolist(),
            "resp_rate": parser.data["resp_rate"].tolist(),
            "sip": parser.data["sip"].tolist(),
            "tidal_vol": parser.data["tidal_vol"].tolist(),
            "tidal_vol_actual": parser.data["tidal_vol_actual"].tolist(),
            "tidal_vol_kg": parser.data["tidal_vol_kg"].tolist(),
            "tidal_vol_spon": parser.data["tidal_vol_spon"].tolist(),
            "bmi": parser.data["bmi"].tolist(),
            "referral": parser.data["referral"].tolist()
        }
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=6002, host="0.0.0.0")
