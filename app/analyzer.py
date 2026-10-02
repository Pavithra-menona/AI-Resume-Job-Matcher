from .skill_extractor import extract_skills
from .matcher import calculate_match
from .scoring import calculate_weighted_score
from .recommendations import get_recommendations
from .semantic_matcher import calculate_semantic_similarity
from .ats_analyzer import analyze_ats
from .resume_improver import generate_resume_improvements


def is_heading(line, keywords):
    """
    Checks whether a line looks like a section heading.
    """

    cleaned = line.strip().lower()

    if not cleaned:
        return False

    cleaned = cleaned.rstrip(":").strip()

    for keyword in keywords:

        if cleaned == keyword:
            return True

        if cleaned.startswith(keyword + ":"):
            return True

    return False


def separate_job_skills(job_description, skills_data):
    """
    Separates job skills into required and preferred skills.
    """

    lines = job_description.splitlines()

    preferred_keywords = [
        "preferred skills",
        "preferred qualifications",
        "preferred requirements",
        "nice to have",
        "nice-to-have",
        "bonus skills",
        "bonus qualifications",
        "optional skills",
        "optional qualifications",
        "desired skills",
        "desired qualifications"
    ]

    required_keywords = [
        "required skills",
        "required qualifications",
        "required requirements",
        "requirements",
        "qualifications",
        "must have",
        "must-have",
        "essential skills",
        "essential qualifications",
        "minimum qualifications"
    ]

    preferred_lines = []
    required_lines = []

    # Default section
    current_section = "required"

    for line in lines:

        cleaned_line = line.strip()

        if not cleaned_line:
            continue

        lower_line = cleaned_line.lower()

        # Preferred section
        if is_heading(
            cleaned_line,
            preferred_keywords
        ):

            current_section = "preferred"
            continue

        # Required section
        if is_heading(
            cleaned_line,
            required_keywords
        ):

            current_section = "required"
            continue

        # Common preferred phrases
        if (
            "preferred qualifications" in lower_line
            or
            "preferred skills" in lower_line
            or
            "nice to have" in lower_line
            or
            "nice-to-have" in lower_line
        ):

            current_section = "preferred"
            continue

        # Store lines
        if current_section == "preferred":

            preferred_lines.append(
                cleaned_line
            )

        else:

            required_lines.append(
                cleaned_line
            )

    required_text = " ".join(
        required_lines
    )

    preferred_text = " ".join(
        preferred_lines
    )

    # Extract skills
    required_skills = extract_skills(
        required_text,
        skills_data
    )

    preferred_skills = extract_skills(
        preferred_text,
        skills_data
    )

    # Remove skills that are already preferred
    required_skills = [
        skill
        for skill in required_skills
        if skill not in preferred_skills
    ]

    return (
        required_skills,
        preferred_skills
    )


def get_skill_categories(
    skills,
    skills_data
):
    """
    Groups skills according to their categories.
    """

    categories = {}

    for skill in skills:

        if skill in skills_data:

            category = skills_data[
                skill
            ]["category"]

            if category not in categories:

                categories[category] = []

            categories[category].append(
                skill
            )

    return categories


def analyze_resume(
    resume_text,
    job_description,
    skills_data,
    skill_weights
):
    """
    Performs the complete resume-job analysis.
    """

    # ==========================================
    # 1. EXTRACT RESUME SKILLS
    # ==========================================

    resume_skills = extract_skills(
        resume_text,
        skills_data
    )

    # ==========================================
    # 2. SEPARATE JOB SKILLS
    # ==========================================

    required_skills, preferred_skills = (
        separate_job_skills(
            job_description,
            skills_data
        )
    )

    # ==========================================
    # 3. EXACT SKILL MATCHING
    # ==========================================

    match_result = calculate_match(
        resume_skills,
        required_skills,
        preferred_skills
    )

    # ==========================================
    # 4. WEIGHTED SKILL SCORE
    # ==========================================

    weighted_score = calculate_weighted_score(
        resume_skills,
        required_skills,
        skill_weights
    )

    # ==========================================
    # 5. SEMANTIC SIMILARITY
    # ==========================================

    semantic_score = calculate_semantic_similarity(
        resume_text,
        job_description
    )

    # ==========================================
    # 6. EXPLAINABLE COMBINED SCORE
    # ==========================================

    # Project-defined weighting:
    #
    # Weighted Skill Score = 40%
    # Overall Skill Match  = 30%
    # Semantic Similarity  = 30%
    #
    # These weights are design choices
    # for this project and are not industry standards.

    weighted_skill_contribution = round(
        weighted_score * 0.40,
        2
    )

    overall_skill_contribution = round(
        match_result["overall_percentage"] * 0.30,
        2
    )

    semantic_contribution = round(
        semantic_score * 0.30,
        2
    )

    combined_score = (
        weighted_skill_contribution
        +
        overall_skill_contribution
        +
        semantic_contribution
    )

    combined_score = round(
        combined_score,
        2
    )

    # ==========================================
    # 7. SCORE BREAKDOWN
    # ==========================================

    score_breakdown = {

        "weighted_skill_score":
            weighted_score,

        "weighted_skill_weight":
            40,

        "weighted_skill_contribution":
            weighted_skill_contribution,

        "overall_skill_match":
            match_result["overall_percentage"],

        "overall_skill_weight":
            30,

        "overall_skill_contribution":
            overall_skill_contribution,

        "semantic_similarity":
            semantic_score,

        "semantic_weight":
            30,

        "semantic_contribution":
            semantic_contribution,

        "final_score":
            combined_score
    }

    # ==========================================
    # 8. ATS ANALYSIS
    # ==========================================

    ats_result = analyze_ats(
        resume_text
    )

    # ==========================================
    # 9. PRIORITIZED LEARNING RECOMMENDATIONS
    # ==========================================

    missing_required_skills = (
        match_result["missing_required"]
    )

    # Sort missing required skills by
    # project-defined skill weight.
    #
    # Higher-weighted skills appear first.

    missing_required_skills = sorted(
        missing_required_skills,
        key=lambda skill: skill_weights.get(
            skill,
            1
        ),
        reverse=True
    )

    recommendations = get_recommendations(
        missing_required_skills
    )

    # ==========================================
    # 10. RESUME IMPROVEMENTS
    # ==========================================

    resume_improvements = (
        generate_resume_improvements(
            ats_result["checks"],
            missing_required_skills,
            ats_result["action_word_count"]
        )
    )

    # ==========================================
    # 11. SKILL CATEGORIES
    # ==========================================

    resume_categories = get_skill_categories(
        resume_skills,
        skills_data
    )

    required_categories = get_skill_categories(
        required_skills,
        skills_data
    )

    preferred_categories = get_skill_categories(
        preferred_skills,
        skills_data
    )

    # ==========================================
    # 12. RETURN COMPLETE ANALYSIS
    # ==========================================

    return {

        "resume_skills":
            resume_skills,

        "required_skills":
            required_skills,

        "preferred_skills":
            preferred_skills,

        "matched_required":
            match_result["matched_required"],

        "missing_required":
            missing_required_skills,

        "matched_preferred":
            match_result["matched_preferred"],

        "missing_preferred":
            match_result["missing_preferred"],

        "required_percentage":
            match_result["required_percentage"],

        "preferred_percentage":
            match_result["preferred_percentage"],

        "overall_percentage":
            match_result["overall_percentage"],

        "weighted_score":
            weighted_score,

        "semantic_score":
            semantic_score,

        "combined_score":
            combined_score,

        "score_breakdown":
            score_breakdown,

        "ats_score":
            ats_result["ats_score"],

        "ats_checks":
            ats_result["checks"],

        "action_word_count":
            ats_result["action_word_count"],

        "recommendations":
            recommendations,

        "resume_improvements":
            resume_improvements,

        "resume_categories":
            resume_categories,

        "required_categories":
            required_categories,

        "preferred_categories":
            preferred_categories
    }