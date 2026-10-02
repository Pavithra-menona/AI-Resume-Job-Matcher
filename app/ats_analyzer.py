import re


def analyze_ats(resume_text):

    text = resume_text.lower()

    checks = {}

    # Contact information

    checks["email"] = bool(
        re.search(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            resume_text
        )
    )

    checks["phone"] = bool(
        re.search(
            r"(\+91[\s-]?)?[6-9]\d{9}",
            resume_text
        )
    )


    # Important resume sections

    checks["skills_section"] = any(
        keyword in text
        for keyword in [
            "skills",
            "technical skills",
            "technical skill"
        ]
    )

    checks["education_section"] = any(
        keyword in text
        for keyword in [
            "education",
            "academic",
            "qualification"
        ]
    )

    checks["experience_section"] = any(
        keyword in text
        for keyword in [
            "experience",
            "work experience",
            "internship",
            "internships"
        ]
    )

    checks["projects_section"] = any(
        keyword in text
        for keyword in [
            "projects",
            "project"
        ]
    )


    # Action keywords

    action_words = [
        "developed",
        "designed",
        "created",
        "implemented",
        "built",
        "managed",
        "analyzed",
        "tested",
        "developed",
        "worked"
    ]

    action_word_count = sum(
        text.count(word)
        for word in action_words
    )


    # Calculate ATS score

    total_checks = len(checks)

    passed_checks = sum(
        checks.values()
    )

    section_score = (
        passed_checks / total_checks
    ) * 100 if total_checks > 0 else 0


    # Action word score

    action_score = min(
        action_word_count * 10,
        100
    )


    # Final ATS score

    ats_score = (
        section_score * 0.7
        +
        action_score * 0.3
    )


    return {
        "ats_score": round(ats_score, 2),
        "checks": checks,
        "action_word_count": action_word_count
    }