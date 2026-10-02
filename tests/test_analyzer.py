from app.analyzer import analyze_resume


# Sample skill database
skills_data = {

    "Python": {
        "category": "Programming",
        "aliases": ["python"]
    },

    "SQL": {
        "category": "Database",
        "aliases": ["sql"]
    },

    "Pandas": {
        "category": "Data Science",
        "aliases": ["pandas"]
    },

    "Git": {
        "category": "Tools",
        "aliases": ["git"]
    },

    "Machine Learning": {
        "category": "AI/ML",
        "aliases": ["machine learning", "ml"]
    },

    "Docker": {
        "category": "Tools",
        "aliases": ["docker"]
    },

    "HTML": {
        "category": "Web Development",
        "aliases": ["html"]
    },

    "CSS": {
        "category": "Web Development",
        "aliases": ["css"]
    },

    "React": {
        "category": "Web Development",
        "aliases": ["react", "reactjs"]
    }
}


# Skill weights
skill_weights = {

    "Python": 3,
    "SQL": 3,
    "Machine Learning": 3,
    "Pandas": 2,
    "Git": 2,
    "Docker": 2,
    "HTML": 1,
    "CSS": 1,
    "React": 2
}


# Sample resume
resume_text = """
Computer Science Engineering Student

Technical Skills:
Python
Pandas
Git
HTML
CSS

Projects:
Developed a web application using Python.
Used Pandas for data analysis.
Used Git for version control.
"""


# Sample job description
job_description = """
Software Developer Intern

Required Skills:
Python
SQL
Pandas
Git
Machine Learning
Docker

Preferred Skills:
HTML
CSS
React
"""


# Run analysis
result = analyze_resume(
    resume_text,
    job_description,
    skills_data,
    skill_weights
)


# ==========================================
# TESTS
# ==========================================

def test_resume_skills():

    assert "Python" in result["resume_skills"]

    assert "Pandas" in result["resume_skills"]

    assert "Git" in result["resume_skills"]


def test_required_skills():

    assert "Python" in result["required_skills"]

    assert "SQL" in result["required_skills"]

    assert "Docker" in result["required_skills"]


def test_matched_required_skills():

    assert "Python" in result["matched_required"]

    assert "Pandas" in result["matched_required"]

    assert "Git" in result["matched_required"]


def test_missing_required_skills():

    assert "SQL" in result["missing_required"]

    assert "Machine Learning" in result["missing_required"]

    assert "Docker" in result["missing_required"]


def test_preferred_skills():

    assert "HTML" in result["preferred_skills"]

    assert "CSS" in result["preferred_skills"]

    assert "React" in result["preferred_skills"]


def test_matched_preferred_skills():

    assert "HTML" in result["matched_preferred"]

    assert "CSS" in result["matched_preferred"]


def test_missing_preferred_skills():

    assert "React" in result["missing_preferred"]


def test_scores_exist():

    assert 0 <= result["required_percentage"] <= 100

    assert 0 <= result["overall_percentage"] <= 100

    assert 0 <= result["weighted_score"] <= 100

    assert 0 <= result["semantic_score"] <= 100

    assert 0 <= result["combined_score"] <= 100

    assert 0 <= result["ats_score"] <= 100


def test_recommendations_exist():

    assert "SQL" in result["recommendations"]

    assert "Machine Learning" in result["recommendations"]

    assert "Docker" in result["recommendations"]