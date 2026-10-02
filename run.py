from flask import Flask, render_template, request
import json
from werkzeug.utils import secure_filename

from app.analyzer import analyze_resume
from app.pdf_reader import extract_text_from_pdf


app = Flask(__name__)

# Maximum uploaded file size: 10 MB
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


# ==========================================
# LOAD SKILL DATABASE
# ==========================================

with open(
    "data/skills.json",
    "r",
    encoding="utf-8"
) as file:

    skills_data = json.load(file)


# ==========================================
# SKILL WEIGHTS
# ==========================================

skill_weights = {
    "Python": 3,
    "SQL": 3,
    "Machine Learning": 3,

    "Pandas": 2,
    "NumPy": 2,

    "Git": 2,
    "Docker": 2,

    "Java": 2,
    "C": 2,
    "C++": 2,
    "C#": 2,

    "JavaScript": 2,
    "TypeScript": 2,

    "React": 2,
    "Angular": 2,
    "Vue": 2,

    "Django": 2,
    "Flask": 2,

    "Node.js": 2,
    "Express.js": 2,

    "MongoDB": 2,

    "Deep Learning": 3,
    "Natural Language Processing": 3,
    "Computer Vision": 3,

    "TensorFlow": 3,
    "PyTorch": 3,
    "Scikit-learn": 3,

    "Kubernetes": 2,

    "AWS": 2,
    "Microsoft Azure": 2,
    "Google Cloud": 2,

    "Linux": 1,

    "REST API": 2,
    "Postman": 1,

    "HTML": 1,
    "CSS": 1,

    "Figma": 1
}


# ==========================================
# FILE SIZE ERROR
# ==========================================

@app.errorhandler(413)
def file_too_large(error):

    return render_template(
        "index.html",
        error=(
            "The uploaded file is too large. "
            "Please upload a PDF smaller than 10 MB."
        )
    ), 413


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    # --------------------------------------
    # GET REQUEST
    # --------------------------------------

    if request.method == "GET":

        return render_template(
            "index.html"
        )


    # --------------------------------------
    # GET RESUME FILE
    # --------------------------------------

    resume_file = request.files.get(
        "resume_file"
    )

    if resume_file is None:

        return render_template(
            "index.html",
            error="Please upload your resume PDF."
        )


    if resume_file.filename == "":

        return render_template(
            "index.html",
            error="Please select your resume PDF."
        )


    # --------------------------------------
    # SECURE FILENAME
    # --------------------------------------

    safe_filename = secure_filename(
        resume_file.filename
    )


    # --------------------------------------
    # CHECK FILE TYPE
    # --------------------------------------

    if not safe_filename.lower().endswith(".pdf"):

        return render_template(
            "index.html",
            error="Invalid file type. Please upload a PDF file."
        )


    # --------------------------------------
    # GET JOB DESCRIPTION
    # --------------------------------------

    job_description = request.form.get(
        "job_description",
        ""
    ).strip()


    if not job_description:

        return render_template(
            "index.html",
            error="Please enter a job description."
        )


    # --------------------------------------
    # EXTRACT RESUME TEXT
    # --------------------------------------

    try:

        resume_text = extract_text_from_pdf(
            resume_file
        )

    except Exception as error:

        print(
            "PDF Reading Error:",
            error
        )

        return render_template(
            "index.html",
            error=(
                "The PDF could not be read. "
                "Please upload a valid text-based PDF."
            )
        )


    # --------------------------------------
    # CHECK EXTRACTED TEXT
    # --------------------------------------

    if not resume_text.strip():

        return render_template(
            "index.html",
            error=(
                "No readable text was found in the PDF. "
                "Please upload a text-based PDF."
            )
        )


    # --------------------------------------
    # ANALYZE RESUME
    # --------------------------------------

    try:

        analysis = analyze_resume(

            resume_text,

            job_description,

            skills_data,

            skill_weights

        )

    except Exception as error:

        print(
            "Analysis Error:",
            error
        )

        return render_template(
            "index.html",
            error=(
                "An error occurred while analyzing "
                "the resume. Please try again."
            )
        )


    # --------------------------------------
    # SHOW RESULTS
    # --------------------------------------

    return render_template(
        "results.html",
        analysis=analysis
    )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )