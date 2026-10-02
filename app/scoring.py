def calculate_weighted_score(resume_skills, job_skills, skill_weights):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    total_weight = 0
    matched_weight = 0

    for skill in job_set:
        weight = skill_weights.get(skill, 1)

        total_weight += weight

        if skill in resume_set:
            matched_weight += weight

    if total_weight > 0:
        score = (matched_weight / total_weight) * 100
    else:
        score = 0

    return round(score, 2)