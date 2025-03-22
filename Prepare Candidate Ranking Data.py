import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data: Candidate names with AI and Manual rankings
data = {
    'Candidate': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'AI_Rank': [1, 2, 4, 3, 5],  # AI-assigned ranks (lower is better)
    'Manual_Rank': [2, 1, 3, 5, 4]  # Manually assigned ranks
}

df = pd.DataFrame(data)
df.set_index('Candidate', inplace=True)

print(df)
