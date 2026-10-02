import re


def normalize_text(text):
    """
    Normalizes text for consistent skill matching.
    """

    text = text.lower()

    # Normalize common punctuation/separators
    text = text.replace("–", "-")
    text = text.replace("—", "-")
    text = text.replace("_", " ")
    text = text.replace("/", " ")

    # Keep + and # because they are important
    # for skills such as C++ and C#
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def extract_skills(text, skills_data):
    """
    Extracts known skills from text
    using aliases and normalized matching.
    """

    text = normalize_text(text)

    found_skills = []

    for skill, details in skills_data.items():

        aliases = details.get(
            "aliases",
            []
        )

        for alias in aliases:

            normalized_alias = normalize_text(
                alias
            )

            # Escape special regex characters
            escaped_alias = re.escape(
                normalized_alias
            )

            # Match complete terms
            pattern = (
                r"(?<![a-zA-Z0-9])"
                + escaped_alias
                + r"(?![a-zA-Z0-9])"
            )

            if re.search(
                pattern,
                text
            ):

                found_skills.append(
                    skill
                )

                break

    return found_skills