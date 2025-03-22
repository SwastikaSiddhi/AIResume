# Set the style for the chart
sns.set(style="whitegrid")

# Create a bar plot of the ranking scores
plt.figure(figsize=(10, 6))
sns.barplot(x='Ranking Score', y='Candidate', data=df_sorted, palette='Blues_d')

# Add titles and labels
plt.title('Candidate Ranking Based on Job Fit', fontsize=16)
plt.xlabel('Ranking Score', fontsize=14)
plt.ylabel('Candidate', fontsize=14)

# Show the plot
plt.show()
