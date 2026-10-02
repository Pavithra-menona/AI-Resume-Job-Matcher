from app.semantic_matcher import calculate_semantic_similarity


resume_text = """
Computer Science student with experience in Python,
Pandas, data analysis and web development.
"""


job_description = """
We are looking for a developer with Python programming
experience and knowledge of data analytics.
"""


score = calculate_semantic_similarity(
    resume_text,
    job_description
)


print("Semantic Similarity Score:", score, "%")