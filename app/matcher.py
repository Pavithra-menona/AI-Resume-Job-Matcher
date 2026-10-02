def calculate_match(
    resume_skills,
    required_skills,
    preferred_skills=None
):
    resume_set = set(resume_skills)
    required_set = set(required_skills)

    if preferred_skills is None:
        preferred_skills = []

    preferred_set = set(preferred_skills)

    # Required skills
    matched_required = sorted(
        resume_set & required_set
    )

    missing_required = sorted(
        required_set - resume_set
    )

    # Preferred skills
    matched_preferred = sorted(
        resume_set & preferred_set
    )

    missing_preferred = sorted(
        preferred_set - resume_set
    )

    # Required skill percentage
    if len(required_set) > 0:
        required_percentage = (
            len(matched_required) / len(required_set)
        ) * 100
    else:
        required_percentage = 0

    # Preferred skill percentage
    if len(preferred_set) > 0:
        preferred_percentage = (
            len(matched_preferred) / len(preferred_set)
        ) * 100
    else:
        preferred_percentage = 0

    # Overall score
    total_skills = len(required_set) + len(preferred_set)
    total_matched = (
        len(matched_required) +
        len(matched_preferred)
    )

    if total_skills > 0:
        overall_percentage = (
            total_matched / total_skills
        ) * 100
    else:
        overall_percentage = 0

    return {
        "matched_required": matched_required,
        "missing_required": missing_required,
        "matched_preferred": matched_preferred,
        "missing_preferred": missing_preferred,
        "required_percentage": round(
            required_percentage, 2
        ),
        "preferred_percentage": round(
            preferred_percentage, 2
        ),
        "overall_percentage": round(
            overall_percentage, 2
        )
    }