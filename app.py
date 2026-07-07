from flask import Flask, render_template, request
import os

from parser import (
    extract_text,
    extract_email,
    extract_phone,
    extract_skills,
    extract_education,
    extract_name
)

app= Flask(__name__)
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    name = ""
    email = ""
    phone = ""
    skills = []
    education = []
    success = ""
    error = ""
    if request.method == "POST":
        if "resume" not in request.files:
            return render_template("index.html", error="Please choose a resume first.")
        uploaded_file = request.files["resume"]
        if uploaded_file.filename == "":
            return render_template("index.html", error="No file selected.")
        filename=uploaded_file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        uploaded_file.save(filepath)
        text = extract_text(filepath)
        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        skills = extract_skills(text)
        education = extract_education(text)
        success= "Resume uploaded Successfully"
    return render_template("index.html", success=success, name=name, email=email, phone=phone, skills=skills, education=education)
if __name__ == "__main__":
    app.run(debug=True)
