def get_recommendations(missing_skills):
    """
    Generates learning recommendations for missing skills.
    """

    recommendations = {

        "Python": {
            "what_to_learn":
                "Learn Python programming fundamentals and practical application development.",

            "topics": [
                "Variables and data types",
                "Conditional statements and loops",
                "Functions",
                "Lists, tuples and dictionaries",
                "Object-oriented programming",
                "File handling",
                "Exception handling"
            ],

            "practice":
                "Build small Python programs such as a calculator, student management system or file analyzer.",

            "project":
                "Build a Python-based Job Application Tracker."
        },

        "SQL": {
            "what_to_learn":
                "Learn how to store, query and manage data using SQL databases.",

            "topics": [
                "SELECT queries",
                "WHERE and ORDER BY",
                "GROUP BY",
                "JOIN operations",
                "Subqueries",
                "INSERT, UPDATE and DELETE",
                "Database normalization"
            ],

            "practice":
                "Create a small database and write queries to search, filter and summarize the data.",

            "project":
                "Build a Student Management Database using Python and SQL."
        },

        "Machine Learning": {
            "what_to_learn":
                "Learn the fundamentals of machine learning and how to build basic predictive models.",

            "topics": [
                "Supervised learning",
                "Unsupervised learning",
                "Regression",
                "Classification",
                "Train-test split",
                "Model evaluation",
                "Feature preprocessing"
            ],

            "practice":
                "Train simple classification and regression models using scikit-learn.",

            "project":
                "Build a House Price Prediction or Student Performance Prediction system."
        },

        "Pandas": {
            "what_to_learn":
                "Learn Pandas for data cleaning, manipulation and analysis.",

            "topics": [
                "Series and DataFrames",
                "Reading CSV files",
                "Filtering data",
                "Sorting data",
                "Missing-value handling",
                "Grouping data",
                "Data aggregation"
            ],

            "practice":
                "Take a public CSV dataset and perform data cleaning and analysis.",

            "project":
                "Build a Data Analysis Dashboard using Pandas."
        },

        "NumPy": {
            "what_to_learn":
                "Learn NumPy for numerical computing and array-based operations.",

            "topics": [
                "NumPy arrays",
                "Array indexing",
                "Array slicing",
                "Mathematical operations",
                "Array reshaping",
                "Statistics",
                "Broadcasting"
            ],

            "practice":
                "Perform mathematical and statistical operations on numerical datasets.",

            "project":
                "Build a simple numerical data analysis tool using NumPy."
        },

        "Git": {
            "what_to_learn":
                "Learn Git for source-code version control and project collaboration.",

            "topics": [
                "git init",
                "git add",
                "git commit",
                "git status",
                "git log",
                "Branches",
                "Merge and pull requests"
            ],

            "practice":
                "Create a Git repository and commit changes while developing a small project.",

            "project":
                "Upload one of your projects to GitHub and maintain it using Git."
        },

        "Docker": {
            "what_to_learn":
                "Learn how Docker packages applications and their dependencies into containers.",

            "topics": [
                "Images",
                "Containers",
                "Dockerfile",
                "Docker commands",
                "Ports",
                "Volumes",
                "Docker Compose"
            ],

            "practice":
                "Containerize a simple Python or Flask application.",

            "project":
                "Create a Dockerized Flask web application."
        },

        "Java": {
            "what_to_learn":
                "Learn Java programming and object-oriented application development.",

            "topics": [
                "Classes and objects",
                "Inheritance",
                "Polymorphism",
                "Interfaces",
                "Exception handling",
                "Collections",
                "File handling"
            ],

            "practice":
                "Build small console-based Java applications.",

            "project":
                "Build a Java-based Employee Management System."
        },

        "JavaScript": {
            "what_to_learn":
                "Learn JavaScript for interactive web applications.",

            "topics": [
                "Variables",
                "Functions",
                "Arrays and objects",
                "DOM manipulation",
                "Events",
                "Promises",
                "Fetch API"
            ],

            "practice":
                "Create interactive web pages using HTML, CSS and JavaScript.",

            "project":
                "Build a browser-based Task Management application."
        },

        "React": {
            "what_to_learn":
                "Learn React for building component-based frontend applications.",

            "topics": [
                "Components",
                "JSX",
                "Props",
                "State",
                "Events",
                "Hooks",
                "API integration"
            ],

            "practice":
                "Build small React applications using components and state.",

            "project":
                "Build a React-based Job Search Dashboard."
        },

        "HTML": {
            "what_to_learn":
                "Learn HTML to structure modern web pages.",

            "topics": [
                "HTML structure",
                "Headings",
                "Forms",
                "Tables",
                "Links",
                "Images",
                "Semantic HTML"
            ],

            "practice":
                "Create a multi-page personal portfolio website.",

            "project":
                "Build a responsive portfolio website."
        },

        "CSS": {
            "what_to_learn":
                "Learn CSS for designing responsive and attractive websites.",

            "topics": [
                "Selectors",
                "Box model",
                "Flexbox",
                "Grid",
                "Responsive design",
                "Animations",
                "Media queries"
            ],

            "practice":
                "Recreate simple website layouts using HTML and CSS.",

            "project":
                "Build a responsive portfolio or landing page."
        },

        "Figma": {
            "what_to_learn":
                "Learn Figma for interface design and prototyping.",

            "topics": [
                "Frames",
                "Components",
                "Auto Layout",
                "Typography",
                "Colors",
                "Prototyping",
                "Design systems"
            ],

            "practice":
                "Recreate existing mobile or web interfaces in Figma.",

            "project":
                "Design a complete job-search or resume-management application."
        }

    }

    result = {}

    for skill in missing_skills:

        if skill in recommendations:

            result[skill] = recommendations[skill]

        else:

            result[skill] = {

                "what_to_learn":
                    f"Learn the fundamentals and practical applications of {skill}.",

                "topics": [
                    f"Introduction to {skill}",
                    f"Core concepts of {skill}",
                    f"Practical usage of {skill}",
                    f"Common tools related to {skill}",
                    f"Project development using {skill}"
                ],

                "practice":
                    f"Build a small practical project using {skill}.",

                "project":
                    f"Create a beginner-friendly project demonstrating {skill}."
            }

    return result