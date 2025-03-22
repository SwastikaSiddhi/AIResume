import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data representing candidates, job titles, skills, and ranking scores
data = {
    'Candidate': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Job Title': ['Software Engineer', 'Data Scientist', 'Data Scientist', 'Software Engineer', 'Machine Learning Engineer'],
    'Skills': ['Python, Django', 'Python, SQL, ML', 'Python, R, ML', 'Python, Java', 'Python, ML, AI'],
    'Ranking Score': [88, 92, 85, 91, 94]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Sort the candidates by Ranking Score in descending order
df_sorted = df.sort_values(by='Ranking Score', ascending=False)

# Display the sorted table
print(df_sorted)
