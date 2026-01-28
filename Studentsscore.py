"""
A script to find the student with the highest score from a list of records.
"""

def main():
    """Main function to iterate through records and find the top score."""
    # List of dictionaries representing student records
    students = [
        {"name": "Alice", "score": 88},
        {"name": "Bob", "score": 95},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 92}
    ]

    # Initialize variables to track the best student
    top_student_name = ""
    highest_score = -1  # Start with a value lower than any possible score

    # Iterate through each dictionary in the list
    for student in students:
        # Use an if statement to check if current score is the new maximum
        if student["score"] > highest_score:
            highest_score = student["score"]
            top_student_name = student["name"]

    # Print the result
    if top_student_name:
        print(f"The student with the highest score is {top_student_name} with {highest_score} points.")

if __name__ == "__main__":
    main()