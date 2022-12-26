import pandas as pd

students = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [65, 84, 49]
}

students_df = pd.DataFrame(students)
print(students_df)

# Loop through rows of DF : iterrows()
for (index, row) in students_df.iterrows():
    if row.student == 'Angela':
        print(row.student)