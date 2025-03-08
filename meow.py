from flask import Flask, render_template, send_file, redirect

app = Flask(__name__)


@app.route("/docs.google.com/spreadsheets/d/1PoHwoUqBY8mSDjuEbA7oepHr1foMOSnA/e")
def redirect_to_netlify():
    return redirect("https://myexcelsheetuiaio.netlify.app", code=302)  
@app.route("/")
@app.route("https://myexcelsheetuiaio.netlify.app/")
def home():
    return render_template("uiaio.html")  

@app.route("/download")
def download_file():
    file_path = "BDMDATA.xlsx" 
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
