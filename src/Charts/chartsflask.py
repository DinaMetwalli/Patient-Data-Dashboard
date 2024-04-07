from flask import Flask, render_template, jsonify
from CSVParser import ParseCSV #need to have it  like this till our main app won't be in another folder

app = Flask(__name__)
parser = ParseCSV()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/import-csv", methods=["POST"])
def import_csv():
    try:
        import_name = "csvfile.csv"  # Corrected the variable assignment
        parser.import_csv(import_name)
        data = {
            "encounterId": parser.data["encounterId"].tolist(),
            "end_tidal_co2": parser.data["end_tidal_co2"].tolist(),
            "referral": parser.data["referral"].tolist(),
        }
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
