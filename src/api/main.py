from flask import Flask, render_template

def main():
    app: Flask = Flask("Feeding Dashboard")

    @app.route('/')
    def index():
        return "<p>Testing</p>"

    print("Starting the server...")
    app.run(debug=True, port=6002, host="0.0.0.0")
if __name__ == "__main__":
    main()