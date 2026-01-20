"""
In-Class Practice: Structured Data and Strings

You will work through this file during class.
Run your code often.
Do not delete existing data structures.
"""

# --------------------------------------------------
# Part 1: Given Data
# --------------------------------------------------

movies = [
    {
        "title": "inception",
        "year": 2010,
        "ratings": [9, 8, 9]
    },
    {
        "title": "the matrix",
        "year": 1999,
        "ratings": [10, 9, 10]
    }
]

# --------------------------------------------------
# Part 2: Extracting Data
# --------------------------------------------------
# Create variables for the following:
# - first_title
# - second_year
# - first_ratings
# - last_rating

# Write your code below
first_title = movies[0]["title"]
print(first_title)
second_year = movies[1]["year"]
print(second_year)
first_ratings = movies[0]["ratings"]
print(first_ratings)
last_rating = movies[1]["ratings"][-1]
print(last_rating)




# --------------------------------------------------
# Part 3: Updating Nested Data
# --------------------------------------------------
# Update the existing data:
# 1. Change the year of the first movie to 2011
# 2. Add a rating of 10 to the second movie
# 3. Change the title of the second movie to "The Matrix Reloaded"

# Write your code below
movies[0]["year"] = 2011
movies[1]["ratings"].append(10)
movies[1]["title"] = "The Matrix Reloaded"
print(movies[1])




# --------------------------------------------------
# Part 4: Working with Strings
# --------------------------------------------------
# Create a variable named clean_title that:
# - uses the first movie's title
# - removes extra spaces (if any)
# - converts the title to title case

# Write your code below
clean_title = movies[0]["title"].title().strip()



# --------------------------------------------------
# Part 5: String Slicing (Bookends)
# --------------------------------------------------
# Create a variable named bookends that contains:
# - the first character of clean_title
# - the last character of clean_title

# Write your code below
bookends = clean_title[0] + clean_title[-1]

print(bookends)



# --------------------------------------------------
# Part 6: Formatting a Summary String
# --------------------------------------------------
# Create a variable named summary with this format:
# Movie: Inception (2011)
#
# Use values from the data structure.
# Do not hard-code the final string.

# Write your code below

summary = f"Movie: {clean_title} ({movies[0]["year"]})"


# Optional: print summary to check your work
print(summary)
