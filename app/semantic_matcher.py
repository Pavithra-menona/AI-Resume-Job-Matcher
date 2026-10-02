from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_semantic_similarity(
    resume_text,
    job_description
):
    """
    Calculates lightweight NLP similarity between
    a resume and a job description using TF-IDF
    and cosine similarity.

    This version is designed to work on low-memory
    deployment environments.
    """

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    try:
        vectors = vectorizer.fit_transform(
            documents
        )

        similarity = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]

    except ValueError:
        similarity = 0

    similarity_percentage = similarity * 100

    return round(
        similarity_percentage,
        2
    )