import importlib.util
from pathlib import Path

def load_student_module():
    """
    Load practice_structured_data.py from the repo root.
    This runs the student's code so we can inspect variables.
    """
    target = Path(__file__).resolve().parents[1] / "practice_structured_data.py"

    assert target.exists(), (
        "Could not find practice_structured_data.py at the repo root.\n"
        "Do not rename or move the file."
    )

    spec = importlib.util.spec_from_file_location("student_work", str(target))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader, "Internal error loading student file."
    spec.loader.exec_module(module)
    return module


# --------------------------------------------------
# 1 point: movies data structure exists and is correct
# --------------------------------------------------

def test_movies_structure():
    m = load_student_module()

    assert hasattr(m, "movies"), "The variable movies should exist."
    assert isinstance(m.movies, list), "movies should be a list."
    assert len(m.movies) == 2, "movies should contain exactly two items."

    for i in [0, 1]:
        assert isinstance(m.movies[i], dict), f"movies[{i}] should be a dictionary."
        for key in ["title", "year", "ratings"]:
            assert key in m.movies[i], f'movies[{i}] is missing key "{key}".'
        assert isinstance(m.movies[i]["ratings"], list), (
            f'movies[{i}]["ratings"] should be a list.'
        )


# --------------------------------------------------
# 1 point: extraction variables
# --------------------------------------------------

def test_extraction_variables():
    m = load_student_module()

    for var in ["first_title", "second_year", "first_ratings", "last_rating"]:
        assert hasattr(m, var), f"Create the variable {var}."

    assert m.first_title == "inception", (
        "first_title should be the title of the first movie."
    )
    assert m.second_year == 1999, (
        "second_year should be the year of the second movie."
    )
    assert m.first_ratings == [9, 8, 9], (
        "first_ratings should be the ratings list for the first movie."
    )
    assert m.last_rating == 10, (
        "last_rating should be the last rating of the second movie."
    )


# --------------------------------------------------
# 1 point: updating nested data
# --------------------------------------------------

def test_updates_to_movies():
    m = load_student_module()

    assert m.movies[0]["year"] == 2011, (
        "Update the year of the first movie to 2011."
    )

    assert m.movies[1]["title"] == "The Matrix Reloaded", (
        'Update the second movie title to "The Matrix Reloaded".'
    )

    assert m.movies[1]["ratings"] == [10, 9, 10, 10], (
        "Add a rating of 10 to the end of the second movie's ratings list."
    )


# --------------------------------------------------
# 1 point: clean_title and bookends
# --------------------------------------------------

def test_string_processing():
    m = load_student_module()

    assert hasattr(m, "clean_title"), (
        "Create a variable named clean_title."
    )
    assert m.clean_title == "Inception", (
        "clean_title should be the first movie title in Title Case."
    )

    assert hasattr(m, "bookends"), (
        "Create a variable named bookends."
    )
    assert m.bookends == "In", (
        "bookends should contain the first and last characters of clean_title."
    )


# --------------------------------------------------
# 1 point: formatted summary string
# --------------------------------------------------

def test_summary_string():
    m = load_student_module()

    assert hasattr(m, "summary"), (
        "Create a variable named summary."
    )

    expected = "Movie: Inception (2011)"
    assert m.summary == expected, (
        "summary should be exactly:\n"
        "Movie: Inception (2011)\n"
        "Use values from the data structure; do not hard-code the final string."
    )
