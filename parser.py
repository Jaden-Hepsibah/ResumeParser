import pdfplumber
import re

def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_email(text):
    email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text)
    if email:
        return email.group()
    return "Email not found"

def extract_phone(text):
    phone = re.search(r"\+?\d[\d -]{8,12}\d", text)
    if phone:
        return phone.group()
    return "Phone number not found"

def extract_skills(text):
    skills_list = ["Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "Django", "Flask", "React", "Node.js", "machine learning", "data analysis", "AWS", "Azure", "Docker", "Kubernetes", "excel", "Power BI", "Tableau", "Git", "Linux"]
    found_skills = []
    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return found_skills

def extract_education(text):
    education_keywords = ["Bachelor", "Master", "PhD", "B.Sc", "M.Sc", "B.E.", "M.E.", "B.Tech", "M.Tech", "Diploma", "B.A.", "M.A.", "B.Com", "M.Com", "BBA", "MBA", "BCA", "MCA"]
    found = []
    for degree in education_keywords:
        if degree.lower() in text.lower():
            found.append(degree)
    return found

def extract_name(text):
    lines= text.split("\n")
    return lines[0]



        