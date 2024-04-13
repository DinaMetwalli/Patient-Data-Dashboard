if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=6002, host="0.0.0.0")
