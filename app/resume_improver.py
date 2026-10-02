def generate_resume_improvements(
    ats_checks,
    missing_required_skills,
    action_word_count
):

    suggestions = []

    # Contact information

    if not ats_checks.get("email", False):
        suggestions.append(
            "Add a professional email address to your resume."
        )

    if not ats_checks.get("phone", False):
        suggestions.append(
            "Add a valid phone number to your resume."
        )


    # Resume sections

    if not ats_checks.get("skills_section", False):
        suggestions.append(
            "Add a clearly labelled Skills or Technical Skills section."
        )

    if not ats_checks.get("education_section", False):
        suggestions.append(
            "Add an Education section with your degree and institution."
        )

    if not ats_checks.get("experience_section", False):
        suggestions.append(
            "Add an Experience or Internship section if you have relevant experience."
        )

    if not ats_checks.get("projects_section", False):
        suggestions.append(
            "Add a Projects section to demonstrate your practical skills."
        )


    # Missing job skills

    if missing_required_skills:

        skills = ", ".join(
            missing_required_skills
        )

        suggestions.append(
            f"Consider learning or demonstrating these required job skills: {skills}."
        )


    # Action words

    if action_word_count == 0:

        suggestions.append(
            "Use strong action words such as developed, designed, implemented, built, analyzed and tested."
        )

    elif action_word_count < 3:

        suggestions.append(
            "Use more action-oriented words to describe your projects and experience."
        )


    # If everything looks good

    if not suggestions:

        suggestions.append(
            "Your resume has passed the basic improvement checks. "
            "Continue tailoring it to each job description."
        )


    return suggestions