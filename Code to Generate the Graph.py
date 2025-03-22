import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# 1. Generate a sample dataset (Replace this with actual data)
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)

# 2. Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train a Random Forest classifier (Replace with your actual model)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Make predictions
y_pred = model.predict(X_test)

# 5. Calculate performance metrics
metrics = {
    "Accuracy": accuracy_score(y_test, y_pred),
    "Precision": precision_score(y_test, y_pred),
    "Recall": recall_score(y_test, y_pred),
    "F1-Score": f1_score(y_test, y_pred)
}

# 6. Convert dictionary to lists for plotting
labels = list(metrics.keys())
values = list(metrics.values())

# 7. Set up Seaborn style
sns.set_style("whitegrid")

# 8. Create a bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x=labels, y=values, palette="coolwarm")

# 9. Add value labels on bars
for i, v in enumerate(values):
    plt.text(i, v + 0.01, f"{v:.2f}", ha='center', fontsize=12)

# 10. Set titles and labels
plt.ylim(0, 1)
plt.title("Model Performance Metrics", fontsize=14)
plt.ylabel("Score", fontsize=12)
plt.xlabel("Metric", fontsize=12)

# 11. Show the plot
plt.show()
