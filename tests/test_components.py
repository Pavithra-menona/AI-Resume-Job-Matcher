from io import BytesIO

from app.pdf_reader import extract_text_from_pdf
from app.skill_extractor import extract_skills


def test_skill_extraction_basic():

    skills_data = {

        "Python": {
            "category": "Programming",
            "aliases": ["python"]
        },

        "SQL": {
            "category": "Database",
            "aliases": ["sql"]
        },

        "React": {
            "category": "Web Development",
            "aliases": ["react", "reactjs"]
        },

        "C++": {
            "category": "Programming",
            "aliases": ["c++", "cpp"]
        },

        "C#": {
            "category": "Programming",
            "aliases": ["c#", "c sharp"]
        }
    }


    text = """
    I have experience with Python,
    SQL, React.js, C++ and C#.
    """


    skills = extract_skills(
        text,
        skills_data
    )


    assert "Python" in skills
    assert "SQL" in skills
    assert "React" in skills
    assert "C++" in skills
    assert "C#" in skills


def test_skill_extraction_does_not_match_partial_words():

    skills_data = {

        "C": {
            "category": "Programming",
            "aliases": ["c"]
        },

        "Python": {
            "category": "Programming",
            "aliases": ["python"]
        }
    }


    text = """
    The candidate has experience with
    Python programming.
    """


    skills = extract_skills(
        text,
        skills_data
    )


    assert "Python" in skills

    # A standalone C should not be detected
    # merely because the letter appears inside
    # another word.
    assert "C" not in skills


def test_skill_extraction_with_separators():

    skills_data = {

        "Python": {
            "category": "Programming",
            "aliases": ["python"]
        },

        "SQL": {
            "category": "Database",
            "aliases": ["sql"]
        }
    }


    text = """
    Python/SQL developer
    Python-based applications
    """


    skills = extract_skills(
        text,
        skills_data
    )


    assert "Python" in skills
    assert "SQL" in skills


def test_pdf_reader_extracts_text():

    from reportlab.pdfgen import canvas

    pdf_buffer = BytesIO()

    pdf = canvas.Canvas(
        pdf_buffer
    )

    pdf.drawString(
        100,
        750,
        "Python Developer"
    )

    pdf.drawString(
        100,
        730,
        "Skills: Python SQL"
    )

    pdf.save()

    pdf_buffer.seek(0)


    text = extract_text_from_pdf(
        pdf_buffer
    )


    assert "Python Developer" in text
    assert "Python SQL" in text