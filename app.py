from flask import Flask, render_template

app = Flask(__name__)

# EXAMS DATA
exams = {
    "upsc": {
        "name": "UPSC",
        "description": "Civil Services Examination",
        "papers": [{"year": "2023", "file": "upsc_2023.pdf"}]
    },
    "gate": {
        "name": "GATE",
        "description": "Graduate Aptitude Test in Engineering",
        "papers": [{"year": "2023", "file": "gate_2023.pdf"}]
    },
    "ssc": {
        "name": "SSC",
        "description": "Staff Selection Commission Exams",
        "papers": [{"year": "2023", "file": "ssc_2023.pdf"}]
    },
    "banking": {
        "name": "Banking",
        "description": "IBPS, SBI & RBI Exams",
        "papers": [{"year": "2023", "file": "banking_2023.pdf"}]
    },
    "neet": {
        "name": "NEET",
        "description": "Medical Entrance Examination",
        "papers": [{"year": "2023", "file": "neet_2023.pdf"}]
    },
    "jee": {
        "name": "JEE",
        "description": "Engineering Entrance Examination",
        "papers": [{"year": "2023", "file": "jee_2023.pdf"}]
    },
    "iit": {
        "name": "IIT-JAM",
        "description": "IIT Postgraduate Entrance Exam",
        "papers": [{"year": "2023", "file": "iit_2023.pdf"}]
    },
    "railway": {
        "name": "Railways",
        "description": "RRB NTPC & Group D Exams",
        "papers": [{"year": "2023", "file": "railway_2023.pdf"}]
    },
    "defence": {
        "name": "Defence",
        "description": "NDA, CDS & AFCAT Exams",
        "papers": [{"year": "2023", "file": "defence_2023.pdf"}]
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/exams")
def exams_page():
    return render_template("exam.html", exams=exams)

@app.route("/exam/<exam_id>")
def exam_detail(exam_id):
    exam = exams.get(exam_id)
    if not exam:
        return "Exam not found"
    return render_template("exam_detail.html", exam=exam)

@app.route("/mock-tests")
def mock_tests():
    exam_list = ["UPSC", "GATE", "SSC", "BANKING", "NEET", "JEE", "IIT"]
    return render_template("mock.html", exams=exam_list)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
