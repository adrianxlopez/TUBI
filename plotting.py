import matplotlib.pyplot as plt 
import pandas as pd  

file_name = "cancer_types_summary.txt"
df = pd.read_csv(file_name, sep="\t", header=0)

# Assign the x (cancer study labels) and y (alteration frequencies)
x = df["Cancer Study"]
y = df["Alteration Frequency"]

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(12, 6))

# Create the bar chart
bars = ax.bar(x, y, color=plt.cm.cool(0.2))

# Label axes and title
ax.set_xlabel("Cancer Study", fontsize=12)
ax.set_yticks((0,30))
ax.set_ylabel("Alteration Frequency", fontsize=12)
ax.set_title("Alteration Frequency by Cancer Study", fontsize=14)

# Rotate the x-axis labels if needed
plt.xticks(rotation=45, ha="right", fontsize=8)

# Annotate each bar with its alteration frequency
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}%',  # Format the label to 2 decimal places
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()
