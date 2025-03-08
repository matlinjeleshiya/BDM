from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route("/docs.google.com/spreadsheets/d/1PoHwoUqBY8mSDjuEbA7oepHr1foMOSnA/e")
def home():
    return render_template("uiaio.html")

@app.route("/download")
def download_file():
    file_path = r"C:\Users\MATLIN JELESHIYA\Desktop\vidhyasagar\BDM\BDMDATA.xlsx"
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
    
