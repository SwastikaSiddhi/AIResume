# Set the style
sns.set_style("whitegrid")

# Plot bar chart
plt.figure(figsize=(8, 5))
df.plot(kind='bar', figsize=(8, 5), colormap="viridis", alpha=0.8)

# Labels & Title
plt.title("Candidate Ranking Comparison: AI vs. Manual")
plt.ylabel("Ranking (Lower is Better)")
plt.xticks(rotation=0)
plt.legend(title="Ranking Source")

# Show the plot
plt.show()
